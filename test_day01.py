from day01 import *


def test_Test1():
    m1 = ["1", "2", "3", "3", "2", "10"]
    assert NumberofIncreases(m1) == 3


def test_Test2():
    m1 = ["1"]
    assert NumberofIncreases(m1) == 0


def test_Test3():
    m1 = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert NumberofIncreasesWithThreeMeasurementSlidingWindow(m1) == 5


def test_Part1Result():
    with open("day01.input.txt", "rt") as inputFile:
        assert NumberofIncreases(inputFile.readlines()) == 1233


def test_Test4():
    m1 = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263, 1]
    assert NumberofIncreasesWithThreeMeasurementSlidingWindow(m1) == 5


def test_Part2Result():
    with open("day01.input.txt", "rt") as inputFile:
        assert NumberofIncreasesWithThreeMeasurementSlidingWindow(inputFile.readlines()) == 1275

def test_Part1Result_N_WindowSize():
    with open("day01.input.txt", "rt") as inputFile:
        assert NumberofIncreasesWithNMeasurementSlidingWindow(inputFile.readlines(), 1) == 1233

def test_Part2Result_N_WindowSize():
    with open("day01.input.txt", "rt") as inputFile:
        assert NumberofIncreasesWithNMeasurementSlidingWindow(inputFile.readlines(), 3) == 1275
