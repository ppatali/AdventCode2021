from day01 import *


def test_Test1():
    m1 = [1, 2, 3, 3, 2, 10]
    assert UpTrendsInSlidingWindow(m1) == 3


def test_Test2():
    m1 = [1]
    assert UpTrendsInSlidingWindow(m1) == 0


def test_Test3():
    m1 = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert UpTrendsInSlidingWindow(m1) == 7


def test_Part1Result():
    with open("src/day01.input.txt", "rt") as inputFile:
        measurements = [int(measurement) for measurement in inputFile.readlines()]
        assert UpTrendsInSlidingWindow(measurements) == 1233


def test_Test4():
    m1 = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263, 1]
    assert UpTrendsInSlidingWindow(m1,3) == 5


def test_Part2Result():
    with open("src/day01.input.txt", "rt") as inputFile:
        measurements = [int(measurement) for measurement in inputFile.readlines()]
        assert UpTrendsInSlidingWindow(measurements, 3) == 1275

