from abc import ABCMeta, abstractmethod
import random
from typing import Tuple

from kifu.board import Board, Player
from kifu.move import Move, NormalMove

class EvaluatorBase(metaclass=ABCMeta):
    @abstractmethod
    def get_choices(self, board:Board) -> Tuple[Move, Move, Move]:
        """
        評価値を計算し、次の一手の選択肢を3つ返す
        """
        pass

class RandomEvaluator(EvaluatorBase):
    """
    ランダムに駒と移動先を選択する
    """

    def get_choices(self, board:Board, turn:Player):
        # 現在手番のプレイヤーの駒を全て取得
        pieces = []
        for line in board.board:
            for piece in line:
                if (piece is not None) and (piece.player == turn):
                    pieces.append(piece)
        
        move1 = self.get_choice(turn, pieces)
        move2 = self.get_choice(turn, pieces)
        move3 = self.get_choice(turn, pieces)

        return (move1, move2, move3)

    def get_choice(self, turn, pieces):
        index = random.randint(1, len(pieces)-1)
        piece = pieces[index]
        pieces.remove(piece)

        return NormalMove(
            turn, piece.piece_type, random.randint(1,9), random.randint(1,9), piece.x, piece.y, False
        )
