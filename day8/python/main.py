filepath = '../input.txt'


def get_layers(image_tall, image_wide, input_value):
    result_1 = [input_value[i:i + image_wide] for i in range(0, len(input_value), image_wide)]
    result = [list(result_1[i:i + image_tall]) for i in range(0, len(result_1), image_tall)]
    return result

def count_digits_of_layer(input_value, digit):
    result = 0
    for i in input_value:
        result += i.count(digit)
    return result

def get_fewer_zeros_layer(input_value):
    result_layer = 0
    result_number = float("inf")
    for i in range(0, len(input_value)):
        zeros = count_digits_of_layer(input_value[i], "0")
        if zeros < result_number:
            result_layer = i + 1
            result_number = zeros
    return result_layer

def main():
    with open(filepath) as fp:
        image = fp.read()
        layers = get_layers(6,25, image)
        fewer_zeros_layer = get_fewer_zeros_layer(layers)
        layer = layers[fewer_zeros_layer-1]
        one_digits = count_digits_of_layer(layer, "1")
        two_digits = count_digits_of_layer(layer, "2")
        print(layer)
        print(one_digits * two_digits)


if __name__ == '__main__':
    main()
