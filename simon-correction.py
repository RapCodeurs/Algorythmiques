"""
0 - Générer une chaine de caractère qui contient 4 chiffres aléatoires, c'est votre séquence initiale.
1 - Ajouter un nouveau nombre aléatoire à la fin de votre séquence
2 - Nettoyer l'écran et affichez "Retenez la séquence" pendant 1 seconde
3 - Afficher la séquence à mémoriser pendant 3 secondes
4 - Nettoyer n'écran et demander la réponse à l'utilisateur
5 - Si la réponse est bonne, afficher pendant 1 seconde "Bonne réponse, votre score est : xxx", puis reboucler à l'étape 1
5bis - Si la réponse n'est pas bonne, sortir du programme et afficher : "Mauvaise réponse, la séquence était : xxxx, votre score final : xxxx"
"""

import time
import random
import os
 
def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

# Génération de la séquence initiale
sequence = ""
for i in range(4):
    chiffre = random.randint(0, 9)
    sequence += str(chiffre)

clear_screen()
print("Bienvenue dans le jeu du Simon")

score = 0
while True:
    print("Retenez la séquence")
    time.sleep(1)
    print(sequence)
    time.sleep(3)
    clear_screen()

    seq_utilisateur = input("Votre réponse : ")
    if seq_utilisateur == sequence:
        score += 1
    else:
        break

    chiffre = random.randint(0, 9)
    sequence += str(chiffre)
    clear_screen()

print("Mauvaise réponse")
print(f"La séquence était {sequence}")
print(f"Votre score final est : {score}")