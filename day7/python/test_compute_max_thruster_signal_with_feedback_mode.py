from unittest import TestCase
from day7.python.main import compute_max_thruster_signal_with_feedback_mode


class TestCompute_max_thruster_signal_with_feedback_mode(TestCase):

    def test_compute_max_thruster_signal_with_feedback_mode_1(self):
        stack = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
        result = compute_max_thruster_signal_with_feedback_mode(stack, 9, 8, 7, 6, 45)
        self.assertEqual(139629729, result[0])
