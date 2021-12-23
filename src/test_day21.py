from day21 import *

def test_Part1_Sample():
    assert 739785 == play(4, 8, dice_deterministic) 


def test_Part1Result():
    assert 802452 == play(7, 10, dice_deterministic)

def test_Part2Result():
    assert 270005289024391 == max(compute_wins(7, 0, 10, 0))