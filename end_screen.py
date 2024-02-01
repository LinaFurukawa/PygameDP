import pygame
import random
from os import path
from sprites import Botao
from config import BLACK, FPS, WIDTH, HEIGHT, RED
from assets import carrega_arquivos
from funcoes import ler_ranking, salvar_pontuacao

def end_game (window, pontuacao):

    clock = pygame.time.Clock()
    ranking = ler_ranking() 

    dicionario_de_arquivos = carrega_arquivos()

    DONE = 0
    PLAYING = 1
    state = PLAYING
    fonte = pygame.font.Font(None, 60)
    fonte_ranking = pygame.font.Font(None, 50)

    while state != DONE:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
        
        window.fill(BLACK)

        texto_pontuacao = f"Pontuação: {pontuacao}"  # Combina texto com a pontuação
        pontuacao_renderizada = fonte.render(texto_pontuacao, True, RED)
        window.blit(pontuacao_renderizada, ((WIDTH - pontuacao_renderizada.get_width()) / 2, HEIGHT / 2 - 300))

        y_pos = 150  # Começando a 150 pixels do topo
        for idx, score in enumerate(ranking[:10]):
            score_text = fonte_ranking.render(f"{idx + 1}. {score}", True, RED)
            window.blit(score_text, (WIDTH / 2 - 100, y_pos))
            y_pos += 50  # Aumenta a posição y para a próxima pontuação

        pygame.display.update()
        clock.tick(FPS)

    return state



            
                



    