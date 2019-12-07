filepath = '../input.txt'

class Position(object):
    def __init__(self, x: int, y: int ):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return str.format("({},{})", self.x, self.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def distanceOf(self, to):
        pass


def main():
    with open(filepath) as fp:
        path1 = fp.readline()
        path2 = fp.readline()

    print(str.format("result is: {}", resolvePuzzle(path1,path2)
))


def getSections(path: str) -> [str]:
    return path.split(',')

def decompose(section: str) -> (str, int):
    direction = section[0]
    distance = section[1:len(section)]
    return direction, int(distance)

def getPositionsOnSection(initialPosition, section: str):
    positionsOnSection = []
    direction, distance = decompose(section)
    if direction == "R":
        for i in range(1, distance+1):
            positionsOnSection.append(Position(initialPosition.x+i, initialPosition.y ))

    if direction == "L":
        for i in range(1, distance + 1):
            positionsOnSection.append(Position(initialPosition.x - i, initialPosition.y))

    if direction == "U":
        for i in range(1, distance + 1):
            positionsOnSection.append(Position(initialPosition.x, initialPosition.y + i))

    if direction == "D":
        for i in range(1, distance + 1):
            positionsOnSection.append(Position(initialPosition.x, initialPosition.y - i))

    return positionsOnSection

def consolidatePositions(positions: set, positionsOnSection):
    result = positions.copy()
    for position in positionsOnSection:
        result.add(position)
    return result


def intersections(pathPositionsWire1: dict, pathPositionsWire2: dict):
    intersection = pathPositionsWire1 & pathPositionsWire2
    return intersection

def computeManhattanDistance(position1: Position, position2: Position):
    return abs(position1.x - position2.x) + abs(position1.y - position2.y)

def getDistanceOfClosestIntersection(centralPortPosition: Position, intersections: list):
    results = []
    for intersection in intersections:
        results.append(computeManhattanDistance(centralPortPosition, intersection))
    results.sort()
    return results[0]

def getPositionsOnPath(centralPortPosition, path):
    currentPosition = centralPortPosition
    sectionsPath = getSections(path)
    positionsPath = set()
    for section in sectionsPath:
        positionsOnSection = getPositionsOnSection(currentPosition, section)
        positionsPath = consolidatePositions(positionsPath, positionsOnSection)
        currentPosition = positionsOnSection[len(positionsOnSection) - 1]
    return positionsPath

def resolvePuzzle(path1, path2):
    centralPortPosition = Position(0, 0)

    positionsPath1 = getPositionsOnPath(centralPortPosition, path1)

    positionsPath2 = getPositionsOnPath(centralPortPosition, path2)

    intersec = intersections(positionsPath1, positionsPath2)

    return getDistanceOfClosestIntersection(centralPortPosition, intersec)






if __name__ == '__main__':
    main()