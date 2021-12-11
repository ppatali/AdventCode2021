from day07 import *


def test_GetAlignWithMinCost_Linear():
    input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    assert (2, 37) == GetAlignWithMinCost(input, CostLinear)


def test_Part1Result():
    with open("src/day07.input.txt", "rt") as inputFile:
        positions = [int(i) for i in inputFile.readline().split(",")]
        assert 339, 343468 == GetAlignWithMinCost(positions)


def test_GetAlignWithMinCost_Accelerated():
    input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    assert (5, 168) == GetAlignWithMinCost(input, CostAccelerated)


def test_Part2Result():
    with open("src/day07.input.txt", "rt") as inputFile:
        positions = [int(i) for i in inputFile.readline().split(",")]
        assert 478, 96086265 == GetAlignWithMinCost(positions, CostAccelerated)
