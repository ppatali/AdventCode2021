# https://adventofcode.com/2021/day/8

from typing import List, Tuple, Dict, Set


def ReadInputLinesAsSets(
    inputLines: List[str],
) -> List[Tuple[List[Set[str]], List[Set[str]]]]:
    lines = []
    for inputLine in inputLines:
        signals, outputs = tuple(inputLine.strip().split(" | "))
        lines.append(
            ([set(s) for s in signals.split()], [set(o) for o in outputs.split()])
        )
    return lines


def Count1478(lines: List[Tuple[List[Set[str]], List[Set[str]]]]) -> int:
    count = 0
    for _, outputs in lines:
        count += len([o for o in outputs if len(o) in [2, 3, 4, 7]])
    return count


def DecodeSignals(signals: List[Set[str]]) -> List[Set[str]]:
    decodedSignals = [set() for _ in range(10)]

    # Find those number whose number of segments is unique - 1,7,4,8
    decodedSignals[1] = next(s for s in signals if len(s) == 2)  # 1
    decodedSignals[7] = next(s for s in signals if len(s) == 3)  # 7
    decodedSignals[4] = next(s for s in signals if len(s) == 4)  # 4
    decodedSignals[8] = next(s for s in signals if len(s) == 7)  # 8

    # Find those whose number of segments are of length 5 - 2,3,5

    # Merge/Union of segments of 1 and 3 results in 3
    decodedSignals[3] = next(
        s for s in signals if len(s) == 5 and decodedSignals[1] | s == s
    )  # 3

    # Merge/Union of segments of 4 and 2 results in 8
    decodedSignals[2] = next(
        s
        for s in signals
        if len(s) == 5
        and decodedSignals[4] | s == decodedSignals[8]
        and s != decodedSignals[3]
    )  # 2

    # Remaining has to be 5
    decodedSignals[5] = next(
        s
        for s in signals
        if len(s) == 5 and s not in [decodedSignals[2], decodedSignals[3]]
    )  # 5

    # Find those whose number of segments are of length 6 - 0,6,9

    # Merge/Union of segments of 1 and 3 results in 3
    decodedSignals[6] = next(
        s for s in signals if len(s) == 6 and decodedSignals[1] | s == decodedSignals[8]
    )  # 6

    # Merge/Union of segments of 4 and 2 results in 8
    decodedSignals[0] = next(
        s
        for s in signals
        if len(s) == 6
        and decodedSignals[4] | s == decodedSignals[8]
        and s != decodedSignals[6]
    )  # 0

    # Remaining has to be 9
    decodedSignals[9] = next(
        s
        for s in signals
        if len(s) == 6 and s not in [decodedSignals[0], decodedSignals[6]]
    )  # 9

    return decodedSignals


def DecodeOutputs(outputs: List[Set[str]], decodeSignals: List[Set[str]]) -> int:
    return int("".join(str(decodeSignals.index(o)) for o in outputs))


def Decode(lines: List[Tuple[List[Set[str]], List[Set[str]]]]) -> List[int]:
    decodedOutputs = []
    for signals, outputs in lines:
        decodedSignals = DecodeSignals(signals)
        decodedOutputs.append(DecodeOutputs(outputs, decodedSignals))
    return decodedOutputs


def main():
    with open("day08.input.txt", "rt") as inputFile:
        readlines = inputFile.readlines()
        lines = ReadInputLinesAsSets(readlines)
        print(f"Number of 1, 4, 7, 8 = {Count1478(lines)}")
        print(f"Sum of all output values = {sum(Decode(lines))}")


if __name__ == "__main__":
    main()
