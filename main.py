"""
Celine Mattar 403
26 Octobre 2022
Jeu de devinette
"""
import random
grand_chiffre, petit_chiffre = 0, 10


def chiffre():

    global grand_chiffre, petit_chiffre
    grand_chiffre = int(input("veuillez definir le plus grand chiffre:"))
    petit_chiffre = int(input("veuillez definir le plus petit chiffre:"))
    print(grand_chiffre, petit_chiffre)


boucle_jeu = True
while boucle_jeu:
    chiffre()

    nombre_defini = random.randint(petit_chiffre, grand_chiffre)
    essaie = 1
    reponse = int(input("devine le chiffre:"))
    while essaie != nombre_defini:
        if reponse > nombre_defini:
            print("le chiffre est plus plus grand")
            essaie = + 1
            reponse = int(input("essaie une ature fois"))
        else:
            print("le chiffre est plus petit")
            essaie = essaie + 1
            reponse = int(input("essaie une autre fois"))

    print("Yay vous avez devinez le bon chiffre !")
    print("nombre d'essaie" + str(essaie))
    rejouer = input("voulez vous rejouer: *veuillez repondre par oui ou non*")

    if rejouer == "non":
        boucle_jeu = False






