"""O algoritmo Quick Sort é conhecido por ter uma boa eficiência na prática, mas seu
pior caso pode ser lento. Como é possível melhorar o desempenho do Quick Sort em
casos específicos? Discuta a estratégia do "QuickSort mediana de três"
"""
"""
O caso da mediana de 3, é uma estratégia eficiente usada para reduzir a complexidade nos piores casos do quick sort. 
Para aplica-lo, é preciso pegar 3 elementos da lista (normalmente o primeiro, o do meio e o ultimo) e fazer a mediana entre eles
para poder pegar um elemento mais proximo do centro da lista e reduz significativamente a chance de ocorrer um desempenho de 
O(n**2).
"""
#O pior caso do quick sort acontece quando a lista está inversamente ordenada

import time
import matplotlib.pyplot as plt

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivo = arr[len(arr)//2]
        left = [x for x in arr if x < pivo]
        right = [x for x in arr if x > pivo]
        middle = [x for x in arr if x == pivo]
        return quick_sort(left) + middle + quick_sort(right)
    
def quick_sort_mediana_3(arr):
    if len(arr) <= 1:
        return arr
    else:
        a = arr[0]
        b = arr[len(arr)//2]
        c = arr[-1]
        pivo = sorted([a,b,c])[1]
        left = [x for x in arr if x < pivo]
        right = [x for x in arr if x > pivo]
        middle = [x for x in arr if x == pivo]
        return quick_sort(left) + middle + quick_sort(right)


###### Testes #######
tamanhos = [100, 500, 1000,5000,10000,100000,1000000]
tempos = []
def calcula_tempo(funcao):
    for tamanho in tamanhos:
        lista = list(range(tamanho, 0, -1))

        inicio = time.time()
        funcao(lista)
        fim = time.time()

        tempo_execucao = fim - inicio
        tempos.append(tempo_execucao)
        print(f"Tamanho da lista: {tamanho}, Tempo de execucao: {tempo_execucao:.5f} segundos")

calcula_tempo(quick_sort)

