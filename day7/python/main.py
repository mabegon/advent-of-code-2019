from day7.python.computer import Computer
from itertools import permutations

def main():
    stack = Computer.get_memory_stack("../input.txt")
    result = 0
    for i in permutations([0,1,2,3,4]):
        partial_result = compute_max_thruster_signal(stack, i[0], i[1], i[2], i[3], i[4])
        if partial_result > result:
            result = partial_result
            print(str.format("Result {} for phases {},{},{},{},{}", result,i[0], i[1], i[2], i[3], i[4]))

    print(str.format("The answer of part 1 is : {}", result))

    for i in permutations([5,6,7,8,9]):
        partial_result = compute_max_thruster_signal_with_feedback_mode(stack, i[0], i[1], i[2], i[3], i[4])
        if partial_result > result:
            result = partial_result
            print(str.format("Result {} for phases {},{},{},{},{}", result,i[0], i[1], i[2], i[3], i[4]))

    print(str.format("The answer of part 2 is : {}", result))


def compute_max_thruster_signal(stack, *phase_settings):
    amp_a = Computer("Amp A", stack)
    amp_b = Computer("Amp B", stack)
    amp_c = Computer("Amp C", stack)
    amp_d = Computer("Amp D", stack)
    amp_e = Computer("Amp E", stack)

    amp_a.input_queue.put(phase_settings[0])
    amp_a.input_queue.put(0)

    amp_b.input_queue = amp_a.output_queue
    amp_c.input_queue = amp_b.output_queue
    amp_d.input_queue = amp_c.output_queue
    amp_e.input_queue = amp_d.output_queue

    amp_b.input_queue.put(phase_settings[1])
    amp_c.input_queue.put(phase_settings[2])
    amp_d.input_queue.put(phase_settings[3])
    amp_e.input_queue.put(phase_settings[4])

    amp_a.start()
    amp_b.start()
    amp_c.start()
    amp_d.start()
    amp_e.start()

    result = amp_e.output_queue.get(True)

    amp_a.join()
    amp_b.join()
    amp_c.join()
    amp_d.join()
    amp_e.join()

    return result


def compute_max_thruster_signal_with_feedback_mode(stack, *phase_settings):
    amp_a = Computer("Amp A", stack)
    amp_b = Computer("Amp B", stack)
    amp_c = Computer("Amp C", stack)
    amp_d = Computer("Amp D", stack)
    amp_e = Computer("Amp E", stack)

    amp_a.input_queue.put(phase_settings[0])
    amp_a.input_queue.put(0)

    amp_b.input_queue = amp_a.output_queue
    amp_c.input_queue = amp_b.output_queue
    amp_d.input_queue = amp_c.output_queue
    amp_e.input_queue = amp_d.output_queue

    amp_b.input_queue.put(phase_settings[1])
    amp_c.input_queue.put(phase_settings[2])
    amp_d.input_queue.put(phase_settings[3])
    amp_e.input_queue.put(phase_settings[4])

    amp_a.start()
    amp_b.start()
    amp_c.start()
    amp_d.start()
    amp_e.start()

    result = 0
    while amp_e.is_alive():
        result = amp_e.output_queue.get(True)
        amp_a.input_queue.put(int(result))

    amp_a.join()
    amp_b.join()
    amp_c.join()
    amp_d.join()
    amp_e.join()

    return result


if __name__ == '__main__':
    main()