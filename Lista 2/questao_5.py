""""Dado um vetor de 25 elementos, foi utilizado o método de ordenação Selection Sort
para ordenar os elementos. Calcule a quantidade total de comparações realizadas
durante o processo de ordenação e demonstre o raciocínio
pelo laço mais interno
utilizado para chegar a esse resultado.
Não é necessário implementar o código, apenas apresente a análise do padrão de
comparações realizadas em cada iteração do laço mais interno do algoritmo.
"""
import random
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
                print("Iteracao:", i)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = []
for i in range(25):
    arr.append(random.randint(1, 500))
teste = selection_sort(arr)
print(teste)

"""O selection sort percorre a lista varias vezes para encontrar o menor elemento na parte desordenada e coloca-lo na posicao
correta. O loop interno compara o elemento atual arr[i] com o proximo elemento arr[i+1], procurando sempre o menor elemento. 
Usando o print da iteracao foi possivel perceber que o loop faz i - 1 iteracoes, como se fosse uma progressao aritmetica. 
Entao quado i = 0 ele faz 24 iteracoes, quando i = 1 ele faz 23 iteracoes e assim por diante.
"""