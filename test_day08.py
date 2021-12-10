from day08 import *


def test_CountDigitsInOutput():
    input = [
        "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
        "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
        "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
        "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
        "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
        "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
        "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
        "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
        "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
        "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
    ]

    lines = ReadInputLinesAsSets(input)
    assert 26 == CountDigitsWithGivenSegmentLengthInOutput(lines, [2, 3, 4, 7])


def test_Part1Result():
    with open("day08.input.txt", "rt") as inputFile:
        readlines = inputFile.readlines()
        lines = ReadInputLinesAsSets(readlines)
        digitsWithSegmentLengthToFind = [2, 3, 4, 7]
        assert 512 == CountDigitsWithGivenSegmentLengthInOutput(
            lines, digitsWithSegmentLengthToFind
        )


def test_ReadInputLinesAsSets():
    input = [
        "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    ]

    lines = ReadInputLinesAsSets(input)
    signals, outputs = lines[0]
    assert signals == [
        {"a", "c", "e", "d", "g", "f", "b"},
        {"c", "d", "f", "b", "e"},
        {"g", "c", "d", "f", "a"},
        {"f", "b", "c", "a", "d"},
        {"d", "a", "b"},
        {"c", "e", "f", "a", "b", "d"},
        {"c", "d", "f", "g", "e", "b"},
        {"e", "a", "f", "b"},
        {"c", "a", "g", "e", "d", "b"},
        {"a", "b"},
    ]
    assert outputs == [
        {"c", "d", "f", "e", "b"},
        {"f", "c", "a", "d", "b"},
        {"c", "d", "f", "e", "b"},
        {"c", "d", "b", "a", "f"},
    ]


def test_DecodeSample1():
    input = [
        "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    ]

    lines = ReadInputLinesAsSets(input)
    assert [5353] == Decode(lines)


def test_DecodeSample2():
    input = [
        "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
        "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
        "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
        "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
        "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
        "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
        "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
        "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
        "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
        "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
    ]

    lines = ReadInputLinesAsSets(input)
    decodedOutputs = Decode(lines)
    assert [
        8394,
        9781,
        1197,
        9361,
        4873,
        8418,
        4548,
        1625,
        8717,
        4315,
    ] == decodedOutputs
    assert 61229 == sum(decodedOutputs)


def test_Part2Result():
    with open("day08.input.txt", "rt") as inputFile:
        readlines = inputFile.readlines()
        lines = ReadInputLinesAsSets(readlines)
        assert 1091165 == sum(Decode(lines))
