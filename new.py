import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sélection d'image")

# Chargement des images
image1 = pygame.image.load("personnages/tamagotchi(1).png")
image2 = pygame.image.load("personnages/tamagotchi(3).png")

# Positionnement des images
image1_rect = image1.get_rect()
image1_rect.topleft = (100, 100)

image2_rect = image2.get_rect()
image2_rect.topleft = (400, 100)

# Liste des images et rectangles correspondants
images = [image1, image2]
image_rects = [image1_rect, image2_rect]

# Boucle principale du jeu
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Vérification si la souris est sur l'une des images
            for index, rect in enumerate(image_rects):
                if rect.collidepoint(event.pos):
                    print("Image", index + 1, "sélectionnée")

    # Effacer l'écran
    screen.fill((255, 255, 255))

    # Afficher les images
    for image, rect in zip(images, image_rects):
        screen.blit(image, rect)

    # Mettre à jour l'affichage
    pygame.display.flip()
