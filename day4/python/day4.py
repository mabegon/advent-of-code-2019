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

def checkExactlyTwoAdjacents(password):
    current = ""
    occurrences = 1
    for c in str(password):
        if c == current:
            occurrences += 1
        elif occurrences == 2:
            return True
        else:
            occurrences = 1
        current = c
    return occurrences == 2

def solvePuzzle():
    totalPasswords = 0
    for password in range(165432, 707912):
        if checkAdjacents(password) and checkNeverDecrease(password):
            totalPasswords += 1
    return totalPasswords

def solvePuzzle2():
    totalPasswords = 0
    for password in range(165432, 707912):
        if checkExactlyTwoAdjacents(password) and checkNeverDecrease(password):
            totalPasswords += 1
    return totalPasswords

def main():
    result = solvePuzzle()
    print(str.format("The number of possible password of Part 1 are: {}", solvePuzzle()))
    print(str.format("The number of possible password of Part 2 are: {}", solvePuzzle2()))


if __name__ == '__main__':
    main()