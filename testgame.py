import pygame
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre du jeu
largeur_fenetre = 400
hauteur_fenetre = 400

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

# Création de la fenêtre du jeu
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Tamagotchi")

# Chargement des images
image_tamagotchi = pygame.image.load("tamagotchi.png")
image_boule = pygame.image.load("boule.png")
image_nourriture = pygame.image.load("nourriture.png")

# Position et variables du Tamagotchi
x_tamagotchi = 150
y_tamagotchi = 150
nourriture = 10
bonheur = 10

# Variables du jeu
jeu_actif = True
clock = pygame.time.Clock()

# Boucle principale du jeu
while jeu_actif:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu_actif = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Interaction avec le tamagotchi
            pos = pygame.mouse.get_pos()
            if x_tamagotchi < pos[0] < x_tamagotchi + 100 and y_tamagotchi < pos[1] < y_tamagotchi + 100:
                bonheur += random.randint(1, 3)
    
    # Gestion des besoins du Tamagotchi
    if bonheur > 0:
        nourriture -= 1
        if nourriture <= 0:
            bonheur -= 1
            nourriture = 0
    else:
        jeu_actif = False
    
    # Affichage des éléments du jeu
    fenetre.fill(blanc)
    fenetre.blit(image_tamagotchi, (x_tamagotchi, y_tamagotchi))
    fenetre.blit(image_boule, (20, 20))
    fenetre.blit(image_nourriture, (20, 150))
    
    # Affichage des besoins du Tamagotchi
    pygame.draw.rect(fenetre, noir, (130, 30, nourriture * 20, 20))
    pygame.draw.rect(fenetre, noir, (130, 160, bonheur * 20, 20))
    
    # Mise à jour de l'affichage
    pygame.display.flip()
    
    # Limite le taux de rafraîchissement à 60 images par seconde
    clock.tick(60)

# Fermeture de Pygame
pygame.quit()
