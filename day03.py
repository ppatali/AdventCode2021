# https://adventofcode.com/2021/day/3

from typing import List, Tuple


def BinaryToDecimal(bits: List) -> int:
    num = 0
    for i in range(len(bits)):
        num = (num << 1) + bits[i]

    return num


def GammaCounter(readings: List, totalBits: int) -> List:

    bitCounters = [0 for i in range(totalBits)]

    for reading in readings:
        reading = reading.strip()  # Remove any newline chars
        for i in range(len(reading)):
            bitCounters[i] += 1 if int(reading[i]) == 1 else -1

    return [1 if c >= 0 else 0 for c in bitCounters]


def ComputePowerConsumption(readings: List, totalBits: int) -> Tuple[int, int, int]:

    gammaBits = GammaCounter(readings, totalBits)
    epsilonBits = [1 if c == 0 else 0 for c in gammaBits]

    gammaVal = BinaryToDecimal(gammaBits)
    epsilonValue = BinaryToDecimal(epsilonBits)
    return gammaVal, epsilonValue, gammaVal * epsilonValue


def LifeSuportRating(readings: List, totalBits: int) -> Tuple[int, int, int]:

    oxygenRatingList = co2RatingList = readings

    for i in range(totalBits):

        if len(oxygenRatingList) > 1:
            oxygenGammaBits = GammaCounter(oxygenRatingList, totalBits)
            oxygenRatingList = [
                reading
                for reading in oxygenRatingList
                if int(reading[i]) == oxygenGammaBits[i]
            ]

        if len(co2RatingList) > 1:
            co2GammaBits = GammaCounter(co2RatingList, totalBits)
            co2RatingList = [
                reading
                for reading in co2RatingList
                if int(reading[i]) != co2GammaBits[i]
            ]

    oxygenRating = BinaryToDecimal([int(c) for c in oxygenRatingList[0] if c.isdigit()])
    co2Rating = BinaryToDecimal([int(c) for c in co2RatingList[0] if c.isdigit()])

    return oxygenRating, co2Rating, oxygenRating * co2Rating


def main():
    with open("day03.input.txt", "rt") as inputFile:

        readings = inputFile.readlines()
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
