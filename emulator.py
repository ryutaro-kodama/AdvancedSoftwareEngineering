from kifu.board import Player
from kifu.move import NormalMove, DropMove

class Emulator:
    def __init__(self, kifu_obj, board, turn=Player.SENTE):
        self.kifu_obj = kifu_obj
        self.board = board
        self.turn = turn
        self.previous_move = None

    def emulate(self, turn_num):
        """
        self.boradをturn_num手数分進める
        """
        assert (0 <= turn_num) and (turn_num <= len(self.kifu_obj.move_list)+1)

        for move in self.kifu_obj.move_list[:turn_num]:
            # board上の駒を動かす
            move.move(self.board, self.turn, self.previous_move)

            # "同"の処理のためにインスタンスを保存
            if isinstance(move, NormalMove) or isinstance(move, DropMove):
                self.previous_move = move

            # 現在の手番を入れ替える
            self.turn = Player.change_turn(self.turn)
