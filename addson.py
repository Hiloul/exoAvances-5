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
son = pygame.mixer.Sound("sons/son.wav")

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
