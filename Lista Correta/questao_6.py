#Serie de collatz
import timeit

def medir_tempo (func, valor):
    inicio = timeit.default_timer()
    func(valor)
    fim = timeit.default_timer()
    return fim - inicio

def collatz_recursivo(valor):
    elementos = [valor]
    if valor == 1:
        return elementos
    elif valor % 2 == 0:
        valor = valor // 2
        elementos.extend(collatz_recursivo(valor))
    elif valor % 2 != 0:
        valor = (3 * valor) + 1
        elementos.extend(collatz_recursivo(valor))
    return elementos


def collatz_iterativo(valor):
    elementos = [valor]
    if valor == 1:
        return elementos
    else:
        while valor != 1:
            if valor % 2 == 0:
                valor = valor // 2
                elementos.append(valor)
            else:
                valor = (3 * valor + 1)
                elementos.append(valor)
    return elementos

######## TESTES #######
#valor maximo de 0 a direita
#print(collatz_recursivo(1000000000000000000000000000000000000000000000000000000000000))

valores_teste = [10, 100, 1000, 5000, 10000, 100000, 1000000, 1000000,10000000]
print ('Comparando o tempo entre as duas funcoes:')
for valor in valores_teste:
    tempo_recursivo = medir_tempo(collatz_recursivo, valor)
    tempo_iterativo = medir_tempo(collatz_iterativo, valor)
    print(f"Valor inicial: {valor}")
    print(f" - Tempo recursivo {tempo_recursivo:.6f} segundos")
    print(f" - Tempo iterativo {tempo_iterativo:.6f} segundos")
    print()
