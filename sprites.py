import pygame
import os
from config import IMG_DIR

class Botao(pygame.sprite.Sprite):
    def __init__(self, assets, nome_do_jogo):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.assets = assets
        self.image = assets['btn'] # assets é um dicionário de imagens, sons e fonts 
        self.mask = pygame.mask.from_surface(self.image)
        #todo objeto precisa de um rect
        # rect é a representação de retangulo feita pelo pygame
        self.rect = self.image.get_rect()
        # é preciso definir onde a imagem deve aparecer no jogo
        self.rect.x = 0
        self.rect.y = 0

        self.nome_do_jogo = nome_do_jogo

    def mouse_over(self, over):
        # Toda a lógica de movimentação deve ser feita aqui
        # Atualização da posição da nave
        if over:
            self.image = self.assets['btn_hover']
        else:
            self.image = self.assets['btn']

class Cherry(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load(os.path.join(IMG_DIR, 'cherries.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))  # Redimensiona a imagem
        self.rect = self.image.get_rect(topleft=position)

class Flower(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load(os.path.join(IMG_DIR, 'flower.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))  # Redimensiona a imagem
        self.rect = self.image.get_rect(topleft=position)
    
class Tree(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load(os.path.join(IMG_DIR, 'tree.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))  # Redimensiona a imagem
        self.rect = self.image.get_rect(topleft=position)

class Fruit(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load(os.path.join(IMG_DIR, 'fruit-tree.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))  # Redimensiona a imagem
        self.rect = self.image.get_rect(topleft=position)

class Ladybug(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load(os.path.join(IMG_DIR, 'ladybug.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))  # Redimensiona a imagem
        self.rect = self.image.get_rect(topleft=position)

