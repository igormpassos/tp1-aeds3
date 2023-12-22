#Igor Marques Passos
#22.2.8118

from manipulaBMP import MovimentacaoEquipamento


def main():

    movimentacao_equipamento = MovimentacaoEquipamento()

    #Recebe o bitmap
    arquivo_bitmap = input("Informe o arquivo bitmap: ")

    cor_inicial = (255, 0, 0)
    cor_destino = (0, 255, 0)

    #Processa o bitmap
    movimentacao_equipamento.processar_bitmap(arquivo_bitmap, cor_inicial, cor_destino)

    caminho = movimentacao_equipamento.encontrar_caminho()
    movimentacao_equipamento.imprimir_caminho(caminho)

main();