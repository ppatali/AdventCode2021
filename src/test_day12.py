from day12 import *


def test_GetNodes():
    test = [
        "start-A",
        "start-b",
        "A-c",
        "A-b",
        "b-d",
        "A-end",
        "b-end",
    ]

    assert {
        "start": ["A", "b"],
        "A": ["c", "b", "end"],
        "c": ["A"],
        "b": ["A", "d", "end"],
        "d": ["b"],
    } == GetNodes(test)


def test_FindPaths_Sample1():
    test = [
        "start-A",
        "start-b",
        "A-c",
        "A-b",
        "b-d",
        "A-end",
        "b-end",
    ]

    testFullPaths = [
        ["start", "A", "b", "A", "c", "A", "end"],
        ["start", "A", "b", "A", "end"],
        ["start", "A", "b", "end"],
        ["start", "A", "c", "A", "b", "A", "end"],
        ["start", "A", "c", "A", "b", "end"],
        ["start", "A", "c", "A", "end"],
        ["start", "A", "end"],
        ["start", "b", "A", "c", "A", "end"],
        ["start", "b", "A", "end"],
        ["start", "b", "end"],
    ]

    caveMap = GetNodes(test)
    fullPaths = []
    FindPaths(caveMap, "start", fullPaths)

    assert 10 == len(fullPaths)

    for path in fullPaths:
        assert path in testFullPaths


def test_FindPaths_Sample2():
    test = [
        "dc-end",
        "HN-start",
        "start-kj",
        "dc-start",
        "dc-HN",
        "LN-dc",
        "HN-end",
        "kj-sa",
        "kj-HN",
        "kj-dc",
    ]

    testFullPaths = [
        ["start", "HN", "dc", "HN", "end"],
        ["start", "HN", "dc", "HN", "kj", "HN", "end"],
        ["start", "HN", "dc", "end"],
        ["start", "HN", "dc", "kj", "HN", "end"],
        ["start", "HN", "end"],
        ["start", "HN", "kj", "HN", "dc", "HN", "end"],
        ["start", "HN", "kj", "HN", "dc", "end"],
        ["start", "HN", "kj", "HN", "end"],
        ["start", "HN", "kj", "dc", "HN", "end"],
        ["start", "HN", "kj", "dc", "end"],
        ["start", "dc", "HN", "end"],
        ["start", "dc", "HN", "kj", "HN", "end"],
        ["start", "dc", "end"],
        ["start", "dc", "kj", "HN", "end"],
        ["start", "kj", "HN", "dc", "HN", "end"],
        ["start", "kj", "HN", "dc", "end"],
        ["start", "kj", "HN", "end"],
        ["start", "kj", "dc", "HN", "end"],
        ["start", "kj", "dc", "end"],
    ]

    caveMap = GetNodes(test)
    fullPaths = []
    FindPaths(caveMap, "start", fullPaths)

    assert 19 == len(fullPaths)

    for path in fullPaths:
        assert path in testFullPaths


def test_FindPaths_Sample3():
    test = [
        "fs-end",
        "he-DX",
        "fs-he",
        "start-DX",
        "pj-DX",
        "end-zg",
        "zg-sl",
        "zg-pj",
        "pj-he",
        "RW-he",
        "fs-DX",
        "pj-RW",
        "zg-RW",
        "start-pj",
        "he-WI",
        "zg-he",
        "pj-fs",
        "start-RW",
    ]

    caveMap = GetNodes(test)
    fullPaths = []
    FindPaths(caveMap, "start", fullPaths)

    assert 226 == len(fullPaths)


def test_Part1Result():
    with open("src/day12.input.txt", "rt") as inputFile:
        lines = [line.strip() for line in inputFile.readlines()]
        caveMap = GetNodes(lines)
        fullPaths = []
        FindPaths(caveMap, "start", fullPaths)

        assert 3563 == len(fullPaths)


