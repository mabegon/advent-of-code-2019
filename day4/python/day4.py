def checkAdjacents(password):
    current = ""
    for c in str(password):
        if c == current:
            return True
        current = c
    return False

def checkNeverDecrease(password):
    current = -1
    for c in str(password):
        if int(c) < current:
            return False
        current = int(c)
    return True


def solvePuzzle():
    totalPasswords = 0
    for password in range(165432, 707912):
        if checkAdjacents(password) and checkNeverDecrease(password):
            totalPasswords += 1
    return totalPasswords

def main():
    result = solvePuzzle()
    print(str.format("The number of possible password are: {}", result))


if __name__ == '__main__':
    main()