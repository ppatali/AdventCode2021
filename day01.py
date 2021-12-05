# https://adventofcode.com/2021/day/1

from typing import List


def NumberofIncreases(measurements: List) -> int:
    if not measurements:
        return 0

    count = 0
    for i in range(1, len(measurements)):

        prev, curr = int(measurements[i - 1]), int(measurements[i])
        # print(f"(prev, curr) = ({prev}, {curr})")
        if prev < curr:
            count += 1

    return count


def NumberofIncreasesWithSlidingWindow(measurements: List) -> int:
    if not measurements:
        return 0

    count = 0
    for i in range(3, len(measurements)):
        sumPrevWindow = (
            int(measurements[i - 3])
            + int(measurements[i - 2])
            + int(measurements[i - 1])
        )
        sumCurrWindow = (
            int(measurements[i - 2]) + int(measurements[i - 1]) + int(measurements[i])
        )

        if sumPrevWindow < sumCurrWindow:
            count += 1

    return count


def main():
    with open("day01.input.txt", "rt") as inputFile:
        print(f"Number of increased measurements = {NumberofIncreases(inputFile.readlines())}")
        inputFile.seek(0)
        print(f"Number of increased measurements with three-measurements sliding window = {NumberofIncreasesWithSlidingWindow(inputFile.readlines())}")

if __name__ == "__main__":
    main()
