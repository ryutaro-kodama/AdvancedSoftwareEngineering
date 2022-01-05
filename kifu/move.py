from abc import ABCMeta, abstractmethod

from kifu.board import Board, Player
from kifu.piece_type import PieceType
from util import int2kansuji, int2zenkaku

class Move(metaclass=ABCMeta):
    @abstractmethod
    def move(self, board:Board, turn:Player, previous_move):
        pass

class NormalMove(Move):
    def __init__(self, turn, piece_type, x, y, old_x, old_y, is_promote):
        self.turn = turn
        self.piece_type = piece_type
        self.x = x
        self.y = y
        self.old_x = old_x
        self.old_y = old_y
        self.is_promote = is_promote

    def __str__(self):
        if self.is_promote:
            return f"{int2zenkaku(self.x)}{int2kansuji(self.y)}{PieceType.piece_type2str(self.piece_type)}" \
                    f"成({self.old_x}{self.old_y})"
        else:
            return f"{int2zenkaku(self.x)}{int2kansuji(self.y)}{PieceType.piece_type2str(self.piece_type)}" \
                    f"({self.old_x}{self.old_y})"

    def move(self, board:Board, turn:Player, previous_move:Move):
        # 移動元にある駒を取り出し、元の場所にはNoneを置いておく
        piece = board.get_piece(self.old_x, self.old_y)
        board.set_piece(self.old_x, self.old_y, None)
        assert piece.piece_type == self.piece_type

        # 移動先に駒があるか確認
        taken_piece = board.get_piece(self.x, self.y)
        if taken_piece != None:
            # 駒があったら手番の駒台に乗せる
            taken_piece.reset(turn)
            board.get_piece_in_hands(turn).take(taken_piece.piece_type)

        # "成"の場合は動かす駒を成らせる
        if self.is_promote:
            piece = piece.promote()

        # 移動先に駒を移動
        piece.move_to(self.x, self.y)
        board.set_piece(self.x, self.y, piece)


class SameMove(Move):
    def __init__(self, turn, piece_type, old_x, old_y, is_promote):
        self.turn = turn
        self.piece_type = piece_type
        self.old_x = old_x
        self.old_y = old_y
        self.is_promote = is_promote

    def __str__(self):
        if self.is_promote:
            return f"同　{PieceType.piece_type2str(self.piece_type)}成({self.old_x}{self.old_y})"
        else:
            return f"同　{PieceType.piece_type2str(self.piece_type)}({self.old_x}{self.old_y})"

    def move(self, board:Board, turn:Player, previous_move:Move):
        # 移動元にある駒を取り出し、元の場所にはNoneを置いておく
        piece = board.get_piece(self.old_x, self.old_y)
        board.set_piece(self.old_x, self.old_y, None)
        assert piece.piece_type == self.piece_type

        # 移動先の駒を取得
        taken_piece = board.get_piece(previous_move.x, previous_move.y)
        assert taken_piece != None
        
        # 手番の駒台に乗せる
        taken_piece.reset(turn)
        board.get_piece_in_hands(turn).take(taken_piece.piece_type)

        # "成"の場合は動かす駒を成らせる
        if self.is_promote:
            piece = piece.promote()

        # 移動先に駒を移動
        piece.move_to(previous_move.x, previous_move.y)
        board.set_piece(previous_move.x, previous_move.y, piece)


class DropMove(Move):
    def __init__(self, turn, piece_type, x, y):
        self.turn = turn
        self.piece_type = piece_type
        self.x = x
        self.y = y

    def __str__(self):
        return f"{int2zenkaku(self.x)}{int2kansuji(self.y)}{PieceType.piece_type2str(self.piece_type)}打"

    def move(self, board:Board, turn:Player, previous_move:Move):
        # 移動先に駒がないことを確認
        taken_piece = board.get_piece(self.x, self.y)
        assert taken_piece == None

        # 駒台から駒を取得
        drop_piece = board.piece_in_hands[turn].drop(self.piece_type, self.x, self.y, turn)
        
        # 移動先に駒を移動
        drop_piece.move_to(self.x, self.y)
        board.set_piece(self.x, self.y, drop_piece)