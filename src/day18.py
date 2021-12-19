# https://adventofcode.com/2021/day/18

from typing import List, Tuple, Dict, Set
from functools import reduce

# I could not solve this using lists and recursion. As I progressed, realized that tree would be better option
# The below solution is using a tree and recursion. It is based entirely on below reddit answer and but had to make minor corrections
# https://www.reddit.com/r/adventofcode/comments/rizw2c/comment/hp4961a/?utm_source=share&utm_medium=web2x&context=3
# A possible improvement that can be done:
# - Notice how the leaf nodes are computed and used to determine first right number and first left number of exploding node
# - Another way would be to store the reference to parent node in the Node and the naviagte the tree structure to find this info
# - Some thing similar to: https://github.com/SwampThingTom/AoC2021/blob/main/Python/18-Snailfish/Snailfish.py

# Some of things learned through this exercise are:
# - Using map and reduce functools
# - Building a simple binary tree
# - If a list contains objects, then index() will do reference comparision
# - other quirks are noted inline below


class Node:
    def __init__(self, v=None, l=None, r=None) -> None:
        self.v, self.l, self.r = v, l, r

    def __str__(self) -> str:
        if self.v is not None:
            return str(self.v)
        return f"[{str(self.l)},{str(self.r)}]"

    def leafnodes(self, vs) -> List[int]:
        # Note: Looking at the next two if statement, had wriiten below if as
        # if self.v
        # But this is incorrect as value of v can be 0 and this statment will be False!
        if self.v is not None:
            vs.append(self)
        if self.l:
            self.l.leafnodes(vs)
        if self.r:
            self.r.leafnodes(vs)
        return vs

    def replace(self, oldchild, newchild):
        if self.l == oldchild:
            self.l = newchild
        else:
            self.r = newchild

    def magnitude(self):
        if self.v is not None:
            return self.v
        else:
            return 3 * self.l.magnitude() + 2 * self.r.magnitude()


def parsefish(line: str, i: int = 0, parent: Node = None):
    if line[i].isdigit():
        return Node(int(line[i])), i + 1

    fish = Node()
    fish.l, i = parsefish(line, i + 1, fish)
    fish.r, i = parsefish(line, i + 1, fish)

    return fish, i + 1


def parse(line):
    return parsefish(line)[0]


def explode(fish, leaves, level=0, parent=None):
    if fish.v is not None:
        return False

    if level == 4:
        # Note: leaves is a list of nodes/objects
        # So when index() is used, actual object references are compared not the value
        # If value was compared, then logic would be incorrect as same value can repeat
        i = leaves.index(fish.l)
        if i > 0:
            leaves[i - 1].v += fish.l.v
        # Note: 2 is used to skip exploded fish.r.v
        if i < len(leaves) - 2:
            leaves[i + 2].v += fish.r.v
        parent.replace(fish, Node(0))
        return True

    if explode(fish.l, leaves, level + 1, fish):
        return True
    return explode(fish.r, leaves, level + 1, fish)


def split(fish, parent=None):
    if fish.v is not None:
        if fish.v < 10:
            return False
        # Note: casting to int is needed otherwise you will be storing floats!
        parent.replace(
            fish, Node(l=Node(int(fish.v / 2)), r=Node(fish.v - int(fish.v / 2)))
        )
        return True
    if split(fish.l, fish):
        return True
    return split(fish.r, fish)


def add(fish1, fish2):
    fish = Node(l=fish1, r=fish2)
    while True:
        if not explode(fish, fish.leafnodes([])):
            if not split(fish):
                break
    return fish


def addall(lines):
    return reduce(add, map(parse, lines))


def maxMagOnPermutation(lines):
    return max(
        add(parse(a), parse(b)).magnitude() for a in lines for b in lines if a != b
    )
