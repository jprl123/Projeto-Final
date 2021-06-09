import pygame
from mapas import *
from config  import *
from assets import *
import random
from sprites import *

#pygame.init()
# Define o mapa com os tipos de tiles
fase = Fase()
#pygame.mixer.init()

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
    porta_group = pygame.sprite.Group()
    
    # define o mapa que esta sendo jogado
    MAP = fase.excel_txt2mapa('mapa1.txt')

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
    
    
    
    while len(porta_group) <= 1:
        x = (28)
        y = (29)
        if MAP[x][y] == EMPTY:
            P = Portav(assets[PORTAV], x*TILE_SIZE, y*TILE_SIZE)
            porta_group.add(P)
            all_sprites.add(P)
            P = Portav(assets[PORTAV], WIDTH-x*TILE_SIZE, y*TILE_SIZE) # espelha do outro lado do mapa
            porta_group.add(P)
            all_sprites.add(P)    
    


    # Cria Sprite do jogador
    player1 = Rato1(assets[RATO1_ESP], 5, 60, blocks,fogo,water)
    player2 = Rato2(assets[RATO2], 5, 5, blocks,fogo,water)  # onde spawna

    
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
    QDONE = 2
    estado = PLAYING
    score = 0

    
    pygame.mixer.music.play(loops=-1)
    while estado != DONE:
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
                        player1.image = assets[RATO1_ESP]
                    if event.key == pygame.K_RIGHT:
                        player1.speedx += SPEED_X
                        player1.image = assets[RATO1]
                    if event.key == pygame.K_a:
                        player2.speedx -= SPEED_X
                        player2.image = assets[RATO2_ESP]
                    if event.key == pygame.K_d:
                        player2.speedx += SPEED_X
                        player2.image = assets[RATO2]
                    elif event.key == pygame.K_UP:
                        player1.jump()
                        assets[JUMP].play()
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
            


        all_sprites.update()

        hit1=pygame.sprite.spritecollide(player1,Queijo_group, True)
        if len(hit1) > 0:
            score+=100
            assets[PEGA_QUEIJO].play()
        hit2=pygame.sprite.spritecollide(player2,Queijo_group, True)
        if len(hit2) > 0: 
            score+=100
            assets[PEGA_QUEIJO].play() 

        hitagua = pygame.sprite.spritecollide(player1,water, False)
        for c1 in hitagua:
            #self.rect.x = 60 * TILE_SIZE
            #self.rect.y = 2 * TILE_SIZE
            estado = QDONE
            print('adad')
            return OVER,score
        
        hitfogo = pygame.sprite.spritecollide(player2,fogo, False)
        for c2 in hitfogo:
            player2.rect.x = 2 * TILE_SIZE
            player2.rect.y = 2 * TILE_SIZE
            player2.kill()
            estado = QDONE
            return OVER,score

            




        # verifica o hit com a porta e verifica se os 2 estão sobre elas
        hit4=pygame.sprite.spritecollide(player2,porta_group, False)
        hit3=pygame.sprite.spritecollide(player1,porta_group, False)
        if len(hit3) > 0 and len(hit4)>0:
                # limpa o mapa
                porta_group.empty()
                Queijo_group.empty()
                all_sprites.empty()
                all_sprites.empty()
                estado = PASSOU
                
                

        
        
        

    
        if estado == PLAYING:

            # redesenha o fundo
            screen.fill(BLACK)  
            screen.blit(assets[BACKGROUND], (0, 0))

            #desenhando o score
            score_text = assets[SCORE_FONT].render("{:08d}".format(score), True, BLUE)
            text_rect = score_text.get_rect()
            text_rect.midtop = (200,950)
            screen.blit(score_text, text_rect)

        # redesenha as sprites   
        all_sprites.draw(screen)

        if estado == PASSOU:
            return 1, score
        

        # Depois de desenhar tudo, inverte o display.
        pygame.display.update()
    return SAIR,score    