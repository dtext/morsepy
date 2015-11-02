from unittest import TestCase
from src.morsepy.morsetree import MorseTree

__author__ = 'dt'


class TestMorseTree(TestCase):

    def setUp(self):
        super().setUp()
        self.mt = MorseTree()
        self.table = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--.."
        }
        self.inv_table = {v: k for k, v in self.table.items()}

    def test_encode(self):
        for char, seq in self.table.items():
            self.assertEqual(self.mt.encode(char), seq)

    def test_decode(self):
        for seq, char in self.inv_table.items():
            self.assertEqual(self.mt.decode(seq), char)

    def test_parse(self):
        self.assertEqual(self.mt.parse("... --- .../... --- ..."), "SOS SOS")
