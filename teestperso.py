import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("salmon")

    # RENDER YOUR GAME HERE
    # Chargement des images
image_tamagotchi = pygame.image.load("tamagotchi.png")
image_boule = pygame.image.load("boule.png")
image_nourriture = pygame.image.load("nourriture.png")

# Position et variables du Tamagotchi
x_tamagotchi = 150
y_tamagotchi = 150
nourriture = 10
bonheur = 10
# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

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
    screen.fill(blanc)
    screen.blit(image_tamagotchi, (x_tamagotchi, y_tamagotchi))
    screen.blit(image_boule, (20, 20))
    screen.blit(image_nourriture, (20, 150))
    
    # Affichage des besoins du Tamagotchi
    pygame.draw.rect(screen, noir, (130, 30, nourriture * 20, 20))
    pygame.draw.rect(screen, noir, (130, 160, bonheur * 20, 20))
    
    # Mise à jour de l'affichage
    pygame.display.flip()
    
    # Limite le taux de rafraîchissement à 60 images par seconde
    clock.tick(60)

pygame.quit()


import pygame
import pygame.mixer

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre du jeu
largeur_fenetre = 800
hauteur_fenetre = 600

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

# Création de la fenêtre du jeu
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Déplacement d'image")

# Initialisation du mixer Pygame
pygame.mixer.init()

# Chargement du son
son = pygame.mixer.Sound("son.wav")

# Chargement de l'image
image = pygame.image.load("personnages/tamagotchi(1).png")
image_rect = image.get_rect()

# Position de départ de l'image
x_image = 100
y_image = 100

# Variables de déplacement
deplacement = 5

# Boucle principale du jeu
running = True
while running:
    fenetre.fill(blanc)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_image -= deplacement
            elif event.key == pygame.K_RIGHT:
                x_image += deplacement
            elif event.key == pygame.K_UP:
                y_image -= deplacement
            elif event.key == pygame.K_DOWN:
                y_image += deplacement
            elif event.key == pygame.K_SPACE:
                x_image += deplacement
                y_image += deplacement
                son.play()
    
    # Limitation des mouvements dans les limites de la fenêtre
    if x_image < 0:
        x_image = 0
    elif x_image > largeur_fenetre - image_rect.width:
        x_image = largeur_fenetre - image_rect.width
    if y_image < 0:
        y_image = 0
    elif y_image > hauteur_fenetre - image_rect.height:
        y_image = hauteur_fenetre - image_rect.height
    
    # Affichage de l'image
    fenetre.blit(image, (x_image, y_image))
    son.play()
    
    # Mise à jour de l'affichage
    pygame.display.flip()

# Fer
