import random
# va servir a générer les nombres de dégats / soins de manière aléatoire

santé_joueur = 50
santé_ennemi = 50
potions_joueur = 3
passer_tour = False
# pas de potions pour l'adversaire, 3 pour le joueur et 50PV pour tout les deux.
# le joueur participe a chaque tour de base.

while True:

    # Tour du joueur
    if  passer_tour:
        print("Vous passez votre tour...")
        passer_tour = False

    else:
        choix_joueur = ""
        while choix_joueur not in ["1", "2"]:
            choix_joueur = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
        if choix_joueur == "1": # Option 1 = Attaque
            attaque_joueur = random.randint(5, 10)
            santé_ennemi -= attaque_joueur
            print(f"Vous avez infligé {attaque_joueur} points de dégats à l'ennemi ⚔️")
        elif choix_joueur == "2" and potions_joueur > 0:  # Option 2 = Potion (à condition d'en avoir)
            bonus_potion = random.randint(15, 50)
            santé_joueur += bonus_potion
            potions_joueur -= 1
            passer_tour = True
            print(f"Vous récupérez {bonus_potion} points de vie ❤️ ({potions_joueur} potions restantes)")
        else:
            print("Vous n'avez plus de potions...")
            continue

    #Fin du jeu si ennemi n'a plus de PV
    if santé_ennemi <= 0:
        print("Tu as gagné !")
        break
    
    # Attaque de l'ennemi si il est toujours vivant
    attaque_ennemi = random.randint(5, 15)
    santé_joueur -= attaque_ennemi
    print(f"L'ennemi vous a infligé {attaque_ennemi} points de dégats ⚔️")

    #Fin du jeu si joueur n'a plus de PV
    if santé_joueur <= 0:
        print("Tu as perdu !")
        break

    # Affichage des Stats à chaque tour.
    print(f"Il vous reste {santé_joueur} points de vie.")
    print(f"Il reste {santé_ennemi} points de vie à l'ennemi.")
    print("-" * 50)


print("Fin du jeu.")