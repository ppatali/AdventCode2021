# https://adventofcode.com/2021/day/8

from typing import List, Tuple, Dict, Set


def IncrAndFlash(octpuses, y, x, flashes) -> bool:
    octpuses[y][x] += 1
    if octpuses[y][x] == 10:
        flashes.append((y, x))
        return True
    else:
        return False


def MoveAStep(octopuses: List[List[int]]) -> int:

    flashes = []
    for y in range(len(octopuses)):
        for x in range(len(octopuses[y])):
            IncrAndFlash(octopuses, y, x, flashes)

    i = 0
    while i < len(flashes):
        y, x = flashes[i]

        # adjacent
        if x - 1 >= 0 and octopuses[y][x - 1] != 10:  # left
            IncrAndFlash(octopuses, y, x - 1, flashes)
        
        if x + 1 < len(octopuses[y]) and octopuses[y][x + 1] != 10:  # right
            IncrAndFlash(octopuses, y, x + 1, flashes)
        
        if y - 1 >= 0 and octopuses[y - 1][x] != 10:  # top
            IncrAndFlash(octopuses, y - 1, x, flashes)
                
        if y + 1 < len(octopuses) and octopuses[y + 1][x] != 10: # botton
            IncrAndFlash(octopuses, y + 1, x, flashes)

        # diagonal
        if (# left, top
            x - 1 >= 0 
            and y - 1 >= 0 
            and octopuses[y - 1][x - 1] != 10
        ):  
            IncrAndFlash(octopuses, y - 1, x - 1, flashes)
        
        if ( # right, top
            x + 1 < len(octopuses[y]) 
            and y - 1 >= 0 
            and octopuses[y - 1][x + 1] != 10
        ):  
            IncrAndFlash(octopuses, y - 1, x + 1, flashes)
        
        if ( # left, botton
            x - 1 >= 0 
            and y + 1 < len(octopuses) 
            and octopuses[y + 1][x - 1] != 10
        ):  
            IncrAndFlash(octopuses, y + 1, x - 1, flashes)
        
        if ( # righ, botton
            x + 1 < len(octopuses[y])
            and y + 1 < len(octopuses)
            and octopuses[y + 1][x + 1] != 10
        ):
            IncrAndFlash(octopuses, y + 1, x + 1, flashes)

        i += 1

    for y, x in flashes:
        octopuses[y][x] = 0

    return len(flashes)


def main():
    with open("day11.input.txt", "rt") as inputFile:
        octopuses = [[int(x) for x in y.strip()] for y in inputFile.readlines()]
        totalFlashes = 0
        for _ in range(100):
            totalFlashes += MoveAStep(octopuses)
        print(f"After 100 steps, total flashes = {totalFlashes}")


if __name__ == "__main__":
    main()
