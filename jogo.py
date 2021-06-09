# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config  import *
from telas import gameover_screen, init_screen, tutorial_screen, gamewin_screen,transi_screen
from game_screen import game_screen
from game_screen2 import game_screen2




pygame.init()
pygame.mixer.init()


# ----- Gera tela principal-------------
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('O Rato e a Rata')
#icone do jogo
gameIcon = pygame.image.load(path.join(img_dir, 'queijo.png'))
pygame.display.set_icon(gameIcon)


state = INICIA
score = 0
while state != SAIR:
    if state == INICIA:
        state = init_screen(screen) #tela inicial
    elif state == INST:
        state = tutorial_screen(screen) # tela de tutorial
    elif state == JOGAR:
        state, score = game_screen(screen)
        if state == PASSOU: #responsavel para passar de fase
            state = transi_screen(screen) #tela de transição
            state, score = game_screen2(screen,score) #tela da fase 2
    elif state == OVER: 
        state = gameover_screen(screen, score) #tela de game over
    elif state == WIN:
        state = gamewin_screen (screen, score) #tela de vencedor
    else:
        state = SAIR
pygame.quit()                

