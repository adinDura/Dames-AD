import pygame

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre et du plateau de jeu
case_size = 80
cases_blanches = (255, 255, 255)
cases_noires = (180, 180, 180)
window_color = (89, 152, 255)
path_to_images = "pictures/"

# Taille du plateau et de la fenêtres
nb_lignes = 10
nb_colonnes = 10
window_width = case_size * nb_colonnes
window_height = case_size * nb_lignes
window_size = (window_width, window_height)

# Création de la fenêtre de jeu
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Damier 10x10")

# Chargement de l'image du pion
pion = pygame.image.load("MA-24_pion.png")
pion = pygame.transform.scale(pion, (case_size, case_size))

# Position initiale des pions
pions_positions = [ (0, 0),(2, 0), (4, 0), (6, 0),(8,0),
(1,1),(3,1),(5,1),(7,1),(9,1),(0,2),(2,2),(4,2),(6,2),(8,2)]

pion_selectionne = None  # Aucun pion sélectionné au départ

# Dessiner le damier
def dessiner_damier():
    for ligne in range(nb_lignes):
        for colonne in range(nb_colonnes):
            couleur_case = cases_blanches if (ligne + colonne) % 2 == 0 else cases_noires
            pygame.draw.rect(
                window,
                couleur_case,
                (colonne * case_size, ligne * case_size, case_size, case_size)
            )

# Dessiner les pions
def dessiner_pions():
    for colonne, ligne in pions_positions:
        window.blit(pion, (colonne * case_size, ligne * case_size))

# Déplacer un pion sélectionné
def deplacer_pion(pion_index, direction):
    colonne, ligne = pions_positions[pion_index]
    if direction == "UP" and ligne > 0:
        pions_positions[pion_index] = (colonne, ligne - 1)
    elif direction == "DOWN" and ligne < nb_lignes - 1:
        pions_positions[pion_index] = (colonne, ligne + 1)
    elif direction == "LEFT" and colonne > 0:
        pions_positions[pion_index] = (colonne - 1, ligne)
    elif direction == "RIGHT" and colonne < nb_colonnes - 1:
        pions_positions[pion_index] = (colonne + 1, ligne)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Gestion de la sélection et du déplacement des pions
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            colonne = mouse_x // case_size
            ligne = mouse_y // case_size
            if (colonne, ligne) in pions_positions:
                pion_selectionne = pions_positions.index((colonne, ligne))
            else:
                pion_selectionne = None

        if event.type == pygame.KEYDOWN and pion_selectionne is not None:
            if event.key == pygame.K_UP:
                deplacer_pion(pion_selectionne, "UP")
            elif event.key == pygame.K_DOWN:
                deplacer_pion(pion_selectionne, "DOWN")
            elif event.key == pygame.K_LEFT:
                deplacer_pion(pion_selectionne, "LEFT")
            elif event.key == pygame.K_RIGHT:
                deplacer_pion(pion_selectionne, "RIGHT")

    # Dessin du damier et des pions
    window.fill(window_color)
    dessiner_damier()
    dessiner_pions()
    pygame.display.flip()


pygame.quit()
