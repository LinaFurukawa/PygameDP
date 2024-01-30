import pygame
import random
from os import path
from sprites import Botao
from config import IMG_DIR, BLACK, FPS, GAME, QUIT, WIDTH, HEIGHT, WHITE
from assets import carrega_arquivos

from config import FPS, WIDTH, HEIGHT, BLACK, BLUE, RED, WHITE
from assets import carrega_arquivos
from config import SND_DIR
from funcoes import gerar_imagens,  conta_sorteada
import random
from game_screen import game_screen

def end_game (window, pontuacao):

    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()

    DONE = 0

    PLAYING = 1

    state = PLAYING

    fonte = pygame.font.Font(None, 75)

    while state != DONE:

        clock.tick(FPS)

        for event in pygame.event.get():
           
            if event.type == pygame.QUIT:
                state = DONE
        
        window.fill(BLACK)

        pontuacao_final_escrito = fonte.render("Pontuação:", True, RED)

        window.blit(pontuacao_final_escrito, (WIDTH/2 - 200, HEIGHT/2 - 200))

        pontuacao_final = fonte.render(str(pontuacao), True, RED)

        window.blit(pontuacao_final, (WIDTH/2 - 170, HEIGHT/2 - 100))

        pygame.display.update()

    return state



            
                



    