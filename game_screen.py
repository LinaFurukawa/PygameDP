import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, BLUE, RED, WHITE
from assets import carrega_arquivos
from config import SND_DIR
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

    n = 1
    lista_imagens = gerar_imagens(n)
    sorteada = random.choice(lista_imagens)
    resposta_jogador = ''
    pontuacao = 0

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
        if agora - tempo_da_ultima_mudanca > 4000:
            tempo_da_ultima_mudanca = agora
            if tela == 'azul':
                tela = 'vermelha'
                
            else:
                tela = 'azul'

                if resposta_jogador == str(conta_sorteada(lista_imagens, sorteada)):
                    pontuacao += 100
    
                lista_imagens = gerar_imagens(n)
                n += 1
                resposta_jogador = ''
                sorteada = random.choice(lista_imagens)

        if tela == 'azul':
    
            # Desenha as imagens na tela
            for imagem in lista_imagens:
                window.blit(imagem["imagem"], (imagem["posicao_x"], imagem["posicao_y"]))

        else:
            window.fill(WHITE)
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
            if resposta_jogador == str(conta_sorteada(lista_imagens, sorteada)):
                text_surface = dicionario_de_arquivos['font'].render('Acertou!', True, BLUE)
                text_rect = text_surface.get_rect()
                text_rect.centerx = WIDTH / 2
                text_rect.centery = HEIGHT / 2 + 100
                window.blit(text_surface, text_rect)
                dicionario_de_arquivos['good_sound'].play()
                

            else:
                text_surface = dicionario_de_arquivos['font'].render('Errou!', True, BLUE)
                text_rect = text_surface.get_rect()
                text_rect.centerx = WIDTH / 2
                text_rect.centery = HEIGHT / 2 + 100
                window.blit(text_surface, text_rect)

        text_pontuacao = dicionario_de_arquivos['font'].render(str(pontuacao), True, BLUE)
        text_pont_rect = text_pontuacao.get_rect()
        text_pont_rect.centerx = WIDTH / 2
        text_pont_rect.centery = HEIGHT - 50
        window.blit(text_pontuacao, text_pont_rect)
        
        pygame.display.update()  # Mostra o novo frame para o jogador

    return state