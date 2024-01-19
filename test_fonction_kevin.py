from typing import Union
from fonctions_score import *

def test_brelan(dicesFigure: list):
    try :
        assert len(dicesFigure) == 3
        assert (dicesFigure[0][1] == dicesFigure[1][1]) and (dicesFigure[0][1] == dicesFigure[2][1])
        assert brelan(dicesFigure) >= 3 and brelan(dicesFigure) <= 18
        return brelan(dicesFigure)
    
    except AssertionError:
         print("Brelan invalide !")

# def test_carre(dicesFigure: list):
#     try :
#         assert len(dicesFigure) == 4
#         assert (dicesFigure[0][1] == dicesFigure[1][1]) and (dicesFigure[0][1] == dicesFigure[2][1]) and (dicesFigure[0][1] == dicesFigure[3][1])
#         assert carre(dicesFigure) >= 4 and carre(dicesFigure) <= 24
#         return carre(dicesFigure)
    
#     except AssertionError:
#          print("Carré invalide !")


#############  test_carre
def test_carre_et_brelan():
    try :
        result = score_full_carre_brelan([5, 5, 5, 5,  2])
        assert result == 5*4
    except AssertionError:
         print(f"AssertionError !! result {result} != 20")

    try :
        result = score_full_carre_brelan([6, 6, 4, 6,  6])
        assert result == 6*4
    except AssertionError:
         print(f"AssertionError !! result {result} != 24")
    try :
        result = score_full_carre_brelan([6, 6, 4, 1,  6])
        assert result == 6*3
    except AssertionError:
         print(f"AssertionError !! result {result} != 18")

test_carre_et_brelan()

# def test_full(dicesFigure: list):
#     try :
#         assert len(dicesFigure) == 5
#         assert (dicesFigure[0][1] == dicesFigure[1][1]) and (dicesFigure[0][1] == dicesFigure[2][1]) and (dicesFigure[3][1] != dicesFigure[0][1]) and (dicesFigure[0][1] != dicesFigure[4][1])
#         assert full(dicesFigure) == 25
#         return full(dicesFigure)
    
#     except AssertionError:
#          print("Full invalide !")

#############  test_full
def test_full():
    try :
        result = score_full_carre_brelan([5, 5, 5, 2,  2])
        assert result == 25
    except AssertionError:
         print(f"AssertionError !! result {result} != 25")

    try :
        result = score_full_carre_brelan([6, 4, 4, 6,  6])
        assert result == 25
    except AssertionError:
         print(f"AssertionError !! result {result} != 25")

    try :
        result = score_full_carre_brelan([6, 4, 4, 5,  6])
        assert result == 0
    except AssertionError:
         print(f"AssertionError !! result {result} != 0")

test_full()

#############   test ps
         
def test_petiteSuite():

    # test_petiteSuite_ok_entre_1_4
    try :
        result = score_petite_suite([1, 4, 3, 6, 2])
        # assert len(dicesFigure) == 4
        assert result == 30
        # return petiteSuite(dicesFigure)
    except AssertionError:
         print(f"AssertionError test_petiteSuite_ok_entre_1_4 !! result {result} != 30")
    
    #test_petiteSuite_ok_entre_2_5
    try :
        result = score_petite_suite([4, 4, 3, 5, 2])
        # assert len(dicesFigure) == 4
        assert result == 30
        # return petiteSuite(dicesFigure)
    except AssertionError:
         print(f"AssertionError test_petiteSuite_ok_entre_2_5 !! result {result} != 30")

    #test_petiteSuite_ok_entre_3_6
    try :
        result = score_petite_suite([4, 4, 3, 5, 6])
        # assert len(dicesFigure) == 4
        assert result == 30
        # return petiteSuite(dicesFigure)
    except AssertionError:
         print(f"AssertionError score_petite_suite !! result {result} != 30")

    #test_petiteSuite_pas de suite 
    try :
        result = score_petite_suite([4, 4, 3, 5, 1])
        # assert len(dicesFigure) == 4
        assert result == 0
        # return petiteSuite(dicesFigure)
    except AssertionError:
         print(f"AssertionError score_petite_suite !! result {result} != 0")

test_petiteSuite()

#############   test gs 1
def test_grande_suite_ok_1_a_5():
    dices = [1, 4, 3, 5,  2]
    result = score_grand_suite(dices)
    try :
        assert result == 40
    except AssertionError:
         print(f"AssertionError !! result {result} != 40")

test_grande_suite_ok_1_a_5()

def test_grande_suite_ok_2_a_6():
    dices = [6, 4, 3, 5, 2]
    result = score_grand_suite(dices)
    try :
        assert result == 40
    except AssertionError:
         print(f"AssertionError !! result {result} != 40")

test_grande_suite_ok_2_a_6()

def test_grande_suite_not_ok():
    dices = [6, 4, 3, 5, 6]
    result = score_grand_suite(dices)
    try :
        assert result == 0
    except AssertionError:
         print(f"AssertionError !! result {result} != 0")

test_grande_suite_not_ok()

def test_chance():
    dices = [2, 3, 3, 4, 4]
    result = score_chance(dices)
    try :
        assert result == 16
    except AssertionError:
         print(f"AssertionError !! result {result} != 16")

test_chance()

