import random
from assets import carrega_arquivos
from config import WIDTH, HEIGHT


def colisao_entre_retangulos(r1_x,r1_y,r1_w,r1_h,r2_x,r2_y,r2_w,r2_h):

    # Verificar se os retângulos colidem
    if r1_x < r2_x + r2_w and r1_x + r1_w > r2_x and r1_y < r2_y + r2_h and r1_y + r1_h > r2_y:
        return True
    else:
        return False
    
    
def verifica_colisoes(imagem,lista_imagens):

    # Verifica se a imagem colide com alguma outra imagem dentro da lista fornecida
    for dic_imagem in lista_imagens:
   
        if colisao_entre_retangulos(imagem["posicao_x"], imagem["posicao_y"], imagem["imagem"].get_rect().width, imagem["imagem"].get_rect().height, 
                                    dic_imagem["posicao_x"], dic_imagem["posicao_y"], dic_imagem["imagem"].get_rect().width, dic_imagem["imagem"].get_rect().height):
            return True
    return False


def gerar_imagens(x):

    lista_imagens = []
    dicionario_de_arquivos = carrega_arquivos()

    # Lista de tipos de imagens possíveis
    tipos_imagens = ['cherries', 'flower', 'fruit-tree', 'ladybug', 'tree']

    # Cria uma lista de tipos de imagens selecionadas aleatoriamente
    imagem_selecionada = random.sample(tipos_imagens,x)

    for i in range(len(imagem_selecionada)):
        
        # Sorteia a quantidade de imagens que aparecerão na tela
        quantidade_imagens = random.randint(5, 10)
        
        # Loop que se repete de acordo com a quantidade de imagens que aparecerão deste tipo
        for j in range(quantidade_imagens):
            
            # Sorteia uma posição aleatória para cada imagem
            posicao_x = random.randint(0, WIDTH-100)
            posicao_y = random.randint(0, HEIGHT-100)

            imagem = {
                "imagem": dicionario_de_arquivos[imagem_selecionada[i]],
                "tipo": imagem_selecionada[i],
                "posicao_x": posicao_x,
                "posicao_y": posicao_y
            }

            # Verifica se a imagem colide com alguma outra imagem
            while verifica_colisoes(imagem, lista_imagens):

                posicao_x = random.randint(0, WIDTH-100)
                posicao_y = random.randint(0, HEIGHT-100)

                imagem = {
                "imagem": dicionario_de_arquivos[imagem_selecionada[i]],
                "tipo": imagem_selecionada[i],
                "posicao_x": posicao_x,
                "posicao_y": posicao_y
                }
            
            # Adiciona a imagem à lista de imagens somente se não colidir com nenhuma outra imagem
            lista_imagens.append(imagem)

    return lista_imagens

def conta_sorteada (lista_imagens, sorteada):

    contagem = 0

    tipo_sorteada = sorteada["tipo"]

    for dic in lista_imagens:

        tipo = dic["tipo"]

        if tipo == tipo_sorteada:

            contagem += 1
    
    return contagem




