# https://adventofcode.com/2021/day/14

from typing import List, Tuple, Dict, Set


def ReadInput(
    lines: List[str],
) -> Tuple[Dict[Tuple[str, str], int], Dict[Tuple[str, str], str]]:
    # First line is the template
    template = {}
    templateline = lines[0]
    for i in range(len(templateline) - 1):
        elem1, elem2 = templateline[i], templateline[i + 1]
        template[(elem1, elem2)] = (
            1 if (elem1, elem2) not in template else template[(elem1, elem2)] + 1
        )

    # Now read all the pair insertion, skipping any lines that does not include "->"
    pairInsertions = {}
    for line in lines:
        if line.find("->") != -1:
            pairchar, insertchar = line.strip().split(" -> ")
            pairInsertions[(pairchar[0], pairchar[1])] = insertchar

    return template, pairInsertions


def StepThrough(
    chain: Dict[Tuple[str, str], int], rules: Dict[Tuple[str, str], str]
) -> Dict[Tuple[str, str], int]:
    newChain: Dict[Tuple[str, str], int] = {}
    for (elem1, elem2), count in chain.items():
        elem3 = rules[(elem1, elem2)]
        
        newChain[(elem1, elem3)] = (
            count
            if (elem1, elem3) not in newChain
            else newChain[(elem1, elem3)] + count
        )
        
        newChain[(elem3, elem2)] = (
            count
            if (elem3, elem2) not in newChain
            else newChain[(elem3, elem2)] + count
        )
    return newChain


def CountElements(chain, lastTemplateElem: str) -> Dict[str, int]:
    elemCounts = {}
    for (elem1, elem2), count in chain.items():
        elemCounts[elem1] = (
            count if elem1 not in elemCounts else elemCounts[elem1] + count
        )
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
