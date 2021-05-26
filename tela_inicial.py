import pygame
from config import *

pygame.init()
# ----- Gera tela principal e icone de jogo

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('O rato e a rata')

gameIcon = pygame.image.load(path.join(img_dir, 'queijo.png'))
pygame.display.set_icon(gameIcon)

game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    screen.fill((255, 255, 255))  # Preenche com a cor branca
    # ----- Atualiza estado do jogo
    pygame.display.update()