import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Dimensions de la fenêtre
screen_width = 800
screen_height = 600

# Dimensions du menu
menu_height = 50

# Création de la fenêtre
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menu avec input")

# Rectangle du menu
menu_rect = pygame.Rect(0, 0, screen_width, menu_height)

# Rectangle du champ de saisie
input_rect = pygame.Rect(100, 100, 200, 30)

# Police de caractères
font = pygame.font.SysFont(None, 24)

# Texte de l'entrée utilisateur
user_input = ""

# Boucle principale du jeu
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.key == pygame.K_RETURN:
                print("Entrée utilisateur :", user_input)
                user_input = ""
            else:
                user_input += event.unicode

    # Effacer l'écran
    screen.fill(WHITE)

    # Dessiner le menu
    pygame.draw.rect(screen, BLUE, menu_rect)

    # Dessiner le champ de saisie
    pygame.draw.rect(screen, WHITE, input_rect)
    pygame.draw.rect(screen, BLACK, input_rect, 2)

    # Afficher le texte de l'entrée utilisateur
    text_surface = font.render(user_input, True, BLACK)
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    # Mettre à jour l'affichage
    pygame.display.flip()


import pygame
import sys

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

# Dimensions du menu déroulant
menu_width = 200
menu_height = 30
option_height = 30

# Création de la fenêtre
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menu déroulant")

# Rectangle du menu déroulant
menu_rect = pygame.Rect(100, 100, menu_width, menu_height)

# Rectangle de l'option sélectionnée
selected_option_rect = pygame.Rect(100, 100, menu_width, option_height)

# Liste des options du menu
menu_options = ["Option 1", "Option 2", "Option 3"]
options_visible = False

# Boucle principale du jeu
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu_rect.collidepoint(event.pos):
                options_visible = not options_visible
            elif options_visible and not selected_option_rect.collidepoint(event.pos):
                options_visible = False

    # Effacer l'écran
    screen.fill(WHITE)

    # Dessiner le menu déroulant
    pygame.draw.rect(screen, BLUE, menu_rect)

    # Dessiner l'option sélectionnée
    pygame.draw.rect(screen, GREEN, selected_option_rect)
    selected_option_text = pygame.font.SysFont(None, 24).render("Sélectionnez une option", True, BLACK)
    screen.blit(selected_option_text, (selected_option_rect.x + 5, selected_option_rect.y + 5))

    # Afficher les options si le menu déroulant est ouvert
    if options_visible:
        for i, option in enumerate(menu_options):
            option_rect = pygame.Rect(menu_rect.x, menu_rect.y + (i + 1) * option_height, menu_width, option_height)
            pygame.draw.rect(screen, BLUE, option_rect)
            option_text = pygame.font.SysFont(None, 24).render(option, True, BLACK)
            screen.blit(option_text, (option_rect.x + 5, option_rect.y + 5))

    # Mettre à jour l'affichage
    pygame.display.flip()
