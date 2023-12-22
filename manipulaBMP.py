from graph import Graph
from typing import List
from PIL import Image

class MovimentacaoEquipamento:
    def __init__(self):
        self.grafo = Graph()
        self.posicao_inicial = None
        self.posicoes_destino = []

# Processa o arquivo bitmap e constrói o grafo
    def processar_bitmap(self, arquivo_bitmap: str, cor_inicial, cor_destino) -> None:
        
        imagem = Image.open(arquivo_bitmap)

        largura, altura = imagem.size

        for i in range(altura):
            for j in range(largura):

                cor_pixel = imagem.getpixel((j, i))

                self.grafo.add_node((i, j))

                # Pos. Inicial
                if cor_pixel == cor_inicial:  # Vermelho
                    self.posicao_inicial = (i, j)
                    #print(self.posicao_inicial)

                 # Pos. Final
                elif cor_pixel == cor_destino:  # Verde
                    self.posicoes_destino.append((i, j))
                    #print(self.posicoes_destino)

                if cor_pixel != (0, 0, 0):  # Não é preto
                    if i > 0 and imagem.getpixel((j, i - 1)) != (0, 0, 0): 
                        self.grafo.add_undirected_edge((i, j), (i - 1, j), 1)
                    if j > 0 and imagem.getpixel((j - 1, i)) != (0, 0, 0): 
                        self.grafo.add_undirected_edge((i, j), (i, j - 1), 1)

# Busca em largura
    def encontrar_caminho(self) -> List[str]:
        fila = [self.posicao_inicial]
        visitados = {self.posicao_inicial: None} 

        while fila:
            atual = fila.pop(0)

            #Posição atual = posição de destino
            if atual in self.posicoes_destino:
                caminho = self.reconstruir_caminho(visitados, atual)
                return self.formatar_caminho(caminho)

            #Add vizinhos não visitados à fila
            for vizinho in self.grafo.neighbors(atual):
                if vizinho not in visitados:
                    visitados[vizinho] = atual
                    fila.append(vizinho)

        return ["Não é possível deslocar o equipamento"]


    def reconstruir_caminho(self, visitados, destino) -> List:
        caminho = [destino]
        while destino in visitados and visitados[destino] is not None:
            destino = visitados[destino]
            caminho.insert(0, destino)
        return caminho

#trata os dados em sequencias
    def formatar_caminho(self, caminho) -> List[str]:
        movimentos = []
        for i in range(len(caminho) - 1):
            atual = caminho[i]
            proximo = caminho[i + 1]

            if proximo[0] < atual[0]:
                movimentos.append("↑")
            elif proximo[0] > atual[0]:
                movimentos.append("↓")
            elif proximo[1] < atual[1]:
                movimentos.append("←")
            elif proximo[1] > atual[1]:
                movimentos.append("→")

        return movimentos

    def imprimir_caminho(self, caminho: List[str]) -> None:
        print("É possivel deslocar o equipamento :")
        if len(caminho) == 1:
            print(caminho[0])
        else:
            print(" ".join(caminho))