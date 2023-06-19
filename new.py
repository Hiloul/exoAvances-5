import pygame
import sys

# Définition de la classe Personnage
class Personnage:
    def __init__(self, image, name, health, strength):
        self.image = image
        self.name = name
        self.health = health
        self.strength = strength

# Initialisation de Pygame
pygame.init()

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Dimensions de la fenêtre
screen_width = 800
screen_height = 600

# Création de la fenêtre
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mon Tamagotchi")

# Liste des personnages
personnages = [
    Personnage(pygame.image.load("personnages/tamagotchi(1).png"), "Personnage 1", 100, 10),
    Personnage(pygame.image.load("personnages/tamagotchi(2).png"), "Personnage 2", 150, 15),
    Personnage(pygame.image.load("personnages/tamagotchi(3).png"), "Personnage 3", 120, 12)
]

# Index du personnage actuellement affiché
current_character_index = 0

# Rectangle de l'image du personnage
character_rect = pygame.Rect(0, 0, 200, 200)
character_rect.center = (screen_width // 2, screen_height // 2)

# Rectangle du menu
menu_rect = pygame.Rect(0, 0, screen_width, 30)
# Boucle principale du jeu
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if character_rect.collidepoint(event.pos):
                selected_character = personnages[current_character_index]
                print("Personnage:", selected_character.name)
                print("Santé:", selected_character.health)
                print("Force:", selected_character.strength)

    # Effacer l'écran
    screen.fill(WHITE)

    # Afficher l'image du personnage
    character_image = personnages[current_character_index].image
    screen.blit(character_image, character_rect)

    # Afficher les caractéristiques du personnage
    selected_character = personnages[current_character_index]
    character_info = f"Tamagotchi: {selected_character.name}  Santé: {selected_character.health}  Force: {selected_character.strength}"
    character_info_text = pygame.font.SysFont(None, 24).render(character_info, True, BLACK)
    character_info_rect = character_info_text.get_rect()
    character_info_rect.center = (screen_width // 2, character_rect.bottom + 30)
    screen.blit(character_info_text, character_info_rect)

    # Dessiner le menu
    pygame.draw.rect(screen, BLUE, menu_rect)

    # Mettre à jour l'affichage
    pygame.display.flip()
