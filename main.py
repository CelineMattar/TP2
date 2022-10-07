#Céline Mattar 403
#29 septembre 2022
#TP2

boucle_jeu = True
while boucle_jeu:
    import random
    chiffre_random = random.randint (1,15)
    print("Dans ce jeu vous devriez deviner un chiffre entre 1 et 15. Si vous avez la mauvaises reponse, vous auriez un indice.")
    reponse = int(input("Ecrivez un chiffre entre 1 et 15"))
    if reponse == chiffre_random:
        print("yay")
    if reponse > chiffre_random :
        print ("essaye un chiffre plus petit")
    if reponse < chiffre_random :
        print ("esaye un chiffre plus grand")