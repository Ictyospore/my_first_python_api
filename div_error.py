#!/etc/python3.6
# -*-coding:UTF-8 -*

numerateur = input("Entrez un numerateur : ")
denominateur = input("Entrez un denominateur : ")

try:
        resultat = numerateur / denominateur
except NameError:
        print("La variable numerateur ou denominateur n'a pas été définie.")
except TypeError:
        print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
except ZeroDivisionError:
        print("La variable denominateur est égale à 0.")
else:
        print("Le résultat obtenu est", resultat)
finally:
        print("Je m'exécute quoi qu'il arrive")
