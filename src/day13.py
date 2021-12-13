# https://adventofcode.com/2021/day/13

from typing import List, Tuple, Dict, Set


def ReadInput(lines: List[str]) -> Tuple[List[str], List[Tuple[str, int]]]:
    xPoints: List[int] = []
    yPoints: List[int] = []
    folds: List[Tuple[str, int]] = []

    for line in lines:
        if line is None or len(line.strip()) == 0:
            continue
        elif line.startswith("fold along"):
            foldAlong, foldAt = line.replace("fold along ", "").split("=")
            folds.append((foldAlong, int(foldAt)))
        else:
            x, y = line.strip().split(",")
            xPoints.append(int(x))
            yPoints.append(int(y))

    matrix = [[0 for _ in range(max(xPoints) + 1)] for _ in range(max(yPoints) + 1)]

    for i in range(len(xPoints)):
        matrix[yPoints[i]][xPoints[i]] = 1

    return matrix, folds


def FoldOnce(matrix: List[List[int]], foldAlong: str, foldAt: int) -> List[str]:
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
        output = FoldOnce(output, foldAlong, foldAt)
    return output


def main():
    with open("day13.input.txt", "rt") as inputFile:
        readlines = [line.strip() for line in inputFile.readlines()]
        matrix, folds = ReadInput(readlines)
        folded = FoldOnce(matrix, folds[0][0], folds[0][1])
        count = sum([sum(x) for x in folded])
        print(f"Part 1 - Number of dots visible after first fold instruction = {count}")

        folded = FoldAll(matrix, folds)
        for y in range(len(folded)):
            print("".join(["#" if x == 1 else " " for x in folded[y]]))

        # Expected output when printed - UEFZCUCJ
        #  # #### #### ####  ##  #  #  ##    ##
        #  # #    #       # #  # #  # #  #    #
        #  # ###  ###    #  #    #  # #       #
        #  # #    #     #   #    #  # #       #
        #  # #    #    #    #  # #  # #  # #  #
        ##  #### #    ####  ##   ##   ##   ##


if __name__ == "__main__":
    main()
