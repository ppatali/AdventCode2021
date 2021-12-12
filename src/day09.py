# https://adventofcode.com/2021/day/9

from typing import List, Tuple, Dict, Set

# [row, col]
ADJACENT_MATRIX = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def WithinBoundary(matrix: List[List[int]], row: int, col: int) -> bool:
    return row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0])


def FindLowPointCoordinates(heatmap: List[str]) -> List[Tuple[int, int]]:
    lowPointCoordinates = []
    for row in range(len(heatmap)):
        for col in range(len(heatmap[row])):
            # Find if this is the local minimum
            if int(heatmap[row][col]) < min(
                [
                    int(heatmap[row + r][col + c])
                    if WithinBoundary(heatmap, row + r, col + c)
                    else 10
                    for r, c in ADJACENT_MATRIX
                ]
            ):
                lowPointCoordinates.append((row, col))
    return lowPointCoordinates


def FindLowPoints(
    heatmap: List[str], lowPointCoorinates: List[Tuple[int, int]]
) -> List[int]:
    return [int(heatmap[i][j]) for (i, j) in lowPointCoorinates]


def ComputRiskScore(lowPoints: List[int]) -> int:
    return sum([lowPoint + 1 for lowPoint in lowPoints])


def FindBasins(
    heatmap: List[str], lowPointCoorinates: List[Tuple[int, int]]
) -> List[List[int]]:
    basins: List[List[int]] = [[] for _ in range(len(lowPointCoorinates))]

    for i in range(len(lowPointCoorinates)):
        queue: List[Tuple[int, int]] = [lowPointCoorinates[i]]

        j = 0  # queue head
        while j < len(queue):
            rowCurr, colCurr = queue[j]  # dequeue
            basins[i].append(int(heatmap[rowCurr][colCurr]))  # add to basin

            # check adjacent points, if valid add to back of the queue
            for r, c in ADJACENT_MATRIX:
                row, col = rowCurr + r, colCurr + c
                if (
                    WithinBoundary(heatmap, row, col)
                    and int(heatmap[row][col]) != 9
                    and (row, col) not in queue
                ):
                    queue.append((row, col))  # enqueue

            j += 1  # next in the queue

    return basins


def Compute3LargestBasinsWeight(basins: List[List[int]]) -> int:
    basinSizes = [len(basin) for basin in basins]
    basinSizes.sort(reverse=True)
    return basinSizes[0] * basinSizes[1] * basinSizes[2]


def main():
    with open("day09.input.txt", "rt") as inputFile:
        heatmap = [line.strip() for line in inputFile.readlines()]
        lowPointCoorinates = FindLowPointCoordinates(heatmap)
        lowPoints = FindLowPoints(heatmap, lowPointCoorinates)
        print(f"Risk score for part 1 = {ComputRiskScore(lowPoints)}")

        basins = FindBasins(heatmap, lowPointCoorinates)
        print(f"3 Largest basins weight = {Compute3LargestBasinsWeight(basins)}")


if __name__ == "__main__":
    main()
