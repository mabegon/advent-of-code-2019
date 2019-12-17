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


class Computer(object):

    def __init__(self):
        self.stack = []

    def load_stack(self, filename):
        self.stack = self.get_memory_stack(filename)

    @staticmethod
    def get_memory_stack(filename):
        with open(filename) as fp:
            code = fp.read()
            stack = code.split(',')
            return stack

    def compute(self):
        self.compute_stack(self.stack)

    def compute_stack(self, stack_in, *inputs):
        stack = stack_in.copy()
        head_position = 0
        output_list = []
        opcode, param1Mode, param2Mode = self.decodeOpcodeAndParamModes(stack[head_position])

        while opcode != OPCODE_HALT:
            if opcode == OPCODE_ADD:
                stack, head_position = self.add(stack, head_position, param1Mode, param2Mode)
            elif opcode == OPCODE_MULTIPLY:
                stack, head_position = self.multiply(stack, head_position, param1Mode, param2Mode)
            elif opcode == OPCODE_INPUT:
                stack, head_position = self.opcode_input(stack, head_position, self.get_input_value(inputs))
            elif opcode == OPCODE_OUTPUT:
                head_position, output = self.opcode_output(stack, head_position)
                output_list.append(output)
            elif opcode == OPCODE_JUMPIFTRUE:
                head_position = self.jumpIfTrue(stack, head_position, param1Mode, param2Mode)
            elif opcode == OPCODE_JUMPIFFALSE:
                head_position = self.jumpIfFalse(stack, head_position, param1Mode, param2Mode)
            elif opcode == OPCODE_LESSTHAN:
                stack, head_position = self.opcode_lessThan(stack, head_position, param1Mode, param2Mode)
            elif opcode == OPCODE_EQUALS:
                stack, head_position = self.opcode_equals(stack, head_position, param1Mode, param2Mode)
            else:
                print("Stack error")
                break
            opcode, param1Mode, param2Mode = self.decodeOpcodeAndParamModes(stack[head_position])
        return stack, output_list

    def get_input_value(self, inputs):
        if len(inputs) > 0:
            input_value = list(inputs).pop(0)
        else:
            input_value = ""
        return input_value

    def add(self, stack, headPosition, param1Mode, param2Mode):
        op1, op2, storePosition = self.getOperationValues(headPosition, param1Mode, param2Mode, stack)

        stack[storePosition] = str(op1 + op2)
        return stack, headPosition + 4

    def multiply(self, stack, head_position, param1Mode, param2Mode):
        op1, op2, storePosition = self.getOperationValues(head_position, param1Mode, param2Mode, stack)
        stack[storePosition] = str(op1 * op2)
        return stack, head_position + 4

    def opcode_input(self, stack, headPosition, value):

        if value == "":
            value = input("Enter value: ")

        position = int(stack[headPosition+1])
        stack[position] = value
        return stack, headPosition + 2

    def opcode_output(self, stack, headPosition):
        position = int(stack[headPosition + 1])
        value = stack[position]
        return headPosition + 2, value

    def jumpIfTrue(self, stack, headPosition, param1Mode, param2Mode):

        condValue, jumpValue = self.getJumpOperationValues(headPosition, param1Mode, param2Mode, stack)

        if condValue > 0:
            return jumpValue
        else:
            return headPosition + 3


    def jumpIfFalse(self, stack, headPosition, param1Mode, param2Mode):

        condValue, jumpValue = self.getJumpOperationValues(headPosition, param1Mode, param2Mode, stack)

        if condValue == 0:
            return jumpValue
        else:
            return headPosition + 3

    def opcode_lessThan(self, stack, headPosition, param1Mode, param2Mode):
        op1, op2, storePosition = self.getOperationValues(headPosition, param1Mode, param2Mode, stack)

        if op1 < op2:
            stack[storePosition] = str(1)
        else:
            stack[storePosition] = str(0)

        return stack, headPosition + 4



    def opcode_equals(self, stack, headPosition, param1Mode, param2Mode):
        op1, op2, storePosition = self.getOperationValues(headPosition, param1Mode, param2Mode, stack)

        if op1 == op2:
            stack[storePosition] = str(1)
        else:
            stack[storePosition] = str(0)

        return stack, headPosition + 4

    def getJumpOperationValues(self, headPosition, param1Mode, param2Mode, stack):
        conditionParam = int(stack[headPosition + 1])
        jumpToParam = int(stack[headPosition + 2])
        if param1Mode == POSITION_MODE:
            condValue = int(stack[conditionParam])
        else:
            condValue = conditionParam
        if param2Mode == POSITION_MODE:
            jumpValue = int(stack[jumpToParam])
        else:
            jumpValue = jumpToParam
        return condValue, jumpValue

    def decodeOpcodeAndParamModes(self, stackValue):
        if len(stackValue) <= 2:
           opcode = int(stackValue)
        else:
           opcode = int(stackValue[-1])

        param1Mode = POSITION_MODE
        param2Mode = POSITION_MODE

        if len(stackValue) >= 3:
            param1Mode = int(stackValue[-3])
        if len(stackValue) >= 4:
            param2Mode = int(stackValue[-4])

        return (opcode, param1Mode, param2Mode)

    def getOperationValues(self, headPosition, param1Mode, param2Mode, stack):
        op1Value, op2Value, storePosition = self.getStackParameters(headPosition, stack)

        if param1Mode == POSITION_MODE:
            op1 = stack[op1Value]
        else:
            op1 = op1Value
        if param2Mode == POSITION_MODE:
            op2 = stack[op2Value]
        else:
            op2 = op2Value
        return int(op1), int(op2), int(storePosition)


    def getStackParameters(self, headPosition, stack):
        op1Position = stack[headPosition + 1]
        op2Position = stack[headPosition + 2]
        storePosition = stack[headPosition + 3]
        return int(op1Position), int(op2Position), int(storePosition)

