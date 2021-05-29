# ===== Inicialização =====
# ----- Importa e inicia pacotes
from os import stat
from tela_inicial2 import init_screen
from mapas import *
import pygame
from config  import *
from assets import *
import random
from sprites import *
from game_screen import *
pygame.init()
pygame.mixer.init()

# ----- Gera tela principal e icone de jogo

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('O rato e a rata')

gameIcon = pygame.image.load(path.join(img_dir, 'queijo.png'))
pygame.display.set_icon(gameIcon)

state = INICIA
while state != QUIT:
    if state == INICIA:
        state == init_screen(screen)
    elif state == JOGAR:
        state == game_screen(screen)
    else:
        state == QUIT
pygame.quit()                

