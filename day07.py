# https://adventofcode.com/2021/day/7
from typing import List, Tuple, Callable


def CostLinear(distance: int) -> int:
    return distance


def CostAccelerated(distance: int) -> int:
    return int((distance * (distance + 1)) / 2)


def GetAlignWithMinCost(
    positions: List[int], costFunc: Callable[[int], int]
) -> Tuple[int, int]:

    minCost = -1
    minCostPos = -1

    minPos, maxPos = min(positions), max(positions)

    for currPos in range(minPos, maxPos + 1):

        cost = 0
        for pos in positions:
            cost += costFunc(abs(currPos - pos))

        if minCost < 0 or cost < minCost:
            minCost = cost
            minCostPos = currPos

    return minCostPos, minCost


def main():
    with open("day07.input.txt", "rt") as inputFile:
        positions = [int(i) for i in inputFile.readline().split(",")]

        alignTo, minCost = GetAlignWithMinCost(positions, CostLinear)
        print(f"PART 1 - Aligning to position {alignTo} with min cost of {minCost}")

        alignTo, minCost = GetAlignWithMinCost(positions, CostAccelerated)
        print(f"PART 2 - Aligning to position {alignTo} with min cost of {minCost}")


if __name__ == "__main__":
    main()
