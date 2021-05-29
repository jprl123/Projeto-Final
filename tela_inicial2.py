import pygame
from config import *
from assets import *  

pygame.init()
# ----- Gera tela principal e icone de jogo

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('O rato e a rata')

def init_screen(screen):
    assets = load_assets()
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    running = True
    while running:
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(assets[MENU], (0,0))

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
