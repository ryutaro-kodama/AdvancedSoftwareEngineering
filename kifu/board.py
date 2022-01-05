from enum import IntEnum, auto

from .piece_type import PieceType
from .piece import *
from util import int2kansuji

class Player(IntEnum):
    SENTE = auto()
    GOTE = auto()

    @staticmethod
    def change_turn(player):
        if player == Player.SENTE:
            return Player.GOTE
        elif player == Player.GOTE:
            return Player.SENTE
        else:
            assert 0


class PieceInHand:
    def __init__(self, ou=0, hisya=0, kaku=0, kin=0, gin=0, keima=0, kyosya=0, fu=0):
        self.piece_in_hand = {
            PieceType.OU: ou,
            PieceType.HISYA: hisya,
            PieceType.KAKU: kaku,
            PieceType.KIN: kin,
            PieceType.GIN: gin,
            PieceType.KEIMA: keima,
            PieceType.KYOSYA: kyosya,
            PieceType.FU: fu
        }

    def take(self, piece_type:PieceType):
        """
        piece_typeの種類の駒の駒台にある数を1つ増やす
        """
        demote = {
            PieceType.RYU: PieceType.HISYA,
            PieceType.UMA: PieceType.KAKU,
            PieceType.NARI_GIN: PieceType.GIN,
            PieceType.NARI_KEI: PieceType.KEIMA,
            PieceType.NARI_KYO: PieceType.KYOSYA,
            PieceType.TO: PieceType.FU,
        }
        if piece_type in demote:
            # 成った駒を取ったなら、成った状態を戻す
            piece_type = demote[piece_type]

        assert piece_type in self.piece_in_hand
        self.piece_in_hand[piece_type] += 1

    def drop(self, piece_type:PieceType, x, y, turn:Player) -> Piece:
        """
        piece_typeの種類の駒の駒台にある数を1つ減らし、その駒のインスタンスを返す
        """
        assert piece_type in self.piece_in_hand
        assert self.piece_in_hand[piece_type] > 0
        self.piece_in_hand[piece_type] -= 1

        drop_piece = PieceFactory.make(piece_type, x, y, turn)

        return drop_piece

    def make_bod(self):
        """
        駒台の状況をbod形式のstringで返す
        """
        str_ = ""

        for piece_type, piece_num in self.piece_in_hand.items():
            if piece_num > 0:
                piece_str = PieceType.piece_type2str(piece_type)
                if piece_num >= 1:
                    piece_str += int2kansuji(piece_num)
                piece_str += "　"

        if str_ == "":
            str_ = "なし"

        return str_


class Board:
    def __init__(self):
        sente = Player.SENTE
        gote = Player.GOTE

        # 右上が(1,1)になるような、9*9の座標
        self.board = [
            [Kyosya(9,1,gote),  Keima(8,1,gote),  Gin(7,1,gote),  Kin(6,1,gote),  Ou(5,1,gote),  Kin(4,1,gote),  Gin(3,1,gote),  Keima(2,1,gote),  Kyosya(1,1,gote) ],
            [None,              Hisya(8,2,gote),  None,           None,           None,          None,           None,           Kaku(2,2,gote),   None             ],
            [Fu(9,3,gote),      Fu(8,3,gote),     Fu(7,3,gote),   Fu(6,3,gote),   Fu(5,3,gote),  Fu(4,3,gote),   Fu(3,3,gote),   Fu(2,3,gote),     Fu(1,3,gote)     ],
            [None,              None,             None,           None,           None,          None,           None,           None,             None             ],
            [None,              None,             None,           None,           None,          None,           None,           None,             None             ],
            [None,              None,             None,           None,           None,          None,           None,           None,             None             ],
            [Fu(9,7,sente),     Fu(8,7,sente),    Fu(7,7,sente),  Fu(6,7,sente),  Fu(5,7,sente), Fu(4,7,sente),  Fu(3,7,sente),  Fu(2,7,sente),    Fu(1,7,sente)    ],
            [None,              Kaku(8,8,sente),  None,           None,           None,          None,           None,           Hisya(2,8,sente), None             ],
            [Kyosya(9,9,sente), Keima(8,9,sente), Gin(7,9,sente), Kin(6,9,sente), Ou(5,9,sente), Kin(4,9,sente), Gin(3,9,sente), Keima(2,9,sente), Kyosya(1,9,sente)]
        ]
        # 先手と後手の駒台上の駒を保持
        self.piece_in_hands = {sente: PieceInHand(), gote: PieceInHand()}

    def get_piece(self, x, y) -> Piece:
        return self.board[y-1][9-x]

    def set_piece(self, x, y, piece:Piece):
        self.board[y-1][9-x] = piece
    
    def get_piece_in_hands(self, player:Player) -> PieceInHand:
        return self.piece_in_hands[player]

    def make_bod(self):
        """
        BOD形式の盤面を作成する
        """
        str_ = ""
        str_ += "後手の持駒：" + self.get_piece_in_hands(Player.GOTE).make_bod() + '\n'
        str_ += " ９ ８ ７ ６ ５ ４ ３ ２ １  \n"
        str_ += "+--------------------------+\n"

        for i, line in enumerate(self.board):
            target = "|"
            for piece in line:
                if piece == None:
                    target += " ・"
                else:
                    if piece.player == Player.SENTE:
                        target += " "
                    else:
                        # 後手ならば"v"を追加
                        target += "v"
                    target += str(piece)
            target += "|" + int2kansuji(i+1)

            str_ += target + '\n'
        
        str_ += "+--------------------------+\n"
        str_ += "先手の持駒：" + self.get_piece_in_hands(Player.SENTE).make_bod() + '\n'

        return str_