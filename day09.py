# https://adventofcode.com/2021/day/8

from typing import List, Tuple, Dict, Set


IMPOSSIBLE_LOWPOINT_HEIGHT = 10
INVALID_BASIN_HEIGHT = 9


def FindLowPointCoordinates(heatmap: List[str]) -> List[Tuple[int, int]]:
    lowPointCoordinates = []
    for y in range(len(heatmap)):
        for x in range(len(heatmap[y])):
            if int(heatmap[y][x]) < min(
                [
                    # check adjacent points
                    int(
                        heatmap[y][x - 1] if x - 1 >= 0 else IMPOSSIBLE_LOWPOINT_HEIGHT
                    ),  # left
                    int(
                        heatmap[y][x + 1]
                        if x + 1 < len(heatmap[y])
                        else IMPOSSIBLE_LOWPOINT_HEIGHT
                    ),  # right
                    int(
                        heatmap[y - 1][x] if y - 1 >= 0 else IMPOSSIBLE_LOWPOINT_HEIGHT
                    ),  # top
                    int(
                        heatmap[y + 1][x]
                        if y + 1 < len(heatmap)
                        else IMPOSSIBLE_LOWPOINT_HEIGHT
                    ),  # bottom
                ]
            ):
                lowPointCoordinates.append((y, x))
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
        tobeProcessed: List[Tuple[int, int]] = [lowPointCoorinates[i]]

        j = 0
        while j < len(tobeProcessed):
            y, x = tobeProcessed[j]

            basins[i].append(int(heatmap[y][x]))  # add to basin

            # check adjacent points, if valid add to back of the queue
            # left
            if (
                x - 1 >= 0
                and int(heatmap[y][x - 1]) != INVALID_BASIN_HEIGHT
                and (y, x - 1) not in tobeProcessed
            ):
                tobeProcessed.append((y, x - 1))

            # right
            if (
                x + 1 < len(heatmap[y])
                and int(heatmap[y][x + 1]) != INVALID_BASIN_HEIGHT
                and (y, x + 1) not in tobeProcessed
            ):
                tobeProcessed.append((y, x + 1))

            # top
            if (
                y - 1 >= 0
                and int(heatmap[y - 1][x]) != INVALID_BASIN_HEIGHT
                and (y - 1, x) not in tobeProcessed
            ):
                tobeProcessed.append((y - 1, x))

            # bottom
            if (
                y + 1 < len(heatmap)
                and int(heatmap[y + 1][x]) != INVALID_BASIN_HEIGHT
                and (y + 1, x) not in tobeProcessed
            ):
                tobeProcessed.append((y + 1, x))

            j += 1

    return basins


def Compute3LargestBasinsWeight(basins: List[List[int]]) -> int:
    basinsSizes = [len(basin) for basin in basins]
    basinsSizes.sort(reverse=True)
    return basinsSizes[0] * basinsSizes[1] * basinsSizes[2]


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
