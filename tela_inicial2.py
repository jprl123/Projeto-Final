import pygame
from config import *
from assets import *  
import os
pygame.init()
# ----- Gera tela principal e icone de jogo

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('O rato e a rata')

game = True
start = True
# ===== Loop principal =====
while game:
    assets = load_assets()
    while start:
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    start == False    
        screen.fill((0, 0, 0))
        screen.blit(assets[MENU], (0,0))
    # ----- Gera saídas
    # ----- Atualiza estado do jogo
        pygame.display.update()
        