def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        print(arr)
        arr[j + 1] = key
    return arr

arr = [16,8,6,14,12,4]
teste = insertion_sort(arr)
print(teste)

""""A resposta para essa pergunta é que o Algoritmo utilizado é o insertion sort. 
A ordem de iteracao dele é pegar o maior elemento da lista e realizar o deslocamento dele para a direita (inverso do codigo que fiz)
entao em cada linha do codigo ele pega o primeiro elemento da lista e faz a comparacao entre os elementos a direita dele
verificando qual elemento é maior que o outro 
"""