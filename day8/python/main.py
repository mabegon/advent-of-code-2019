filepath = '../input.txt'
BLACK = "0"
WHITE = "1"
TRANS = "2"

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

def print_data_layer(layer):
    for i in layer:
        print(i)

def print_layer(layer):
    for i in layer:
        pretty_line = []
        for char in list(i):
            if char == BLACK:
                pretty_line.append("  ")
            else:
                pretty_line.append("# ")
        print("".join(pretty_line))

def flat_layers(input_value):
    result = input_value[0]
    for layer_index in range(1, len(input_value)):
        layer = input_value[layer_index]
        for line_index in range(0, len(layer)):
            line = layer[line_index]
            for char_index in range(0, len(line)):
                char_value = line[char_index]
                if char_value != "2" and result[line_index][char_index] == "2":
                    result_line = list(result[line_index])
                    result_line[char_index] = char_value
                    result[line_index] = "".join(result_line)
    return result

def main():
    with open(filepath) as fp:
        image = fp.read()
        layers = get_layers(6,25, image)
        fewer_zeros_layer = get_fewer_zeros_layer(layers)
        layer = layers[fewer_zeros_layer-1]
        one_digits = count_digits_of_layer(layer, "1")
        two_digits = count_digits_of_layer(layer, "2")
        print_data_layer(layer)
        print(one_digits * two_digits)
        print("PART TWO")
        result = flat_layers(layers)
        print_layer(result)


if __name__ == '__main__':
    main()


