def insertion_sort(lista: list, inicio: int, fim: int):
    for indice_lista in range(inicio + 1, fim):
        posicao_analisada = indice_lista

        while posicao_analisada > 0 and lista[posicao_analisada] < lista[posicao_analisada - 1]:
            aux = lista[posicao_analisada]
            lista[posicao_analisada] = lista[posicao_analisada - 1]
            lista[posicao_analisada - 1] = aux
            posicao_analisada -= 1
