import pygame
from mapas import *
from config  import *
from assets import *
import random
from sprites import *


# Define o mapa com os tipos de tiles
fase = Fase()


def game_screen(screen):
    clock = pygame.time.Clock()
    # Carrega assets
    assets = load_assets()
    # Cria um grupo de todos os sprites.
    all_sprites = pygame.sprite.Group()
    all_maps = pygame.sprite.Group() 
    # Cria um grupo somente com os sprites de bloco.
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_maps'] = all_maps
    blocks = pygame.sprite.Group()
    fogo = pygame.sprite.Group()
    water = pygame.sprite.Group()
    Queijo_group = pygame.sprite.Group() 
    porta_group = pygame.sprite.Group()
    

    MAP = fase.mapa

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
    player1 = Rato1(assets[RATO1], 5, 62, blocks,fogo,water)
    player2 = Rato2(assets[RATO2], 5, 1, blocks,fogo,water)  # onde spawna

    
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
                #pygame.mixer.music.play(loops=-1)
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
            
            
            if estado == QDONE:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_screen(screen) 
        
        
        
        score_text = assets[SCORE_FONT].render("{:08d}".format(score), True, BLUE)
        score_over = assets[OVER_FONT].render("{:08d}".format(score), True, BLUE)
        textoover1 = assets[OVER_FONT].render('Aperte ESPAÇO para reiniciar o jogo', True, BLUE)
        gameover = assets[SCORE_FONT].render('GAME OVER', True, BLUE)




        




        all_sprites.update()
        all_maps.update()

        hit1=pygame.sprite.spritecollide(player1,Queijo_group, True)
        if len(hit1) > 0:
            score+=100
            assets[PEGA_QUEIJO].play()
        hit2=pygame.sprite.spritecollide(player2,Queijo_group, True)
        if len(hit2) > 0: 
            score+=100
            assets[PEGA_QUEIJO].play() 
            estado = QDONE

        hit4=pygame.sprite.spritecollide(player2,porta_group, False)
        hit3=pygame.sprite.spritecollide(player1,porta_group, False)
        if len(hit3) > 0 and len(hit4)>0:
            if not passou_de_fase:
                porta_group.empty()
                Queijo_group.empty()
                all_sprites.empty()
                fase.avancar_fase()
                MAP = fase.mapa
                # Cria os blocos de acordo com o mapa
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
                        print(f'fase: {fase.fase}')
                all_sprites.update()
                pygame.display.update() 
                passou_de_fase = True
        
        
        
        elif estado == QDONE:
            player1.kill()
            player2.kill()


        
        
        

        # A cada loop, redesenha o fundo e os sprites
        if estado == PLAYING:
            screen.fill(BLACK)  
            screen.blit(assets[BACKGROUND], (0, 0))
            score_text = assets[SCORE_FONT].render("{:08d}".format(score), True, BLUE)
            text_rect = score_text.get_rect()
            text_rect.midtop = (WIDTH / 2, 1000)
            screen.blit(score_text, text_rect)
        if estado == QDONE:
            all_sprites.empty()
            screen.fill(BLACK)
            screen.blit(gameover,   (860, 240))
            screen.blit(score_over, (860, 540))
            screen.blit(textoover1, (860, 740))    
        all_sprites.draw(screen)

        
        #desenhando o score
        
        

        # Depois de desenhar tudo, inverte o display.
        pygame.display.update() 
