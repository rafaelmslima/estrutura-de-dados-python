import time
import matplotlib.pyplot as plt
import random

# Funções de ordenação
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivo = arr[len(arr) // 2]
        left = [x for x in arr if x < pivo]
        right = [x for x in arr if x > pivo]
        middle = [x for x in arr if x == pivo]
        return quick_sort(left) + middle + quick_sort(right)
    
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr) // 2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left, right)

def merge(left, right):
    lista = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lista.append(left[i])
            i += 1
        else:
            lista.append(right[j])
            j += 1
    lista.extend(left[i:])
    lista.extend(right[j:])
    return lista

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(arr):
    count = 1
    while count != 0:
        count = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                count += 1
    return arr

def calcula_tempo(funcao, lista):
    inicio = time.time()
    funcao(lista.copy())  
    fim = time.time()
    return fim - inicio

tamanhos = [100, 1000, 2000, 3000, 4000, 5000]

# Dicionário para armazenar os tempos de execução para cada algoritmo
tempos = { "Quick Sort": [], "Merge Sort": [], "Insertion Sort": [], "Selection Sort": [], "Bubble Sort": [] }
algoritmos = { "Quick Sort": quick_sort, "Merge Sort": merge_sort, "Insertion Sort": insertion_sort, "Selection Sort": selection_sort, "Bubble Sort": bubble_sort }

for tamanho in tamanhos:
    lista = random.sample(range(tamanho * 10), tamanho)
    for nome, funcao in algoritmos.items():
        tempo_execucao = calcula_tempo(funcao, lista)
        tempos[nome].append(tempo_execucao)
        print(f"Algoritmo: {nome}, Tamanho da lista: {tamanho}, Tempo de execução: {tempo_execucao:.5f} segundos")

plt.figure(figsize=(12, 6))
for nome, tempo in tempos.items():
    plt.plot(tamanhos, tempo, marker='o', label=nome)
plt.xlabel('Tamanho da Lista')
plt.ylabel('Tempo de Execução (s)')
plt.title('Comparação de Algoritmos de Ordenação com Listas Randômicas')
plt.legend()
plt.show()

# Teste com lista de 50.000 elementos em ordem decrescente
lista_decrescente = list(range(50000, 0, -1))
tempos_decrescente = {nome: calcula_tempo(funcao, lista_decrescente) for nome, funcao in algoritmos.items()}

# Plotagem dos tempos de execução para a lista decrescente de 50.000 elementos
plt.figure(figsize=(8, 4))
plt.bar(tempos_decrescente.keys(), tempos_decrescente.values())
plt.xlabel('Algoritmo')
plt.ylabel('Tempo de Execução (s)')
plt.title('Comparação de Algoritmos de Ordenação com Lista Decrescente (50.000 elementos)')
plt.show()