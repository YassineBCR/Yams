from typing import Union
from functions import brelan, carre, full, petiteSuite

def test_brelan(dicesFigure: list):
    try :
        assert len(dicesFigure) == 3
        assert (dicesFigure[0][1] == dicesFigure[1][1]) and (dicesFigure[0][1] == dicesFigure[2][1])
        assert brelan(dicesFigure) >= 3 and brelan(dicesFigure) <= 18
        return brelan(dicesFigure)
    
    except AssertionError:
         print("Brelan invalide !")

def test_carre(dicesFigure: list):
    try :
        assert len(dicesFigure) == 4
        assert (dicesFigure[0][1] == dicesFigure[1][1]) and (dicesFigure[0][1] == dicesFigure[2][1]) and (dicesFigure[0][1] == dicesFigure[3][1])
        assert carre(dicesFigure) >= 4 and carre(dicesFigure) <= 24
        return carre(dicesFigure)
    
    except AssertionError:
         print("Carré invalide !")

def test_full(dicesFigure: list):
    try :
        assert len(dicesFigure) == 5
        assert (dicesFigure[0][1] == dicesFigure[1][1]) and (dicesFigure[0][1] == dicesFigure[2][1]) and (dicesFigure[3][1] != dicesFigure[0][1]) and (dicesFigure[0][1] != dicesFigure[4][1])
        assert full(dicesFigure) == 25
        return full(dicesFigure)
    
    except AssertionError:
         print("Full invalide !")

def test_petiteSuite(dicesFigure: list):
    sum = 0
    for d in dicesFigure :
        sum += dicesFigure[d][1]
        return sum
    
    try :
        assert len(dicesFigure) == 4
        assert 
        assert petiteSuite(dicesFigure) == 30
        return petiteSuite(dicesFigure)
    
    except AssertionError:
         print("Full invalide !")