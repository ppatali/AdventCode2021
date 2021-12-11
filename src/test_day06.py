from day06 import *


def test_Evolve():
    day0Expected = [3, 4, 3, 1, 2]
    day10Expected = [0, 1, 0, 5, 6, 0, 1, 2, 2, 3, 7, 8]
    day18Expected = [
        6,
        0,
        6,
        4,
        5,
        6,
        0,
        1,
        1,
        2,
        6,
        0,
        1,
        1,
        1,
        2,
        2,
        3,
        3,
        4,
        6,
        7,
        8,
        8,
        8,
        8,
    ]

    population = day0Expected.copy()
    assert (len(day10Expected), day10Expected) == (
        EvolveForDays(population, 10),
        population,
    )

    population = day0Expected.copy()
    assert (len(day18Expected), day18Expected) == (
        EvolveForDays(population, 18),
        population,
    )

    population = day10Expected.copy()
    assert (len(day18Expected), day18Expected) == (
        EvolveForDays(population, 8),
        population,
    )

    population = day0Expected.copy()
    assert 5934 == EvolveForDays(population, 80)


def test_Part1Result():
    with open("src/day06.input.txt", "rt") as inputFile:
        population = [int(i) for i in inputFile.readline().split(",")]
        assert 360268 == EvolveForDays(population, 80)


def test_EvolveGenerations():
    day0Expected = [3, 4, 3, 1, 2]
    day10Expected = [0, 1, 0, 5, 6, 0, 1, 2, 2, 3, 7, 8]
    day18Expected = [
        6,
        0,
        6,
        4,
        5,
        6,
        0,
        1,
        1,
        2,
        6,
        0,
        1,
        1,
        1,
        2,
        2,
        3,
        3,
        4,
        6,
        7,
        8,
        8,
        8,
        8,
    ]

    assert len(day10Expected) == EvolvePopulationForDaysUsingGeneration(
        day0Expected, 10
    )
    assert len(day18Expected) == EvolvePopulationForDaysUsingGeneration(
        day0Expected, 18
    )
    assert 26984457539 == EvolvePopulationForDaysUsingGeneration(day0Expected, 256)


def test_Part2Result():
    with open("src/day06.input.txt", "rt") as inputFile:
        population = [int(i) for i in inputFile.readline().split(",")]
        assert 1632146183902 == EvolvePopulationForDaysUsingGeneration(population, 256)
