import matplotlib.pyplot as plt

def maior_soma_quadratico(lista):
    n = len(lista)
    maior_soma = 0
    for i in range(n):
        for j in range(i + 2, n):  # Garante que i e j estejam separados por ao menos 2 índices
            soma = lista[i] + lista[j]
            if soma > maior_soma:
                maior_soma = soma
    return maior_soma  # Retorna a maior soma após todos os loops

# Testando a função
lista = []
for element in range(1, 50001):
    lista.append(element)
teste = maior_soma_quadratico(lista)
print(teste)  # Saída esperada: 39 (maior soma é 19 + 20)

# Gerando os dados
tamanhos_lista = range(2, 1001, 50)  # Tamanhos da lista de 2 até 1000, variando de 50 em 50
maiores_somas = []

for tamanho in tamanhos_lista:
    lista = list(range(1, tamanho + 1))  # Cria uma lista de 1 até o tamanho atual
    soma_maxima = maior_soma_quadratico(lista)  # Calcula a maior soma para essa lista
    maiores_somas.append(soma_maxima)  # Armazena a maior soma

# Plotando o gráfico
plt.plot(tamanhos_lista, maiores_somas, label="Maior Soma")
plt.title("Maior Soma Quadrática em Função do Tamanho da Lista")
plt.xlabel("Tamanho da Lista")
plt.ylabel("Maior Soma")
plt.legend()
plt.grid(True)  # Adiciona a grade ao gráfico
plt.show()