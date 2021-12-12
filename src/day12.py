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
    caveMap: Dict[str, List[str]],
    fromCave: str,
    fullPaths: List[List[str]],
    partialPath: List[str],
) -> None:

    if fromCave == "end":
        partialPath.append("end")
        fullPaths.append(partialPath.copy())
        partialPath.pop()
    else:
        partialPath.append(fromCave)  # push

        for toCave in caveMap[fromCave]:
            if (
                toCave == "end"
                or IsBigCave(toCave)
                or (IsSmallCave(toCave) and toCave not in partialPath)
            ):
                FindPaths(caveMap, toCave, fullPaths, partialPath)

        partialPath.pop()  # pop


def main():
    with open("day12.input.txt", "rt") as inputFile:
        lines = [line.strip() for line in inputFile.readlines()]
        caveMap = GetNodes(lines)
        fullPaths = []
        FindPaths(caveMap, "start", fullPaths, [])
        print(f"Total number of paths = {len(fullPaths)}")


if __name__ == "__main__":
    main()
