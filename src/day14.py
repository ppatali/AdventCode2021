# https://adventofcode.com/2021/day/14

from collections import Counter
from typing import List, Tuple, Dict, Set


def ReadInput(
    lines: List[str],
) -> Tuple[Dict[Tuple[str, str], int], Dict[Tuple[str, str], str]]:
    # Parse the first line as template
    template = Counter([tuple(lines[0][i : i + 2]) for i in range(len(lines[0]) - 1)])
    
    # Now read all the pair insertion, skipping any lines that does not include "->"
    pairInsertions = dict([line.strip().split(" -> ") for line in lines if line.find("->") != -1])
    pairInsertions = {(key[0], key[1]) : value for key, value in pairInsertions.items()}

    return template, pairInsertions


def StepThrough(
    chain: Dict[Tuple[str, str], int], rules: Dict[Tuple[str, str], str]
) -> Dict[Tuple[str, str], int]:
    newChain: Dict[Tuple[str, str], int] = Counter()
    for (elem1, elem2), count in chain.items():
        elem3 = rules[(elem1, elem2)]
        newChain[(elem1, elem3)] += count        
        newChain[(elem3, elem2)] += count
    return newChain


def CountElements(chain, lastTemplateElem: str) -> Dict[str, int]:
    elemCounts = Counter()
    for (elem1, elem2), count in chain.items():
        elemCounts[elem1] += count
    # for the last element in the template, add 1
    elemCounts[lastTemplateElem] += 1
    return elemCounts


def main():
    with open("day14.input.txt", "rt") as inputFiles:
        lines = [line.strip() for line in inputFiles.readlines()]

    template, rules = ReadInput(lines)
    chain = template
    for _ in range(10):
        chain = StepThrough(chain, rules)
    elemCounts = CountElements(chain, lines[0][-1])
    diff = max(elemCounts.values()) - min(elemCounts.values())
    print(
        f"Part 1 - Difference between quantity of most common and least common element = {diff}"
    )

    chain = template
    for _ in range(40):
        chain = StepThrough(chain, rules)
    elemCounts = CountElements(chain, lines[0][-1])
    diff = max(elemCounts.values()) - min(elemCounts.values())

    print(
        f"Part 2 - Difference between quantity of most common and least common element = {diff}"
    )


if __name__ == "__main__":
    main()
