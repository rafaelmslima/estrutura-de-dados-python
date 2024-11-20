""""Imagine que por acaso um vetor que já esteja ordenado seja passado para ser
ordenado pelo algoritmo BubbleSort, devido ao seu grande número de iterações
serão realizadas diversas verificações. Dessa forma, utilizando o algoritmo do
BubbleSort clássico como base, apresente uma melhoria ao código do BubbleSort
para que ele consiga identificar se o vetor é ordenado durante a sua execução e não
realize todas iterações.
"""
import time
def bubble_sort(arr):
    trocou = True
    while trocou:
        trocou = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                trocou = True
    return arr

arr = [9,8,7,6,5,4,3,2,1]
tamanhos = [100, 1000, 10000, 100000, 1000000, 1000000000]
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

calcula_tempo(bubble_sort)