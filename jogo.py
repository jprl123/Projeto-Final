# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config  import *
from tela_inicial2 import init_screen, tutorial_screen
from game_screen import game_screen
from game_screen2 import game_screen2




pygame.init()
pygame.mixer.init()


# ----- Gera tela principal e icone de jogo
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('O Rato e a Rata')

gameIcon = pygame.image.load(path.join(img_dir, 'queijo.png'))
pygame.display.set_icon(gameIcon)

state = INICIA
while state != SAIR:
    if state == INICIA:
        state = init_screen(screen)
    elif state == INST:
        state = tutorial_screen(screen)
    elif state == JOGAR:
        state = game_screen(screen)
        if state == 1:
            state = game_screen2(screen)
    else:
        state = SAIR
pygame.quit()                

