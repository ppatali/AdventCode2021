# https://adventofcode.com/2021/day/8

from typing import List, Tuple

MAP_DIGIT_SEGMENT_LENGTH = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}


def ReadInputLines(inputLines: List[str]) -> List[Tuple[List[str], List[str]]]:
    lines = []
    for inputLine in inputLines:
        signals, outputs = tuple(inputLine.strip().split(" | "))
        lines.append((signals.split(), outputs.split()))
    return lines


def CountDigitsInOutput(
    lines: List[Tuple[List[str], List[str]]], digitsToFind: List[int]
) -> int:
    count = 0
    for _, outputs in lines:
        for output in outputs:
            for digit in digitsToFind:
                if len(output) == MAP_DIGIT_SEGMENT_LENGTH[digit]:
                    count += 1
    return count


def main():
    with open("day08.input.txt", "rt") as inputFile:
        readlines = inputFile.readlines()
        lines = ReadInputLines(readlines)
        digitsToFind = [1, 4, 7, 8]
        print(
            f"Number of occurances of {digitsToFind} = {CountDigitsInOutput(lines, digitsToFind)}"
        )


if __name__ == "__main__":
    main()
