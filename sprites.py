import pygame
from config import *
from assets import *





# Define estados possíveis dos personagens 
PARADO = 0
PULANDO = 1
CAINDO = 2


#representa os blocos do cenário
class Tile(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, tile_img, x, y):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        # Ajusta o tamanho
        tile_img = pygame.transform.scale(tile_img, (TILE_SIZE, TILE_SIZE))
        # define a imagem
        self.image = tile_img
        self.rect = self.image.get_rect()
        # Posicionamento do tile
        self.rect.x = TILE_SIZE * y
        self.rect.y = TILE_SIZE * x


class Rato1(pygame.sprite.Sprite): # rato vermelho(fogo)
    def __init__(self,player_img,x,y,blocks,fogo,water):
        
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        #define a imagem
        self.image = player_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        #define o estado inicial
        self.state = PARADO
        #Guarda os Grupos para tratar as colisoes
        self.blocks = blocks
        self.fogo = fogo
        self.water = water

        #posiciona o personagem
        self.rect.x = y * TILE_SIZE
        self.rect.bottom = x * TILE_SIZE

        #definindo as velocidades
        self.speedx = 0
        self.speedy = 0
    def update(self):
        # responsavel pela mecanica da gravidade
        # Atualiza a velocidade ultilizando a gravidade
        self.speedy += GRAVITY
        
        # faz com que o rato não execute um double jump
        if self.speedy > 0:
            self.state = CAINDO
        
        # Atualiza a posição 
        self.rect.y += self.speedy

        # Se colidiu volta para o ponto antes da colisão
        hitbloco = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição para antes da colisão
        for c in hitbloco:
            if self.speedy > 0: # verifica se ele estava indo para baixo
                self.rect.bottom = c.rect.top
                # Se colidiu para de cair
                self.speedy = 0
                #atualiza o estado
                self.state = PARADO
            elif self.speedy < 0: # verifica se ele estava indo para cima
                self.rect.top = c.rect.bottom
                # Se colidiu para de cair
                self.speedy = 0
                #atualiza o estado
                self.state = PARADO
        
        # Tenta andar em x
        self.rect.x += self.speedx
        
        
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        # Se colidiu volta para o ponto antes da colisão
        hitbloco = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição para antes da colisão
        for c in hitbloco:
            # Estava indo para a direita
            if self.speedx > 0:
                self.rect.right = c.rect.left
            # Estava indo para a esquerda
            elif self.speedx < 0:
                self.rect.left = c.rect.right

    # função que faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == PARADO:
            self.speedy -= JUMP_SIZE
            self.state = PULANDO






class Rato2(pygame.sprite.Sprite): #rato azul(agua)
    def __init__(self,player2_img,x,y,blocks,fogo,water):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        #define a imagem
        self.image = player2_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        #define o estado inicial
        self.state = PARADO

        #Guarda os Grupos para tratar as colisoes
        self.blocks = blocks
        self.fogo = fogo
        self.water = water

        #posiciona o personagem
        self.rect.x = y * TILE_SIZE
        self.rect.bottom = x * TILE_SIZE

        #definindo as velocidades
        self.speedx = 0
        self.speedy = 0

        

    def update(self):
        # responsavel pela mecanica da gravidade
        # Atualiza a velocidade ultilizando a gravidade
        self.speedy += GRAVITY
        # Atualiza o estado para caindo
        if self.speedy > 0: #verifica a velocidade
            self.state = CAINDO
        # Atualiza a posição y
        self.rect.y += self.speedy

        # Se colidiu volta para o ponto antes da colisão
        hitbloco = pygame.sprite.spritecollide(self,self.blocks,False)
        # Corrige o personagem para antes da colisão
        for c in hitbloco:
            if self.speedy > 0: # verifica se ele estava indo para baixo
                self.rect.bottom = c.rect.top
                # Se colidiu para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = PARADO
            elif self.speedy < 0: # verifica se ele estava indo para cima
                self.rect.top = c.rect.bottom
                # Se colidiu para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = PARADO
        # Tentar em andar no eixo X
        self.rect.x += self.speedx

        # Mantem dentro da tela 
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        
        # Se colidiu volta para o ponto antes da colisão
        hitbloco = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição para antes da colisão
        # necessario para evitar bugs com o bloco
        for c in hitbloco:
            # verifica os hits em x
            if self.speedx > 0:
                self.rect.right = c.rect.left
            elif self.speedx < 0:
                self.rect.left = c.rect.right

    #faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == PARADO:
            self.speedy -= JUMP_SIZE
            self.state = PULANDO
            

#classe que produz o queio no mapa
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

# classe que cria a porta para passar de nivel
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
