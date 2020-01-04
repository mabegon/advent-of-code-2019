from unittest import TestCase
from day8.python.main import get_layers, count_digits_of_layer, get_fewer_zeros_layer, flat_layers


class Test(TestCase):
    def test_get_layers(self):

        input_value = "123456789012"
        image_wide = 3
        image_tall = 2
        result_expected = [["123", "456"], ["789", "012"]]

        result = get_layers(image_tall, image_wide, input_value)
        self.assertEqual(result_expected, result)


    def test_count_zeros_of_layer_return_0(self):
        input_value = ["123", "456"]
        result_expected = 0
        result = 0
        result = count_digits_of_layer(input_value,"0")
        self.assertEqual(result_expected, result)

    def test_count_zeros_of_layer_return_1(self):
        input_value = ["123", "406"]
        result_expected = 1
        result = count_digits_of_layer(input_value,"0")
        self.assertEqual(result_expected, result)

    def test_count_zeros_of_layer_return_3(self):
        input_value = ["103", "006"]
        result_expected = 3
        result = count_digits_of_layer(input_value,"0")
        self.assertEqual(result_expected, result)

    def test_fewer_zeros_layer_return_1(self):
        input_value = [["123", "456"], ["789", "012"]]
        result_expected = 1
        result_layer = get_fewer_zeros_layer(input_value)
        self.assertEqual(result_layer, result_expected)


    def test_fewer_zeros_layer_return_1_also(self):
        input_value = [["123", "456"], ["789", "212"], ["789", "212"]]
        result_expected = 1
        result_layer = get_fewer_zeros_layer(input_value)
        self.assertEqual(result_layer, result_expected)

    def test_fewer_zeros_layer_return_2(self):
        input_value = [["103", "450"], ["789", "012"]]
        result_expected = 2
        result_layer = get_fewer_zeros_layer(input_value)
        self.assertEqual(result_layer, result_expected)

    def test_flat_layers(self):
        input_value = [["02","22"],["11","22"],["22","12"],["00","00"]]
        image_wide = 2
        image_tall = 2
        result_expected = ["01", "10"]

        result = flat_layers(input_value)

        self.assertEqual(result_expected, result)

