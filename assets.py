import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR

CHERRIES = 'cherries'
FLOWER = 'flower'
TREE = 'tree'
FRUIT = 'fruit-tree'
LADYBUG = 'ladybug'


def carrega_arquivos():
    dicionario_de_arquivos = {}
    dicionario_de_arquivos['btn'] = pygame.image.load(os.path.join(IMG_DIR, 'btn1.png')).convert()

    larg_imagem = 60
    alt_imagem = 60

    dicionario_de_arquivos[CHERRIES] = pygame.image.load(os.path.join(IMG_DIR, 'cherries.png')).convert_alpha()
    dicionario_de_arquivos[CHERRIES] = pygame.transform.scale (dicionario_de_arquivos[CHERRIES], (larg_imagem, alt_imagem))

    dicionario_de_arquivos[FLOWER] = pygame.image.load(os.path.join(IMG_DIR, 'flower.png')).convert_alpha()
    dicionario_de_arquivos[FLOWER] = pygame.transform.scale (dicionario_de_arquivos[FLOWER], (larg_imagem, alt_imagem))

    dicionario_de_arquivos[TREE] = pygame.image.load(os.path.join(IMG_DIR, 'tree.png')).convert_alpha()
    dicionario_de_arquivos[TREE] = pygame.transform.scale (dicionario_de_arquivos[TREE], (larg_imagem, alt_imagem))

    dicionario_de_arquivos[FRUIT] = pygame.image.load(os.path.join(IMG_DIR, 'fruit-tree.png')).convert_alpha()
    dicionario_de_arquivos[FRUIT] =  pygame.transform.scale (dicionario_de_arquivos[FRUIT], (larg_imagem, alt_imagem))

    dicionario_de_arquivos[LADYBUG] = pygame.image.load(os.path.join(IMG_DIR, 'ladybug.png')).convert_alpha()
    dicionario_de_arquivos[LADYBUG] = pygame.transform.scale (dicionario_de_arquivos[LADYBUG], (larg_imagem, alt_imagem))

    # sons 
    dicionario_de_arquivos['good_sound'] = pygame.mixer.Sound(os.path.join(SND_DIR,'yeah-boy-114748.mp3'))    # quando o jogador acerta a quantidade
    dicionario_de_arquivos['final_sound'] = pygame.mixer.Sound(os.path.join(SND_DIR,'ragtime-logo-standard-version-116100.mp3')) 
    dicionario_de_arquivos['game_sound'] = pygame.mixer.Sound(os.path.join(SND_DIR,'funny-and-comical-melody-glide-synth-bass-and-trumpet-21398.mp3')) 
    dicionario_de_arquivos['bad_sound'] = pygame.mixer.Sound(os.path.join(SND_DIR,'wah-wah.wav')) 

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

    