from day09 import *


def test_FindLowPointCoordinates():
    test = [
        "2199943210",
        "3987894921",
        "9856789892",
        "8767896789",
        "9899965678",
    ]

    assert [(0, 1), (0, 9), (2, 2), (4, 6)] == FindLowPointCoordinates(test)


def test_FindLowPoint():
    test = [
        "2199943210",
        "3987894921",
        "9856789892",
        "8767896789",
        "9899965678",
    ]

    assert [1, 0, 5, 5] == FindLowPoints(test, FindLowPointCoordinates(test))


def test_RiskScore():
    test = [
        "2199943210",
        "3987894921",
        "9856789892",
        "8767896789",
        "9899965678",
    ]

    assert 15 == ComputRiskScore(FindLowPoints(test, FindLowPointCoordinates(test)))


def test_Part1Result():
    with open("day09.input.txt", "rt") as inputFile:
        heatmap = [line.strip() for line in inputFile.readlines()]
        assert 425 == ComputRiskScore(
            FindLowPoints(heatmap, FindLowPointCoordinates(heatmap))
        )


def test_FindBasins():
    test = [
        "2199943210",
        "3987894921",
        "9856789892",
        "8767896789",
        "9899965678",
    ]

    lowPointCoordinates = FindLowPointCoordinates(test)
    basins = FindBasins(test, lowPointCoordinates)

    assert [
        [1, 2, 3],
        [0, 1, 1, 2, 2, 2, 3, 4, 4],
        [5, 8, 6, 8, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8],
        [5, 6, 6, 6, 7, 7, 8, 8, 8],
    ] == basins


def test_Compute3LargestBasinsWeight():
    test = [
        "2199943210",
        "3987894921",
        "9856789892",
        "8767896789",
        "9899965678",
    ]

    lowPointCoordinates = FindLowPointCoordinates(test)
    assert 1134 == Compute3LargestBasinsWeight(FindBasins(test, lowPointCoordinates))


def test_Part2Result():
    with open("day09.input.txt", "rt") as inputFile:
        heatmap = [line.strip() for line in inputFile.readlines()]
        lowPointCoorinates = FindLowPointCoordinates(heatmap)
        lowPoints = FindLowPoints(heatmap, lowPointCoorinates)
        basins = FindBasins(heatmap, lowPointCoorinates)
        assert 1135260 == Compute3LargestBasinsWeight(basins)
