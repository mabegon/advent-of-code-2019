import math

filepath = '../input.txt'

def main():
    with open(filepath) as fp:
        total = 0
        for massStr in fp:
            mass = int(massStr.strip())
            total = total + calculateFuel(mass)
        print(total)

def calculateFuel(mass) -> int:
    result = math.floor( mass / 3) - 2
    return result

if __name__ == '__main__':
    main()