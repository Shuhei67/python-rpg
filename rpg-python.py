import random

santé_joueur = 50
santé_ennemi = 50
potions_joueur = 3
passer_tour = False


while True:

    if  passer_tour:
        print("Vous passez votre tour...")
        passer_tour = False

    else:
        choix_joueur = ""
        while choix_joueur not in ["1", "2"]:
            choix_joueur = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
        if choix_joueur == "1": 
            attaque_joueur = random.randint(5, 10)
            santé_ennemi -= attaque_joueur
            print(f"Vous avez infligé {attaque_joueur} points de dégats à l'ennemi ⚔️")
        elif choix_joueur == "2" and potions_joueur > 0:
            bonus_potion = random.randint(15, 50)
            santé_joueur += bonus_potion
            potions_joueur -= 1
            passer_tour = True
            print(f"Vous récupérez {bonus_potion} points de vie ❤️ ({potions_joueur} potions restantes)")
        else:
            print("Vous n'avez plus de potions...")
            continue

    if santé_ennemi <= 0:
        print("Tu as gagné !")
        break
    
    attaque_ennemi = random.randint(5, 15)
    santé_joueur -= attaque_ennemi
    print(f"L'ennemi vous a infligé {attaque_ennemi} points de dégats ⚔️")

    if santé_joueur <= 0:
        print("Tu as perdu !")
        break

    print(f"Il vous reste {santé_joueur} points de vie.")
    print(f"Il reste {santé_ennemi} points de vie à l'ennemi.")
    print("-" * 50)


print("Fin du jeu.")