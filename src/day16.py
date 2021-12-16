# https://adventofcode.com/2021/day/15

from typing import List, Tuple, Dict, Set
import math

HEX_TO_BINARY = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def HexToBinary(hex: str) -> str:
    # using nested list comprehension for flattening
    return [c for h in hex for c in HEX_TO_BINARY[h]]


def ReadInt(data: str, start: int, len: int) -> int:
    return int("".join(data[start : start + len]), 2)


def ReadVersion(data: str, start: int) -> Tuple[int, int]:
    return (ReadInt(data, start, 3), start + 3)


def ReadTypeID(data: str, start: int) -> Tuple[int, int]:
    return (ReadInt(data, start, 3), start + 3)


def ReadLiteral(data: str, start: int) -> Tuple[int, int]:
    literal = []
    i = start
    lastGroup = False
    while not lastGroup:
        lastGroup = data[i] == "0"
        literal.extend(data[i + 1 : i + 5])
        i += 5
    return (ReadInt(literal, 0, len(literal)), i)


def ReadOperatorLengthTypeID(data: str, start: int) -> Tuple[int, int, int]:
    lengthTypeID = int(data[start])
    datalen = 15 if lengthTypeID == 0 else 11
    return (lengthTypeID, ReadInt(data, start + 1, datalen), start + 1 + datalen)


def SumVersions(data: str, index: int) -> Tuple[int, int]:
    version, i = ReadVersion(data, index)
    typeid, i = ReadTypeID(data, i)
    total = version
    if typeid == 4:
        _, i = ReadLiteral(data, i)
    else:
        lengthTypeID, subPacketInfo, i = ReadOperatorLengthTypeID(data, i)
        if lengthTypeID == 0:  # Mode : total length in bits of the sub-packets
            ilimit = i + subPacketInfo
            while i < ilimit:
                sum, i = SumVersions(data, i)
                total += sum
        else:  # Mode - number of sub-packets
            for p in range(subPacketInfo):
                sum, i = SumVersions(data, i)
                total += sum

    return total, i


def FindValue(data: str, index: int) -> Tuple[int, int]:
    version, i = ReadVersion(data, index)
    typeid, i = ReadTypeID(data, i)

    if typeid == 4:
        return ReadLiteral(data, i)
    else:
        values = []
        lengthTypeID, subPacketInfo, i = ReadOperatorLengthTypeID(data, i)
        if lengthTypeID == 0:  # Mode : total length in bits of the sub-packets
            ilimit = i + subPacketInfo
            while i < ilimit:
                value, i = FindValue(data, i)
                values.append(value)
        else:  # Mode - number of sub-packets
            for p in range(subPacketInfo):
                value, i = FindValue(data, i)
                values.append(value)

        if typeid == 0:
            value = sum(values)
        elif typeid == 1:
            value = math.prod(values)
        elif typeid == 2:
            value = min(values)
        elif typeid == 3:
            value = max(values)
        elif typeid == 5:
            value = values[0] > values[1]
        elif typeid == 6:
            value = values[0] < values[1]
        elif typeid == 7:
            value = values[0] == values[1]

        return value, i


def main():
    with open("day16.input.txt", "rt") as inputFile:
        lines = [line.strip() for line in inputFile.readlines()]
        sumVersion, index = SumVersions(HexToBinary(lines[0]), 0)
        print(f"Part 1 - Sum of all versions = {sumVersion}")

        value, index = FindValue(HexToBinary(lines[0]), 0)
        print(f"Part 2 - Value of expression = {value}")


if __name__ == "__main__":
    main()
