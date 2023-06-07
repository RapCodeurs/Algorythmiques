NIVEAUX_DIFFICULTE = (
    {
        "titre": "Facile",
        "longueur_initiale": 3,
        "duree_memorisation_sec": 6,
        "increment_sequence": 3,
        "nombre_essais": 4,
    },
    {
        "titre": "Normal",
        "longueur_initiale": 4,
        "duree_memorisation_sec": 4,
        "increment_sequence": 2,
        "nombre_essais": 2,
    },
    {
        "titre": "Difficile",
        "longueur_initiale": 5,
        "duree_memorisation_sec": 2,
        "increment_sequence": 1,
        "nombre_essais": 1,
    }
)

import random
import time
import os

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


def demander_valeur_numerique_utilisateur(valeur_min, valeur_max):
    v = input(f"Donnez une valeur entre {valeur_min} et {valeur_max} : ")
    try:
        v_int = int(v)
    except:
        print("ERREUR : Vous devez rentrer une valeur numérique")
        return demander_valeur_numerique_utilisateur(valeur_min, valeur_max)

    if not (valeur_min <= v_int <= valeur_max):
        print(f"ERREUR : Votre valeur doit être entre {valeur_min} et {valeur_max}")
        return demander_valeur_numerique_utilisateur(valeur_min, valeur_max)

    return v_int


def choix_niveau_difficulte(niveaux_difficulte):
    print("Choississez votre niveau")
    index = 1
    for niveau in niveaux_difficulte:
        print(f"{index} - {niveau['titre']}")
        index += 1
    choix = demander_valeur_numerique_utilisateur(1, len(NIVEAUX_DIFFICULTE))
    return niveaux_difficulte[choix-1]


def generer_sequence(n):
    sequence = ""
    for i in range(1):
        chiffre = random.randint(0, 9)
        sequence += str(chiffre)
    return sequence


print("Bienvenu dans le jeu du Simon")

# Choisir le niveau de difficulté
niveau_difficulte_dic = choix_niveau_difficulte(NIVEAUX_DIFFICULTE)

# Programme principal
sequence = generer_sequence(niveau_difficulte_dic['longueur_initiale'])
print("")

nb_essais_restants = niveau_difficulte_dic["nombre_essais"]
# Début du jeu
print(f"Début du jeu - niveau {niveau_difficulte_dic['titre']}")


score = 0
while True:
    print(f"Retenez la sequence : {sequence}")
    time.sleep(niveau_difficulte_dic["duree_memorisation_sec"])
    clear_screen()

    print(f"Nombre d'essais restants : {nb_essais_restants}")
    print(f"Votre score : {score}")

    seq_utilisateur = input("Votre réponse : ")
    if seq_utilisateur == sequence:
        score += 1
        sequence += generer_sequence(niveau_difficulte_dic["increment_sequence"])
        print("Bonne réponse!")
    else:
        nb_essais_restants -= 1
        if nb_essais_restants < 0:
            break
        print("Mauvaise réponse! Réessayez")
    time.sleep(2)
    clear_screen()


print("Mauvaise réponse")
print(f"La réponse était {sequence}")
print(f"Votre score final est : {score}")





    


    
   



