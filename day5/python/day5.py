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
            stack, headPosition = add(stack, headPosition, param1Mode, param2Mode)
        elif opcode == OPCODE_MULTIPLY:
            stack, headPosition = multiply(stack, headPosition, param1Mode, param2Mode)
        elif opcode == OPCODE_INPUT:
            stack, headPosition = opcode_input(stack, headPosition)
        elif opcode == OPCODE_OUTPUT:
            headPosition = opcode_output(stack, headPosition)
        elif opcode == OPCODE_JUMPIFTRUE:
            headPosition = jumpIfTrue(stack, headPosition, param1Mode, param2Mode)
        elif opcode == OPCODE_JUMPIFFALSE:
            headPosition = jumpIfFalse(stack, headPosition, param1Mode, param2Mode)
        elif opcode == OPCODE_LESSTHAN:
            stack, headPosition = opcode_lessThan(stack, headPosition, param1Mode, param2Mode)
        elif opcode == OPCODE_EQUALS:
            stack, headPosition = opcode_equals(stack, headPosition, param1Mode, param2Mode)
        else:
            print("Stack error")
            break
        opcode, param1Mode, param2Mode = decodeOpcodeAndParamModes(stack[headPosition])
    return stack


def add(stack, headPosition, param1Mode, param2Mode):
    op1, op2, storePosition = getOperationValues(headPosition, param1Mode, param2Mode, stack)

    stack[storePosition] = str(op1 + op2)
    return stack, headPosition + 4

def multiply(stack, headPosition, param1Mode, param2Mode):
    op1, op2, storePosition = getOperationValues(headPosition, param1Mode, param2Mode, stack)
    stack[storePosition] = str(op1 * op2)
    return stack, headPosition + 4

def opcode_input(stack, headPosition):
    userValue = input("Enter value: ")
    position = int(stack[headPosition+1])
    stack[position] = userValue
    return stack, headPosition + 2

def opcode_output(stack, headPosition):
    position = int(stack[headPosition + 1])
    value = stack[position]
    print(str.format("The Value is : {}", value))
    return headPosition + 2

def jumpIfTrue(stack, headPosition, param1Mode, param2Mode):

    condValue, jumpValue = getJumpOperationValues(headPosition, param1Mode, param2Mode, stack)

    if condValue > 0:
        return jumpValue
    else:
        return headPosition + 3


def jumpIfFalse(stack, headPosition, param1Mode, param2Mode):

    condValue, jumpValue = getJumpOperationValues(headPosition, param1Mode, param2Mode, stack)

    if condValue == 0:
        return jumpValue
    else:
        return headPosition + 3

def opcode_lessThan(stack, headPosition, param1Mode, param2Mode):
    op1, op2, storePosition = getOperationValues(headPosition, param1Mode, param2Mode, stack)

    if op1 < op2:
        stack[storePosition] = str(1)
    else:
        stack[storePosition] = str(0)

    return stack, headPosition + 4



def opcode_equals(stack, headPosition, param1Mode, param2Mode):
    op1, op2, storePosition = getOperationValues(headPosition, param1Mode, param2Mode, stack)

    if op1 == op2:
        stack[storePosition] = str(1)
    else:
        stack[storePosition] = str(0)

    return stack, headPosition + 4

def getJumpOperationValues(headPosition, param1Mode, param2Mode, stack):
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

def decodeOpcodeAndParamModes(stackValue):
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

def getOperationValues(headPosition, param1Mode, param2Mode, stack):
    op1Value, op2Value, storePosition = getStackParameters(headPosition, stack)

    if param1Mode == POSITION_MODE:
        op1 = stack[op1Value]
    else:
        op1 = op1Value
    if param2Mode == POSITION_MODE:
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


if __name__ == '__main__':
    main()