import queue
from threading import Thread, RLock

OPCODE_EQUALS = 8
OPCODE_LESSTHAN = 7
OPCODE_JUMPIFFALSE = 6
OPCODE_OUTPUT = 4
OPCODE_INPUT = 3
OPCODE_MULTIPLY = 2
OPCODE_ADD = 1
OPCODE_JUMPIFTRUE = 5
OPCODE_HALT = 99

POSITION_MODE = 0


class Computer(Thread):

    def __init__(self, id, stack):
        Thread.__init__(self)
        self.stack = stack
        self.input_queue = queue.Queue()
        self.output_queue = queue.Queue()
        self.id = id


    def load_stack(self, filename):
        self.stack = self.get_memory_stack(filename)

    @staticmethod
    def get_memory_stack(filename):
        with open(filename) as fp:
            code = fp.read()
            stack_str = code.split(',')
            stack = [int(x) for x in stack_str]
            return stack

    def compute(self):
        self.compute_stack(self.stack)

    def compute_stack(self, stack_in, *inputs):
        stack = stack_in.copy()
        head_position = 0
        output_list = []
        input_values = list(inputs)
        opcode, param1_mode, param2_mode = self.decodeOpcodeAndParamModes(stack[head_position])

        while opcode != OPCODE_HALT:
            if opcode == OPCODE_ADD:
                stack, head_position = self.add(stack, head_position, param1_mode, param2_mode)
            elif opcode == OPCODE_MULTIPLY:
                stack, head_position = self.multiply(stack, head_position, param1_mode, param2_mode)
            elif opcode == OPCODE_INPUT:
                stack, head_position = self.opcode_input(stack, head_position, self.get_input_value())
            elif opcode == OPCODE_OUTPUT:
                head_position, output = self.opcode_output(stack, head_position)
                output_list.append(output)
            elif opcode == OPCODE_JUMPIFTRUE:
                head_position = self.jumpIfTrue(stack, head_position, param1_mode, param2_mode)
            elif opcode == OPCODE_JUMPIFFALSE:
                head_position = self.jumpIfFalse(stack, head_position, param1_mode, param2_mode)
            elif opcode == OPCODE_LESSTHAN:
                stack, head_position = self.opcode_lessThan(stack, head_position, param1_mode, param2_mode)
            elif opcode == OPCODE_EQUALS:
                stack, head_position = self.opcode_equals(stack, head_position, param1_mode, param2_mode)
            else:
                print("Stack error")
                break
            opcode, param1_mode, param2_mode = self.decodeOpcodeAndParamModes(stack[head_position])
        return stack, output_list

    def compute_stack_queue_version(self, stack_in):
        stack = stack_in.copy()
        head_position = 0
        opcode, param1_mode, param2_mode = self.decodeOpcodeAndParamModes(stack[head_position])

        while opcode != OPCODE_HALT:
            if opcode == OPCODE_ADD:
                stack, head_position = self.add(stack, head_position, param1_mode, param2_mode)
            elif opcode == OPCODE_MULTIPLY:
                stack, head_position = self.multiply(stack, head_position, param1_mode, param2_mode)
            elif opcode == OPCODE_INPUT:
                stack, head_position = self.opcode_input(stack, head_position)
            elif opcode == OPCODE_OUTPUT:
                head_position, output = self.opcode_output(stack, head_position)
            elif opcode == OPCODE_JUMPIFTRUE:
                head_position = self.jumpIfTrue(stack, head_position, param1_mode, param2_mode)
            elif opcode == OPCODE_JUMPIFFALSE:
                head_position = self.jumpIfFalse(stack, head_position, param1_mode, param2_mode)
            elif opcode == OPCODE_LESSTHAN:
                stack, head_position = self.opcode_lessThan(stack, head_position, param1_mode, param2_mode)
            elif opcode == OPCODE_EQUALS:
                stack, head_position = self.opcode_equals(stack, head_position, param1_mode, param2_mode)
            else:
                print("Stack error")
                break
            opcode, param1_mode, param2_mode = self.decodeOpcodeAndParamModes(stack[head_position])
        return stack

    def get_input_value_old(self, inputs):
        if len(inputs) > 0:
            input_value = inputs.pop(0)
        else:
            input_value = ""
        return input_value

    def get_input_value(self):
      #  print(str.format("[{}] Getting Input Value", self.id))
        input_value = self.input_queue.get(True)
       # print(str.format("[{}] Input Value: {}", self.id, input_value))
        return input_value


    def add(self, stack, head_position, param1_mode, param2_mode):
        op1, op2, store_position = self.getOperationValues(head_position, param1_mode, param2_mode, stack)

        stack[store_position] = op1 + op2
        return stack, head_position + 4

    def multiply(self, stack, head_position, param1_mode, param2_mode):
        op1, op2, store_position = self.getOperationValues(head_position, param1_mode, param2_mode, stack)
        stack[store_position] = op1 * op2
        return stack, head_position + 4

    def opcode_input(self, stack, head_position):
        value = self.get_input_value()
        position = stack[head_position+1]
        stack[position] = int(value)

        return stack, head_position + 2

    def opcode_output(self, stack, head_position):
        position = stack[head_position + 1]
        value = stack[position]
        self.output_queue.put(value, False)
        return head_position + 2, value

    def jumpIfTrue(self, stack, head_position, param1_mode, param2_mode):

        condValue, jumpValue = self.getJumpOperationValues(head_position, param1_mode, param2_mode, stack)

        if condValue > 0:
            return jumpValue
        else:
            return head_position + 3


    def jumpIfFalse(self, stack, head_position, param1_mode, param2_mode):

        condValue, jumpValue = self.getJumpOperationValues(head_position, param1_mode, param2_mode, stack)

        if condValue == 0:
            return jumpValue
        else:
            return head_position + 3

    def opcode_lessThan(self, stack, head_position, param1_mode, param2_mode):
        op1, op2, store_position = self.getOperationValues(head_position, param1_mode, param2_mode, stack)

        if op1 < op2:
            stack[store_position] = 1
        else:
            stack[store_position] = 0

        return stack, head_position + 4



    def opcode_equals(self, stack, head_position, param1_mode, param2_mode):
        op1, op2, store_position = self.getOperationValues(head_position, param1_mode, param2_mode, stack)

        if op1 == op2:
            stack[store_position] = 1
        else:
            stack[store_position] = 0

        return stack, head_position + 4

    def getJumpOperationValues(self, head_position, param1_mode, param2_mode, stack):
        conditionParam = stack[head_position + 1]
        jumpToParam = stack[head_position + 2]
        if param1_mode == POSITION_MODE:
            condValue = stack[conditionParam]
        else:
            condValue = conditionParam
        if param2_mode == POSITION_MODE:
            jumpValue = stack[jumpToParam]
        else:
            jumpValue = jumpToParam
        return condValue, jumpValue

    def decodeOpcodeAndParamModes(self, stack_value):

        stack_value_str = str(stack_value)
        if len(stack_value_str) <= 2:
           opcode = int(stack_value_str)
        else:
           opcode = int(stack_value_str[-1])

        param1_mode = POSITION_MODE
        param2_mode = POSITION_MODE

        if len(stack_value_str) >= 3:
            param1_mode = int(stack_value_str[-3])
        if len(stack_value_str) >= 4:
            param2_mode = int(stack_value_str[-4])

        return (opcode, param1_mode, param2_mode)

    def getOperationValues(self, head_position, param1_mode, param2_mode, stack):
        op1Value, op2Value, store_position = self.getStackParameters(head_position, stack)

        if param1_mode == POSITION_MODE:
            op1 = stack[op1Value]
        else:
            op1 = op1Value
        if param2_mode == POSITION_MODE:
            op2 = stack[op2Value]
        else:
            op2 = op2Value
        return op1, op2, store_position

    def getStackParameters(self, head_position, stack):
        op1Position = stack[head_position + 1]
        op2Position = stack[head_position + 2]
        store_position = stack[head_position + 3]
        return op1Position, op2Position, store_position

    def run(self) -> None:
        self.compute_stack_queue_version(self.stack)