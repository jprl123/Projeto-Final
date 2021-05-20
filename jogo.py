# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
WIDTH = 1280
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello World!')

# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
RATO_WIDTH = 150 
RATO_HEIGHT = 138
assets = {}
assets['background'] = pygame.image.load('assets/img/back.png').convert()
assets['rato'] = pygame.image.load('assets/img/rato.png').convert_alpha()
assets['rato'] = pygame.transform.scale(assets['rato'],(RATO_WIDTH, RATO_HEIGHT))

# Carrega os sons do jogo
'''pygame.mixer.music.load('assets/snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')
pygame.mixer.music.set_volume(0.4)
assets['pega_queijo'] = pygame.mixer.Sound('assets/snd/expl3.wav')
assets['passar de fase'] = pygame.mixer.Sound('assets/snd/expl6.wav')
assets['score'] = pygame.mixer.Sound('assets/snd/pew.wav')'''

class Rato(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['rato']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.groups = groups
        self.assets = assets

    def update(self):
        # Atualização da posição
        self.rect.x += self.speedx
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

# Criando o jogador
all_sprites = pygame.sprite.Group()
groups = {}
groups['all_sprites'] = all_sprites
player = Rato(groups, assets)
all_sprites.add(player)




clock = pygame.time.Clock()
FPS = 60
# ===== Loop principal =====
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx -= 8
            if event.key == pygame.K_RIGHT:
                player.speedx += 8
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx += 8
            if event.key == pygame.K_RIGHT:
                player.speedx -= 8




    all_sprites.update()
    # ----- Gera saídas
    window.fill((0, 0, 0)) 
    window.blit(assets['rato'], (10, 10))
    window.blit(assets['background'], (0, 0))
    all_sprites.draw(window)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados