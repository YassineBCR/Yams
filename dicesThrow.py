import random

def initialiser_des():

    des = [0, 0, 0, 0, 0] 
    des = [0, 0, 0, 0, 0]
    return des

def lancer_des(des):

    resultats = []
    for i in range(len(des)):
        resultat = random.randint(1, 6)
        resultats.append((i + 1, resultat)) 
        resultats.append((i + 1, resultat))
        print(f"Dé {i + 1}, {resultat}")

    return resultats

mes_des = initialiser_des()
print("Valeurs initiales des dés :", mes_des)

print("\nLancer des dés :")
resultats_lancer = lancer_des(mes_des)
print(resultats_lancer)


def relancer_des(resultats):

    des_relances = set()
    relance = True

    while relance:
        try:
            relance = input("Voulez-vous relancer des dés ? (Oui/Non): ").lower().startswith('o')
            if relance:
                nb_relances = int(input("Combien de dés voulez-vous relancer ? "))
                if 0 <= nb_relances <= len(resultats):
                    for _ in range(nb_relances):
                        num_de = int(input(f"Quel dé voulez-vous relancer ? (1-{len(resultats)}): "))
                        if 1 <= num_de <= len(resultats):
                            resultat = random.randint(1, 6)
                            print(f"Dé {num_de} relancé, nouveau résultat : {resultat}")
                            resultats[num_de - 1] = (num_de, resultat)
                        else:
                            print("Numéro de dé invalide.")
                else:
                    print(f"Nombre de dés à relancer invalide. Maximum autorisé : {len(resultats)}")
            else:
            if not des_relances:
                relance = input("Voulez-vous relancer des dés ? (Oui/Non): ").lower().startswith('o')
                if not relance:
                    print("Fin des relances.")
                    break

            nb_relances = int(input(f"Combien de dés voulez-vous relancer ? (1-{len(resultats)}) "))
            if 0 < nb_relances <= len(resultats):
                for _ in range(nb_relances):
                    num_de = int(input(f"Quel dé voulez-vous relancer ? (1-{len(resultats)}): "))
                    if 1 <= num_de <= len(resultats) and num_de not in des_relances:
                        resultat = random.randint(1, 6)
                        print(f"Dé {num_de} relancé, nouveau résultat : {resultat}")
                        resultats[num_de - 1] = (num_de, resultat)
                        des_relances.add(num_de)
                    else:
                        print("Numéro de dé invalide ou déjà relancé.")
            elif nb_relances == 0:
                print("Fin des relances.")
                break
            else:
                print(f"Nombre de dés à relancer invalide. Maximum autorisé : {len(resultats)}")
        except ValueError:
            print("Veuillez entrer un nombre entier.")

    return resultats

resultats_lancer = [(1, 4), (2, 2), (3, 5), (4, 3), (5, 6)]
print("Résultats des dés initiaux :", resultats_lancer)
mes_des = initialiser_des()
print("Valeurs initiales des dés :", mes_des)

print("\nPremier lancer des dés :")
resultats_lancer = lancer_des(mes_des)
print(resultats_lancer)

resultats_relances = relancer_des(resultats_lancer)
print("\nRelancer des dés :")
resultats_relances = relancer_des(resultats_lancer.copy())
print("Résultats après les relances :", resultats_relances)
#derniere modif 18.01.24 16:46 by yassine