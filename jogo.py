# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config  import *
from tela_inicial2 import init_screen, tutorial_screen
from game_screen import game_screen



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
    elif state == OVER:
        state = gameover_screen(screen)
    else:
        state = SAIR
pygame.quit()                

