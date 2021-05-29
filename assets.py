import pygame
from os import path
import os
from config  import *



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
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(font_dir, 'PressStart2P.ttf'), 28)
    assets[MENU] = pygame.image.load(path.join(img_dir, 'Menu inicial.png')).convert()
    assets[MENU] = pygame.transform.scale(assets[MENU],(WIDTH,HEIGHT))
    # Carrega os sons do jogo
    pygame.mixer.music.load(os.path.join(snd_dir, 'Tetris.ogg'))
    pygame.mixer.music.set_volume(0.4)
    assets[FASE] = pygame.mixer.Sound(os.path.join(snd_dir, 'uepa.wav'))
    assets[JUMP] = pygame.mixer.Sound(os.path.join(snd_dir, 'jump.wav'))
    #assets[JUMP] = pygame.mixer.Sound(os.path.join(snd_dir, 'rapaz.wav'))
    #assets[PEGA_QUEIJO] = pygame.mixer.Sound('assets/snd/expl3.wav')
    return assets

