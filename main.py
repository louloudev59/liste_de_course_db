import time
import json

while True:
    choix = int(input("Bienvenue dans votre liste de course. Merci de choisir parmi les 5 options suivantes laquelle voulez-vous exécuter :\n 1 : Afficher la liste de course\n 2 : Ajouter un élément dans la liste de course\n 3 : Supprimer un élément dans la liste de course\n 4 : Vider les éléments de la liste de courses\n 5 : Quitter le programme\n Votre choix : "))

    if choix < 1 or choix > 5:
        print("Veuillez choisir un nombre valide !")
        time.sleep(3)
    else:
        if choix == 1:
            try:
                with open("liste.json", "r") as f:
                    donnees = json.load(f)
                    if donnees:
                        print(f"Actuellement, dans la liste de courses, vous avez : {donnees}")
                    else:
                        print("La liste de courses est vide.")
                time.sleep(5)
            except FileNotFoundError:
                print("La liste de courses est vide.")
                time.sleep(5)
        elif choix == 2:
            with open("liste.json", "a") as f:
                ajouter = input("Quel élément souhaitez-vous ajouter : ")
                if ajouter.strip():  # Vérifie si l'entrée n'est pas vide
                    if not ajouter.endswith(", "):
                        ajouter += ", "
                    f.write(ajouter + "\n")
                    print(f"L'élément {ajouter.strip(', ')} a bien été ajouté à la liste de course")
                else:
                    print("L'élément ne peut pas être vide.")
                time.sleep(3)