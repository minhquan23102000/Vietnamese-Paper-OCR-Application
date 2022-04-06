class CCCD(object):
    ROIS = {
        "id": [(456, 308, 403, 53)],
        "name": [
            (325, 393, 771, 64),
        ],
        "birth_date": [(658, 451, 216, 54)],
        "gender": [(538, 495, 95, 44)],
        "address": [(786, 639, 343, 39), (318, 672, 791, 52)],
        "place_birth": [(326, 586, 792, 47)],
        "date_expire": [(155, 653, 152, 31)],
    }

    CHECK_ROI = (313, 174, 597, 63)
    
    NOT_PREPROCESSOR = ['date_expire']
    
class HOCBA(object):
    ROIS = {
        "name": [(340, 699, 574, 111)],
        "gender": [(1402, 706, 162, 119)],
        "birthday": [(368, 818, 395, 57)],
        "place_birth": [(368, 894, 217, 77)],
        "ethnic": [(344, 956, 108, 100)],
        "address": [(370, 1117, 884, 100)],
        "name_father": [(370, 1202, 398, 99)],
        "job_father": [(1396, 1209, 312, 96)],
        "name_morther": [(374, 1286, 366, 96)],
        "job_morther":[(1400, 1286, 161, 96)],
        "address_notice": [(370, 1117, 884, 100)],
        "graduate_date": [(222, 2572, 120, 69)],
        "year_infor_10": [(90, 2357, 237, 81)],
        "class_infor_10": [(443, 2369, 97, 61)],
        "school_infor_10": [(604, 2576, 809, 50)],
        "year_infor_11": [(97, 2461, 234, 80)],
        "class_infor_11": [(443, 2480, 101, 50)],
        "school_infor_11": [(604, 2472, 809, 73)],
        "year_infor_12": [(97, 2561, 238, 84)],
        "class_infor_12": [(439, 2572, 109, 62)],
        "school_infor_12": [(602, 2365, 811, 57)]
    }
    CHECK_ROI = (824, 334, 647, 203)
