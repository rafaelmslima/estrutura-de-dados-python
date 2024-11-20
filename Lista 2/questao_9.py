"""
Algoritmo 1 - Selection Sort
Algoritmo 2 - Bubble Sort
Algotirmo 3 - Insertion Sort

Fiquei um pouco bugado nessa questao, nao entendi a segunda parte... Mas acho que é isso
Algoritmo 1 - Selection Sort
1ª linha - Iteracao 0
2ª Linha - Iteracao 1
3ª Linha - Iteracao 2

Algoritmo 2 - Bubble Sort
1ª Linha - Iteracao 0
2ª Linha - Iteracao 1
3ª Linha - Iteracao 2

Algoritmo 3 - Insertion Sort
1ª Linha -  Iteracao 0
2ª Linha - Iteracao 1
3ª Linha - Iteracao 2 
"""

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        print(arr)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
                print("Iteracao:", i)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(arr):
    trocou = True
    while trocou:
        trocou = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                print(arr)

                trocou = True
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(arr)

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        print(arr)
        arr[j + 1] = key
    return arr

arr = [81, 15, 4, 20, 7, 47, 14, 20, 4]
insertion_sort(arr)