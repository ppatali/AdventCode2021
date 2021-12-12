# https://adventofcode.com/2021/day/8

from typing import List, Tuple, Dict, Set

# [row, col]
ADJACENT_MATRIX = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, -1], [-1, 1], [1, 1]]


def WithinBoundary(matrix: List[List[int]], row: int, col: int) -> bool:
    return row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0])


def MoveAStep(octopuses: List[List[int]]) -> int:

    flasheQueue = []
    for row in range(len(octopuses)):
        for col in range(len(octopuses[row])):
            octopuses[row][col] += 1
            if octopuses[row][col] == 10:
                flasheQueue.append((row, col))  # enqueue

    i = 0  # queue head
    while i < len(flasheQueue):
        for r, c in ADJACENT_MATRIX:
            row, col = flasheQueue[i][0] + r, flasheQueue[i][1] + c  # dequeue
            if WithinBoundary(octopuses, row, col) and octopuses[row][col] != 10:
                octopuses[row][col] += 1
                if octopuses[row][col] == 10:
                    flasheQueue.append((row, col))  # enqueue
        i += 1

    for row, col in flasheQueue:
        octopuses[row][col] = 0

    return len(flasheQueue)


def AreAllOctopusesFlash(octopuses: List[List[int]]) -> bool:
    for row in range(len(octopuses)):
        for col in range(len(octopuses[row])):
            if octopuses[row][col] != 0:
                return False
    return True


def FindSynchronizedFlashStep(octopuses: List[List[int]]) -> int:
    step = 0
    while not AreAllOctopusesFlash(octopuses):
        step += 1
        MoveAStep(octopuses)
    return step


def main():
    with open("day11.input.txt", "rt") as inputFile:
        octopuses = [[int(col) for col in row.strip()] for row in inputFile.readlines()]
        totalFlashes = 0
        for _ in range(100):
            totalFlashes += MoveAStep(octopuses)
        print(f"After 100 steps, total flashes = {totalFlashes}")

        inputFile.seek(0)
        octopuses = [[int(col) for col in row.strip()] for row in inputFile.readlines()]
        syncStep = FindSynchronizedFlashStep(octopuses)
        print(f"Number of steps when all octopuses flash together = {syncStep}")


if __name__ == "__main__":
    main()
