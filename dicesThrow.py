import random
import figureTests as ft
import fonctions_score as fs

def initialiser_des():

    des = [0, 0, 0, 0, 0] 
    des = [0, 0, 0, 0, 0]
    return des

def lancer_des(des):
    resultats = []
    for i in range(len(des)):
        resultat = random.randint(1, 6)
        resultats.append(resultat) 
        print(f"Dé {i + 1}, {resultat}")

    return resultats

def relancer_des(dices):
    whichDiceList = []

    for r in range(2):
        relance = input("\nVoulez-vous relancer des dés ? (Oui/Non): ").lower()
        if r <= 1 :
            try:
                if relance == 'oui' :
                    nb_relances = int(input("\nCombien de dés voulez-vous relancer (1-5) ?"))

                    for i in range(nb_relances):
                        if i == 0 :
                            whichDice = int(input(f"\nQuel est le premier dés que voulez-vous relancer ? (1-5): "))
                            whichDiceList.append(whichDice)
                        else :
                            whichDice = int(input(f"\nQuel est le {i+1}ème dés que voulez-vous relancer ? (1-5): "))
                            whichDiceList.append(whichDice)

                    for d in range(len(dices)):
                        if d+1 in whichDiceList:
                            resultat = random.randint(1, 6)
                            dices.pop(d)
                            dices.append(resultat) 
                    
                    print(f"\nVotre nouvelle main : {dices}")
                
                elif relance == 'non':
                    print(f"\nVotre main est toujours la même : {dices}")
                    return dices
                
            except ValueError:
                print("\nVeuillez répondre par oui pour non.")
        
        else :
            print(f"\nVous ne pouvez plus relancer les dés. Voici votre main : {dices}")
            
    return dices

figures = ["Brelan", "Carré", "Full", "Petite Suite", "Grande Suite", "Yams", "Chance"]

def choix_figure(dices):
    figure = input("\nQuel figure choisissez-vous ? (Brelan, Carré, Full, Petite Suite, Grande Suite, Yams, Chance)").lower()

    match figure:
        case "brelan":
            return print(fs.score_full_carre_brelan(dices))
        case "carré":
            return print(fs.score_full_carre_brelan(dices))
        case "full":
            return print(fs.score_full_carre_brelan(dices))
        case "petite suite":
            return print(fs.score_petite_suite(dices))
        case "grande suite":
            return print(fs.score_grand_suite(dices))
        case "yams":
            return print(fs.score_yams(dices))
        case "chance" :
            return print(fs.score_chance(dices))
        case _:
            return "Figure incorrecte"

myDices = initialiser_des()
print("Valeurs initiales des dés :", myDices)

print("\nLancement des dés...")
print("...")

myDices = lancer_des(myDices)
print(f"\nVotre main : {myDices}")

print("\n...")
myDices = relancer_des(myDices)

print("\n...")
my_score = choix_figure(myDices)