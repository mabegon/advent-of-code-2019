OPCODE_OUTPUT = 4
OPCODE_INPUT = 3
OPCODE_MULTIPLY = 2
OPCODE_ADD = 1
OPCODE_HALT = 99

filepath = '../input.txt'

def main():
    stack = get_memory_stack()
    computeStack(stack)


def get_memory_stack():
    with open(filepath) as fp:
        code = fp.read()
        stack = code.split(',')
        #stack = [int(x) for x in stackStr]
        return stack

def computeStack(stack):
    headPosition = 0
    opcode, param1Mode, param2Mode = decodeOpcodeAndParamModes(stack[headPosition])

    while opcode != OPCODE_HALT:
        if opcode == OPCODE_ADD:
            stack = add(stack, headPosition, param1Mode, param2Mode)
        elif opcode == OPCODE_MULTIPLY:
            stack = multiply(stack, headPosition, param1Mode, param2Mode)
        elif opcode == OPCODE_INPUT:
            stack = opcode_input(stack, headPosition)
        elif opcode == OPCODE_OUTPUT:
            opcode_output(stack, headPosition)
        else:
            print("Stack error")
            break
        headPosition = nextCommand(opcode, headPosition)
        opcode, param1Mode, param2Mode = decodeOpcodeAndParamModes(stack[headPosition])
    return stack


def add(stack, headPosition, param1Mode, param2Mode):
    op1, op2, storePosition = getOperationValues(headPosition, param1Mode, param2Mode, stack)

    stack[storePosition] = str(op1 + op2)
    return stack

def multiply(stack, headPosition, param1Mode, param2Mode):
    op1, op2, storePosition = getOperationValues(headPosition, param1Mode, param2Mode, stack)
    stack[storePosition] = str(op1 * op2)
    return stack

def opcode_input(stack, headPosition):
    userValue = input("Enter value: ")
    position = int(stack[headPosition+1])
    stack[position] = userValue
    return stack

def opcode_output(stack, headPosition):
    position = int(stack[headPosition + 1])
    value = stack[position]
    print(str.format("The Value is : {}", value))

def decodeOpcodeAndParamModes(stackValue):
    if len(stackValue) <= 2:
       opcode = int(stackValue)
    else:
       opcode = int(stackValue[-1])

    param1Mode = 0
    param2Mode = 0

    if len(stackValue) >= 3:
        param1Mode = int(stackValue[-3])
    if len(stackValue) >= 4:
        param2Mode = int(stackValue[-4])

    return (opcode, param1Mode, param2Mode)

def getOperationValues(headPosition, param1Mode, param2Mode, stack):
    op1Value, op2Value, storePosition = getStackParameters(headPosition, stack)

    if param1Mode == 0:
        op1 = stack[op1Value]
    else:
        op1 = op1Value
    if param2Mode == 0:
        op2 = stack[op2Value]
    else:
        op2 = op2Value
    return int(op1), int(op2), int(storePosition)


def getStackParameters(headPosition, stack):
    op1Position = stack[headPosition + 1]
    op2Position = stack[headPosition + 2]
    storePosition = stack[headPosition + 3]
    return int(op1Position), int(op2Position), int(storePosition)

def getResult(stack):
    return stack[0]


def nextCommand(opcode, headPosition):
    if opcode == OPCODE_INPUT or opcode == OPCODE_OUTPUT:
        return headPosition + 2
    return headPosition + 4


if __name__ == '__main__':
    main()