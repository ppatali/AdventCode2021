from typing import List, Tuple, Dict, Set
import math


def HighestYShort(TY0):
    return int((abs(TY0) - 1) * (abs(TY0)) / 2.0)


def FindArthProg(TX0, TX1):
    for n in range(TX0):
        v = int(n * (n + 1) / 2.0)
        if TX0 <= v and v <= TX1:
            return n


# Although I had figured out brute force x and y loop limits properly, I fumbled with the while loop logic
# The following C# answer helped in resolving my mental block
# https://github.com/PaxPumpkin/AdventOfCode/blob/master/AoC_2021/Day17_TrickShot.cs
def FindInitVelToHitTarget(TX0, TX1, TY0, TY1):
    minX = FindArthProg(TX0, TX1)
    hits = set()
    highestY = 0
    for x in range(minX, TX1 + 1):
        for y in range(TY0, abs(TY0)):
            xPos, yPos = 0, 0
            xVel, yVel = x, y
            currhighestY = 0
            while xPos <= TX1 and yPos >= TY0:
                xPos += xVel
                yPos += yVel
                currhighestY = max(currhighestY, yPos)
                if TX0 <= xPos and xPos <= TX1 and TY0 <= yPos and yPos <= TY1:
                    hits.add((x, y))
                    highestY = max(highestY, currhighestY)
                xVel -= 0 if xVel == 0 else 1
                yVel -= 1
    return hits, highestY


def main():
    with open("day17.input.txt", "rt") as inputFile:
        input = (
            inputFile.readline()
            .strip()
            .replace("target area: x=", "")
            .replace("y=", "")
            .split(", ")
        )
        TX0, TX1, TY0, TY1 = [int(n) for xy in input for n in xy.split("..")]

        hits, highestY = FindInitVelToHitTarget(TX0, TX1, TY0, TY1)
        print(
            f"Number of velocities to hit target = {len(hits)}; With highest Y = {highestY}"
        )


if __name__ == "__main__":
    main()
