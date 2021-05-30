import pygame
from mapas import *
from config  import *
from assets import *
import random
from sprites import *


# Define o mapa com os tipos de tiles
MAP = Mapa('mapa3.txt').mapa

def game_screen(screen):
    clock = pygame.time.Clock()
    # Carrega assets
    assets = load_assets()
    # Cria um grupo de todos os sprites.
    all_sprites = pygame.sprite.Group()
    # Cria um grupo somente com os sprites de bloco.
    groups = {}
    groups['all_sprites'] = all_sprites
    blocks = pygame.sprite.Group()
    fogo = pygame.sprite.Group()
    water = pygame.sprite.Group()
    Queijo_group = pygame.sprite.Group() 
    
    # cria os queijos no mapa
    while len(Queijo_group) <= 10:
        x = random.randint(2,30)
        y = random.randint(2,15)
        if MAP[x][y] == EMPTY:
            Q = Queijo(assets[QUEIJO], x*TILE_SIZE, y*TILE_SIZE)
            Queijo_group.add(Q)
            all_sprites.add(Q)
            Q = Queijo(assets[QUEIJO], WIDTH-x*TILE_SIZE, y*TILE_SIZE) # espelha do outro lado do mapa
            Queijo_group.add(Q)
            all_sprites.add(Q)
        
    


    # Cria Sprite do jogador
    player1 = Rato1(assets[RATO1], 5, 62, blocks,fogo,water)
    player2 = Rato2(assets[RATO2], 5, 1, blocks,fogo,water)  # onde spawna

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

    PLAYING = 0
    DONE = 1

    estado = PLAYING
    score = 0
    lives = 3
    
    pygame.mixer.music.play(loops=-1)
    while estado != DONE:
        assets = load_assets()
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                estado = DONE
            # Só verifica o teclado se está no estado de jogo
            if estado == PLAYING:
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_LEFT:
                        player1.speedx -= SPEED_X
                    if event.key == pygame.K_RIGHT:
                        player1.speedx += SPEED_X
                    if event.key == pygame.K_a:
                        player2.speedx -= SPEED_X
                    if event.key == pygame.K_d:
                        player2.speedx += SPEED_X
                    elif event.key == pygame.K_UP:
                        player1.jump()
                        assets[JUMP].play()
                        #lives -= 1
                    elif event.key == pygame.K_w:  
                        player2.jump()
                        assets[JUMP].play()
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_LEFT:
                        player1.speedx += SPEED_X
                    if event.key == pygame.K_RIGHT:
                        player1.speedx -= SPEED_X
                    if event.key == pygame.K_a:
                        player2.speedx += SPEED_X
                    if event.key == pygame.K_d:
                        player2.speedx -= SPEED_X
        #verifica se tem vida
        if lives == 0:
                    estado = DONE    
        all_sprites.update()
        
        hit1=pygame.sprite.spritecollide(player1,Queijo_group, True)
        if len(hit1) > 0:
            score+=100
        hit2=pygame.sprite.spritecollide(player2,Queijo_group, True)
        if len(hit2) > 0: 
            score+=100  
            
            
                 

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)  
        screen.blit(assets[BACKGROUND], (0, 0))
        all_sprites.draw(screen)
        
        #desenhando o score
        text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, BLUE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2, 1000)
        screen.blit(text_surface, text_rect)


        # Desenhando as vidas
        text_surface = assets[SCORE_FONT].render(chr(9829) *lives, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2, 970)
        screen.blit(text_surface, text_rect)
        

        # Depois de desenhar tudo, inverte o display.
        pygame.display.update() 
