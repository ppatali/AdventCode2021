# https://adventofcode.com/2021/day/1

from typing import List


def UpTrendsInSlidingWindow(measurements: List, windowSize: int = 1) -> int:
    count = 0
    for i in range(windowSize, len(measurements)):
        if measurements[i - windowSize] < measurements[i]:
            count += 1
    return count


def main():
    with open("day01.input.txt", "rt") as inputFile:
        measurements = [int(measurement) for measurement in inputFile.readlines()]
        print(
            f"Number of increased measurements = "
            f"{UpTrendsInSlidingWindow(measurements)}"
        )

        print(
            f"Number of increased measurements with three-measurements sliding window = "
            f"{UpTrendsInSlidingWindow(measurements, 3)}"
        )


if __name__ == "__main__":
    main()
