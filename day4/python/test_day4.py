from unittest import TestCase
import day4


class TestDay4(TestCase):
    def test_checkAdjacents_when_True(self):
        self.assertEqual(True, day4.checkAdjacents(123356))

    def test_checkAdjacents_when_False(self):
        self.assertEqual(False, day4.checkAdjacents(123456))

    def test_checkNeverDecrease_when_True(self):
        self.assertEqual(True, day4.checkNeverDecrease(112233))

    def test_checkNeverDecrease_when_False(self):
        self.assertEqual(False, day4.checkNeverDecrease(112213))

    def test_checkExactlyTwoAdjacents_when_True(self):
        self.assertEqual(True, day4.checkExactlyTwoAdjacents(112233))

    def test_checkExactlyTwoAdjacents_when_True2(self):
        self.assertEqual(True, day4.checkExactlyTwoAdjacents(122446))

    def test_checkExactlyTwoAdjacents_when_True3(self):
        self.assertEqual(True, day4.checkExactlyTwoAdjacents(122444))

    def test_checkExactlyTwoAdjacents_when_False(self):
        self.assertEqual(False, day4.checkExactlyTwoAdjacents(123444))

    def test_checkExactlyTwoAdjacents_when_False(self):
        self.assertEqual(False, day4.checkExactlyTwoAdjacents(688889))

