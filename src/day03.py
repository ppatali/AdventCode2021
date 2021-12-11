# https://adventofcode.com/2021/day/3

from typing import List, Tuple


def BinaryToDecimal(bits: List) -> int:
    num = 0
    for i in range(len(bits)):
        num = (num << 1) + bits[i]
    return num


# Count the number of 1s and 0s in the same bit position of each item in the list
# Gamma bit for that position is either
#   1 if 1 occurs more number of times or
#   0 if 0 occurs more number of times
# If both occurs equal number of times, then gamma bit is 1
def GammaCounter(readings: List, totalBits: int) -> List:

    bitCounters = [0 for i in range(totalBits)]

    for reading in readings:
        reading = reading.strip()
        for i in range(len(reading)):
            bitCounters[i] += (
                1 if int(reading[i]) == 1 else -1
            )  # step up (if 1) and step down (if 0) counter

    return [
        1 if c >= 0 else 0 for c in bitCounters
    ]  # Based on count at each pos, convert to 0 or 1 flag


def ComputePowerConsumption(readings: List, totalBits: int) -> Tuple[int, int, int]:

    gammaBits = GammaCounter(readings, totalBits)
    epsilonBits = [1 if c == 0 else 0 for c in gammaBits]  # Just inverse of gamma bits

    gammaVal = BinaryToDecimal(gammaBits)
    epsilonValue = BinaryToDecimal(epsilonBits)
    return gammaVal, epsilonValue, gammaVal * epsilonValue


def FilterOnBitCriteria(
    ratingList: List, totalBits: int, bitPos: int, inverseCompare: bool
) -> List:
    # Although not necessary, we are computing gamma counter for all bit positions
    gammaBits = GammaCounter(ratingList, totalBits)
    return [
        # pick only items for which bit at bitPos matches corresponding bit in Gamma counter
        reading
        for reading in ratingList
        if (
            not inverseCompare and int(reading[bitPos]) == gammaBits[bitPos]
        )  # For oxygen rating
        or (
            inverseCompare and int(reading[bitPos]) != gammaBits[bitPos]
        )  # For co2 rating
    ]


def LifeSuportRating(readings: List, totalBits: int) -> Tuple[int, int, int]:

    oxygenRatingList = co2RatingList = readings

    for i in range(totalBits):
        if len(oxygenRatingList) > 1:
            oxygenRatingList = FilterOnBitCriteria(
                oxygenRatingList, totalBits, i, False
            )
        if len(co2RatingList) > 1:
            co2RatingList = FilterOnBitCriteria(co2RatingList, totalBits, i, True)

    oxygenRating = BinaryToDecimal([int(c) for c in oxygenRatingList[0]])
    co2Rating = BinaryToDecimal([int(c) for c in co2RatingList[0]])

    return oxygenRating, co2Rating, oxygenRating * co2Rating


def main():
    with open("day03.input.txt", "rt") as inputFile:

        # Read all liens and remove any newline chars
        readings = [reading.strip() for reading in inputFile.readlines()]

        gammaVal, epsilonValue, power = ComputePowerConsumption(readings, 12)
        print(f"gammaCounter = {gammaVal}")
        print(f"epsilonCounter = {epsilonValue}")
        print(f"power = {power}")

        oxygenRating, co2Rating, lifeSupportRating = LifeSuportRating(readings, 12)
        print(f"oxygenRating = {oxygenRating}")
        print(f"co2Rating = {co2Rating}")
        print(f"lifeSupportRating = {lifeSupportRating}")


if __name__ == "__main__":
    main()
