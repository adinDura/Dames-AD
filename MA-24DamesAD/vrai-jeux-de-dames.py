import pygame

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre et du plateau de jeu
case_size = 80

cases_brunes_claires = (210, 180, 140)  # Couleur brun clair
cases_brunes_foncées = (139, 69, 19)    # Couleur brun foncé
window_color = (89, 152, 255)  # Couleur de fond de la fenêtre

# Taille du plateau et de la fenêtre
nb_lignes = 10
nb_colonnes = 10
window_width = case_size * nb_colonnes
window_height = case_size * nb_lignes
window_size = (window_width, window_height)

# Création de la fenêtre de jeu
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Damier 10x10")

# Chargement des images des pions
pion_rouge = pygame.image.load("bmw_PNG99548.png")
pion_rouge = pygame.transform.scale(pion_rouge, (case_size, case_size))

pion_bleu = pygame.image.load("circle-flag-of-bosnia-and-herzegovina-free-png.webp")
pion_bleu = pygame.transform.scale(pion_bleu, (case_size, case_size))

# Positions initiales des pions rouges
pions_rouges_positions = [(0, 0), (2, 0), (4, 0), (6, 0), (8, 0),
                          (1, 1), (3, 1), (5, 1), (7, 1), (9, 1),
                          (0,2),   (2,2),  (4,2),(6,2),   (8,2),
                          (1,3), (3,3),(5,3),(7,3),(9,3)]

# Positions initiales des pions bleus
pions_bleus_positions = [(0, 8), (2, 8), (4, 8), (6, 8), (8, 8),
                         (1, 9), (3, 9), (5, 9), (7, 9), (9, 9),
                         (1,7),(3,7),  (5,7),(7,7),   (9,7),
                         (0,6), (2,6),(4,6),(6,6),(8,6)]

pion_selectionne = None  # Aucun pion sélectionné au départ
type_pion_selectionne = None  # Type de pion sélectionné ("bosnie" ou "BMW")

# Dessiner le damier
def dessiner_damier():
    for ligne in range(nb_lignes):
        for colonne in range(nb_colonnes):
            couleur_case = cases_brunes_claires if (ligne + colonne) % 2 == 0 else cases_brunes_foncées
            pygame.draw.rect(
                window,
                couleur_case,
                (colonne * case_size, ligne * case_size, case_size, case_size)
            )

# Dessiner les pions
def dessiner_pions():
    for colonne, ligne in pions_rouges_positions:
        window.blit(pion_rouge, (colonne * case_size, ligne * case_size))
    for colonne, ligne in pions_bleus_positions:
        window.blit(pion_bleu, (colonne * case_size, ligne * case_size))

# Déplacer un pion sélectionné en diagonale
def deplacer_pion(pion_index, direction, type_pion):
    if type_pion == "rouge":
        positions = pions_rouges_positions
    elif type_pion == "bleu":
        positions = pions_bleus_positions
    else:
        return

    colonne, ligne = positions[pion_index]
    if direction == "UP_LEFT" and ligne > 0 and colonne > 0:
        positions[pion_index] = (colonne - 1, ligne - 1)
    elif direction == "UP_RIGHT" and ligne > 0 and colonne < nb_colonnes - 1:
        positions[pion_index] = (colonne + 1, ligne - 1)
    elif direction == "DOWN_LEFT" and ligne < nb_lignes - 1 and colonne > 0:
        positions[pion_index] = (colonne - 1, ligne + 1)
    elif direction == "DOWN_RIGHT" and ligne < nb_lignes - 1 and colonne < nb_colonnes - 1:
        positions[pion_index] = (colonne + 1, ligne + 1)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Gestion de la sélection des pions
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            colonne = mouse_x // case_size
            ligne = mouse_y // case_size

            if (colonne, ligne) in pions_rouges_positions:
                pion_selectionne = pions_rouges_positions.index((colonne, ligne))
                type_pion_selectionne = "rouge"
            elif (colonne, ligne) in pions_bleus_positions:
                pion_selectionne = pions_bleus_positions.index((colonne, ligne))
                type_pion_selectionne = "bleu"
            else:
                pion_selectionne = None
                type_pion_selectionne = None

        # Gestion du déplacement des pions
        if event.type == pygame.KEYDOWN and pion_selectionne is not None:
            if event.key == pygame.K_q:  # Haut-gauche
                deplacer_pion(pion_selectionne, "UP_LEFT", type_pion_selectionne)
            elif event.key == pygame.K_e:  # Haut-droite
                deplacer_pion(pion_selectionne, "UP_RIGHT", type_pion_selectionne)
            elif event.key == pygame.K_a:  # Bas-gauche
                deplacer_pion(pion_selectionne, "DOWN_LEFT", type_pion_selectionne)
            elif event.key == pygame.K_d:  # Bas-droite
                deplacer_pion(pion_selectionne, "DOWN_RIGHT", type_pion_selectionne)

    # Dessin du damier et des pions
    window.fill(window_color)  # Remplir l'arrière-plan avec une couleur de fond
    dessiner_damier()  # Dessiner le damier
    dessiner_pions()   # Dessiner les pions
    pygame.display.flip()  # Rafraîchir l'affichage

pygame.quit()
