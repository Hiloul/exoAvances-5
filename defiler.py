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
pygame.display.set_caption("Sélection et déplacement du personnage")

# Chargement des images des personnages
personnage1 = pygame.image.load("personnages/tamagotchi(1).png")
personnage2 = pygame.image.load("personnages/tamagotchi(2).png")
personnage3 = pygame.image.load("personnages/tamagotchi(3).png")

# Liste des images des personnages
personnages = [personnage1, personnage2, personnage3]

# Index du personnage sélectionné
index_personnage = 2

# Position de départ du personnage
x_personnage = 100
y_personnage = 100

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
                # Déplacer le personnage vers la gauche
                x_personnage -= deplacement
            elif event.key == pygame.K_RIGHT:
                # Déplacer le personnage vers la droite
                x_personnage += deplacement
            elif event.key == pygame.K_UP:
                # Déplacer le personnage vers le haut
                y_personnage -= deplacement
            elif event.key == pygame.K_DOWN:
                # Déplacer le personnage vers le bas
                y_personnage += deplacement
            elif event.key == pygame.K_SPACE:
                # Changer de personnage sélectionné
                index_personnage = (index_personnage + 1) % len(personnages)
    
    # Affichage du personnage sélectionné
    personnage = personnages[index_personnage]
    personnage_rect = personnage.get_rect()
    fenetre.blit(personnage, (x_personnage, y_personnage))
    
    # Mise à jour de l'affichage
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
