#Céline Mattar 403
#29 septembre 2022
#TP2

boucle_jeu = True
while boucle_jeu:
    import random
    chiffre_random = random.randint (1,15)
    reponse = int(input("Ecrivez un chiffre entre 1 et 15"))
    if reponse == chiffre_random:
        print("yay")
    if reponse > chiffre_random :
        print ("essaye un chiffre plus petit")
    if reponse < chiffre random :
        print ("esaye un chiffre plus grand")