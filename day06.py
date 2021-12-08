# https://adventofcode.com/2021/day/6
from typing import List, Tuple

TIMER_INIT_NEWBORN = 8
TIMER_INIT_ADULT = 6
TIMER_BIRTHING = 0


def EvolveToNextStage(population: List[int]) -> None:
    currentPopulation = len(population)
    for i in range(currentPopulation):
        if population[i] == TIMER_BIRTHING:
            population[i] = TIMER_INIT_ADULT
            population.append(TIMER_INIT_NEWBORN)
        else:
            population[i] -= 1


def EvolveForDays(population: List[int], days: int) -> int:
    for i in range(days):
        EvolveToNextStage(population)
    return len(population)


def GetGeneration(population: List[int]) -> List[int]:
    generations = [0] * (TIMER_INIT_NEWBORN + 1)
    for i in population:
        generations[i] += 1
    return generations


def EvolveGenerationsToNextStage(generations: List[int]) -> List[int]:
    nextGenerations = [0] * (TIMER_INIT_NEWBORN + 1)

    for i in range(len(generations)):
        if i == TIMER_BIRTHING:
            nextGenerations[TIMER_INIT_ADULT] += generations[i]
            nextGenerations[TIMER_INIT_NEWBORN] += generations[i]
        else:
            nextGenerations[i - 1] += generations[i]

    return nextGenerations


def EvolveGenerationsForDays(
    generations: List[int], days: int
) -> Tuple[int, List[int]]:
    for i in range(days):
        generations = EvolveGenerationsToNextStage(generations)

    return sum(generations), generations


def EvolvePopulationForDaysUsingGeneration(population: List[int], days: int) -> int:
    generations = GetGeneration(population)
    populationCount, generations = EvolveGenerationsForDays(generations, days)
    return populationCount


def main():
    with open("day06.input.txt", "rt") as inputFile:
        population = [int(i) for i in inputFile.readline().split(",")]
        print(
            f"PART 1 - Popuation after 80 days = {EvolveForDays(population.copy(), 80)}"
        )

        print(
            f"PART 2 - Popuation after 256 days using Generations method = {EvolvePopulationForDaysUsingGeneration(population.copy(), 256)}"
        )


if __name__ == "__main__":
    main()
