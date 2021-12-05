from day03 import *


def test_Test1():
    readings = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    gammaVal, epsilonValue, power = ComputePowerConsumption(readings, 5)
    assert 22 == gammaVal
    assert 9 == epsilonValue
    assert 198 == power


def test_Part1Result():
    with open("day03.input.txt", "rt") as inputFile:
        gammaVal, epsilonValue, power = ComputePowerConsumption(
            inputFile.readlines(), 12
        )
        assert 2484 == gammaVal
        assert 1611 == epsilonValue
        assert 4001724 == power


def test_Test2():
    readings = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]
    oxygenRating, co2Rating, lifeSupportRating = LifeSuportRating(readings, 5)
    assert 23 == oxygenRating
    assert 10 == co2Rating
    assert 230 == lifeSupportRating


def test_Part2Result():
    with open("day03.input.txt", "rt") as inputFile:
        readings = [reading.strip() for reading in inputFile.readlines()]
        oxygenRating, co2Rating, lifeSupportRating = LifeSuportRating(readings, 12)
        assert 2545 == oxygenRating
        assert 231 == co2Rating
        assert 587895 == lifeSupportRating
