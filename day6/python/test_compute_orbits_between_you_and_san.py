from unittest import TestCase

from day6.python.main import compute_orbits_between_you_and_san


class TestCompute_orbits_between_you_and_san(TestCase):
    def test_compute_orbits_between_you_and_san_should_return_0(self):
        input_data = ["COM)I", "I)YOU", "I)SAN"]
        total_expected = 0
        total = compute_orbits_between_you_and_san(input_data)
        self.assertEqual(total_expected, total)

    def test_compute_orbits_between_you_and_san_should_return_1(self):
        input_data = ["COM)K", "K)I", "K)YOU", "I)SAN"]
        total_expected = 1
        total = compute_orbits_between_you_and_san(input_data)
        self.assertEqual(total_expected, total)

    def test_compute_orbits_between_you_and_san_should_return_4(self):
        input_data = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L", "K)YOU", "I)SAN"]
        total_expected = 4
        total = compute_orbits_between_you_and_san(input_data)
        self.assertEqual(total_expected, total)