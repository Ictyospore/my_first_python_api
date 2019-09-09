#!/etc/python3.6
# -*-coding:UTF-8 -*
# Programme testant si une année, saisie par l'utilisateur, est bissextile ou non

annee = input("Saisissez une année : ") # On attend que l'utilisateur fournisse l'annee qu'il desire tester
try:
    annee = int(annee) # Risque d'erreur si l'utilisateur n'a pas saisi un nombre
    #assert annee > 0
    if annee <= 0:
        raise ValueError("l'année saisie est négative ou nulle")
except ValueError:
    print("La valeur saisie est invalide (l'année est peut-être négative).")
#except ValueError:
#    print("Vous n'avez pas saisi un nombre")
except AssertionError:
    print("Vous n'avez pas entré une année > 0")
except type_de_l_exception as exception_retournee:
    #print("Veuillez saisir un entier")
    print("Nature de l'erreur : ", exception_retournee)

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("L'annee saisie est bissextile.")
else:
    print("L'annee saisie n'est pas bissextile.")
