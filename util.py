def kansuji2int(kansuji):
    convert = {
        "一": 1,
        "二": 2,
        "三": 3,
        "四": 4,
        "五": 5,
        "六": 6,
        "七": 7,
        "八": 8,
        "九": 9
    }
    if kansuji in convert:
        return convert[kansuji]
    else:
        assert 0

def int2kansuji(int_):
    convert = {
        1 : "一",
        2 : "二",
        3 : "三",
        4 : "四",
        5 : "五",
        6 : "六",
        7 : "七",
        8 : "八",
        9 : "九",
        10 : "十",
        11 : "十一",
        12 : "十二",
        13 : "十三",
        14 : "十四",
        15 : "十五",
        16 : "十六",
        17 : "十七",
        18 : "十八"
    }
    if int_ in convert:
        return convert[int_]
    else:
        assert 0

def zenkaku2int(zenkaku):
    convert = {
        "１": 1,
        "２": 2,
        "３": 3,
        "４": 4,
        "５": 5,
        "６": 6,
        "７": 7,
        "８": 8,
        "９": 9
    }
    if zenkaku in convert:
        return convert[zenkaku]
    else:
        assert 0

def int2zenkaku(int_):
    convert = {
        1: "１",
        2: "２",
        3: "３",
        4: "４",
        5: "５",
        6: "６",
        7: "７",
        8: "８",
        9: "９"
    }
    if int_ in convert:
        return convert[int_]
    else:
        assert 0