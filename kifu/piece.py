from abc import ABCMeta, abstractmethod

from kifu.piece_type import PieceType

class Piece(metaclass=ABCMeta):
    """
    各駒を表現するクラス
    """
    piece_type = None

    def __init__(self, x, y, player):
        # 座標
        self.x = x
        self.y = y
        # この駒の持ち手
        self.player = player
    
    def reset(self, player):
        """
        駒の座標をリセットし、持ち手をplayerにする
        """
        self.x = 0
        self.y = 0
        self.player = player
    
    def move_to(self, x, y):
        self.x = x
        self.y = y

    def promote(self):
        """
        成った後の駒のインスタンスを返す
        """
        assert 0


class Ou(Piece):
    piece_type = PieceType.OU

    def __str__(self):
        return "玉"


class Hisya(Piece):
    piece_type = PieceType.HISYA

    def __str__(self):
        return "飛"

    def promote(self) -> Piece:
        return Ryu(self.x, self.y, self.player)


class Ryu(Piece):
    piece_type = PieceType.RYU

    def __str__(self):
        return "竜"


class Kaku(Piece):
    piece_type = PieceType.KAKU

    def __str__(self):
        return "角"

    def promote(self) -> Piece:
        return Uma(self.x, self.y, self.player)


class Uma(Piece):
    piece_type = PieceType.UMA

    def __str__(self):
        return "馬"


class Kin(Piece):
    piece_type = PieceType.KIN

    def __str__(self):
        return "金"


class Gin(Piece):
    piece_type = PieceType.GIN

    def __str__(self):
        return "銀"

    def promote(self) -> Piece:
        return NariGin(self.x, self.y, self.player)


class NariGin(Piece):
    piece_type = PieceType.NARI_GIN

    def __str__(self):
        return "全"


class Keima(Piece):
    piece_type = PieceType.KEIMA

    def __str__(self):
        return "桂"

    def promote(self) -> Piece:
        return NariKei(self.x, self.y, self.player)


class NariKei(Piece):
    piece_type = PieceType.NARI_KEI

    def __str__(self):
        return "圭"


class Kyosya(Piece):
    piece_type = PieceType.KYOSYA

    def __str__(self):
        return "香"

    def promote(self) -> Piece:
        return NariKyo(self.x, self.y, self.player)


class NariKyo(Piece):
    piece_type = PieceType.NARI_KYO

    def __str__(self):
        return "杏"


class Fu(Piece):
    piece_type = PieceType.FU

    def __str__(self):
        return "歩"

    def promote(self) -> Piece:
        return To(self.x, self.y, self.player)


class To(Piece):
    piece_type = PieceType.TO

    def __str__(self):
        return "と"


class PieceFactory:
    @staticmethod
    def make(piece_type:PieceType, x, y, turn) -> Piece:
        convert = {
            PieceType.OU: Ou,
            PieceType.HISYA: Hisya,
            PieceType.RYU: Ryu,
            PieceType.KAKU: Kaku,
            PieceType.UMA: Uma,
            PieceType.KIN: Kin,
            PieceType.GIN: Gin,
            PieceType.NARI_GIN: NariGin,
            PieceType.KEIMA: Keima,
            PieceType.NARI_KEI: NariKei,
            PieceType.KYOSYA: Kyosya,
            PieceType.NARI_KYO: NariKyo,
            PieceType.FU: Fu,
            PieceType.TO: To
        }
        if piece_type in convert:
            return convert[piece_type](x, y, turn)
        else:
            assert 0