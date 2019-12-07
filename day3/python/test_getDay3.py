from unittest import TestCase
import day3
from day3 import Position


class TestDay3(TestCase):
    def test_getSections_with_empty_path(self):
        path = ""
        sections = day3.getSections(path)
        self.assertEqual([''], sections)

    def test_getSections_with_one_section_path(self):
        path = "R1"
        sections = day3.getSections(path)
        self.assertEqual(['R1'], sections)

    def test_getSections_with_two_section_path(self):
        path = "R1,L2"
        sections = day3.getSections(path)
        self.assertEqual(['R1', 'L2'], sections)

    def test_decomposeSection(self):
        section = "R1"
        direction, distance = day3.decompose(section)
        self.assertEqual("R", direction)
        self.assertEqual(1, distance)

    def test_getPositionsOnSection(self):
        section = "R1"
        initialPostion= Position(0, 0)
        expectedPositions = [Position(1, 0)]
        positionsOnSection = day3.getPositionsOnSection(initialPostion, section)
        self.assertEqual(expectedPositions, positionsOnSection)

    def test_getPositionsOnSection_distance_2(self):
        section = "R2"
        initialPostion = Position(0, 0)
        expectedPositions = [Position(1, 0), Position(2,0)]
        positionsOnSection = day3.getPositionsOnSection(initialPostion, section)
        self.assertEqual(expectedPositions, positionsOnSection)

    def test_getPositionsOnSection_distance_3(self):
        section = "R3"
        initialPostion = Position(0, 0)
        expectedPositions = [Position(1, 0), Position(2,0), Position(3,0)]
        positionsOnSection = day3.getPositionsOnSection(initialPostion, section)
        self.assertEqual(expectedPositions, positionsOnSection)

    def test_getPositionsOnSection_distance_2_to_left(self):
        section = "L2"
        initialPostion = Position(0, 0)
        expectedPositions = [Position(-1, 0), Position(-2, 0)]
        positionsOnSection = day3.getPositionsOnSection(initialPostion, section)
        self.assertEqual(expectedPositions, positionsOnSection)

    def test_getPositionsOnSection_distance_2_to_up(self):
        section = "U2"
        initialPostion = Position(0, 0)
        expectedPositions = [Position(0, 1), Position(0, 2)]
        positionsOnSection = day3.getPositionsOnSection(initialPostion, section)
        self.assertEqual(expectedPositions, positionsOnSection)

    def test_getPositionsOnSection_distance_2_to_down(self):
        section = "D2"
        initialPostion = Position(0, 0)
        expectedPositions = [Position(0, -1), Position(0, -2)]
        positionsOnSection = day3.getPositionsOnSection(initialPostion, section)
        self.assertEqual(expectedPositions, positionsOnSection)

    def test_consolidatePositions(self):
        pathPositions = {Position(0, 0), Position(1, 0)}
        sectionPostions = [Position(2, 0), Position(1, 0)]

        expectedPathPositions = {Position(0, 0), Position(1, 0), Position(2, 0)}

        self.assertEqual(expectedPathPositions, day3.consolidatePositions(pathPositions, sectionPostions))

    def test_intersection2(self):
        pathPositionsWire1 = {Position(0, 0), Position(1, 0)}
        pathPositionsWire2 = {Position(2, 0), Position(1, 0)}

        expectedPathPositions = {Position(1, 0)}

        self.assertEqual(expectedPathPositions, day3.intersections(pathPositionsWire1, pathPositionsWire2))

    def test_computeManhattanDistance(self):
        centralPortPosition = Position(0, 0)
        wireCrossPosition = Position(3, 3)
        distanceExpected = 6

        self.assertEqual(distanceExpected, day3.computeManhattanDistance(centralPortPosition, wireCrossPosition))

    def test_getDistanceOfClosestIntersection(self):
        centralPortPosition = Position(0, 0)
        wireCrossPosition1 = Position(5, 5)
        wireCrossPosition2 = Position(3, 3)
        wireCrossPosition3 = Position(4, 4)
        distanceExpected = 6

        self.assertEqual(distanceExpected, day3.getDistanceOfClosestIntersection(centralPortPosition, [wireCrossPosition1,wireCrossPosition2, wireCrossPosition3]) )

    def test_getPositionsOnPath(self):
        path = "R1,U1,L1"
        centralPosition = Position(0,0)
        positionsOnPathExpected = {Position(1,0), Position(1,1), Position(0,1)}

        positionsOnPath = day3.getPositionsOnPath(centralPosition, path)

        self.assertEqual(positionsOnPathExpected, positionsOnPath)

    def test_day3_example1(self):
        path1 = "R8,U5,L5,D3"
        path2 = "U7,R6,D4,L4"
        expectedDistance = 6
        self.assertEqual(expectedDistance, day3.resolvePuzzle(path1, path2))

    def test_day3_example2(self):
        path1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
        path2 = "U62,R66,U55,R34,D71,R55,D58,R83"
        expectedDistance = 159
        self.assertEqual(expectedDistance, day3.resolvePuzzle(path1, path2))

    def test_day3_example3(self):
        path1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
        path2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
        expectedDistance = 135
        self.assertEqual(expectedDistance, day3.resolvePuzzle(path1, path2))


