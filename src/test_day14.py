from day14 import *

def test_ReadInput():
    test = [
        "NNCB",
        "",
        "CH -> B","HH -> N","CB -> H","NH -> C","HB -> C","HC -> B",
        "HN -> C","NN -> C","BH -> H","NC -> B","NB -> B","BN -> B",
        "BB -> N","BC -> B","CC -> N","CN -> C"
    ]

    expected = (
        {("N", "N") : 1, ("N", "C"): 1, ("C", "B"): 1}, 
        {
            ("C","H"): "B", ("H","H"): "N", ("C","B"): "H", ("N","H"): "C", 
            ("H","B"): "C", ("H","C"): "B", ("H","N"): "C", ("N","N"): "C", 
            ("B","H"): "H", ("N","C"): "B", ("N","B"): "B", ("B","N"): "B", 
            ("B","B"): "N", ("B","C"): "B", ("C","C"): "N", ("C","N"): "C"
        }
    ) 

    assert expected == ReadInput(test)

def test_StepThrough():
    test = [
        "NNCB",
        "",
        "CH -> B","HH -> N","CB -> H","NH -> C","HB -> C","HC -> B",
        "HN -> C","NN -> C","BH -> H","NC -> B","NB -> B","BN -> B",
        "BB -> N","BC -> B","CC -> N","CN -> C"
    ]

    template, rules = ReadInput(test)
    chain = StepThrough(template, rules)
    chain = StepThrough(chain, rules)
    chain = StepThrough(chain, rules)
    chain = StepThrough(chain, rules)

    expected = {
        ('N', 'B'): 9, ('B', 'B'): 9, ('B', 'N'): 6, 
        ('B', 'C'): 4, ('C', 'C'): 2, ('C', 'N'): 3, ('N', 'C'): 1, 
        ('C', 'B'): 5, ('B', 'H'): 3, ('H', 'C'): 3, ('H', 'H'): 1, 
        ('H', 'N'): 1, ('N', 'H'): 1
    }
    assert expected == chain

def test_Part1_Sample():
    test = [
        "NNCB",
        "",
        "CH -> B","HH -> N","CB -> H","NH -> C","HB -> C","HC -> B",
        "HN -> C","NN -> C","BH -> H","NC -> B","NB -> B","BN -> B",
        "BB -> N","BC -> B","CC -> N","CN -> C"
    ]

    template, rules = ReadInput(test)
    chain = template
    for _ in range(10): 
        chain = StepThrough(chain, rules)
    
    elemCounts = CountElements(chain, test[0][-1])
    diff = max(elemCounts.values()) - min(elemCounts.values())

    assert 1588 == diff


def test_Part1Result():
    with open("src/day14.input.txt", "rt") as inputFiles:
        lines  = [line.strip() for line in inputFiles.readlines()]

    template, rules = ReadInput(lines)
    chain = template
    for _ in range(10): 
        chain = StepThrough(chain, rules)    
    elemCounts = CountElements(chain, lines[0][-1])
    diff = max(elemCounts.values()) - min(elemCounts.values())
    
    assert 2947 == diff

def test_Part2_Sample():
    test = [
        "NNCB",
        "",
        "CH -> B","HH -> N","CB -> H","NH -> C","HB -> C","HC -> B",
        "HN -> C","NN -> C","BH -> H","NC -> B","NB -> B","BN -> B",
        "BB -> N","BC -> B","CC -> N","CN -> C"
    ]

    template, rules = ReadInput(test)
    chain = template
    for _ in range(40): 
        chain = StepThrough(chain, rules)    
    elemCounts = CountElements(chain, test[0][-1])
    diff = max(elemCounts.values()) - min(elemCounts.values())

    assert 2188189693529 == diff

def test_Part2Result():
    with open("src/day14.input.txt", "rt") as inputFiles:
        lines  = [line.strip() for line in inputFiles.readlines()]

    template, rules = ReadInput(lines)
    chain = template
    for _ in range(40): 
        chain = StepThrough(chain, rules)    
    elemCounts = CountElements(chain, lines[0][-1])
    diff = max(elemCounts.values()) - min(elemCounts.values())
    
    assert 3232426226464 == diff