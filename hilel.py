import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Redimensionnement d'image")

# Chargement de l'image
image = pygame.image.load("image.png")

# Redimensionnement de l'image
new_width = 200  # Nouvelle largeur de l'image
new_height = 150  # Nouvelle hauteur de l'image
resized_image = pygame.transform.scale(image, (new_width, new_height))

# Positionnement de l'image
image_rect = resized_image.get_rect()
image_rect.center = (400, 300)

# Boucle principale du jeu
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Effacer l'écran
    screen.fill((255, 255, 255))

    # Afficher l'image redimensionnée
    screen.blit(resized_image, image_rect)

    # Mettre à jour l'affichage
    pygame.display.flip()
import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Redimensionnement d'image")

# Chargement de l'image
image = pygame.image.load("image.png")

# Redimensionnement de l'image
new_width = 200  # Nouvelle largeur de l'image
new_height = 150  # Nouvelle hauteur de l'image
resized_image = pygame.transform.scale(image, (new_width, new_height))

# Positionnement de l'image
image_rect = resized_image.get_rect()
image_rect.center = (400, 300)

# Boucle principale du jeu
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Effacer l'écran
    screen.fill((255, 255, 255))

    # Afficher l'image redimensionnée
    screen.blit(resized_image, image_rect)

    # Mettre à jour l'affichage
    pygame.display.flip()
