
# les 5 dés doivent etre identiques 
def score_yams(dices: list):
    # on mémorise le premier dés
    x=dices[0]
    for r in dices:
        # print(f"x={x} r = {r}")
        # si un dè dans la boucle est différent du premier donc 0
        if r != x:
            return 0
    return 50  

def score_grand_suite(dices: list):
    dices.sort()
    #print(f"gds{dices}")
    # on parcourt le tableau sauf le dernier élément 
    # pour arreter la boucler avant le dernier élément car sinon on va sortir du tableau
    # lorsqu'on veut comparer l'élément actuel avec l'élément suivant 
    # (le dernier ne peut pas comparer avec le suivant car il n'y en a pas)
    for i in range(len(dices)-1):
        #print(f"i={dices[i]} i+1={dices[i+1]}  ")
        if (dices[i]+1) != dices[i+1]:
            return 0
    return 40

def score_petite_suite(dices: list):
    dices.sort()
    #print(f"gds{dices}")
    # on crée un compteur pour compter le nombre d'éléments qui se suivent
    count = 1
    for i in range(len(dices)-1):
        #print(f"i={dices[i]} i+1={dices[i+1]}  ")
        # si l'élément suivant est une suite de l'élément actuel
        if ((dices[i]+1) == dices[i+1]): 
            count+=1
        #si l'élément suivant est le même donc on ne fait rien
        elif ((dices[i]) == dices[i+1]):
            count
        else: 
            #remise à zéro du compteur
            count = 1
        if count == 4: 
            return 30
    #print(f"count : {count}")
    return 0

# 
def score_full_carre_brelan(dices: list):
    # print()
    # print("score_full")
    # print(f"{dices}")
    dices.sort()

    # on met un dés dans le premier numéro
    premier_numero_de_des = dices[0]
    deuxieme_numero_de_des = 0
    count1 = 0
    count2 = 0
 
    ## trouver le 2e numéro différent du premier 
    for r in dices:
        if r != premier_numero_de_des:
            deuxieme_numero_de_des = r

    # compter le nomnbre de dés identiques et mettre dans des compteurs séparés
    for r in dices:
        if r == premier_numero_de_des:
            count1+=1
        elif r == deuxieme_numero_de_des:
            count2+=1

    # print(f"dé n°1={premier_numero_de_des}x{count1}; dé n°2={deuxieme_numero_de_des}x{count2}")
            
    # bien vérifier qu'on ait 3 dés identiques d'un côté et 2 dés identiques de l'autre côté
    if count1 == 3 and count2 == 2:
        return 25
    if count1 == 2 and count2 == 3:
        return 25
    
    # pour le carre
    if count1 == 4:
        return 4* premier_numero_de_des
    if count2 == 4:
        return 4* deuxieme_numero_de_des
    
    # vérifier pour le brelan
    if count1 == 3:
        return 3* premier_numero_de_des
    if count2 == 3:
        return 3* deuxieme_numero_de_des

    return 0

def score_chance(dices: list):
    sum = 0
    for r in dices:
        sum+=r
        
    return sum

def score(resultats_relances: list):
    dices=[]
    for i in range(len(resultats_relances)):
        dices.append(resultats_relances[i][1])
    # print(dices)
    
    result = score_yams(dices) 
    if result != 0:
        return result
    result = score_grand_suite(dices)
    if result != 0:
        return result
    result = score_petite_suite(dices)
    if result != 0:
        return result
    result = score_full_carre_brelan(dices)
    if result != 0:
        return result
    result = score_chance(dices)
    if result != 0:
        return result

# print (score([(1, 6), (2, 6), (3, 6), (4, 6), (5, 6)]))
# print (score([(1, 6), (2, 5), (3, 4), (4, 3), (5, 2)]))
# print (score([(1, 6), (2, 6), (3, 6), (4, 6), (5, 2)]))