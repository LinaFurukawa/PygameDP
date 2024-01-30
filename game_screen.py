import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, BLUE, RED
from assets import carrega_arquivos
from funcoes import gerar_imagens,  conta_sorteada
import random

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()

    DONE = 0
    PLAYING = 1
    state = PLAYING

    tela = 'azul'
    tempo_da_ultima_mudanca = pygame.time.get_ticks()

    lista_imagens = gerar_imagens(2)
    resposta_jogador = ''

    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            if event.type == pygame.KEYDOWN:
                resposta_jogador += event.unicode
                

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca

        # Lógica para alternar as cores
        agora = pygame.time.get_ticks()
        if agora - tempo_da_ultima_mudanca > 2000:
            tempo_da_ultima_mudanca = agora
            if tela == 'azul':
                tela = 'vermelha'
            else:
                tela = 'azul'

        if tela == 'azul':
            window.fill(BLUE)

            sorteada = random.choice(lista_imagens)
            
            resposta_jogador = ''

            # Desenha as imagens na tela
            for imagem in lista_imagens:
                window.blit(imagem["imagem"], (imagem["posicao_x"], imagem["posicao_y"]))


        else:
            window.fill(RED)
            # Dimensões do retângulo
            rect_width = WIDTH / 2
            rect_height = HEIGHT / 4

            # Posição do retângulo
            rect_x = (WIDTH - rect_width) / 2
            rect_y = (HEIGHT - rect_height) / 2

            # Desenha um retângulo centralizado na tela, perguntando a quantidade da imagem que apareceu
            pygame.draw.rect(window, BLACK, (rect_x, rect_y, rect_width, rect_height))

            # Adiciona um texto sobrepondo o retângulo
            text_surface = dicionario_de_arquivos['font'].render('Quantos ?', True, BLUE)
            text_rect = text_surface.get_rect()
            text_rect.centerx = WIDTH / 2
            text_rect.centery = HEIGHT / 2 - 100
            window.blit(text_surface, text_rect)

            # Adiciona a imagem do tipo que apareceu

            window.blit(sorteada["imagem"], (WIDTH / 2 + 100, HEIGHT / 2 - 130))

            text_surface = dicionario_de_arquivos['font'].render(resposta_jogador, True, BLUE)
            text_rect = text_surface.get_rect()
            text_rect.centerx = WIDTH / 2
            text_rect.centery = HEIGHT / 2
            window.blit(text_surface, text_rect)

            # Verifica se o jogador acertou a quantidade de imagens
            contagem = str(conta_sorteada(lista_imagens, sorteada))
            
            if resposta_jogador == contagem:
                text_surface = dicionario_de_arquivos['font'].render('Acertou!', True, BLUE)
                text_rect = text_surface.get_rect()
                text_rect.centerx = WIDTH / 2
                text_rect.centery = HEIGHT / 2 + 100
                window.blit(text_surface, text_rect)


            else:
                text_surface = dicionario_de_arquivos['font'].render('Errou!', True, BLUE)
                text_rect = text_surface.get_rect()
                text_rect.centerx = WIDTH / 2
                text_rect.centery = HEIGHT / 2 + 100
                window.blit(text_surface, text_rect)



        pygame.display.update()  # Mostra o novo frame para o jogador

    return state