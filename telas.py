import pygame
from config import *
from assets import *  
from os import path


# função que produz a tela inicial
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
        screen.fill(BLACK)
        screen.blit(menu, (0,0))
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    return state

# funcao que produz a tela de tutorial
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
        screen.fill(BLACK)
        screen.blit(tutorial, (0,0))
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    return state


# função que produz a tela de game over
def gameover_screen(screen,score):
    assets = load_assets()
    clock = pygame.time.Clock()
    score_over = assets[OVER_FONT].render("{:08d}".format(score), True, BLUE)
    textoover1 = assets[OVER_FONT].render('Aperte ESPAÇO para reiniciar o jogo', True, BLUE)
    textoover2 = assets[OVER_FONT].render('Aperte ESC se quiser sair do jogo', True, BLUE)
    gameover = assets[SCORE_FONT].render('GAME OVER', True, BLUE)
    #Limpa eventos -> parecia que ao carregar essa página o pygame estava com eventos da outra tela
    pygame.event.clear()
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
                if event.key == pygame.K_SPACE:
                    state = JOGAR
                    running = False
                if event.key == pygame.K_ESCAPE:
                    state = SAIR
                    running = False
        screen.fill(BLACK)
        screen.blit(assets[TELATRANSI], (0, 0))
        screen.blit(gameover,   (860, 240))
        screen.blit(score_over, (860, 540))
        screen.blit(textoover1, (460, 740))
        screen.blit(textoover2, (480, 840))
        pygame.display.flip()
    return state

# função que produz a tela de Win
def gamewin_screen(screen,score):
    assets = load_assets()
    clock = pygame.time.Clock()
    score_over = assets[OVER_FONT].render("{:08d}".format(score), True, BLUE)
    textoover1 = assets[OVER_FONT].render('Aperte ESPAÇO para reiniciar o jogo', True, BLUE)
    textoover2 = assets[OVER_FONT].render('Aperte ESC se quiser sair do jogo', True, BLUE)
    gamewin = assets[SCORE_FONT].render('YOU WIN', True, BLUE)
    #Limpa eventos -> parecia que ao carregar essa página o pygame estava com eventos da outra tela
    pygame.event.clear()
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
                if event.key == pygame.K_SPACE:
                    state = JOGAR
                    running = False
                if event.key == pygame.K_ESCAPE:
                    state = SAIR
                    running = False
        #produz a tela de WIN
        screen.fill(BLACK)
        screen.blit(assets[TELATRANSI], (0, 0))
        screen.blit(gamewin,   (860, 240))
        screen.blit(score_over, (860, 540))
        screen.blit(textoover1, (460, 740))
        screen.blit(textoover2, (480, 840))
        pygame.display.flip()
    return state

def transi_screen(screen):
    assets = load_assets()
    clock = pygame.time.Clock()
    textoover1 = assets[OVER_FONT].render('FASE 2 APERTE ESPAÇO PARA CONTINUAR', True, BLUE)
    #Limpa eventos -> parecia que ao carregar essa página o pygame estava com eventos da outra tela
    pygame.event.clear()
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
                if event.key == pygame.K_SPACE:
                    state = JOGAR
                    running = False
        #produz a tela de WIN
        screen.fill(BLACK)
        screen.blit(assets[TELATRANSI], (0, 0))
        screen.blit(textoover1, (460, HEIGHT//2))
        pygame.display.flip()
    return state