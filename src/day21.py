# https://adventofcode.com/2021/day/21

from typing import List, Tuple, Callable


def dice_deterministic(last: int) -> int:
    return (last % 100) + 1 if last is not None else 1


def roll_dice_thrice(dice: Callable[[int], int], last: int = None) -> List[int]:
    r1 = dice(last)
    r2 = dice(r1)
    r3 = dice(r2)
    return [r1, r2, r3]


def move_pos(curr_pos: int, steps: int) -> int:
    return (curr_pos + steps - 1) % 10 + 1


def play(start_p1: int, start_p2: int, dice: Callable[[int], int]):
    # matrix of each player [current position on board, score]
    players = [[start_p1, 0], [start_p2, 0]]

    player_no = 0
    dice_roll_count = 0
    dice_last_pos = None

    while players[0][1] < 1000 and players[1][1] < 1000:
        dice_roll_count += 3
        dice_rolls = roll_dice_thrice(dice, dice_last_pos)

        players[player_no][0] = move_pos(players[player_no][0], sum(dice_rolls))
        players[player_no][1] += players[player_no][0]

        # get ready for next player turn
        dice_last_pos = dice_rolls[2]
        player_no = 1 if player_no == 0 else 0

    return dice_roll_count * (players[1][1] if players[0][1] >= 1000 else players[0][1])


def main():
    print(
        "Part 1 - Result of (dice_roll_count * looser's score) =",
        play(7, 10, dice_deterministic),
    )


if __name__ == "__main__":
    main()
