# https://adventofcode.com/2021/day/15

from typing import List, Tuple, Dict, Set

LARGE_RISK = 1000000000

# This method ended up very slow and could not produce solution even after running for 30 minutes
def FindMinPathBruteForce(
    riskMap: List[List[int]],
    row: int,
    col: int,
    minRisk: int,
    pathRisk: int = 0
) -> None:

    riskMapSize = len(riskMap)
    # enter current position
    if row != 0 or col != 0:
        pathRisk += riskMap[row][col]

    # reached bottom right?
    if row == riskMapSize - 1 and col == riskMapSize - 1:        
        if pathRisk < minRisk:
            minRisk = pathRisk
    # keep exploring by going bottom and right 
    else:
        if col < riskMapSize - 1:
            minRisk = FindMinPathBruteForce(riskMap, row, col + 1, minRisk, pathRisk)
        if row < riskMapSize - 1:
            minRisk = FindMinPathBruteForce(riskMap, row + 1, col, minRisk, pathRisk)
    
    pathRisk -= riskMap[col][row]

    return minRisk

# This method of using Dijkstra algo is based on this solution
# https://github.com/michaeljgallagher/Advent-of-Code/blob/master/2021/15.py
from time import perf_counter_ns
import heapq
def FindMinPathDijkstra(riskMap):
    row, col = len(riskMap), len(riskMap[0])
    risks = {}
    heap = [(0, 0, 0)]

    while heap:
        risk, i, j = heapq.heappop(heap)
        if (i, j) == (row - 1, col - 1):
            return risk
        
        for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= ni < row and 0 <= nj < col:
                nrisk = risk + riskMap[ni][nj]
                if (ni, nj) not in risks or nrisk < risks[(ni, nj)]:
                    risks[(ni, nj)] = nrisk
                    heapq.heappush(heap, (nrisk, ni, nj))


def ReplicateGraph(riskMap, down, right):
    row, col = len(riskMap), len(riskMap[0])
    newRow, newCol = row * down, col * right
    newRiskMap = [[0 for _ in range(newCol)] for _ in range(newRow)]
    for i in range(newRow):
        for j in range(newCol):
            dist = i // row + j // col
            risk = riskMap[i % row][j % col] + dist
            risk = risk % 9 or risk
            newRiskMap[i][j] = risk
    return newRiskMap

# The code to compute time taken in baased on
# https://github.com/neelakantankk/Advent_of_Code_2021/blob/main/Day_14/day_14_p01.py
def main():
    with open("day15.input.txt", "rt") as inputFile:
        graph = [[int(n) for n in line.strip()] for line in inputFile.readlines()]
        START = perf_counter_ns()
        minRisk = FindMinPathDijkstra(graph)
        END = perf_counter_ns()
        ELAPSED = END - START
        print(f"Part 1 - lowest total risk of any path = {minRisk} (Time taken:{ELAPSED} ns/{ELAPSED/(10**6):.2f} ms/{ELAPSED/(10**9):.2f} s)")

        newGraph = ReplicateGraph(graph, 5, 5)
        START = perf_counter_ns()
        minRisk = FindMinPathDijkstra(newGraph)
        END = perf_counter_ns()
        ELAPSED = END - START
        print(f"Part 2 - lowest total risk of any path = {minRisk} (Time taken:{ELAPSED} ns/{ELAPSED/(10**6):.2f} ms/{ELAPSED/(10**9):.2f} s)")

if __name__ == "__main__":
    main()

