from unittest import TestCase
import day1


class TestCalculateFuelIncludingFuelMass(TestCase):
    def test_calculateFuelIncludingFuelMass_with_initial_mass_of_14(self):
        self.assertEqual(2, day1.calculateFuelIncludingFuelMass(14))

    def test_calculateFuelIncludingFuelMass_with_initial_mass_of_1969(self):
        self.assertEqual(966, day1.calculateFuelIncludingFuelMass(1969))

    def test_calculateFuelIncludingFuelMass_with_initial_mass_of_100756(self):
        self.assertEqual(50346, day1.calculateFuelIncludingFuelMass(100756))