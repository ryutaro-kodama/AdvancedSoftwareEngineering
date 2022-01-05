import argparse

from evaluator.evaluator import RandomEvaluator
from kifu.board import Board
from kif_parser import KifParser
from emulator import Emulator

def set_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="specify the path to .kif file")
    parser.add_argument("turn_num", help="specify the turn")
    parser.set_defaults(func=main)

    args = parser.parse_args()
    return args

def main(arg):
    lines = load_kif_file(arg.path)

    kif_parser = KifParser()
    kifu_obj = kif_parser.parse(lines)

    board = Board()
    emulator = Emulator(kifu_obj, board)
    emulator.emulate(int(arg.turn_num))

    bod = board.make_bod()
    print(bod)

    evaluator = RandomEvaluator()
    choices = evaluator.get_choices(board, emulator.turn)

    for i, move in enumerate(choices):
        print(f"{i}: {move}")

def load_kif_file(path):
    with open(path, mode='r', encoding="utf-8") as f:
        lines = f.readlines()
    lines = [line.replace('\n', '') for line in lines]
    return lines

if __name__ == "__main__":
    args = set_arg_parser()
    args.func(args)