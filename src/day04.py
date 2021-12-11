# https://adventofcode.com/2021/day/4

from typing import List, Tuple


def ReadInput(filename: str) -> Tuple[List[int], List[List[List[int]]]]:
    with open(filename, "rt") as inputFile:
        # read all draws as list of int
        firstline = inputFile.readline().strip()
        draws = [int(n) for n in firstline.split(",")]

        # read all boards as List[List[List[int]]]
        boards = []
        board = None

        nextline = inputFile.readline()
        while nextline:
            nextline = nextline.strip()

            # If empty line, add current board to list
            if len(nextline) == 0:
                if board:
                    boards.append(board)
                    board = None
            else:
                # start of a new board
                if not board:
                    board = []
                # add row to current board
                board.append([int(c) for c in nextline.split()])

            nextline = inputFile.readline()

        # Append the last board to the list
        if board:
            boards.append(board)

        return (draws, boards)


MARKER = -1


def MarkBoard(board: List[List[int]], draw: int) -> None:
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == draw:
                board[r][c] = MARKER


def IsAWinner(board: List[List[int]]) -> bool:
    # check row-wise
    for r in range(len(board)):
        marked = False
        for c in range(len(board[r])):
            if board[r][c] == MARKER:
                marked = True
            else:
                marked = False
                break
        if marked:
            return True

    # check column-wise
    # Assume all rows have same number of elements
    for c in range(len(board[0])):
        marked = False
        for r in range(len(board)):
            if board[r][c] == MARKER:
                marked = True
            else:
                marked = False
                break

        if marked:
            return True

    return False


def GetBoardScore(board: List[List[int]], lastDraw: int) -> int:
    score = 0
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] != MARKER:
                score += board[r][c]

    return score * lastDraw


def PlayBingo(fileName: str) -> int:
    score = -1

    draws, boards = ReadInput(fileName)

    for draw in draws:
        for board in boards:
            MarkBoard(board, draw)
            if IsAWinner(board):
                score = GetBoardScore(board, draw)
                break
        if score != -1:
            break

    return score


def PlayBingoToLoose(fileName: str) -> int:

    draws, boards = ReadInput(fileName)

    winnerBoardIndices = set()
    lastWinnerBoardIndex = None
    lastWinningDraw = None

    for draw in draws:

        for i in range(len(boards)):
            if i in winnerBoardIndices:
                continue

            MarkBoard(boards[i], draw)
            if IsAWinner(boards[i]):
                winnerBoardIndices.add(i)
                lastWinnerBoardIndex = i
                lastWinningDraw = draw

    if len(winnerBoardIndices) > 1:
        return GetBoardScore(boards[lastWinnerBoardIndex], lastWinningDraw)
    else:
        return None


def main():
    score = PlayBingo("day04.input.txt")
    print(f"Play to Win - Score = {score}")

    score = PlayBingoToLoose("day04.input.txt")
    print(f"Play to Loose - Score = {score}")


if __name__ == "__main__":
    main()
