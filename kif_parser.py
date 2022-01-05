import re

from kifu.kifu import Kifu
from kifu.handicap import Handicap
from kifu.move import NormalMove, SameMove, DropMove
from kifu.piece_type import PieceType
from util import kansuji2int, zenkaku2int

class KifParser:
    def parse(self, lines):
        """
        kifファイルのテキストを受け取り、parseしてKifuオブジェクトを返す
        """
        start_date = self.parse_start_date(lines)
        finish_date = self.parse_finish_date(lines)
        handicap = self.parse_handicap(lines)
        players = self.parse_players(lines)
        move_list = self.parse_move_list(lines)
        finish = self.parse_finish(lines)
        return Kifu(start_date, finish_date, handicap, players, move_list, finish)

    def parse_start_date(self, lines):
        for line in lines:
            if line.startswith("開始日時"):
                return line.replace("開始日時：", "")
        return ""

    def parse_finish_date(self, lines):
        for line in lines:
            if line.startswith("終了日時"):
                return line.replace("終了日時：", "")
        return ""

    def parse_handicap(self, lines):
        for line in lines:
            if line.startswith("手合割"):
                handicap_str = line.replace("手合割：", "")
                return Handicap.str2handicap(handicap_str)

    def parse_players(self, lines):
        result = {"先手": "", "後手": "", "上手": "", "下手": "", }
        for line in lines:
            if line.startswith("先手"):
                result["先手"] = line.replace("先手：", "")
            elif line.startswith("後手"):
                result["後手"] = line.replace("後手：", "")
            elif line.startswith("上手"):
                result["上手"] = line.replace("上手：", "")
            elif line.startswith("下手"):
                result["下手"] = line.replace("下手：", "")
        return result

    def parse_move_list(self, lines):
        result = []
        for line in lines:
            if re.match(r'[1-9]', line) is not None:
                line_splited = line.split(" ")
                move_str = line_splited[1]

                # 移動させた駒のparse
                piece_type_match = re.search(r'[玉|飛|龍|竜|角|馬|金|銀|成銀|全|桂|成桂|圭|香|成香|杏|歩|と]', move_str)
                if piece_type_match is None:
                    # "投了"等の指し手ではない場合
                    continue
                piece_type = PieceType.str2piece_type(piece_type_match.group())

                # 何手目かのparse
                turn = re.match(r'[1-9]{1,3}', line_splited[0])

                # 移動先座標のparse
                if re.search(r'[１|２|３|４|５|６|７|８|９][一|二|三|四|五|六|七|八|九]', move_str) is not None:
                    x = zenkaku2int(
                        re.search(r'[１|２|３|４|５|６|７|８|９]', move_str).group()
                    )
                    y = kansuji2int(
                        re.search(r'[一|二|三|四|五|六|七|八|九]', move_str).group()
                    )
                else:
                    x = 0
                    y = 0

                # 移動元座標のparse
                old_point = re.search(r'\([1-9][1-9]\)', move_str)
                if old_point is not None:
                    old_point_list = old_point.group()
                    old_x, old_y = int(old_point_list[1]), int(old_point_list[2])
                else:
                    old_x = 0
                    old_y = 0

                # 成のparse
                if "成" in move_str:
                    is_promote = True
                else:
                    is_promote = False

                if "同" in move_str:
                    move = SameMove(turn, piece_type, old_x, old_y, is_promote)
                elif "打" in move_str:
                    move = DropMove(turn, piece_type, x, y)
                else:
                    move = NormalMove(turn, piece_type, x, y, old_x, old_y, is_promote)
                result.append(move)
        return result

    def parse_finish(self, lines):
        for line in lines:
            finish_match = re.search(r"[中断|投了|持将棋|千日手|詰み|切れ負け|反則勝ち|反則負け|入玉勝ち|不戦勝|不戦敗]", line)
            if finish_match is not None:
                return finish_match.group()
            else:
                ""