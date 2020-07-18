import time
from ListaRandomica import lista_randomica
from SelectionSort import selection_sort
from InsertionSort import insertion_sort
from MergeSort import merge_sort
from QuickSort import quick_sort


def demonstracao(lista:list, nome_algoritmo:str, algoritmo, builtin:bool=False):
    tempo = time.time()
    print('Começando o ' + nome_algoritmo + '...')
    if not builtin:
        algoritmo(lista, 0, len(lista))
    else:
        if algoritmo:
            lista = algoritmo(lista)
        else:
            lista.sort()
    tempo = time.time() - tempo
    print('Lista ordenada:', lista)
    print(f'Tempo gasto: {tempo:.5f} segundos\n')


if __name__ == '__main__':
    # lista = [8, 10, 6, 3, 1, 5, 2, 9, 4, 7]
    lista = lista_randomica(10001, 99999, True)

    print('lista original: ', lista, '\n')

    demonstracao(lista[:], 'sorted built-in function', sorted, True)
    demonstracao(lista[:], 'sort built-in attribute', None, True)
    demonstracao(lista[:], 'selection sort', selection_sort)
    demonstracao(lista[:], 'insertion sort', insertion_sort)
    demonstracao(lista[:], 'merge sort', merge_sort)
    demonstracao(lista[:], 'quick sort', quick_sort)