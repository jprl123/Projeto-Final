# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config  import *
from telas import gameover_screen, init_screen, tutorial_screen, gamewin_screen
from game_screen import game_screen
from game_screen2 import game_screen2




pygame.init()
pygame.mixer.init()


# ----- Gera tela principal e icone de jogo
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('O Rato e a Rata')


state = INICIA
score = 0
while state != SAIR:
    if state == INICIA:
        state = init_screen(screen)
    elif state == INST:
        state = tutorial_screen(screen)
    elif state == JOGAR:
        state, score = game_screen(screen)
        print(state)
        if state == 1:
            state, score = game_screen2(screen)
    elif state == OVER: 
        state = gameover_screen(screen, score)
    elif state == WIN:
        state = gamewin_screen (screen, score)
    else:
        state = SAIR
pygame.quit()                

