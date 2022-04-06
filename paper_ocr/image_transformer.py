import cv2
import numpy as np


class ImageTransformer(object):
    def __init__(self, base_img_path, per_point_match=0.3):
        self.orb = cv2.ORB_create(1000)
        self.baseImg = cv2.imread(base_img_path)
        self.baseH, self.baseW, self.baseC = self.baseImg.shape
        self.per_point_match = per_point_match
        self.kpBase, self.desBase = self.orb.detectAndCompute(self.baseImg, None)
        
    def transform(self, img):
        #Detect keypoint on img2
        kp, des = self.orb.detectAndCompute(img, None)

        #Init BF Matcher, find the matches points of two images
        bf = cv2.BFMatcher(cv2.NORM_HAMMING)
        matches = list(bf.match(des, self.desBase))

        #Select top per_point_match 
        matches.sort(key=lambda x: x.distance)
        best_matches = matches[:int(len(matches)*self.per_point_match)]
        
        #Init source points and destination points for findHomography function.
        srcPoints = np.float32([kp[point.queryIdx].pt for point in best_matches]).reshape(-1,1,2)
        dstPoints = np.float32([self.kpBase[point.trainIdx].pt for point in best_matches]).reshape(-1,1,2)


        #Find Homography of two images
        matrix_transform, _ = cv2.findHomography(srcPoints, dstPoints,cv2.RANSAC, 5.0)

        #Transform the image to have the same structure as the base image
        img_final = cv2.warpPerspective(img, matrix_transform, (self.baseW, self.baseH))
        
        return img_final
