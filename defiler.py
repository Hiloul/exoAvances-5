import pygame

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
pygame.display.set_caption("Choix du personnage")

# Chargement des images
images = [
    pygame.image.load("personnages/tamagotchi(1).png"),
    pygame.image.load("personnages/tamagotchi(2).png"),
    pygame.image.load("personnages/tamagotchi(3).png"),
    pygame.image.load("personnages/tamagotchi(4).png"),
    pygame.image.load("personnages/tamagotchi(5).png"),
    pygame.image.load("personnages/tamagotchi(6).png"),
    pygame.image.load("personnages/tamagotchi(7).png"),
    pygame.image.load("personnages/tamagotchi(8).png"),
    pygame.image.load("personnages/tamagotchi(9).png"),
    pygame.image.load("personnages/tamagotchi(10).png")
]

# Index de l'image sélectionnée
index_image = 0

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
                # Défiler vers l'image précédente
                index_image = (index_image - 1) % len(images)
            elif event.key == pygame.K_RIGHT:
                # Défiler vers l'image suivante
                index_image = (index_image + 1) % len(images)
    
    # Affichage de l'image sélectionnée
    image = images[index_image]
    image_rect = image.get_rect()
    fenetre.blit(image, (x_image, y_image))
    
    # Mise à jour de l'affichage
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
