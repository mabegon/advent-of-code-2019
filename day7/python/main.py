from day7.python.computer import Computer

def main():
    stack = Computer.get_memory_stack("../input.txt")

    result = compute_max_thruster_signal(stack)

    print (str.format("The answer of part 1 is : {}", result))


def compute_max_thruster_signal(stack, *phase_settings):
    amp_a = Computer()
    amp_b = Computer()
    amp_c = Computer()
    amp_d = Computer()
    amp_e = Computer()

    a_stack, a_output = amp_a.compute_stack(stack, phase_settings[0], 0)
    b_stack, b_output = amp_b.compute_stack(stack, phase_settings[1], a_output[0])
    c_stack, c_output = amp_c.compute_stack(stack, phase_settings[2], b_output[0])
    d_stack, d_output = amp_d.compute_stack(stack, phase_settings[3], c_output[0])
    e_stack, e_output = amp_e.compute_stack(stack, phase_settings[4], d_output[0])
    return e_output


if __name__ == '__main__':
    main()