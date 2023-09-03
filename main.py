import sys
import json
import time

liste = "liste.json"

menu = """Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
? Votre choix : """

choix = ["1", "2", "3", "4", "5"]

with open(liste, "r") as f:
        liste = json.load(f)

while True:
    choix_user = ""
    while choix_user not in choix:
        choix_user = input(menu)
        if choix_user not in choix:
            print("Veuillez choisir une option valide !")
            time.sleep(3)

    if choix_user == "1":
        item = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        liste.append(item)
        print(f"L'élément {item} a bien été ajouté à la liste.")
        time.sleep(2)
    elif choix_user == "2":
        item = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        if item in liste:
            liste.remove(item)
            print(f"L'élément {item} a bien été supprimé de la liste.")
            time.sleep(2)
        else:
            print(f"L'élément {item} n'est pas dans la liste.")
            time.sleep(2)
    elif choix_user == "3":
        if liste:
            print("Voici le contenu de votre liste :")
            for i, item in enumerate(liste, 1):
                print(f"{i}. {item}")
                time.sleep(2)
                
        else:
            print("Votre liste ne contient aucun élément.")
            time.sleep(2)
    elif choix_user == "4":
        liste.clear()
        print("La liste a été vidée de son contenu.")
        time.sleep(2)
    elif choix_user == "5":
        with open(liste, "w") as f:
            json.dump(liste, f, indent=4)
        print("À bientôt !")
        sys.exit()

    print("-" * 50)