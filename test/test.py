import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


import unittest

from kifu.board import Player, PieceInHand, Board
from kifu.piece_type import PieceType

class TestBoard(unittest.TestCase):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_feature_one(self):
        pass


class TestPieceInHand(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.piece_in_hand = PieceInHand()

    def test_take(self):
        self.piece_in_hand.take(PieceType.HISYA)
        self.piece_in_hand.take(PieceType.HISYA)
        self.piece_in_hand.take(PieceType.KAKU)
        self.piece_in_hand.take(PieceType.GIN)
        self.piece_in_hand.take(PieceType.NARI_GIN)
        self.piece_in_hand.take(PieceType.NARI_GIN)
        self.piece_in_hand.take(PieceType.FU)
        self.piece_in_hand.take(PieceType.TO)

        self.assertEqual(self.piece_in_hand.piece_in_hand[PieceType.HISYA], 2)
        self.assertEqual(self.piece_in_hand.piece_in_hand[PieceType.KAKU], 1)
        self.assertEqual(self.piece_in_hand.piece_in_hand[PieceType.KIN], 0)
        self.assertEqual(self.piece_in_hand.piece_in_hand[PieceType.GIN], 3)
        self.assertEqual(self.piece_in_hand.piece_in_hand[PieceType.KEIMA], 0)
        self.assertEqual(self.piece_in_hand.piece_in_hand[PieceType.KYOSYA], 0)
        self.assertEqual(self.piece_in_hand.piece_in_hand[PieceType.FU], 2)

    def test_drop(self):
        self.piece_in_hand.take(PieceType.HISYA)
        self.piece_in_hand.take(PieceType.HISYA)
        self.piece_in_hand.take(PieceType.KAKU)
        self.piece_in_hand.take(PieceType.GIN)
        self.piece_in_hand.take(PieceType.NARI_GIN)
        self.piece_in_hand.take(PieceType.NARI_GIN)
        self.piece_in_hand.take(PieceType.FU)
        self.piece_in_hand.take(PieceType.TO)

        self.piece_in_hand.drop(PieceType.HISYA, -1, -1, Player.SENTE)
        self.piece_in_hand.drop(PieceType.NARI_GIN, -1, -1, Player.SENTE)
        self.piece_in_hand.drop(PieceType.FU, -1, -1, Player.SENTE)

        self.assertEqual(self.piece_in_hand.piece_in_hand[PieceType.HISYA], 1)
        self.assertEqual(self.piece_in_hand.piece_in_hand[PieceType.KAKU], 1)
        self.assertEqual(self.piece_in_hand.piece_in_hand[PieceType.KIN], 0)
        self.assertEqual(self.piece_in_hand.piece_in_hand[PieceType.GIN], 2)
        self.assertEqual(self.piece_in_hand.piece_in_hand[PieceType.KEIMA], 0)
        self.assertEqual(self.piece_in_hand.piece_in_hand[PieceType.KYOSYA], 0)
        self.assertEqual(self.piece_in_hand.piece_in_hand[PieceType.FU], 1)

if __name__ == "__main__":
    unittest.main()