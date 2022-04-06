from constant.roi_constant import CCCD, HOCBA


class Detector(object):

    ROOT_BASE_IMG = "constant/base_img/"

    def paper_detect(self, paper_name):
        result = {"paper": None, "base_img": None, "roi": None}
        if paper_name == "cccd":
            result["paper"] = "cccd"
            result["roi"] = CCCD

        if paper_name == "hocba":
            result["paper"] = "hocba"
            result["roi"] = HOCBA

        result["base_img"] = self.get_base_img(paper_name)
        return result

    def get_base_img(self, paper_name):
        return self.ROOT_BASE_IMG + paper_name + "_base.jpg"
