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
    pos_p1, score_p1, pos_p2, score_p2 = start_p1, 0, start_p2, 0

    dice_roll_count = 0
    dice_last_pos = None

    while score_p1 < 1000 and score_p2 < 1000:
        dice_rolls = roll_dice_thrice(dice, dice_last_pos)
        dice_last_pos = dice_rolls[2]
        dice_roll_count += 3
        
        pos_p1 = move_pos(pos_p1, sum(dice_rolls))
        score_p1 += pos_p1
        if score_p1 >= 1000:
            break
        
        dice_rolls = roll_dice_thrice(dice, dice_last_pos)
        dice_last_pos = dice_rolls[2]
        dice_roll_count += 3
        
        pos_p2 = move_pos(pos_p2, sum(dice_rolls))
        score_p2 += pos_p2
        if score_p2 >= 1000:
            break

    return dice_roll_count * min(score_p1, score_p2)


def main():
    print(
        "Part 1 - Result of (dice_roll_count * looser's score) =",
        play(7, 10, dice_deterministic),
    )


if __name__ == "__main__":
    main()
