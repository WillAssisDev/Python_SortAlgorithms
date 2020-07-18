def selection_sort(lista: list, inicio: int, fim: int):
    for indice_lista in range(inicio, fim):
        posicao_menor = indice_lista

        for posicao_atual in range(indice_lista, fim):
            if lista[posicao_atual] < lista[posicao_menor]:
                posicao_menor = posicao_atual

        aux = lista[indice_lista]
        lista[indice_lista] = lista[posicao_menor]
        lista[posicao_menor] = aux
