from day02 import *


def test_Part1Result():
    with open("day02.input.txt", "rt") as inputFile:
        finalHorizPos, finalDepth = Navigate(inputFile.readlines())
        assert finalHorizPos == 1975 and finalDepth == 800
        assert finalHorizPos * finalDepth == 1580000


def test_Part2Result():
    with open("day02.input.txt", "rt") as inputFile:
        finalHorizPos, finalDepth, finalAim = NavigatewithAim(inputFile.readlines())
        assert finalHorizPos == 1975 and finalDepth == 633551 and finalAim == 800
        assert finalHorizPos * finalDepth == 1251263225
