import random

def choisir_mot():
    mots = ["pendu", "anaconda", "maison", "voyage", "jeu", "quinoa","television","molengeek","soleil","cocotier","palmier"]
    return random.choice(mots)

def afficher_mot_cache(mot, lettres_trouvees):
    mot_cache = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_cache += lettre
        else:
            mot_cache += "_"
    return mot_cache


def est_lettre_valide(lettre):
    return len(lettre) == 1

mot_a_deviner = choisir_mot()
lettres_trouvees = []
essais_restants = 9

print("Bienvenue au jeu du pendu!")
print("Le mot à deviner a", len(mot_a_deviner), "lettres.")

while essais_restants > 0:
    lettre = input("Entrez une lettre : ")

   
    if not est_lettre_valide(lettre):
        print("Une lettre à la fois s'il vous plait.")
        continue

    

    if lettre in lettres_trouvees:
        print("Cette lettre est la bonne. Continuez, trouvez en d'autres.")
    elif lettre in mot_a_deviner:
        print("Bien joué !")
        lettres_trouvees.append(lettre)
    else:
        print("La lettre n'est pas dans le mot.")
        essais_restants -= 1

    mot_cache = afficher_mot_cache(mot_a_deviner, lettres_trouvees)
    print(mot_cache)
    print("Il vous reste {} chances sur 9".format(essais_restants))

    if "_" not in mot_cache:
        print("Félicitations ! Vous avez trouvé le mot :", mot_a_deviner)
        break

if essais_restants == 0:
    print("Il n'y a plus d'essais. Le mot à trouver était :", mot_a_deviner)
