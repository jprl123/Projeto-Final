# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from os import path
pygame.init()

# ----- Gera tela principal
WIDTH = 1920
HEIGHT = 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello World!')
FPS = 60 
TILE_SIZE = 60 # Tamanho de cada tile (cada tile é um quadrado)
# Define a aceleração da gravidade
GRAVITY = 5
# Define a velocidade inicial no pulo
JUMP_SIZE = TILE_SIZE
# Define a velocidade em x
SPEED_X = 5

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

TITULO = 'Exemplo de Tiles'
JUMP_SIZE = TILE_SIZE
BLOCK = 0
FOGO = 1
WATER = 2
EMPTY = -1


img_dir = path.join(path.dirname(__file__), 'assets\img')
rato1 = 'player_img'
rato2 = 'player2_img'
# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
RATO_WIDTH = 100 
RATO_HEIGHT = 50
QUEIJO_WIDTH = 50
QUEIJO_HEIGHT = 38
assets = {}
assets['background'] = pygame.image.load('assets/img/mapa.png').convert()
assets['background'] = pygame.transform.scale(assets['background'],(WIDTH,HEIGHT))
assets['rato1'] = pygame.image.load('assets/img/rato1.png').convert_alpha()
assets['rato1'] = pygame.transform.scale(assets['rato1'],(RATO_WIDTH, RATO_HEIGHT))
assets['rato2'] = pygame.image.load('assets/img/rato2.png').convert_alpha()
assets['rato2'] = pygame.transform.scale(assets['rato2'],(RATO_WIDTH, RATO_HEIGHT))
assets['queijo'] = pygame.image.load('assets/img/queijo.png').convert_alpha()
assets['queijo'] = pygame.transform.scale(assets['queijo'],(QUEIJO_WIDTH, QUEIJO_HEIGHT))



# Define o mapa com os tipos de tiles
MAP = [
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,BLOCK,BLOCK,BLOCK,BLOCK, BLOCK, BLOCK,BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,BLOCK,BLOCK,BLOCK,BLOCK, BLOCK, BLOCK,BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK, BLOCK],
    [BLOCK, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY,BLOCK,BLOCK,BLOCK,BLOCK, BLOCK, BLOCK,BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,BLOCK,BLOCK,BLOCK,BLOCK, BLOCK, BLOCK,BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,BLOCK,BLOCK,BLOCK,BLOCK, BLOCK, BLOCK,BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY,BLOCK,BLOCK,BLOCK,BLOCK, BLOCK, BLOCK,BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,BLOCK,BLOCK,BLOCK,BLOCK, BLOCK, BLOCK,BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, WATER, WATER,BLOCK,BLOCK,BLOCK,BLOCK, BLOCK, BLOCK,BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK, BLOCK],
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY,BLOCK,BLOCK,BLOCK,BLOCK, BLOCK, BLOCK,BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,BLOCK,BLOCK,BLOCK,BLOCK, BLOCK, BLOCK,BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY,BLOCK,BLOCK,BLOCK,BLOCK, BLOCK, BLOCK,BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK,BLOCK, BLOCK, BLOCK,BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, EMPTY, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK,BLOCK, BLOCK, BLOCK,BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK,BLOCK, BLOCK, BLOCK,BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK,BLOCK, BLOCK, BLOCK,BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK,BLOCK, BLOCK, BLOCK,BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK, BLOCK],
    [BLOCK, BLOCK, BLOCK, FOGO, FOGO, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK, BLOCK],
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK, BLOCK,BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK,BLOCK,BLOCK,BLOCK],
]

# Define estados possíveis do jogador
STILL = 0
JUMPING = 1
FALLING = 2
# Class que representa os blocos do cenário
class Tile(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, tile_img, row, column):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        # Aumenta o tamanho do tile.
        tile_img = pygame.transform.scale(tile_img, (TILE_SIZE, TILE_SIZE))
        # Define a imagem do tile.
        self.image = tile_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        # Posiciona o tile
        self.rect.x = TILE_SIZE * column
        self.rect.y = TILE_SIZE * row


# Carrega os sons do jogo
'''pygame.mixer.music.load('assets/snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')
pygame.mixer.music.set_volume(0.4)
assets['pega_queijo'] = pygame.mixer.Sound('assets/snd/expl3.wav')
assets['passar de fase'] = pygame.mixer.Sound('assets/snd/expl6.wav')
assets['score'] = pygame.mixer.Sound('assets/snd/pew.wav')'''


class Rato1(pygame.sprite.Sprite):
    def __init__(self,player_img,row,column,blocks,fogo,water):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.state = STILL
        self.blocks = blocks
        self.fogo = fogo
        self.water = water
        # row é o índice da linha embaixo do personagem
        self.rect.x = column * TILE_SIZE
        self.rect.bottom = row * TILE_SIZE
        self.speedx = 0
        self.speedy = 0

        #self.groups = groups
        self.assets = assets

    def update(self):
        # Tenta andar em y
        # Atualiza a velocidade aplicando a aceleração da gravidade
        self.speedy += GRAVITY
        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = FALLING
        # Atualiza a posição y
        self.rect.y += self.speedy
        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para baixo
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL
            # Estava indo para cima
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL
        # Tenta andar em x
        self.rect.x += self.speedx
        # Corrige a posição caso tenha passado do tamanho da janela
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right >= WIDTH:
            self.rect.right = WIDTH - 1
        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para a direita
            if self.speedx > 0:
                self.rect.right = collision.rect.left
            # Estava indo para a esquerda
            elif self.speedx < 0:
                self.rect.left = collision.rect.right
        # Método que faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING

