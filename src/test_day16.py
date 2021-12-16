from day16 import *

def test_HexToBinary():
    assert "110100101111111000101000" == "".join(HexToBinary("D2FE28"))
    assert "00111000000000000110111101000101001010010001001000000000" == "".join(HexToBinary("38006F45291200"))
    assert "11101110000000001101010000001100100000100011000001100000" == "".join(HexToBinary("EE00D40C823060"))
    
    
def test_ReadVersion():
    assert (6, 3) == ReadVersion(HexToBinary("D2FE28"), 0)
    assert (1, 3) == ReadVersion(HexToBinary("38006F45291200"), 0)
    assert (7, 3) == ReadVersion(HexToBinary("EE00D40C823060"), 0)

def test_ReadTypeID():
    assert (4, 6) == ReadTypeID(HexToBinary("D2FE28"), 3)
    assert (6, 6) == ReadTypeID(HexToBinary("38006F45291200"), 3)
    assert (3, 6) == ReadTypeID(HexToBinary("EE00D40C823060"), 3)

def test_ReadLiteral():
    assert (2021, 21) == ReadLiteral(HexToBinary("D2FE28"), 6)
    assert (10, 11) == ReadLiteral([c for c in "11010001010"], 6)
    assert (20, 16) == ReadLiteral([c for c in "01010010001001000000000"], 6)

def test_ReadOperatorLengthTypeID():
    assert (0, 27, 22) == ReadOperatorLengthTypeID(HexToBinary("38006F45291200"), 6)
    assert (1, 3, 18) == ReadOperatorLengthTypeID(HexToBinary("EE00D40C823060"), 6)

def test_Part1_Sample():
    assert 16 == SumVersions(HexToBinary("8A004A801A8002F478"), 0)[0]
    assert 12 == SumVersions(HexToBinary("620080001611562C8802118E34"), 0)[0]
    assert 23 == SumVersions(HexToBinary("C0015000016115A2E0802F182340"), 0)[0]
    assert 31 == SumVersions(HexToBinary("A0016C880162017C3686B18A3D4780"), 0)[0]

def test_Part1Result():
    with open("src/day16.input.txt", "rt") as inputFile:
        lines = [line.strip() for line in inputFile.readlines()]
        sumVersion, index = SumVersions(HexToBinary(lines[0]), 0)
        assert sumVersion == 908

def test_Part2_Sample():
    assert 3 == FindValue(HexToBinary("C200B40A82"), 0)[0]
    assert 54 == FindValue(HexToBinary("04005AC33890"), 0)[0]
    assert 7 == FindValue(HexToBinary("880086C3E88112"), 0)[0]
    assert 9 == FindValue(HexToBinary("CE00C43D881120"), 0)[0]
    assert 1 == FindValue(HexToBinary("D8005AC2A8F0"), 0)[0]
    assert 0 == FindValue(HexToBinary("F600BC2D8F"), 0)[0]
    assert 0 == FindValue(HexToBinary("9C005AC2F8F0"), 0)[0]
    assert 1 == FindValue(HexToBinary("9C0141080250320F1802104A08"), 0)[0]

def test_Part1Result():
    with open("src/day16.input.txt", "rt") as inputFile:
        lines = [line.strip() for line in inputFile.readlines()]
        value, index = FindValue(HexToBinary(lines[0]), 0)
        assert value == 10626195124371