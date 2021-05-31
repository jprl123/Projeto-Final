import pygame
from config import *
from assets import *  
from os import path

def init_screen(screen): 
    assets = load_assets()
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    menu = pygame.image.load(path.join(img_dir, 'Menu inicial.png')).convert()
    menu = pygame.transform.scale(assets[MENU],(WIDTH,HEIGHT))

    running = True
    while running:
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = SAIR
                running = False
            if event.type == pygame.KEYUP:
                state = INST
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(menu, (0,0))

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state

def tutorial_screen(screen): 
    assets = load_assets()
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    tutorial = assets[TUTORIAL]

    running = True
    while running:
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = SAIR
                running = False
            if event.type == pygame.KEYUP:
                state = JOGAR
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(tutorial, (0,0))

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state

