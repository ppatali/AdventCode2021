# https://adventofcode.com/2021/day/5

from typing import List, Tuple


def ReadInputLines(inputLines: List[str]) -> List[Tuple[int, int, int, int]]:
    lines = []
    for inputLine in inputLines:
        inputLine = inputLine.strip()
        lines.append(tuple([int(n) for n in inputLine.replace(" -> ", ",").split(",")]))
    return lines


def FindMaxXY(lines: List[Tuple[int, int, int, int]]) -> Tuple[int, int]:
    maxX = maxY = -1
    for x1, y1, x2, y2 in lines:
        if x1 > maxX:
            maxX = x1
        if x2 > maxX:
            maxX = x2
        if y1 > maxY:
            maxY = y1
        if y2 > maxY:
            maxY = y2
    return maxX, maxY


def PlotHorizontalAndVerticalLines(
    lines: List[Tuple[int, int, int, int]]
) -> List[List[int]]:
    maxX, maxY = FindMaxXY(lines)

    # Init a ZERO matrix of size maxX+1 by maxY+1
    matrix = [[0] * (maxY + 1) for _ in range(maxX + 1)]

    for x1, y1, x2, y2 in lines:
        if x1 == x2:  # vertical line
            for y in range(y1 if y1 <= y2 else y2, y1 + 1 if y1 > y2 else y2 + 1):
                matrix[y][x1] += 1
        elif y1 == y2:  # horizontal line
            for x in range(x1 if x1 <= x2 else x2, x1 + 1 if x1 > x2 else x2 + 1):
                matrix[y1][x] += 1

    return matrix


def PlotHorizontalAndVerticalAndDiagonalLines(
    lines: List[Tuple[int, int, int, int]]
) -> List[List[int]]:
    maxX, maxY = FindMaxXY(lines)

    # Init a ZERO matrix of size maxX+1 by maxY+1
    matrix = [[0] * (maxY + 1) for _ in range(maxX + 1)]

    for x1, y1, x2, y2 in lines:
        xi = 1 if x1 < x2 else -1 if x1 > x2 else 0
        yi = 1 if y1 < y2 else -1 if y1 > y2 else 0

        x = x1
        y = y1
        while x != x2 or y != y2:
            matrix[y][x] += 1
            x += xi
            y += yi

        matrix[y][x] += 1

    return matrix


def CountOverlap(matrix: List[List[int]]) -> int:
    count = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            count += 1 if matrix[r][c] > 1 else 0
    return count


def main():
    with open("day05.input.txt", "rt") as inputFile:
        lines = ReadInputLines(inputFile.readlines())
        matrix = PlotHorizontalAndVerticalLines(lines)
        print(
            f"Overlap count when horizontal and vertical lines are considered = {CountOverlap(matrix)}"
        )

        matrix2 = PlotHorizontalAndVerticalAndDiagonalLines(lines)
        print(
            f"Overlap count when horizontal, vertical and diagonal lines are considered = {CountOverlap(matrix2)}"
        )


if __name__ == "__main__":
    main()
