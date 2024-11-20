""""Escreva um código em Python para verificar se uma lista contém algum par de
elementos cuja soma seja igual a um valor específico. Qual é a complexidade de
tempo desse algoritmo? Explique o porquê. Faça uma análise da complexidade.
"""

def verifica_array(lista, resultado):
    for i in range(len(lista)): 
        n = lista[i]
        for j in range(i+1,len(lista)):
            if lista[i] + lista[j] == resultado:
                return print(f"Existe sim um par de elementos {lista[i]} e {lista[j]} cujo resultado é {resultado}")
    return print(f"Nao existe um par de elementos cujo a soma seja {resultado}")
        
lista = []

for i in range(0,1000000,2):
    lista.append(i)
verifica_array(lista, 11)
#verificando o uso dos 2 loops for aí acima, é possível perceber que esse código possui complexidade O(n**2)