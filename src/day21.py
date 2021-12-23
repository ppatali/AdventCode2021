# https://adventofcode.com/2021/day/21

from typing import List, Tuple, Callable
import functools
import itertools
import collections


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


# using cycle() for the dice
# Ref: https://www.youtube.com/watch?v=rEyAbeV48tI


def play_method2(start_p1: int, start_p2) -> int:
    dice = itertools.cycle(range(1, 101))
    pos_p1, score_p1, pos_p2, score_p2 = start_p1, 0, start_p2, 0
    dice_roll_count = 0

    while True:
        pos_p1 = move_pos(pos_p1, next(dice) + next(dice) + next(dice))
        dice_roll_count += 3
        score_p1 += pos_p1
        if score_p1 >= 1000:
            break

        pos_p2 = move_pos(pos_p2, next(dice) + next(dice) + next(dice))
        dice_roll_count += 3
        score_p2 += pos_p2
        if score_p2 >= 1000:
            break
    return dice_roll_count * min(score_p1, score_p2)


# Note: Part 2 - The below solution is based on following YouTube video
# https://www.youtube.com/watch?v=rEyAbeV48tI
# https://github.com/anthonywritescode/aoc2021/tree/main/day21

# Things learned from this solutions
# - itertools.product
# - functools.cache (for memoization)


# Note: itertools.product below is equivalent to for loop on (1,2,3) nested 3 levels deep
# Since the permutations of the dice repeats, a counter for each unique sum is used to
# which reducing the number of looping
rolls = collections.Counter(
    sum(pt) for pt in itertools.product((1, 2, 3), (1, 2, 3), (1, 2, 3))
)


@functools.cache
def compute_wins(
    pos_p1: int, score_p1: int, pos_p2: int, score_p2: int
) -> Tuple[int, int]:
    wins_p1 = wins_p2 = 0
    for k, ct in rolls.items():
        newpos_p1 = move_pos(pos_p1, k)
        newscore_p1 = newpos_p1 + score_p1
        if newscore_p1 >= 21:
            wins_p1 += ct
        else:
            tmp_wins_p2, tmp_wins_p1 = compute_wins(
                pos_p2, score_p2, newpos_p1, newscore_p1
            )
            wins_p1 += tmp_wins_p1 * ct
            wins_p2 += tmp_wins_p2 * ct

    return wins_p1, wins_p2


def main():
    print(
        "Part 1 - Result of (dice_roll_count * looser's score) =",
        play(7, 10, dice_deterministic),
    )
    print(
        "Part 1 - Method 2- Result of (dice_roll_count * looser's score) =",
        play_method2(7, 10),
    )
    print(
        "Part 2 - Method 2 - Wins = ",
        compute_wins(7, 0, 10, 0),
    )


if __name__ == "__main__":
    main()
