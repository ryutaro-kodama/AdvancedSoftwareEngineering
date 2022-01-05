from enum import IntEnum, auto

class Handicap(IntEnum):
    HIRATE = auto()
    KYO = auto()
    MIGI_KYO = auto()
    KAKU = auto()
    HISYA = auto()
    HI_KYO = auto()
    NIMAI = auto()
    SANMAI = auto()
    YONMAI = auto()
    GOMAI = auto()
    HIDARI_GOMAI = auto()
    ROKUMAI = auto()
    HIDARI_NANAMAI = auto()
    MIGI_NANAMAI = auto()
    HATIMAI = auto()
    JYUMAI = auto()
    ELSE = auto()

    @staticmethod
    def str2handicap(handicap_str):
        conversion = {
            "平手": Handicap.HIRATE,
            "香落ち": Handicap.KYO,
            "右香落ち": Handicap.MIGI_KYO,
            "角落ち": Handicap.KAKU,
            "飛車落ち": Handicap.HISYA,
            "飛香落ち": Handicap.HI_KYO,
            "二枚落ち": Handicap.NIMAI,
            "三枚落ち": Handicap.SANMAI,
            "四枚落ち": Handicap.YONMAI,
            "五枚落ち": Handicap.GOMAI,
            "左五枚落ち": Handicap.HIDARI_GOMAI,
            "六枚落ち": Handicap.ROKUMAI,
            "左七枚落ち": Handicap.HIDARI_NANAMAI,
            "右七枚落ち": Handicap.MIGI_NANAMAI,
            "八枚落ち": Handicap.HATIMAI,
            "十枚落ち": Handicap.JYUMAI,
            "その他": Handicap.ELSE
        }
        if handicap_str in conversion:
            return conversion[handicap_str]
        else:
            return Handicap.ELSE