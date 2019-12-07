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