class Rato2(pygame.sprite.Sprite):
    def __init__(self,player2_img,row, column, blocks,fogo,water):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = player2_img
        self.rect = self.image.get_rect()
        self.state = STILL
        self.blocks = blocks
        self.fogo = fogo
        self.water = water
        # row é o índice da linha embaixo do personagem
        self.rect.x = column * TILE_SIZE
        self.rect.bottom = row * TILE_SIZE
        self.speedx = 0
        self.speedy = 0

        #self.groups = groups
        self.assets = assets

    def update(self):
        # Tenta andar em y
        # Atualiza a velocidade aplicando a aceleração da gravidade
        self.speedy += GRAVITY
        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = FALLING
        # Atualiza a posição y
        self.rect.y += self.speedy
        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para baixo
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL
            # Estava indo para cima
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL
        # Tenta andar em x
        self.rect.x += self.speedx
        # Corrige a posição caso tenha passado do tamanho da janela
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right >= WIDTH:
            self.rect.right = WIDTH - 1
        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para a direita
            if self.speedx > 0:
                self.rect.right = collision.rect.left
            # Estava indo para a esquerda
            elif self.speedx < 0:
                self.rect.left = collision.rect.right
        # Método que faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING
def load_assets(img_dir):
    assets = {}
    assets['background'] = pygame.image.load('assets/img/mapa.png').convert()
    assets['background'] = pygame.transform.scale(assets['background'],(WIDTH,HEIGHT))
    assets['rato1'] = pygame.image.load('assets/img/rato1.png').convert_alpha()
    assets['rato1'] = pygame.transform.scale(assets['rato1'],(RATO_WIDTH, RATO_HEIGHT))
    assets['rato2'] = pygame.image.load('assets/img/rato2.png').convert_alpha()
    assets['rato2'] = pygame.transform.scale(assets['rato2'],(RATO_WIDTH, RATO_HEIGHT))
    assets['queijo'] = pygame.image.load('assets/img/queijo.png').convert_alpha()
    assets['queijo'] = pygame.transform.scale(assets['queijo'],(QUEIJO_WIDTH, QUEIJO_HEIGHT))
    assets[BLOCK] = pygame.image.load(path.join(img_dir, 'block.png')).convert()
    assets[FOGO] = pygame.image.load(path.join(img_dir, 'fogo.png')).convert()
    assets[WATER] = pygame.image.load(path.join(img_dir, 'water.png')).convert()
    return assets





clock = pygame.time.Clock()
def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock.tick(FPS)

    # Carrega assets
    assets = load_assets(img_dir)

    # Cria um grupo de todos os sprites.
    all_sprites = pygame.sprite.Group()
    # Cria um grupo somente com os sprites de bloco.
    # Sprites de block são aqueles que impedem o movimento do jogador
    blocks = pygame.sprite.Group()
    fogo = pygame.sprite.Group()
    water = pygame.sprite.Group()

    
    #groups = {}
    #groups['all_sprites'] = all_sprites
    # Cria Sprite do jogador
    player = Rato1(assets['rato1'], 12, 2, blocks,fogo,water)
    player2 = Rato2(assets['rato2'], 12, 2, blocks,fogo,water)

    # Cria tiles de acordo com o mapa
    for row in range(len(MAP)):
        for column in range(len(MAP[row])):
            tile_type = MAP[row][column]
            if tile_type == BLOCK:
                tile = Tile(assets[tile_type], row, column)
                all_sprites.add(tile)
                blocks.add(tile)
            if tile_type == FOGO:
                tile = Tile(assets[tile_type], row, column)
                all_sprites.add(tile)
                fogo.add(tile)
            if tile_type == WATER:
                tile = Tile(assets[tile_type], row, column)
                all_sprites.add(tile)
                water.add(tile)
            
            

    all_sprites.add(player,player2)













    PLAYING = 0
    DONE = 1

    state = PLAYING
    while state != DONE:
        assets = load_assets(img_dir)
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player.speedx -= 8
                if event.key == pygame.K_RIGHT:
                    player.speedx += 8
                if event.key == pygame.K_a:
                    player2.speedx -= 8
                if event.key == pygame.K_d:
                    player2.speedx += 8
                elif event.key == pygame.K_UP:
                    player.jump()
                elif event.key == pygame.K_w:  
                    player2.jump()
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player.speedx += 8
                if event.key == pygame.K_RIGHT:
                    player.speedx -= 8
                if event.key == pygame.K_a:
                    player2.speedx += 8
                if event.key == pygame.K_d:
                    player2.speedx -= 8
        
        all_sprites.update()
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        all_sprites.draw(screen)
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        #window.blit(assets['rato1'], (10, 10))
        #window.blit(assets['rato2'], (10, 10))
        #window.blit(assets['background'], (0, 0))
        pygame.display.update() 
    # Nome do jogo
pygame.display.set_caption(TITULO)
# Imprime instruções
print('*' * len(TITULO))
print(TITULO.upper())
print('*' * len(TITULO))
print('Utilize as setas do teclado para andar e pular.')
# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()

