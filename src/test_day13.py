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
    matrix, folds = ReadInput(input)

    assert expectedOutput == matrix
    assert [('y', 7), ('x', 5)] == folds

def test_FoldOnce():
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
    matrix, folds = ReadInput(input)
    
    folded1 = FoldOnce(matrix, folds[0][0], folds[0][1])
    assert expectedOutput1 == folded1

    folded2 = FoldOnce(folded1, folds[1][0], folds[1][1])
    assert expectedOutput2 == folded2

def test_Part1Result():
    with open("src/day13.input.txt", "rt") as inputFile:
        readlines = [line.strip() for line in inputFile.readlines()]
        matrix, folds = ReadInput(readlines)
        folded = FoldOnce(matrix, folds[0][0], folds[0][1])
        count = sum([sum(x) for x in folded])
        assert 669 == count

def test_Part2Result():
    expectedOutput = [
        [1,0,0,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,0,1,1,0,0,1,0,0,1,0,0,1,1,0,0,0,0,1,1,0],
        [1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,0,0,1,0],
        [1,0,0,1,0,1,1,1,0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1,0],
        [1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1,0],
        [1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0],
        [0,1,1,0,0,1,1,1,1,0,1,0,0,0,0,1,1,1,1,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0],
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
        matrix, folds = ReadInput(readlines)
        folded = FoldAll(matrix, folds)
        assert expectedOutput == folded #