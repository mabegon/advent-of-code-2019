from unittest import TestCase

from day7.python.main import compute_max_thruster_signal


class TestCompute_max_thruster_signal(TestCase):
    def test_compute_max_thruster_signal(self):

        stack = ["3","15","3","16","1002","16","10","16","1","16","15","15","4","15","99","0","0"]
        result = compute_max_thruster_signal(stack, 4, 3, 2, 1, 0)
        self.assertEqual("43210", result[0])


    def test_compute_max_thruster_signal_2(self):

        stack = ["3","23","3","24","1002","24","10","24","1002","23","-1","23","101","5","23","23","1","24","23","23","4","23","99","0","0"]
        result = compute_max_thruster_signal(stack, 0, 1, 2, 3, 4)
        self.assertEqual("54321", result[0])