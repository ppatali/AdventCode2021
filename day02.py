# https://adventofcode.com/2021/day/2

from typing import List, Tuple


def Navigate(startX: int, startY: int, route: List) -> Tuple[int, int]:
    finalX, finalY = startX, startY

    for instruction in route:
        direction, distance = instruction.split()
        if direction == "forward":
            finalX += int(distance)
        elif direction == "down":
            finalY += int(distance)
        elif direction == "up":
            finalY -= int(distance)

    return finalX, finalY


def NavigatewithAim(
    startX: int, startY: int, startZ: int, route: List
) -> Tuple[int, int, int]:
    finalX, finalY, finalZ = startX, startY, startZ

    for instruction in route:
        direction, distance = instruction.split()
        if direction == "forward":
            finalX += int(distance)
            finalY += finalZ * int(distance)
        elif direction == "down":
            finalZ += int(distance)
        elif direction == "up":
            finalZ -= int(distance)

    return finalX, finalY, finalZ


def main():
    with open("day02.input.txt", "rt") as inputFile:
        finalX, finalY, finalZ = NavigatewithAim(0, 0, 0, inputFile.readlines())
        print(f"Final position:")
        print(f"(X, Y, Z) = ({finalX}, {finalY}, {finalZ})")
        print(f"X * Y = {finalX *finalY}")


if __name__ == "__main__":
    main()
