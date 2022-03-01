from constant.roi_constant import CCCD


class Detector(object):
    
    ROOT_BASE_IMG = 'constant/base_img/'
    
    def paper_detect(self, paper_name):
        result = {'paper': None, 'base_img': None, 'roi': None}
        if paper_name == 'cccd':
            result['paper'] = 'cccd'
            result['base_img'] = self.get_base_img(paper_name)
            result['roi'] = CCCD
        
        return result    
        
    def get_base_img(self, paper_name):
        return self.ROOT_BASE_IMG + paper_name + "_base.jpg"

