import pygame
import os
from config import FPS, WIDTH, HEIGHT, BLACK, BLUE, RED, WHITE
from assets import carrega_arquivos
from funcoes import conta_sorteada, salvar_pontuacao, verifica_colisoes
from sprites import Cherry, Flower, Tree, Fruit, Ladybug
import random

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()
    sprite_classes = [Cherry, Flower, Tree, Fruit, Ladybug]

    DONE = 0
    PLAYING = 1
    state = PLAYING

    tela = 'azul'
    tempo_da_ultima_mudanca = pygame.time.get_ticks()

    all_sprites = pygame.sprite.Group()

    n_types = 1  # Inicializa quantos tipos diferentes de sprites serão usados
    tipos_selecionados = sprite_classes[:n_types]  # Seleciona os tipos de sprites permitidos

    for SpriteClass in tipos_selecionados:
        quantidade = random.randint(5, 10)  # Escolhe uma quantidade aleatória entre 5 e 10
        for _ in range(quantidade):
            while True:
                sprite = SpriteClass(position=(random.randint(0, WIDTH-60), random.randint(0, HEIGHT-60)))
                if not verifica_colisoes(sprite, all_sprites):
                    all_sprites.add(sprite)
                    break
    sorteada = random.choice(all_sprites.sprites())  # Escolhe um novo sprite sorteado após adicionar os novos sprites  
    
    resposta_jogador = ''
    pontuacao = 0
    vidas = 3

    # Adiciona o som do jogo
    dicionario_de_arquivos['game_sound'].play(loops=-1)

    # ===== Loop principal =====
    while state != DONE and state != "ending":
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            if event.type == pygame.KEYDOWN:
                if event.unicode.isdigit():
                    resposta_jogador += event.unicode  # Adiciona o dígito à resposta
                # Verifica se a tecla Enter (pygame.K_RETURN) foi pressionada para finalizar a entrada
                elif event.key == pygame.K_RETURN and resposta_jogador:
                    # Converte a resposta do jogador para um inteiro e verifica a resposta
                    resposta_numerica = int(resposta_jogador)
                    if resposta_numerica == conta_sorteada(all_sprites, sorteada):
                        dicionario_de_arquivos['good_sound'].play()
                        pontuacao += 100
                    else:
                        dicionario_de_arquivos['bad_sound'].play()
                        vidas -= 1
                        if vidas == 0:
                            print(f"Tentando salvar pontuação: {pontuacao}")
                            salvar_pontuacao(pontuacao)
                            state = "ending"
                            dicionario_de_arquivos['final_sound'].play()
                            pygame.time.wait(3000)
                    resposta_jogador = ''  # Limpa a resposta para a próxima entrada
                
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

                n_types = min(n_types + 1, len(sprite_classes))  # Aumenta o número de tipos de sprite
                all_sprites.empty()  # Esvazia o grupo de sprites antes de adicionar novos

                tipos_selecionados = sprite_classes[:n_types]  # Seleciona os tipos de sprites permitidos

                for SpriteClass in tipos_selecionados:
                    quantidade = random.randint(5, 10)  # Escolhe uma quantidade aleatória entre 5 e 10
                    for _ in range(quantidade):
                        while True:
                            sprite = SpriteClass(position=(random.randint(0, WIDTH-60), random.randint(0, HEIGHT-60)))
                            if not verifica_colisoes(sprite, all_sprites):
                                all_sprites.add(sprite)
                                break
                sorteada = random.choice(all_sprites.sprites())  # Escolhe um novo sprite sorteado após adicionar os novos sprites
               
                all_sprites.draw(window)
                resposta_jogador = ''

        if tela == 'azul':
            all_sprites.draw(window)  # Desenha todos os sprites na tela

        else:
            if vidas == 0:
                state = "ending"

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
            text_rect.centery = HEIGHT / 2 - 180
            window.blit(text_surface, text_rect)

            sorteada.rect.x = text_rect.right + 10  # Posiciona a imagem 10 pixels à direita do texto
            sorteada.rect.y = text_rect.centery - sorteada.rect.height / 2  # Centraliza verticalmente em relação ao texto
            window.blit(sorteada.image, sorteada.rect)

            # Adiciona a instrução abaixo da imagem sorteada
            instrucao_surface = dicionario_de_arquivos['font'].render('Digite ENTER no final', True, BLUE)
            instrucao_rect = instrucao_surface.get_rect()
            instrucao_rect.centerx = WIDTH / 2
            instrucao_rect.top = sorteada.rect.bottom + 10  # 10 pixels abaixo da imagem sorteada
            window.blit(instrucao_surface, instrucao_rect)

            # Adiciona a imagem do tipo que apareceu
            window.blit(sorteada.image, sorteada.rect)

            text_surface = dicionario_de_arquivos['font'].render(resposta_jogador, True, BLUE)
            text_rect = text_surface.get_rect()
            text_rect.centerx = WIDTH / 2
            text_rect.centery = HEIGHT / 2
            window.blit(text_surface, text_rect)

        text_pontuacao = dicionario_de_arquivos['font'].render(str(pontuacao), True, BLUE)
        text_pont_rect = text_pontuacao.get_rect()
        text_pont_rect.centerx = WIDTH / 2
        text_pont_rect.centery = HEIGHT - 50
        window.blit(text_pontuacao, text_pont_rect)

        coracao_surface = dicionario_de_arquivos['font_media'].render(chr(9829) * vidas, True, (255, 0, 0))
        coracao_rect = coracao_surface.get_rect()
        window.blit(coracao_surface, (20,20))
        
        pygame.display.update()  # Mostra o novo frame para o jogador

    return state, pontuacao