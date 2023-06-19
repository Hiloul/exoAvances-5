import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sélection et défilement d'images")

# Chargement des images
image1 = pygame.image.load("personnages/tamagotchi(1).png")
image2 = pygame.image.load("personnages/tamagotchi(3).png")

# Positionnement des images
image1_rect = image1.get_rect()
image1_rect.topleft = (100, 100)

image2_rect = image2.get_rect()
image2_rect.topleft = (400, 100)

# Liste des images
images = [image1, image2]
current_image_index = 0  # Indice de l'image actuellement affichée
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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_image_index -= 1
                if current_image_index < 0:
                    current_image_index = len(images) - 1
            elif event.key == pygame.K_RIGHT:
                current_image_index += 1
                if current_image_index >= len(images):
                    current_image_index = 0

    # Effacer l'écran
    screen.fill((255, 255, 255))

    # Afficher l'image actuelle
    screen.blit(images[current_image_index], image1_rect)

    # Mettre à jour l'affichage
    pygame.display.flip()