def test_FindPaths_Sample1_Part2():
    test = [
        "start-A",
        "start-b",
        "A-c",
        "A-b",
        "b-d",
        "A-end",
        "b-end",
    ]

    testFullPaths = [
        ["start", "A", "b", "A", "b", "A", "c", "A", "end"],
        ["start", "A", "b", "A", "b", "A", "end"],
        ["start", "A", "b", "A", "b", "end"],
        ["start", "A", "b", "A", "c", "A", "b", "A", "end"],
        ["start", "A", "b", "A", "c", "A", "b", "end"],
        ["start", "A", "b", "A", "c", "A", "c", "A", "end"],
        ["start", "A", "b", "A", "c", "A", "end"],
        ["start", "A", "b", "A", "end"],
        ["start", "A", "b", "d", "b", "A", "c", "A", "end"],
        ["start", "A", "b", "d", "b", "A", "end"],
        ["start", "A", "b", "d", "b", "end"],
        ["start", "A", "b", "end"],
        ["start", "A", "c", "A", "b", "A", "b", "A", "end"],
        ["start", "A", "c", "A", "b", "A", "b", "end"],
        ["start", "A", "c", "A", "b", "A", "c", "A", "end"],
        ["start", "A", "c", "A", "b", "A", "end"],
        ["start", "A", "c", "A", "b", "d", "b", "A", "end"],
        ["start", "A", "c", "A", "b", "d", "b", "end"],
        ["start", "A", "c", "A", "b", "end"],
        ["start", "A", "c", "A", "c", "A", "b", "A", "end"],
        ["start", "A", "c", "A", "c", "A", "b", "end"],
        ["start", "A", "c", "A", "c", "A", "end"],
        ["start", "A", "c", "A", "end"],
        ["start", "A", "end"],
        ["start", "b", "A", "b", "A", "c", "A", "end"],
        ["start", "b", "A", "b", "A", "end"],
        ["start", "b", "A", "b", "end"],
        ["start", "b", "A", "c", "A", "b", "A", "end"],
        ["start", "b", "A", "c", "A", "b", "end"],
        ["start", "b", "A", "c", "A", "c", "A", "end"],
        ["start", "b", "A", "c", "A", "end"],
        ["start", "b", "A", "end"],
        ["start", "b", "d", "b", "A", "c", "A", "end"],
        ["start", "b", "d", "b", "A", "end"],
        ["start", "b", "d", "b", "end"],
        ["start", "b", "end"],
    ]

    caveMap = GetNodes(test)
    fullPaths = []
    FindPaths2(caveMap, "start", fullPaths)

    assert 36 == len(fullPaths)

    for path in fullPaths:
        assert path in testFullPaths


def test_FindPaths_Sample2_Part2():
    test = [
        "dc-end",
        "HN-start",
        "start-kj",
        "dc-start",
        "dc-HN",
        "LN-dc",
        "HN-end",
        "kj-sa",
        "kj-HN",
        "kj-dc",
    ]

    caveMap = GetNodes(test)
    fullPaths = []
    FindPaths2(caveMap, "start", fullPaths)

    assert 103 == len(fullPaths)


def test_FindPaths_Sample3_Part2():
    test = [
        "fs-end",
        "he-DX",
        "fs-he",
        "start-DX",
        "pj-DX",
        "end-zg",
        "zg-sl",
        "zg-pj",
        "pj-he",
        "RW-he",
        "fs-DX",
        "pj-RW",
        "zg-RW",
        "start-pj",
        "he-WI",
        "zg-he",
        "pj-fs",
        "start-RW",
    ]

    caveMap = GetNodes(test)
    fullPaths = []
    FindPaths2(caveMap, "start", fullPaths, [])

    assert 3509 == len(fullPaths)


def test_Part2Result():
    with open("src/day12.input.txt", "rt") as inputFile:
        lines = [line.strip() for line in inputFile.readlines()]
        caveMap = GetNodes(lines)
        fullPaths = []
        FindPaths2(caveMap, "start", fullPaths)

        assert 105453 == len(fullPaths)
