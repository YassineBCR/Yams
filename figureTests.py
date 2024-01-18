from typing import Union
from function import brelan, carre, full, lilSuite, bigSuite, yams, chance, minorFigure


def test_brelan(dices: list, value: int):
    sumBrelan = 0
    otherValues = []
    brelanValue = 0

    for d in dices :
        if d == value:
            sumBrelan += d
            brelanValue = d
        elif d != value:
            otherValues.append(d)

    try :
        assert len(dices) == 5
        assert sumBrelan == value * 3
        assert brelanValue == value
        assert len(otherValues) == 2
        assert otherValues[0] != value
        assert otherValues[1] != value
        assert brelan(dices) == value * 3
        
        return brelan(dices)
    
    except AssertionError:
         print("Brelan invalide !")


def test_carre(dices: list, value: int):
    sumCarre = 0
    otherValues = []
    carreValue = 0

    for d in dices :
        if d == value:
            sumCarre += d
            carreValue = d
        elif d != value:
            otherValues.append(d)

    try :
        assert len(dices) == 5
        assert sumCarre == value * 4
        assert carreValue == value
        assert len(otherValues) == 2
        assert otherValues[0] != value
        assert otherValues[1] != value
        assert carre(dices) == value * 4
        
        return carre(dices)
    
    except AssertionError:
         print("Carré invalide !")


def test_full(dices: list, value: int):
    sumBrelan = 0
    otherValues = []
    brelan = 0

    for d in dices :
        if d == value:
            sumBrelan += d
            brelan = d
        elif d != value:
            otherValues.append(d)

    try :
        assert len(dices) == 5
        assert sumBrelan == value * 3
        assert brelan == value
        assert len(otherValues) == 2
        assert otherValues[0] != value
        assert otherValues[1] != value
        assert full(dices, value) == 25
        
        return full(dices, value)
    
    except AssertionError:
         print("Full invalide !")


def test_lilSuite(dices: list):
    sum = 0
    for i in range(5) :
        sum += dices[i]
    
    try :
        assert len(dices) == 4
        assert sum in range(11,25) and sum not in [15,20]
        assert lilSuite(dices) == 30
        
        return lilSuite(dices)
    
    except AssertionError:
         print("Petite Suite invalide !")


def test_bigSuite(dices: list):
    dices.sort()
    sum = 0
    for d in dices :
        sum += dices[d]
    
    try :
        assert len(dices) == 5
        assert sum in [15,20]
        assert bigSuite(dices) == 40
        
        return bigSuite(dices)
    
    except AssertionError:
         print("Grande Suite invalide !")


def test_yams(dices: list, value: int):
    sum = 0
    sameValue = False

    for d in dices :
        sum += d
        if d == value:
            sameValue = True
        else :
            sameValue = False
    
    try :
        assert len(dices) == 5
        assert sameValue == True
        assert sum == value * 5
        assert yams(dices, value) == 50
        
        return yams(dices, value)
    
    except AssertionError:
         print("Yams invalide !")


def test_chance(dices: list):
    sum = 0

    for d in dices :
        sum += d

    try :
        assert len(dices) == 5
        assert sum in range(5,31)
        assert chance(dices) == 30
        
        return chance(dices)
    
    except AssertionError:
         print("Chance invalide !")


def test_minorFigure(dices: list,value: int):
    dices.sort()
    sum = 0
    count = 0

    for d in dices :
        if d == value:
            sum += d
            count += 1

    try :
        assert len(dices) == 5
        assert sum == value * count
        assert minorFigure(dices, value) == value * count

        return minorFigure(dices, value)
    
    except AssertionError:
        print("Figure mineure invalide !")