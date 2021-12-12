# https://adventofcode.com/2021/day/12

from typing import List, Tuple, Dict, Set


def GetNodes(lines: List[str]) -> Dict[str, List[str]]:
    nodes: Dict[str, List[str]] = {}

    for line in lines:
        node1, node2 = line.split("-")
        if node1 in nodes:
            nodes[node1].append(node2)
        else:
            nodes[node1] = [node2]

        if node1 != "start" and node2 != "end":
            if node2 in nodes:
                nodes[node2].append(node1)
            else:
                nodes[node2] = [node1]

    return nodes


def IsSmallCave(name: str) -> bool:
    return name != "start" and name != "end" and name.islower()


def IsBigCave(name: str) -> bool:
    return name != "start" and name != "end" and name.isupper()


def FindPaths(
    caveMap: Dict[str, List[str]],  # valid/available caves to caves paths
    fromCave: str,  # currently in this cave
    fullPaths: List[List[str]],  # full paths found so far
    partialPath: List[str] = [],  # caves in the path constructed so far
) -> None:

    # push the current cave
    partialPath.append(fromCave)

    if fromCave == "end":
        fullPaths.append(list(partialPath.copy()))
    else:
        for toCave in caveMap[fromCave]:
            # As per rule, check if it is valid to visit the next cave
            if (
                toCave == "end"
                or IsBigCave(toCave)
                or (IsSmallCave(toCave) and toCave not in partialPath)
            ):
                FindPaths(caveMap, toCave, fullPaths, partialPath)

    # pop the current cave, as we are returning back to previous cave
    partialPath.pop()


def FindPaths2(
    caveMap: Dict[str, List[str]],  # valid/available caves to caves paths
    fromCave: str,  # currently in this cave
    fullPaths: List[List[str]],  # full paths found so far
    partialPath: List[str] = [],  # caves in the path constructed so far,
    caveVisitCounter: Dict[str, int] = {},
) -> None:

    # push the current cave
    partialPath.append(fromCave)
    if fromCave not in caveVisitCounter:
        caveVisitCounter[fromCave] = 0
    caveVisitCounter[fromCave] += 1

    if fromCave == "end":
        fullPaths.append(list(partialPath.copy()))
    else:
        for toCave in caveMap[fromCave]:
            # As per rule, check if it is valid to visit the next cave
            if toCave == "end" or IsBigCave(toCave):
                FindPaths2(caveMap, toCave, fullPaths, partialPath, caveVisitCounter)
            elif IsSmallCave(toCave):
                if toCave not in partialPath or (  # if cave not visited before
                    caveVisitCounter[toCave]
                    < 2  # this cave should have been max once before
                    and sum(  # no other small cave visited 2 times
                        count == 2
                        for cave, count in caveVisitCounter.items()
                        if cave != toCave and IsSmallCave(cave)
                    )
                    == 0
                ):
                    FindPaths2(
                        caveMap, toCave, fullPaths, partialPath, caveVisitCounter
                    )

    # pop the current cave, as we are returning back to previous cave
    partialPath.pop()
    caveVisitCounter[fromCave] -= 1


def main():
    with open("day12.input.txt", "rt") as inputFile:
        lines = [line.strip() for line in inputFile.readlines()]
        caveMap = GetNodes(lines)
        fullPaths = []
        FindPaths(caveMap, "start", fullPaths)
        print(f"Part 1 - Total number of paths = {len(fullPaths)}")

        fullPaths2 = []
        FindPaths2(caveMap, "start", fullPaths2)
        print(f"Part 2 - Total number of paths = {len(fullPaths2)}")


if __name__ == "__main__":
    main()
