from os import path



#Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'assets\img')
font_dir = path.join(path.dirname(__file__), 'assets','font')
snd_dir = path.join(path.dirname(__file__), 'assets\snd')


# predefinições para as imagens
RATO1 = 'rato1_img'
RATO2 = 'rato2_img'
QUEIJO = 'queijo_img'
BACKGROUND = 'background_img'
SCORE_FONT = 'score_font'
JUMP = 'rapaz_snd'
FASE = 'uepa_snd'
MENU = 'menu_img'





BLOCK = 0
FOGO = 1
WATER = 2
EMPTY = -1


# Dados gerais do jogo.
WIDTH = 1920 # Largura da tela
HEIGHT = 1080 # Altura da tela
FPS = 45 # Frames por segundo
TILE_SIZE = 30 # Tamanho de cada tile (cada tile é um quadrado)

# Define tamanhos
RATO_HEIGHT = TILE_SIZE*2 #int(50*(2/3))
RATO_WIDTH = TILE_SIZE #int(25*(2/3))
QUEIJO_WIDTH = TILE_SIZE
QUEIJO_HEIGHT = TILE_SIZE

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo 
INIT = 0
GAME = 1
QUIT = 2

#gravidade
GRAVITY = 3
#velocidade do pulo
JUMP_SIZE = TILE_SIZE
#velocidade em x
SPEED_X = 10

