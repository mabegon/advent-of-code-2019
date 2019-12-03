from unittest import TestCase
import day2


class TestComputeStack(TestCase):
    def test_computeStack_1(self):
        stack = [1,0,0,0,99]
        stackResult = day2.computeStack(stack)
        self.assertEqual([2,0,0,0,99], stackResult)

    def test_computeStack_2(self):
        stack = [2,3,0,3,99]
        stackResult = day2.computeStack(stack)
        self.assertEqual([2,3,0,6,99], stackResult)

    def test_computeStack_3(self):
        stack = [2,4,4,5,99,0]
        stackResult = day2.computeStack(stack)
        self.assertEqual([2,4,4,5,99,9801], stackResult)

    def test_computeStack_4(self):
        stack = [1,1,1,4,99,5,6,0,99]
        stackResult = day2.computeStack(stack)
        self.assertEqual([30,1,1,4,2,5,6,0,99], stackResult)

    def test_compute_answer_day_2_1(self):
        self.assertEqual(4690667, day2.answer_day_2_1())

