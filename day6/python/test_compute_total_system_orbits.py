from unittest import TestCase

from day6.python.main import compute_total_system_orbits

class TestCompute_total_system_orbits(TestCase):
    def test_compute_total_system_orbits(self):
        total_expected = 0
        total = compute_total_system_orbits([])
        self.assertEqual(total_expected, total)

    def test_compute_total_system_orbits_should_return_1(self):
        input_data = ["COM)B"]
        total_expected = 1
        total = compute_total_system_orbits(input_data)
        self.assertEqual(total_expected, total)

    def test_compute_total_system_orbits_should_return_3(self):
        input_data = ["COM)B", "B)C"]
        total_expected = 3
        total = compute_total_system_orbits(input_data)
        self.assertEqual(total_expected, total)

    def test_compute_total_system_orbits_should_return_6(self):
        input_data = ["COM)B", "B)C", "C)D"]
        total_expected = 6
        total = compute_total_system_orbits(input_data)
        self.assertEqual(total_expected, total)

    def test_compute_total_system_orbits_should_return_42(self):
        input_data = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"]
        total_expected = 42
        total = compute_total_system_orbits(input_data)
        self.assertEqual(total_expected, total)