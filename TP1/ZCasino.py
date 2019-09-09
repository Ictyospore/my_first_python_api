#!/etc/python3.6
# -*-coding:UTF-8 -*

import random, math



# Entree utilisateur
i = 0
credit = input("De combien de crédits disposez-vous ? ")
while (i == 0):
    mise = input("Misez une somme : ")
    reste = credit
    credit = credit - mise
    if(credit < 0):
        print("Vous n'avez pas assez de crédits")
        mise = reste 
        print "Votre mise est votre reste - allin", mise

    # Entree module random
    result = random.randrange(50)
    print("La roue tourne ...")
    print("Le résultat est : ")
    print(result)

    # Regles du jeu
    if(mise == result):
        credit = credit + mise * 3
    elif((mise%2 == 0 and result%2 == 0) or (mise%2 != 0 and result%2 != 0)):
        credit = credit + mise / 2
    #else:
    #    continue

    # Stats fin de tour
    print("Fin de tour")
    print 'Crédits : ', math.ceil(credit)
    if(credit > 0):
        restart = raw_input("Voulez-vous rejouer ? 'Y'/'N' \n")
        if(restart == 'Y' or restart == 'y'):
            i = 0
        elif(restart == 'N' or restart == 'n'):
            i = 1
        else:
            break
    else:
        i = 1
        print("Vous avez épuisé vos crédits")
        print("Fin de la partie ...")
