# https://adventofcode.com/2021/day/13

from typing import List, Tuple, Dict, Set


def ReadInput(lines: List[str]) -> Tuple[List[str], List[Tuple[int, int]], List[Tuple[str, int]]]:
    folds: List[Tuple[str, int]] = []
    points: List[Tuple[int, int]] = []
    maxX, maxY = -1, -1

    for line in lines:
        if line is None or len(line.strip()) == 0:
            continue
        elif line.startswith("fold along"):
            foldAlong, foldAt = line.replace("fold along ", "").split("=")
            folds.append((foldAlong, int(foldAt)))
        else:
            x, y = line.strip().split(",")
            maxX, maxY = max(maxX, int(x)), max(maxY, int(y))
            points.append((int(x),int(y)))

    matrix = [[0 for _ in range(maxX + 1)] for _ in range(maxY + 1)]

    for (x, y) in points:
        matrix[y][x] = 1

    return matrix, points, folds


def Fold(matrix: List[List[int]], foldAlong: str, foldAt: int) -> List[List[int]]:
    maxX, maxY = len(matrix[0]), len(matrix)
    # Fold vertically?
    if foldAlong == "x":
        output = [[0 for _ in range(foldAt)] for _ in range(maxY)]
        for x in range(foldAt):
            for y in range(maxY):
                if foldAt + 1 + x < maxX:
                    output[y][foldAt - 1 - x] = (
                        matrix[y][foldAt - 1 - x] | matrix[y][foldAt + 1 + x]
                    )
        return output
    elif foldAlong == "y":
        output = [[0 for _ in range(maxX)] for _ in range(foldAt)]
        for x in range(maxX):
            for y in range(foldAt):
                if foldAt + 1 + y < maxY:
                    output[foldAt - 1 - y][x] = (
                        matrix[foldAt - 1 - y][x] | matrix[foldAt + 1 + y][x]
                    )
        return output


def FoldAll(matrix: List[List[int]], folds: List[Tuple[str, int]]) -> List[List[int]]:
    output = matrix
    for foldAlong, foldAt in folds:
        output = Fold(output, foldAlong, foldAt)
    return output

# In this methods, the points are not plotted on a matrix
# the logic instead uses only the list of points
# Hence it is both space and time efficient as compared to using matrix
# The logic is to check the point with respect to axis of folding
#   if right side or bottom of the axis, then add the reflection of that point to list
def FoldUsingPoints(points: List[Tuple[int, int]], foldAlong: str, foldAt: int) -> List[Tuple[int, int]]:
    output = []
    LARGE_NUM = 1000000000
    foldAxisX = foldAt if foldAlong == "x" else LARGE_NUM
    foldAxisY = foldAt if foldAlong == "y" else LARGE_NUM
    for x, y in points:
        # If right of axis, compute the reflection
        x1 = x if x < foldAxisX else foldAxisX - (x - foldAxisX)
        # If bottom of axis, compute the reflection
        y1 = y if y < foldAxisY else foldAxisY - (y - foldAxisY)
        if (x1, y1) not in output:
            output.append((x1, y1))
    return output


def FoldAllUsingPoints(points: List[Tuple[int, int]], folds: List[Tuple[str, int]]) -> List[List[int]]:
    output = points
    for foldAlong, foldAt in folds:
        output = FoldUsingPoints(output, foldAlong, foldAt)
    return output


def main():
    with open("day13.input.txt", "rt") as inputFile:
        readlines = [line.strip() for line in inputFile.readlines()]
        matrix, points, folds = ReadInput(readlines)
        
        folded = Fold(matrix, folds[0][0], folds[0][1])
        count = sum([sum(x) for x in folded])
        print(f"Part 1 - Method A - Number of dots visible after first fold instruction = {count}")
        
        folded = FoldUsingPoints(points, folds[0][0], folds[0][1])
        print(f"Part 1 - Method B - Number of dots visible after first fold instruction = {len(folded)}")

        print(f"Part 2 - Method A")
        folded = FoldAll(matrix, folds)
        for y in range(len(folded)):
            print("".join(["#" if x == 1 else " " for x in folded[y]]))

        print(f"Part 2 - Method B")
        folded = FoldAllUsingPoints(points, folds)
        
        # make matrix of points and print
        maxX = max([x for x, _ in folded])
        maxY = max([y for _, y in folded])
        for y in range(maxY + 1):
            line = ""
            for x in range(maxX + 1):
                line += "#" if (x, y) in folded else " "
            print(line)

        # Expected output when printed - UEFZCUCJ
        #  # #### #### ####  ##  #  #  ##    ##
        #  # #    #       # #  # #  # #  #    #
        #  # ###  ###    #  #    #  # #       #
        #  # #    #     #   #    #  # #       #
        #  # #    #    #    #  # #  # #  # #  #
         ##  #### #    ####  ##   ##   ##   ##


if __name__ == "__main__":
    main()
