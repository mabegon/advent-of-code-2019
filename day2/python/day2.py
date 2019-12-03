filepath = '../input.txt'


def add(stack, headPosition):
    op1Position, op2Position, storePosition = getStackPositions(headPosition, stack)

    op1 = stack[op1Position]
    op2 = stack[op2Position]
    stack[storePosition] = op1 + op2
    return stack


def getStackPositions(headPosition, stack):
    op1Position = stack[headPosition + 1]
    op2Position = stack[headPosition + 2]
    storePosition = stack[headPosition + 3]
    return op1Position, op2Position, storePosition


def multiply(stack, headPosition):

    op1Position, op2Position, storePosition = getStackPositions(headPosition, stack)

    op1 = stack[op1Position]
    op2 = stack[op2Position]
    stack[storePosition] = op1 * op2
    return stack

def main():
    print ("Answer: " + str(answer_day_2_1()))

def answer_day_2_1():
    stack = get_memory_stack()
    stack[1] = 12
    stack[2] = 2
    stack = computeStack(stack)

    return stack[0]

def computeStack(stack):
    headPosition = 0
    while stack[headPosition] != 99:
        if stack[headPosition] == 1:
            stack = add(stack, headPosition)
        elif stack[headPosition] == 2:
            stack = multiply(stack, headPosition)
        else:
            print("Stack error")
            break
        headPosition = nextCommand(headPosition)
    return stack


def nextCommand(headPosition):
    return headPosition + 4


def get_memory_stack():
    with open(filepath) as fp:
        code = fp.read()
        stackStr = code.split(',')
        stack = [int(x) for x in stackStr]
        return stack

if __name__ == '__main__':
    main()