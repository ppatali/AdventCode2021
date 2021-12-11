from day10 import *


def test_FindFirstCorruption():
    test = [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]

    assert ["}", ")", "]", ")", ">"] == FindFirstCorruption(test)


def test_ComputeScore():
    test = ["}", ")", "]", ")", ">"]
    assert 26397 == ComputeCorruptionScore(test)


def test_FindAutoCompletes():
    test = [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]

    assert [
        "}}]])})]",
        ")}>]})",
        "}}>}>))))",
        "]]}}]}]}>",
        "])}>",
    ] == FindAutoCompletes(test)


def test_ComputeAutoCompletWinner():
    test = ["}}]])})]", ")}>]})", "}}>}>))))", "]]}}]}]}>", "])}>"]
    assert 288957 == ComputeAutoCompletWinner(test)


def test_Part1Result():
    with open("day10.input.txt", "rt") as inputFile:
        lines = [l.strip() for l in inputFile.readlines()]
        corruptions = FindFirstCorruption(lines)
        assert 366027 == ComputeCorruptionScore(corruptions)


def test_Part2Result():
    with open("day10.input.txt", "rt") as inputFile:
        lines = [l.strip() for l in inputFile.readlines()]
        autocompletes = FindAutoCompletes(lines)
        assert 1118645287 == ComputeAutoCompletWinner(autocompletes)
