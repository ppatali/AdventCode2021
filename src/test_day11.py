from day11 import *


def test_MoveAStep_Sample1():
    test = [
        [1, 1, 1, 1, 1],
        [1, 9, 9, 9, 1],
        [1, 9, 1, 9, 1],
        [1, 9, 9, 9, 1],
        [1, 1, 1, 1, 1],
    ]

    testAfterStep1 = [
        [3, 4, 5, 4, 3],
        [4, 0, 0, 0, 4],
        [5, 0, 0, 0, 5],
        [4, 0, 0, 0, 4],
        [3, 4, 5, 4, 3],
    ]

    testAfterStep2 = [
        [4, 5, 6, 5, 4],
        [5, 1, 1, 1, 5],
        [6, 1, 1, 1, 6],
        [5, 1, 1, 1, 5],
        [4, 5, 6, 5, 4],
    ]

    assert 9 == MoveAStep(test)
    assert test == testAfterStep1

    assert 0 == MoveAStep(test)
    assert test == testAfterStep2


def test_MoveAStep_Sample2():
    test = [
        [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
        [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
        [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
        [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
        [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
        [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
        [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
        [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
        [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
        [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
    ]

    testAfterStep10 = [
        [0, 4, 8, 1, 1, 1, 2, 9, 7, 6],
        [0, 0, 3, 1, 1, 1, 2, 0, 0, 9],
        [0, 0, 4, 1, 1, 1, 2, 5, 0, 4],
        [0, 0, 8, 1, 1, 1, 1, 4, 0, 6],
        [0, 0, 9, 9, 1, 1, 1, 3, 0, 6],
        [0, 0, 9, 3, 5, 1, 1, 2, 3, 3],
        [0, 4, 4, 2, 3, 6, 1, 1, 3, 0],
        [5, 5, 3, 2, 2, 5, 2, 3, 5, 0],
        [0, 5, 3, 2, 2, 5, 0, 6, 0, 0],
        [0, 0, 3, 2, 2, 4, 0, 0, 0, 0],
    ]

    testAfterStep100 = [
        [0, 3, 9, 7, 6, 6, 6, 8, 6, 6],
        [0, 7, 4, 9, 7, 6, 6, 9, 1, 8],
        [0, 0, 5, 3, 9, 7, 6, 9, 3, 3],
        [0, 0, 0, 4, 2, 9, 7, 8, 2, 2],
        [0, 0, 0, 4, 2, 2, 9, 8, 9, 2],
        [0, 0, 5, 3, 2, 2, 2, 8, 7, 7],
        [0, 5, 3, 2, 2, 2, 2, 9, 6, 6],
        [9, 3, 2, 2, 2, 2, 8, 9, 6, 6],
        [7, 9, 2, 2, 2, 8, 6, 8, 6, 6],
        [6, 7, 8, 9, 9, 9, 8, 7, 6, 6],
    ]

    flashCount = 0
    for _ in range(10):
        flashCount += MoveAStep(test)
    assert flashCount == 204
    assert test == testAfterStep10

    for _ in range(90):
        flashCount += MoveAStep(test)
    assert flashCount == 1656
    assert test == testAfterStep100


def test_Part1Result():
    with open("src/day11.input.txt", "rt") as inputFile:
        octopuses = [[int(col) for col in row.strip()] for row in inputFile.readlines()]
        totalFlashes = 0
        for _ in range(100):
            totalFlashes += MoveAStep(octopuses)
        assert 1634 == totalFlashes


def test_AreAllOctopusesFlash():
    test = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    assert AreAllOctopusesFlash(test)
    test[3][4] = 1
    assert not AreAllOctopusesFlash(test)


def test_FindSynchronizedFlashStep():
    test = [
        [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
        [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
        [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
        [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
        [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
        [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
        [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
        [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
        [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
        [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
    ]

    assert 195 == FindSynchronizedFlashStep(test)


def test_Part2Result():
    with open("src/day11.input.txt", "rt") as inputFile:
        octopuses = [[int(col) for col in row.strip()] for row in inputFile.readlines()]
        assert 210 == FindSynchronizedFlashStep(octopuses)
