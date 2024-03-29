import random
import pygame
import os
from assets import carrega_arquivos
from config import WIDTH, HEIGHT

def colisao_entre_retangulos(r1_x,r1_y,r1_w,r1_h,r2_x,r2_y,r2_w,r2_h):

    # Verificar se os retângulos colidem
    if r1_x < r2_x + r2_w and r1_x + r1_w > r2_x and r1_y < r2_y + r2_h and r1_y + r1_h > r2_y:
        return True
    else:
        return False
    
def verifica_colisoes(sprite, all_sprites):

    for outro_sprite in all_sprites:
        if sprite != outro_sprite and pygame.sprite.collide_rect(sprite, outro_sprite):
            return True
    return False

def conta_sorteada(all_sprites, sorteada):

    contagem = 0
    tipo_sorteada = sorteada.__class__.__name__  # Usa o nome da classe como tipo

    for sprite in all_sprites:
        tipo = sprite.__class__.__name__  # Usa o nome da classe como tipo
        if tipo == tipo_sorteada:
            contagem += 1

    return contagem

def salvar_pontuacao(pontuacao):
    try:
        with open('ranking.txt', 'a') as arquivo:
            arquivo.write(f"{pontuacao}\n")
        print(f"Pontuação {pontuacao} salva com sucesso.")
    except Exception as e:
        print("Erro ao salvar pontuação:", e)

def ler_ranking():
    try:
        with open('ranking.txt', 'r') as arquivo:
            pontuacoes = arquivo.readlines()
        pontuacoes = [int(p.strip()) for p in pontuacoes]
        pontuacoes.sort(reverse=True)
        return pontuacoes[:10]
    except Exception as e:
        print("Erro ao ler ranking:", e)
        return []
    
#def gerar_imagens(x):

    lista_imagens = []
    dicionario_de_arquivos = carrega_arquivos()
    tipos_imagens = ['cherries', 'flower', 'fruit-tree', 'ladybug', 'tree']
    imagem_selecionada = random.sample(tipos_imagens, x)

    for tipo in imagem_selecionada:
        quantidade_imagens = random.randint(5, 10)
        for _ in range(quantidade_imagens):
            imagem = sortear_posicao_imagem(tipo, lista_imagens, dicionario_de_arquivos)
            lista_imagens.append(imagem)

    return lista_imagens

#def sortear_posicao_imagem(tipo, lista_imagens, dicionario_de_arquivos):
    while True:
        posicao_x = random.randint(0, WIDTH-100)
        posicao_y = random.randint(0, HEIGHT-100)
        imagem = {
            "imagem": dicionario_de_arquivos[tipo],
            "tipo": tipo,
            "posicao_x": posicao_x,
            "posicao_y": posicao_y
        }
        if not verifica_colisoes(imagem, lista_imagens):
            return imagem