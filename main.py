# on va demander à l'utilisateur de faire un choix entre voir la liste de courses, supprimer un élément et ajouter un élément ainsi que vider la liste ou la fermer
# on va vérifier si il a choisi 1 et s'il a choisi 1, on va print la liste de courses
# on va vérifier s'il a choisi 2 et si il a choisi 2, on va demander quel élément ajouter
# on va vérifier s'il a choisi 3 et si il a choisi 3, on va demander quel élément supprimer
# on va vérifier s'il a choisi 4 et si il a choisi 4, on va vider la liste avec .clear
# on va vérifier s'il a choisi 5 et si il a choisi 5, on va dire au revoir et on va break
# si aucune des conditions respectés, on demande de rechoisir
import time
import json


while True:
    choix = int(input("Bienvenue dans votre liste de course. Merci de choisir parmi les 5 options suivantes laquelle voulez-vous exécuter :\n 1 : Afficher la liste de course\n 2 : Ajouter un élément dans la liste de course\n 3 : supprimer un élément dans la liste de course\n 4 : Vider les éléments de la liste de courses\n 5 : Quitter le programme\n Votre choix : "))
    if choix < 1 or choix > 5:
        print("Veuillez choisir un nombre valide !")
        time.sleep(3)
    else:
        if choix == 1:
            with open("liste.json", "r") as f:
                donnees = json.load(f)
                print(f"Actuellement, dans la liste de courses, vous avez : {donnees}")
                time.sleep(5)
        elif choix == 2:
            with open("liste.json", "a") as f:
                ajouter = input("Quel élément souhaitez-vous ajouter : ")  
                json.dump(ajouter, f)
                f.write(",\n")
                print(f"L'élément {ajouter} a bien été ajouté à la liste de course")
                time.sleep(3)
