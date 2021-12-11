# https://adventofcode.com/2021/day/8

from typing import List, Tuple, Dict, Set


def FindLowPointCoordinates(heatmap: List[str]) -> List[Tuple[int, int]]:
    lowPointCoordinates = []
    for y in range(len(heatmap)):
        for x in range(len(heatmap[y])):
            # Find if this is the local minimum
            if int(heatmap[y][x]) < min(
                [
                    # check adjacent points
                    int(heatmap[y][x - 1] if x - 1 >= 0 else 10),  # left
                    int(heatmap[y][x + 1] if x + 1 < len(heatmap[y]) else 10),  # right
                    int(heatmap[y - 1][x] if y - 1 >= 0 else 10),  # top
                    int(heatmap[y + 1][x] if y + 1 < len(heatmap) else 10),  # bottom
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
        queue: List[Tuple[int, int]] = [lowPointCoorinates[i]]

        j = 0
        while j < len(queue):
            y, x = queue[j]

            basins[i].append(int(heatmap[y][x]))  # add to basin

            # check adjacent points, if valid add to back of the queue
            # left
            if x - 1 >= 0 and int(heatmap[y][x - 1]) != 9 and (y, x - 1) not in queue:
                queue.append((y, x - 1))

            # right
            if x + 1 < len(heatmap[y]) and int(heatmap[y][x + 1]) != 9 and (y, x + 1) not in queue:
                queue.append((y, x + 1))

            # top
            if y - 1 >= 0 and int(heatmap[y - 1][x]) != 9 and (y - 1, x) not in queue:
                queue.append((y - 1, x))

            # bottom
            if y + 1 < len(heatmap) and int(heatmap[y + 1][x]) != 9 and (y + 1, x) not in queue:
                queue.append((y + 1, x))

            j += 1

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
