from day02 import *


def test_Part1Result():
    with open("day02.input.txt", "rt") as inputFile:
        finalX, finalY = Navigate(0, 0, inputFile.readlines())
        assert finalX == 1975 and finalY == 800
        assert finalX * finalY == 1580000


def test_Part1Result():
    with open("day02.input.txt", "rt") as inputFile:
        finalX, finalY, finalZ = NavigatewithAim(0, 0, 0, inputFile.readlines())
        assert finalX == 1975 and finalY == 633551 and finalZ == 800
        assert finalX * finalY == 1251263226
