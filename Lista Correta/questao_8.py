"""Expliqe o papel da pilha de chamadas (call stack) no contexto de funções recursivas.
Como a manipulação da pilha afeta o desempenho e uso de memória em algoritmos
recursivos?"""


"""
A pilha de chamadas (call Stack) é uma estrutura essencial para recursividade. Ela armazena informacoes sobre cada chamada ativa
de uma funcao (parametros, variaveis locais e o ponto de retorno). Quando uma funcao chama outra ou a si mesma, uma nova entrada
é empilhada na pilha de chamadas e ao fim essa entrada é removida da fila.

Em recursividade, cada chamada cria uma nova entrada na pilha de chamadas, permitindo que: 
 - Armazena o estado exclusivo para cada chamada da funcao(parametros, variaveis locais) o que possibilita o bom funcionamento da
 recursao
 - Retorno ao ponto correto: ao finalizar, a funcao retorna para o ponto exato de onde foi chamada

A pilha de chamadas afeta o desepenho e o uso de memoria pois cada chamada recursiva consome espaco na pilha de chamadas, o que
aumenta o uso de memoria e se o algoritmo fizer a pilha crescer rapidamente, pode gerar um stack overflow.
Ela também afeta o desempenho pois a cada manipulacao da pilha, seja incluindo ou removendo entradas ou retornando a funcao,
adiciona um custo extra ao tempo de execucao. 
"""