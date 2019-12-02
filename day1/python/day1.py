import math

filepath = '../input.txt'

def main():
    with open(filepath) as fp:
        total = 0
        for massStr in fp:
            mass = int(massStr.strip())
            total = total + calculateFuelIncludingFuelMass(mass)
        print(total)

def calculateFuel(mass) -> int:
    result = math.floor( mass / 3) - 2
    return result

def calculateFuelIncludingFuelMass(mass) -> int:
    fuelMass = calculateFuel(mass)
    if fuelMass > 0:
        fuelMass = fuelMass + calculateFuelIncludingFuelMass(fuelMass)
    else:
        fuelMass = 0
    return fuelMass

if __name__ == '__main__':
    main()