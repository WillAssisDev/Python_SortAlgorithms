def merge_sort(lista: list, inicio: int, fim: int):
    quantidade = fim - inicio

    if quantidade > 1:
        meio = (inicio + fim) // 2

        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)

        lista_aux = []
        indice_esquerda = inicio
        indice_direita = meio
        while indice_esquerda < meio and indice_direita < fim:
            if lista[indice_esquerda] < lista[indice_direita]:
                lista_aux.append(lista[indice_esquerda])
                indice_esquerda += 1
            else:
                lista_aux.append(lista[indice_direita])
                indice_direita += 1

        while indice_esquerda < meio:
            lista_aux.append(lista[indice_esquerda])
            indice_esquerda += 1

        while indice_direita < fim:
            lista_aux.append(lista[indice_direita])
            indice_direita += 1

        indice_aux = 0
        for indice_lista in range(inicio, fim):
            lista[indice_lista] = lista_aux[indice_aux]
            indice_aux += 1
