import pygame
from config import *
from assets import *
import random
from mapas import *



# Define estados possíveis do jogador
PARADO = 0
PULANDO = 1
CAINDO = 2
#representa os blocos do cenário
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
        # Posiciona
        self.rect.x = TILE_SIZE * y
        self.rect.y = TILE_SIZE * x


class Rato1(pygame.sprite.Sprite):
    def __init__(self,player_img,x,y,blocks,fogo,water):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.state = PARADO
        self.blocks = blocks
        self.fogo = fogo
        self.water = water
        self.rect.x = y * TILE_SIZE
        self.rect.bottom = x * TILE_SIZE
        self.speedx = 0
        self.speedy = 0
    def update(self):
        # Atualiza a velocidade aplicando a aceleração da gravidade
        self.speedy += GRAVITY
        # faz com que o rato não execute um double jump
        if self.speedy > 0:
            self.state = CAINDO
        # Atualiza a posição 
        self.rect.y += self.speedy
        # Se colidiu com algum bloco, volta para antes 
        hitbloco = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for c in hitbloco:
            # Estava indo para baixo
            if self.speedy > 0:
                self.rect.bottom = c.rect.top
                # Se colidiu para de cair
                self.speedy = 0
                self.state = PARADO
            # Estava indo para cima
            elif self.speedy < 0:
                self.rect.top = c.rect.bottom
                # Se colidiu para de cair
                self.speedy = 0
                self.state = PARADO
        # Tenta andar em x
        self.rect.x += self.speedx
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        hitbloco = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for c in hitbloco:
            # Estava indo para a direita
            if self.speedx > 0:
                self.rect.right = c.rect.left
            # Estava indo para a esquerda
            elif self.speedx < 0:
                self.rect.left = c.rect.right
        #colisão para quando tocar no agua
        hitagua = pygame.sprite.spritecollide(self,self.water, False)
        for c1 in hitagua:
            self.rect.x = 60 * TILE_SIZE
            self.rect.y = 2 * TILE_SIZE


        # Método que faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == PARADO:
            self.speedy -= JUMP_SIZE
            self.state = PULANDO

class Rato2(pygame.sprite.Sprite): # rato agua
    def __init__(self,player2_img,x,y,blocks,fogo,water):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = player2_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.state = PARADO
        self.blocks = blocks
        self.fogo = fogo
        self.water = water
        self.rect.x = y * TILE_SIZE
        self.rect.bottom = x * TILE_SIZE
        self.speedx = 0
        self.speedy = 0

    def update(self):
        # Tenta andar em y
        # Atualiza a velocidade aplicando a aceleração da gravidade
        self.speedy += GRAVITY
        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = CAINDO
        # Atualiza a posição y
        self.rect.y += self.speedy
        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        hitbloco = pygame.sprite.spritecollide(self,self.blocks,False)
        # Corrige a posição do personagem para antes da colisão
        for c in hitbloco:
            # Estava indo para baixo
            if self.speedy > 0:
                self.rect.bottom = c.rect.top
                # Se colidiu para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = PARADO
            # Estava indo para cima
            elif self.speedy < 0:
                self.rect.top = c.rect.bottom
                # Se colidiu para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = PARADO
        # Tenta andar em x
        self.rect.x += self.speedx
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        hitbloco = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for c in hitbloco:
            # verifica os hits em x
            if self.speedx > 0:
                self.rect.right = c.rect.left
            elif self.speedx < 0:
                self.rect.left = c.rect.right
        
        #colisão para quando tocar no fogo
        hitfogo = pygame.sprite.spritecollide(self,self.fogo, False)
        for c2 in hitfogo:
            self.rect.x = 2 * TILE_SIZE
            self.rect.y = 2 * TILE_SIZE
            
          
    #faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == PARADO:
            self.speedy -= JUMP_SIZE
            self.state = PULANDO
            
class Queijo(pygame.sprite.Sprite):
    def __init__(self,queijo_img, x, y):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = queijo_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.midtop = (x,y)
    def update(self):
        pass

class Portav(pygame.sprite.Sprite):
    def __init__(self,portav_img, x, y):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = portav_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.midtop = (x,y)
    def update(self):
        pass   
