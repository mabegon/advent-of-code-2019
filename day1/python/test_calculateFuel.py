from unittest import TestCase
import day1


class TestCalculateFuel(TestCase):
    def test_calculateFuel_with_mass_is_12(self):
        self.assertEqual(day1.calculateFuel(12),2)

    def test_calculateFuel_with_mass_is_14(self):
        self.assertEqual(day1.calculateFuel(14),2)

    def test_calculateFuel_with_mass_is_1969(self):
        self.assertEqual(day1.calculateFuel(1969), 654)

    def test_calculateFuel_with_mass_is_100756(self):
        self.assertEqual(day1.calculateFuel(100756), 33583)