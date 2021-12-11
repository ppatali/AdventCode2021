# https://adventofcode.com/2021/day/10

from typing import List, Tuple, Dict, Set

BRACKETS = {"(": ")", "[": "]", "{": "}", "<": ">"}
CORRUPTION_POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
INCOMPLETE_POINTS = {")": 1, "]": 2, "}": 3, ">": 4}


def FindFirstCorruption(lines: List[str]) -> List[str]:
    corruptions = []
    for line in lines:
        stack = []
        for c in line:
            if c in BRACKETS.keys():
                stack.append(c)
            elif len(stack) == 0:
                corruptions.append(c)
                break
            elif BRACKETS[stack.pop()] != c:
                corruptions.append(c)
    return corruptions


def ComputeCorruptionScore(corruptions: List[str]):
    score = 0
    for c in corruptions:
        score += CORRUPTION_POINTS[c]
    return score


def FindAutoCompletes(lines: List[str]) -> List[str]:
    autocompletes = []
    for line in lines:
        stack = []
        corrupted = False
        for c in line:
            if c in BRACKETS.keys():
                stack.append(c)
            elif len(stack) == 0:
                corrupted = True
                break
            elif BRACKETS[stack.pop()] != c:
                corrupted = True

        if corrupted:
            continue

        autocompletes.append("".join([BRACKETS[c] for c in reversed(stack)]))

    return autocompletes


def ComputeAutoCompletWinner(autocompletes: List[str]):
    scores = []
    for line in autocompletes:
        score = 0
        for c in line:
            score = 5 * score + INCOMPLETE_POINTS[c]
        scores.append(score)
    scores.sort()
    return scores[len(scores) >> 1]


def main():
    with open("day10.input.txt", "rt") as inputFile:
        lines = [l.strip() for l in inputFile.readlines()]
        corruptions = FindFirstCorruption(lines)
        print(f"Syntax error score = {ComputeCorruptionScore(corruptions)}")

        autocompletes = FindAutoCompletes(lines)
        print(
            f"Auto completion winnder score = {ComputeAutoCompletWinner(autocompletes)}"
        )


if __name__ == "__main__":
    main()
