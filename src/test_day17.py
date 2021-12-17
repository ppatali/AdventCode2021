from day17 import *


def test_HighestYShort_Sample():
    assert 45 == HighestYShort(-10)


def test_Part1Result():
    with open("src/day17.input.txt", "rt") as inputFile:
        input = (
            inputFile.readline()
            .strip()
            .replace("target area: x=", "")
            .replace("y=", "")
            .split(", ")
        )
        _, _, TY0, _ = [int(n) for xy in input for n in xy.split("..")]
        assert 4095 == HighestYShort(TY0)


def test_Part1And2_Sample():
    hits, highestY = FindInitVelToHitTarget(20, 30, -10, -5)
    assert len(hits) == 112 and 45 == highestY


def test_Part1And2Result():
    with open("src/day17.input.txt", "rt") as inputFile:
        input = (
            inputFile.readline()
            .strip()
            .replace("target area: x=", "")
            .replace("y=", "")
            .split(", ")
        )
        TX0, TX1, TY0, TY1 = [int(n) for xy in input for n in xy.split("..")]

        hits, highestY = FindInitVelToHitTarget(TX0, TX1, TY0, TY1)
        assert len(hits) == 3773 and 4095 == highestY
