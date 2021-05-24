# ===== Inicialização =====
# ----- Importa e inicia pacotes
from mapas import *
import pygame
from config  import *
from assets import *
pygame.init()

# ----- Gera tela principal

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('O rato e a rata')


# ----- Inicia estruturas de dados
game = True

# Define o mapa com os tipos de tiles
MAP = mapa_3

# Define estados possíveis do jogador
STILL = 0
JUMPING = 1
FALLING = 2
# Class que representa os blocos do cenário
class Tile(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, tile_img, x, y):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        # Aumenta o tamanho do tile.
        tile_img = pygame.transform.scale(tile_img, (TILE_SIZE, TILE_SIZE))
        # Define a imagem do tile.
        self.image = tile_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        # Posiciona o tile
        self.rect.x = TILE_SIZE * y
        self.rect.y = TILE_SIZE * x


class Rato1(pygame.sprite.Sprite):
    def __init__(self,player_img,x,y,blocks,fogo,water):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.state = STILL
        self.blocks = blocks
        self.fogo = fogo
        self.water = water
        # row é o índice da linha embaixo do personagem
        self.rect.x = y * TILE_SIZE
        self.rect.bottom = x * TILE_SIZE
        self.speedx = 0
        self.speedy = 0

        #self.groups = groups
        #self.assets = assets

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
        #colisão para quando tocar no agua
        hitagua = pygame.sprite.spritecollide(self,self.water, False)
        for collision1 in hitagua:
            print('colidiu')
            # Estava indo para baixo
            self.rect.x = 2 * TILE_SIZE
            self.rect.y = 2 * TILE_SIZE


    
        # Método que faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING

class Rato2(pygame.sprite.Sprite):
    def __init__(self,player2_img,x,y,blocks,fogo,water):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = player2_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.state = STILL
        self.blocks = blocks
        self.fogo = fogo
        self.water = water
        # row é o índice da linha embaixo do personagem
        self.rect.x = y * TILE_SIZE
        self.rect.bottom = x * TILE_SIZE
        self.speedx = 0
        self.speedy = 0

        #self.groups = groups
        #self.assets = assets

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
        collisions = pygame.sprite.spritecollide(self,self.blocks,False)
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
        
        #colisão para quando tocar no fogo
        hitfogo = pygame.sprite.spritecollide(self,self.fogo, False)
        for collision2 in hitfogo:
            print('colidiu')
            self.rect.x = 60 * TILE_SIZE
            self.rect.y = 2 * TILE_SIZE

            
        
        # Método que faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING
class Queijo(pygame.sprite.Sprite):
    def __init__(self,queijo_img, x, y):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = queijo_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.midtop = (WIDTH / 2,  1000)

    def update(self):    
        if pygame.sprite.collide_rect(self, Rato1, Rato2):
        #check what kind of box it was
            if self.image == 'score':
                self.score += 100
            self.kill()            
          




clock = pygame.time.Clock()
def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock.tick(FPS)

    # Carrega assets
    assets = load_assets()

    # Cria um grupo de todos os sprites.
    all_sprites = pygame.sprite.Group()
    # Cria um grupo somente com os sprites de bloco.
    # Sprites de block são aqueles que impedem o movimento do jogador
    groups = {}
    groups['all_sprites'] = all_sprites
    blocks = pygame.sprite.Group()
    fogo = pygame.sprite.Group()
    water = pygame.sprite.Group()
    Queijo_group = pygame.sprite.Group() 
    Queijo_group.update()
    


    # Cria Sprite do jogador
    player1 = Rato1(assets[RATO1], 5, 2, blocks,fogo,water)
    player2 = Rato2(assets[RATO2], 5, 62, blocks,fogo,water)  # onde spawna

    # Cria os blocos de acordo com o mapa
    for x in range(len(MAP)):
        for y in range(len(MAP[x])):
            tile_type = MAP[x][y]
            if tile_type == BLOCK:
                tile = Tile(assets[tile_type], x, y)
                all_sprites.add(tile)
                blocks.add(tile)
            elif tile_type == FOGO:
                tile = Tile(assets[tile_type], x, y)
                all_sprites.add(tile)
                fogo.add(tile)
            elif tile_type == WATER:
                tile = Tile(assets[tile_type], x, y)
                all_sprites.add(tile)
                water.add(tile)
            
    all_sprites.add(player1,player2)

    #if len(Rato2.update())


    PLAYING = 0
    DONE = 1
    score = 0
    state = PLAYING
    pygame.mixer.music.play(loops=-1)
    while state != DONE:
        assets = load_assets()
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            # Só verifica o teclado se está no estado de jogo
            if state == PLAYING:
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_LEFT:
                        player1.speedx -= 8
                    if event.key == pygame.K_RIGHT:
                        player1.speedx += 8
                    if event.key == pygame.K_a:
                        player2.speedx -= 8
                    if event.key == pygame.K_d:
                        player2.speedx += 8
                    elif event.key == pygame.K_UP:
                        player1.jump()
                    elif event.key == pygame.K_w:  
                        player2.jump()
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_LEFT:
                        player1.speedx += 8
                    if event.key == pygame.K_RIGHT:
                        player1.speedx -= 8
                    if event.key == pygame.K_a:
                        player2.speedx += 8
                    if event.key == pygame.K_d:
                        player2.speedx -= 8
            
        all_sprites.update()

    
        # A cada loop, redesenha o fundo e os sprites
        #atualiza a tela
        screen.fill(BLACK)  
        screen.blit(assets[BACKGROUND], (0, 0))
        all_sprites.draw(screen)
        
        #desenhando o score
        text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, BLUE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  1000)
        screen.blit(text_surface, text_rect)
        

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        pygame.display.update() 
try:
    game_screen(screen)
finally:
    pygame.quit()