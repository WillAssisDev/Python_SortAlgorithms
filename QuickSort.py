def quick_sort(lista: list, inicio: int, fim: int):
    quantidade = fim - inicio

    if quantidade > 1:
        posicao_pivo = fim - 1

        quantidade_menores = 0
        for indice_lista in range(0, fim - 1):
            if lista[indice_lista] <= lista[posicao_pivo]:
                aux = lista[indice_lista]
                lista[indice_lista] = lista[quantidade_menores]
                lista[quantidade_menores] = aux
                quantidade_menores += 1

        aux = lista[posicao_pivo]
        lista[posicao_pivo] = lista[quantidade_menores]
        lista[quantidade_menores] = aux

        posicao_pivo = quantidade_menores

        quick_sort(lista, inicio, posicao_pivo)
        quick_sort(lista, posicao_pivo + 1, fim)
