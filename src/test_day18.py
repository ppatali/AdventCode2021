from day18 import *


def test_addAll_Sample1():
    input = ["[1,1]", "[2,2]", "[3 3]", "[4,4]"]
    expected = "[[[[1,1],[2,2]],[3,3]],[4,4]]"
    assert expected == str(addall(input))

    input = ["[1,1]", "[2,2]", "[3 3]", "[4,4]", "[5,5]"]
    expected = "[[[[3,0],[5,3]],[4,4]],[5,5]]"
    assert expected == str(addall(input))

    input = ["[1,1]", "[2,2]", "[3 3]", "[4,4]", "[5,5]", "[6,6]"]
    expected = "[[[[5,0],[7,4]],[5,5]],[6,6]]"
    assert expected == str(addall(input))


def test_addAll_Sample2():
    input = [
        "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
        "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",
        "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]",
        "[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]",
        "[7,[5,[[3,8],[1,4]]]]",
        "[[2,[2,2]],[8,[8,1]]]",
        "[2,9]",
        "[1,[[[9,3],9],[[9,0],[0,7]]]]",
        "[[[5,[7,4]],7],1]",
        "[[[[4,2],2],6],[8,7]]",
    ]

    expected = "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"
    fish = addall(input)
    assert expected == str(fish) and 3488 == fish.magnitude()


def test_addAll_Sample3():
    input = [
        "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
        "[[[5,[2,8]],4],[5,[[9,9],0]]]",
        "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
        "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
        "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
        "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
        "[[[[5,4],[7,7]],8],[[8,3],8]]",
        "[[9,3],[[9,9],[6,[4,9]]]]",
        "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
        "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]",
    ]

    expected = "[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]"
    fish = addall(input)
    assert expected == str(fish) and 4140 == fish.magnitude()


def test_Magnitude():
    assert 143 == parse("[[1,2],[[3,4],5]]").magnitude()
    assert 1384 == parse("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]").magnitude()
    assert 445 == parse("[[[[1,1],[2,2]],[3,3]],[4,4]]").magnitude()
    assert 791 == parse("[[[[3,0],[5,3]],[4,4]],[5,5]]").magnitude()
    assert 1137 == parse("[[[[5,0],[7,4]],[5,5]],[6,6]]").magnitude()
    assert (
        3488
        == parse("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]").magnitude()
    )


def test_Part1Result():
    with open("src/day18.input.txt", "rt") as inputFile:
        input = [line.strip() for line in inputFile.readlines()]
        expected = "[[[[6,8],[9,7]],[[9,5],[9,0]]],[[[9,9],[5,7]],[[5,0],[8,0]]]]"
        fish = addall(input)
        assert expected == str(fish) and 4176 == fish.magnitude()


def test_Part2_Sample3():
    input = [
        "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
        "[[[5,[2,8]],4],[5,[[9,9],0]]]",
        "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
        "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
        "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
        "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
        "[[[[5,4],[7,7]],8],[[8,3],8]]",
        "[[9,3],[[9,9],[6,[4,9]]]]",
        "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
        "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]",
    ]

    expected = "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"
    assert 3993 == maxMagOnPermutation(input)


def test_Part1Result():
    with open("src/day18.input.txt", "rt") as inputFile:
        input = [line.strip() for line in inputFile.readlines()]
        fish = addall(input)
        assert 4633 == maxMagOnPermutation(input)
