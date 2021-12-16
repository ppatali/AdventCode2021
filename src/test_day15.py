from day15 import * 

def test_Sample1_Part1():
    test = [
        [1,1,6,3,7,5,1,7,4,2],
        [1,3,8,1,3,7,3,6,7,2],
        [2,1,3,6,5,1,1,3,2,8],
        [3,6,9,4,9,3,1,5,6,9],
        [7,4,6,3,4,1,7,1,1,1],
        [1,3,1,9,1,2,8,1,3,7],
        [1,3,5,9,9,1,2,4,2,1],
        [3,1,2,5,4,2,1,6,3,9],
        [1,2,9,3,1,3,8,5,2,1],
        [2,3,1,1,9,4,4,5,8,1],
    ]

    assert 40 == FindMinPathBruteForce(test, 0, 0, LARGE_RISK)
    assert 40 == FindMinPathDijkstra(test)

def test_Part1Result():
    with open("src/day15.input.txt", "rt") as inputFile:
        graph = [[int(n) for n in line.strip()] for line in inputFile.readlines()]
        assert 698 == FindMinPathDijkstra(graph)

def test_Sample1_Part2():
    test = [
        [1,1,6,3,7,5,1,7,4,2],
        [1,3,8,1,3,7,3,6,7,2],
        [2,1,3,6,5,1,1,3,2,8],
        [3,6,9,4,9,3,1,5,6,9],
        [7,4,6,3,4,1,7,1,1,1],
        [1,3,1,9,1,2,8,1,3,7],
        [1,3,5,9,9,1,2,4,2,1],
        [3,1,2,5,4,2,1,6,3,9],
        [1,2,9,3,1,3,8,5,2,1],
        [2,3,1,1,9,4,4,5,8,1],
    ]

    assert 315 == FindMinPathDijkstra(ReplicateGraph(test, 5, 5))

def test_Part2Result():
    with open("src/day15.input.txt", "rt") as inputFile:
        graph = [[int(n) for n in line.strip()] for line in inputFile.readlines()]
        newGraph = ReplicateGraph(graph, 5, 5)
        assert 3022 == FindMinPathDijkstra(newGraph)
