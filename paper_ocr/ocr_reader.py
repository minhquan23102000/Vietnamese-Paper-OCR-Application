
import pytesseract

#Declare pytessecart excuteable path
pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR/tesseract'

import string

from .cropper import cropImageRoi
from .detector import Detector
from .image_transformer import ImageTransformer
from .preprocessor import ocr_preprocess


class OCRReader(object):
    def __init__(self, tesseract_config = '-l vie --oem 1 --psm 6'):
        self.detector = Detector()
        self.config = tesseract_config

    def ocr(self, image):
        result =  pytesseract.image_to_string(image, config=self.config).strip()
        return result
    
    def fit(self, paper_name, img):
        self.paper = self.detector.paper_detect(paper_name)
        self.transformer = ImageTransformer(self.paper['base_img'])
        self.img = self.transformer.transform(img)
    
    
    
    def check_paper(self):
        baseCheck = cropImageRoi(self.transformer.baseImg, self.paper['roi'].CHECK_ROI)
        imgCheck = cropImageRoi(self.img, self.paper['roi'].CHECK_ROI)
        
        baseCheck = ocr_preprocess(baseCheck)
        imgCheck = ocr_preprocess(imgCheck)
        
        if self.ocr(baseCheck) != self.ocr(imgCheck):
            return False
        
        return True
        
    
    def read(self, paper_name, img):
        self.fit(paper_name, img)
        
        if not self.check_paper():
            raise Exception("This image do not fit with the base image")
        
        result = dict()
        
        for k, rois in self.paper['roi'].ROIS.items():
            data = ''
            for r in rois:
                cropImg = cropImageRoi(self.img, r)
                
                if k not in self.paper['roi'].NOT_PREPROCESSOR:
                    cropImg = ocr_preprocess(cropImg)
                
                data += self.ocr(cropImg) + ' '
            
            result[k] = data.strip()
            
        return result
