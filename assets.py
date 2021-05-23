import pygame
from os import path
from config  import *



def load_assets(img_dir):
    assets = {}
    assets[BACKGROUND] = pygame.image.load(path.join(img_dir, 'mapa.png')).convert()
    assets[BACKGROUND] = pygame.transform.scale(assets[BACKGROUND],(WIDTH,HEIGHT))
    assets[RATO1] = pygame.image.load(path.join(img_dir, 'rato1.png')).convert_alpha()
    assets[RATO1] = pygame.transform.scale(assets[RATO1],(RATO_WIDTH, RATO_HEIGHT))
    assets[RATO2] = pygame.image.load(path.join(img_dir, 'rato2.png')).convert_alpha()
    assets[RATO2] = pygame.transform.scale(assets[RATO2],(RATO_WIDTH, RATO_HEIGHT))
    assets[QUEIJO] = pygame.image.load(path.join(img_dir, 'queijo.png')).convert_alpha()
    assets[QUEIJO] = pygame.transform.scale(assets['queijo'],(QUEIJO_WIDTH, QUEIJO_HEIGHT))
    assets[BLOCK] = pygame.image.load(path.join(img_dir, 'block.png')).convert()
    assets[FOGO] = pygame.image.load(path.join(img_dir, 'fogo.png')).convert()
    assets[WATER] = pygame.image.load(path.join(img_dir, 'water.png')).convert()
    # Carrega os sons do jogo
    #pygame.mixer.music.load('assets/snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')
    #pygame.mixer.music.set_volume(0.4)
    #assets['pega_queijo'] = pygame.mixer.Sound('assets/snd/expl3.wav')
    #assets['passar de fase'] = pygame.mixer.Sound('assets/snd/expl6.wav')
    #assets['score'] = pygame.mixer.Sound('assets/snd/pew.wav')
    return assets

