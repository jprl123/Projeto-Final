import pygame
from os import path
import os
from config  import *


#define os assets e guarda em um dicionario
def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(path.join(img_dir, 'mapa.png')).convert()
    assets[BACKGROUND] = pygame.transform.scale(assets[BACKGROUND],(WIDTH,HEIGHT))
    assets[RATO1] = pygame.image.load(path.join(img_dir, 'rato1.png')).convert_alpha()
    assets[RATO1] = pygame.transform.scale(assets[RATO1],(RATO_WIDTH, RATO_HEIGHT))
    assets[RATO2] = pygame.image.load(path.join(img_dir, 'rato2.png')).convert_alpha()
    assets[RATO2] = pygame.transform.scale(assets[RATO2],(RATO_WIDTH, RATO_HEIGHT))
    assets[QUEIJO] = pygame.image.load(path.join(img_dir, 'queijo.png')).convert_alpha()
    assets[QUEIJO] = pygame.transform.scale(assets[QUEIJO],(QUEIJO_WIDTH, QUEIJO_HEIGHT))
    assets[BLOCK] = pygame.image.load(path.join(img_dir, 'block.png')).convert()
    assets[FOGO] = pygame.image.load(path.join(img_dir, 'fogo.png')).convert()
    assets[WATER] = pygame.image.load(path.join(img_dir, 'water.png')).convert()
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(font_dir, 'PressStart2P.ttf'), 30)
    assets[MENU] = pygame.image.load(path.join(img_dir, 'Menu inicial.png')).convert()
    assets[MENU] = pygame.transform.scale(assets[MENU],(WIDTH,HEIGHT))
    assets[TUTORIAL] = pygame.image.load(path.join(img_dir, 'tutorial.png')).convert()
    assets[TUTORIAL] = pygame.transform.scale(assets[TUTORIAL],(WIDTH,HEIGHT))
    assets[PORTAV] = pygame.image.load(path.join(img_dir, 'ratoV.png')).convert_alpha()
    assets[PORTAV] = pygame.transform.scale(assets[PORTAV],(PORTAV_WIDTH,PORTAV_HEIGHT))
    assets[OVER_FONT] = pygame.font.Font(os.path.join(font_dir, 'PressStart2P.ttf'), 30)
    assets[RATO1_ESP] = pygame.image.load(path.join(img_dir, 'rato1(ani(e).png')).convert_alpha()
    assets[RATO1_ESP] = pygame.transform.scale(assets[RATO1_ESP],(RATO_WIDTH, RATO_HEIGHT))
    assets[RATO2_ESP] = pygame.image.load(path.join(img_dir, 'rato2(ani(e).png')).convert_alpha()
    assets[RATO2_ESP] = pygame.transform.scale(assets[RATO2_ESP],(RATO_WIDTH, RATO_HEIGHT))
    assets[BACKGROUND2] = pygame.image.load(path.join(img_dir, 'mapa2.png')).convert()
    assets[BACKGROUND2] = pygame.transform.scale(assets[BACKGROUND2],(WIDTH,HEIGHT))
    assets[TELATRANSI] = pygame.image.load(path.join(img_dir, 'gameWO.png')).convert()
    assets[TELATRANSI] = pygame.transform.scale(assets[TELATRANSI],(WIDTH,HEIGHT))
    # Carrega os sons do jogo
    pygame.mixer.music.load(os.path.join(snd_dir, 'Tetris.ogg'))
    pygame.mixer.music.set_volume(0.05)
    assets[JUMP] = pygame.mixer.Sound(os.path.join(snd_dir, 'jump.wav'))
    assets[PEGA_QUEIJO] = pygame.mixer.Sound(os.path.join(snd_dir, 'rapaz.wav'))
    return assets

