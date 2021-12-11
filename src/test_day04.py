from day04 import *


def test_ReadFileInput():
    testDraws = [
        7,
        4,
        9,
        5,
        11,
        17,
        23,
        2,
        0,
        14,
        21,
        24,
        10,
        16,
        13,
        6,
        15,
        25,
        12,
        22,
        18,
        20,
        8,
        19,
        3,
        26,
        1,
    ]
    testBoards = [
        [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [21, 9, 14, 16, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19],
        ],
        [
            [3, 15, 0, 2, 22],
            [9, 18, 13, 17, 5],
            [19, 8, 7, 25, 23],
            [20, 11, 10, 24, 4],
            [14, 21, 16, 12, 6],
        ],
        [
            [14, 21, 17, 24, 4],
            [10, 16, 15, 9, 19],
            [18, 8, 23, 26, 20],
            [22, 11, 13, 6, 5],
            [2, 0, 12, 3, 7],
        ],
    ]
    readDraws, readBoards = ReadInput("src/day04.test.input.txt")
    assert testDraws == readDraws
    assert testBoards == readBoards


def test_MarkBoard():
    testBoard = [
        [22, 13, 17, 11, 0],
        [8, 2, 23, 4, 24],
        [21, 9, 14, 16, 7],
        [6, 10, 3, 18, 5],
        [1, 12, 20, 15, 19],
    ]

    expectedBoard = [
        [22, 13, 17, 11, 0],
        [8, 2, 23, MARKER, 24],
        [21, 9, 14, 16, 7],
        [6, 10, 3, MARKER, 5],
        [1, 12, 20, 15, 19],
    ]

    MarkBoard(testBoard, 18)
    MarkBoard(testBoard, 4)

    assert testBoard == expectedBoard


def test_IsAWinner():

    assert True == IsAWinner(
        [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [MARKER, MARKER, MARKER, MARKER, MARKER],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19],
        ]
    )

    assert False == IsAWinner(
        [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [MARKER, MARKER, MARKER, MARKER, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19],
        ]
    )

    assert True == IsAWinner(
        [
            [22, 13, 17, 11, MARKER],
            [8, 2, 23, 4, MARKER],
            [21, 9, 14, 16, MARKER],
            [6, 10, 3, 18, MARKER],
            [1, 12, 20, 15, MARKER],
        ]
    )

    assert False == IsAWinner(
        [
            [22, 13, 17, 11, MARKER],
            [8, 2, 23, 4, MARKER],
            [21, 9, 14, 16, MARKER],
            [6, 10, 3, 18, MARKER],
            [1, 12, 20, 15, 19],
        ]
    )

    assert True == IsAWinner(
        [
            [22, 13, 17, 11, MARKER],
            [MARKER, MARKER, MARKER, MARKER, MARKER],
            [21, 9, 14, 16, MARKER],
            [6, 10, 3, 18, MARKER],
            [1, 12, 20, 15, MARKER],
        ]
    )


def test_GetBoardScore():
    testBoard = [
        [22, MARKER, 17, 11, MARKER],
        [8, 2, MARKER, 4, 24],
        [MARKER, MARKER, MARKER, MARKER, MARKER],
        [6, 10, 3, 18, 5],
        [MARKER, 12, 20, 15, MARKER],
    ]

    testDraw = 10

    assert 177 * 10 == GetBoardScore(testBoard, testDraw)


def test_Part1Result():
    assert 4512 == PlayBingo("src/day04.test.input.txt")
    assert 49860 == PlayBingo("src/day04.input.txt")


def test_Part2Result():
    assert 1924 == PlayBingoToLoose("src/day04.test.input.txt")
    assert 24628 == PlayBingoToLoose("src/day04.input.txt")
