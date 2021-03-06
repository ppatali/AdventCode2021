from day13 import *

def test_ReadInput():
    input = [
        "6,10",
        "0,14",
        "9,10",
        "0,3",
        "10,4",
        "4,11",
        "6,0",
        "6,12",
        "4,1",
        "0,13",
        "10,12",
        "3,4",
        "3,0",
        "8,4",
        "1,10",
        "2,14",
        "8,10",
        "9,0",
        "",
        "fold along y=7",
        "fold along x=5",
    ]

    expectedOutput = [
        [0,0,0,1,0,0,1,0,0,1,0],
        [0,0,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,1,0,1],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,1,0,1,1,0],
        [0,0,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0],
        [1,0,1,0,0,0,0,0,0,0,0],
    ]
    matrix, _, folds = ReadInput(input)

    assert expectedOutput == matrix
    assert [('y', 7), ('x', 5)] == folds

def test_Fold():
    input = [
        "6,10",
        "0,14",
        "9,10",
        "0,3",
        "10,4",
        "4,11",
        "6,0",
        "6,12",
        "4,1",
        "0,13",
        "10,12",
        "3,4",
        "3,0",
        "8,4",
        "1,10",
        "2,14",
        "8,10",
        "9,0",
        "",
        "fold along y=7",
        "fold along x=5",
    ]

    expectedOutput1 = [
        [1,0,1,1,0,0,1,0,0,1,0],
        [1,0,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0,1],
        [1,0,0,0,1,0,0,0,0,0,0],
        [0,1,0,1,0,0,1,0,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
    ]

    expectedOutput2 = [
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
        [0,0,0,0,0],
        [0,0,0,0,0],
    ]

    matrix, points, folds = ReadInput(input)
    
    folded1 = Fold(matrix, folds[0][0], folds[0][1])
    assert expectedOutput1 == folded1

    folded2 = Fold(folded1, folds[1][0], folds[1][1])
    assert expectedOutput2 == folded2

    expectedOutput1 = [
        (6, 4),(0, 0),(9, 4),(0, 3),(10, 4),(4, 3),(6, 0),(6, 2),(4, 1),
        (0, 1),(10, 2),(3, 4),(3, 0),(8, 4),(1, 4),(2, 0),(9, 0)
    ]

    folded1 = FoldUsingPoints(points, folds[0][0], folds[0][1])
    assert expectedOutput1 == folded1

    expectedOutput2 = [
        (4, 4), (0, 0), (1, 4), (0, 3), (0, 4), (4, 3), (4, 0), (4, 2), 
        (4, 1), (0, 1), (0, 2), (3, 4), (3, 0), (2, 4), (2, 0), (1, 0)
    ]
    folded2 = FoldUsingPoints(folded1, folds[1][0], folds[1][1])
    assert expectedOutput2 == folded2

def test_Part1Result():
    with open("src/day13.input.txt", "rt") as inputFile:
        readlines = [line.strip() for line in inputFile.readlines()]
        matrix, points, folds = ReadInput(readlines)
        folded = Fold(matrix, folds[0][0], folds[0][1])
        count = sum([sum(x) for x in folded])
        assert 669 == count

        folded = FoldUsingPoints(points, folds[0][0], folds[0][1])
        assert 669 == len(folded)

def test_Part2Result():
    expectedOutput = [
        [1,0,0,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0,1,1,0,0,1,0,0,1,0,0,1,1,0,0,0,0,1,1,0],
        [1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,0,0,1,0],
        [1,0,0,1,0,1,1,1,0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1,0],
        [1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1,0],
        [1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0],
        [0,1,1,0,0,1,1,1,1,0,1,0,0,0,0,1,1,1,1,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0],
    ]
    
    expectedPoints = [
        (17, 0),(32, 5),(12, 2),(10, 2),(7, 0),(26, 5),(17, 2),(28, 0),(32, 0),(13, 0),
        (38, 0),(7, 2),(0, 0),(20, 4),(16, 3),(23, 4),(27, 5),(16, 0),(37, 5),(5, 2),
        (3, 4),(25, 4),(31, 0),(17, 5),(15, 0),(5, 4),(8, 5),(37, 0),(15, 5),(7, 5),
        (30, 3),(38, 1),(18, 5),(36, 5),(33, 1),(38, 4),(33, 4),(6, 2),(28, 1),(18, 0),
        (22, 0),(25, 1),(5, 1),(20, 3),(0, 1),(5, 3),(28, 2),(8, 0),(3, 1),(25, 3),(1, 5),
        (30, 1),(20, 1),(25, 0),(3, 2),(10, 5),(2, 5),(35, 4),(6, 5),(6, 0),(38, 3),(0, 2),
        (28, 3),(3, 3),(11, 2),(28, 4),(3, 0),(12, 0),(5, 5),(16, 5),(15, 4),(22, 5),(10, 1),
        (31, 5),(10, 3),(5, 0),(10, 0),(0, 4),(30, 4),(25, 2),(0, 3),(20, 2),(23, 1),(10, 4),
        (21, 5),(18, 1),(21, 0),(38, 2),(30, 2),(11, 0)
    ]

    #Expected output when printed - UEFZCUCJ
    #  # #### #### ####  ##  #  #  ##    ## 
    #  # #    #       # #  # #  # #  #    # 
    #  # ###  ###    #  #    #  # #       #
    #  # #    #     #   #    #  # #       #
    #  # #    #    #    #  # #  # #  # #  #
     ##  #### #    ####  ##   ##   ##   ##
    with open("src/day13.input.txt", "rt") as inputFile:
        readlines = [line.strip() for line in inputFile.readlines()]
        matrix, points, folds = ReadInput(readlines)
        folded = FoldAll(matrix, folds)
        assert expectedOutput == folded

        folded = FoldAllUsingPoints(points, folds)
        assert folded == expectedPoints
