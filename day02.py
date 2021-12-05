# https://adventofcode.com/2021/day/2

from typing import List, Tuple


def Navigate(startHorizPos: int, startDepth: int, route: List) -> Tuple[int, int]:
    finalHorizPos, finalDepth = startHorizPos, startDepth

    for instruction in route:
        direction, distance = instruction.split()
        if direction == "forward":
            finalHorizPos += int(distance)
        elif direction == "down":
            finalDepth += int(distance)
        elif direction == "up":
            finalDepth -= int(distance)

    return finalHorizPos, finalDepth


def NavigatewithAim(
    startHorizPos: int, startDepth: int, startAim: int, route: List
) -> Tuple[int, int, int]:
    finalHorizPos, finalDepth, finalAim = startHorizPos, startDepth, startAim

    for instruction in route:
        direction, distance = instruction.split()
        if direction == "forward":
            finalHorizPos += int(distance)
            finalDepth += finalAim * int(distance)
        elif direction == "down":
            finalAim += int(distance)
        elif direction == "up":
            finalAim -= int(distance)

    return finalHorizPos, finalDepth, finalAim


def main():
    with open("day02.input.txt", "rt") as inputFile:
        finalHorizPos, finalDepth, finalAim = NavigatewithAim(
            0, 0, 0, inputFile.readlines()
        )
        print(f"Final position:")
        print(
            f"(Horizontal Position, Depth, Aim) = ({finalHorizPos}, {finalDepth}, {finalAim})"
        )
        print(f"Horizontal Position * Depth = {finalHorizPos *finalDepth}")


if __name__ == "__main__":
    main()
