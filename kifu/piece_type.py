from enum import IntEnum, auto

class PieceType(IntEnum):
    OU = auto()
    HISYA = auto()
    RYU = auto()
    KAKU = auto()
    UMA = auto()
    KIN = auto()
    GIN = auto()
    NARI_GIN = auto()
    KEIMA = auto()
    NARI_KEI = auto()
    KYOSYA = auto()
    NARI_KYO = auto()
    FU = auto()
    TO = auto()

    @staticmethod
    def str2piece_type(piece_type_str):
        conversion = {
            "玉": PieceType.OU,
            "飛": PieceType.HISYA,
            "龍": PieceType.RYU,
            "竜": PieceType.RYU,
            "角": PieceType.KAKU,
            "馬": PieceType.UMA,
            "金": PieceType.KIN,
            "銀": PieceType.GIN,
            "成銀": PieceType.NARI_GIN,
            "全": PieceType.NARI_GIN,
            "桂": PieceType.KEIMA,
            "成桂": PieceType.NARI_KEI,
            "圭": PieceType.NARI_KEI,
            "香": PieceType.KYOSYA,
            "成香": PieceType.NARI_KYO,
            "杏": PieceType.NARI_KYO,
            "歩": PieceType.FU,
            "と": PieceType.TO
        }
        if piece_type_str in conversion:
            return conversion[piece_type_str]
        else:
            assert 0

    @staticmethod
    def piece_type2str(piece_type):
        conversion = {
            PieceType.OU : "玉",
            PieceType.HISYA : "飛",
            PieceType.RYU : "龍",
            PieceType.RYU : "竜",
            PieceType.KAKU : "角",
            PieceType.UMA : "馬",
            PieceType.KIN : "金",
            PieceType.GIN : "銀",
            PieceType.NARI_GIN : "成銀",
            PieceType.NARI_GIN : "全",
            PieceType.KEIMA : "桂",
            PieceType.NARI_KEI : "成桂",
            PieceType.NARI_KEI : "圭",
            PieceType.KYOSYA : "香",
            PieceType.NARI_KYO : "成香",
            PieceType.NARI_KYO : "杏",
            PieceType.FU : "歩",
            PieceType.TO : "と"
        }
        if piece_type in conversion:
            return conversion[piece_type]
        else:
            assert 0