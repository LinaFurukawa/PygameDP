import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR

CHERRIES = 'cherries'
FLOWER = 'flower'
TREE = 'tree'
FRUIT = 'fruit'
LADYBUG = 'ladybug'


def carrega_arquivos():
    dicionario_de_arquivos = {}
    dicionario_de_arquivos['btn'] = pygame.image.load(os.path.join(IMG_DIR, 'btn1.png')).convert()

    larg_tela = 60
    alt_tela = 60


    dicionario_de_arquivos[CHERRIES] = pygame.image.load(os.path.join(IMG_DIR, 'cherries.png')).convert_alpha()
    dicionario_de_arquivos[CHERRIES] = pygame.transform.scale (dicionario_de_arquivos[CHERRIES], (larg_tela, alt_tela))

    dicionario_de_arquivos[FLOWER] = pygame.image.load(os.path.join(IMG_DIR, 'flower.png')).convert_alpha()
    dicionario_de_arquivos[FLOWER] = pygame.transform.scale (dicionario_de_arquivos[FLOWER], (larg_tela, alt_tela))

    dicionario_de_arquivos[TREE] = pygame.image.load(os.path.join(IMG_DIR, 'tree.png')).convert_alpha()
    dicionario_de_arquivos[TREE] = pygame.transform.scale (dicionario_de_arquivos[TREE], (larg_tela, alt_tela))

    dicionario_de_arquivos[FRUIT] = pygame.image.load(os.path.join(IMG_DIR, 'fruit-tree.png')).convert_alpha()
    dicionario_de_arquivos[FRUIT] =  pygame.transform.scale (dicionario_de_arquivos[FRUIT], (larg_tela, alt_tela))

    dicionario_de_arquivos[LADYBUG] = pygame.image.load(os.path.join(IMG_DIR, 'fruit-tree.png')).convert_alpha()
    dicionario_de_arquivos[LADYBUG] = pygame.transform.scale (dicionario_de_arquivos[LADYBUG], (larg_tela, alt_tela))


    #mudando tamanho das imagens
    largura = dicionario_de_arquivos['btn'].get_rect().width * .25
    altura = dicionario_de_arquivos['btn'].get_rect().height * .25
    dicionario_de_arquivos['btn'] = pygame.transform.scale(dicionario_de_arquivos['btn'], (largura, altura))

    dicionario_de_arquivos['btn_hover'] = pygame.image.load(os.path.join(IMG_DIR, 'btn1_hover.png')).convert()
    dicionario_de_arquivos['btn_hover'] = pygame.transform.scale(dicionario_de_arquivos['btn_hover'], (largura, altura))

    #carregando Fonte
    dicionario_de_arquivos['font'] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 22)
    dicionario_de_arquivos['font_media'] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 30)
    return dicionario_de_arquivos
