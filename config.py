from os import path



#Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'assets\img')

RATO1 = 'rato1_img'
RATO2 = 'rato2_img'
QUEIJO = 'queijo_img'
BACKGROUND = 'background_img'
BLOCK = 0
FOGO = 1
WATER = 2
EMPTY = -1


# Dados gerais do jogo.
WIDTH = 1920 # Largura da tela
HEIGHT = 1080 # Altura da tela
FPS = 60 # Frames por segundo


# Define tamanhos
RATO_HEIGHT = 50
RATO_WIDTH = 25
QUEIJO_WIDTH = 50
QUEIJO_HEIGHT = 38

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2

#define os FPS
FPS = 30 


TILE_SIZE = 30 # Tamanho de cada tile (cada tile é um quadrado)
# Define a aceleração da gravidade
GRAVITY = 3.5
# Define a velocidade inicial no pulo
JUMP_SIZE = TILE_SIZE
# Define a velocidade em x
SPEED_X = 5

