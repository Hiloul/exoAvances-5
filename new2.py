import pygame
import sys
import pygame.mixer

# Initialisation de Pygame
pygame.init()

# Couleur de fond
background_color = (241, 184, 168)  # Blanc
# Création de la fenêtre
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sélection et défilement d'images")
# F1B8A8
# Initialisation du mixer Pygame
pygame.mixer.init()

# Chargement du son
son = pygame.mixer.Sound("sons/son-selection.wav")


# Chargement des images
image1 = pygame.image.load("personnages/tamagotchi(1).png")
image2 = pygame.image.load("personnages/tamagotchi(2).png")
image3 = pygame.image.load("personnages/tamagotchi(3).png")
image4 = pygame.image.load("personnages/tamagotchi(4).png")
image5 = pygame.image.load("personnages/tamagotchi(5).png")
image6 = pygame.image.load("personnages/tamagotchi(6).png")
image7 = pygame.image.load("personnages/tamagotchi(7).png")
image8 = pygame.image.load("personnages/tamagotchi(8).png")
image9 = pygame.image.load("personnages/tamagotchi(9).png")
image10 = pygame.image.load("personnages/tamagotchi(10).png")

# # Redimensionnement de l'image
# new_width = 200  # Nouvelle largeur de l'image
# new_height = 150  # Nouvelle hauteur de l'image
# resized_image = pygame.transform.scale(images, (new_width, new_height))


# Positionnement des images
# image_rect = resized_image.get_rect()
# image_rect.center = (400, 300)
image1_rect = image1.get_rect()
image1_rect.center = (400, 300)

image2_rect = image2.get_rect()
image2_rect.center = (400, 300)

image3_rect = image1.get_rect()
image3_rect.center = (400, 300)

image4_rect = image2.get_rect()
image4_rect.center = (400, 300)

image5_rect = image1.get_rect()
image5_rect.center = (400, 300)

image6_rect = image2.get_rect()
image6_rect.center = (400, 300)

image7_rect = image1.get_rect()
image7_rect.center = (400, 300)

image8_rect = image2.get_rect()
image8_rect.center = (400, 300)

image9_rect = image1.get_rect()
image9_rect.center = (400, 300)

image10_rect = image2.get_rect()
image10_rect.center = (400, 300)

# Liste des images
images = [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10 ]
current_image_index = 0  # Indice de l'image actuellement affichée
image_rects = [image1_rect, image2_rect, image3_rect, image4_rect, image5_rect, image6_rect, image7_rect, image8_rect, image9_rect, image10_rect]

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
                    son.play()
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
    # screen.fill((255, 255, 255))
   # Remplir l'écran avec la couleur de fond
    screen.fill(background_color)
    # Afficher l'image actuelle
    screen.blit(images[current_image_index], image1_rect)

    # Mettre à jour l'affichage
    pygame.display.flip()
