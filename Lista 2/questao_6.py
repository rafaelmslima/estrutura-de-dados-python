def algoritmo(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        print (f"A chave agora é: {chave}")
        j= i - 1
        while j >= 0 and lista[j] > chave:
            print(f"O indice de iteracao agora é: {j}")
            lista[j + 1]  = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

#LETRA A) Esse é o algoritmo do insertion sort
#LETRA B) O(N**2)pois temos dois loops aninhados
#LETRA C) 

arr = [64, 46, 77, 34, 87, 45, 34, 2]
teste = algoritmo(arr)
print(teste)

"""" Loop for externo: pega a partir do segundo elemento da lista e atribui cada elemento da lista a uma chave que será usada no 
loop interno. 
 - Loop externo se inicia em 46, faz a compacarao com o primeiro elemento da lista (atraves do loop interno) e se ele for menor
 que o primeiro elemento, realiza a troca de posicoes e seleciona o proximo elemento como a chave.
 - O loop interno vai fazer a comparacao da chave com os elementos a esquerda dele. Ou seja, se a chave for 46, o loop interno 
 fará a comparacao com 64. Se a chave for 77, fara a comparacao com 46 e 64 e assim por diante. 
 ---------------------------------- Desenhando ----------------------------------------
 - 1ª iteracao:  
 chave = 46 // Indice da lista = 0
 Troca o 46 e o 64 de lugar
 - 2ª iteracao:
 chave = 77 // Indice da lista = 2
 77 nao troca de lugar com ninguem pois é maior que todos a esquerda
 - 3ª iteracao: 
 chave = 34 // Indice da lista = 0
 Faz a comparacao de 34 com 77 e move o 77 para o local do 34, depois faz a comparacao do 34 com o 64 e move o 64 para o local do
 34, depois faz a comparacao do 34 com o 46 e move o 34 para o primeiro indice da lista. Como j fica > 0, o loop interno para e 
 a chave é atualizada
 
 Isso acontece em todas as iteracoes até que acabe. 
"""