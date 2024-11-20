class Node():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.next = None

class Lista_simples():
    def __init__(self):
        self.head = None
    
    def adicionar_no_fim(self, nome, idade):
        novo_no = Node(nome, idade)
        if self.head is None:
            self.head = novo_no
        else:
            atual = self.head
            while atual.next:
                atual = atual.next
            atual.next = novo_no
    
    def display(self):
        elementos = []
        atual = self.head
        while atual != None:
              elementos.append((atual.nome, atual.idade))
              atual = atual.next
        return elementos

def mesclar_listas(lista1, lista2):
    no_auxiliar = Node(None, None)
    atual = no_auxiliar

    atual1 = lista1.head
    atual2 = lista2.head

    while atual1 is not None and atual2 is not None:
        if atual1.idade <= atual2.idade:
            atual.next = atual1
            atual1 = atual1.next
        else:
            atual.next = atual2
            atual2 = atual2.next
        atual = atual.next
    if atual1 is not None:
            atual.next = atual1
    elif atual2 is not None:
            atual.next = atual2
    lista_mesclada = Lista_simples()
    lista_mesclada.head = no_auxiliar.next
    return lista_mesclada.display()

####### TESTE ######
lista1 = Lista_simples()
lista1.adicionar_no_fim('Alice', 35)
lista1.adicionar_no_fim('Rafael', 26)
lista1.adicionar_no_fim('Joao', 34)
lista1.adicionar_no_fim('Paulo', 33)
lista1.adicionar_no_fim('Pedro', 32)
lista1.adicionar_no_fim('Ricardo', 25)

lista2 = Lista_simples()
lista2.adicionar_no_fim('Amora', 20)
lista2.adicionar_no_fim('Amor', 21)
lista2.adicionar_no_fim('Amorinha', 22)
lista2.adicionar_no_fim('Cris', 23)
lista2.adicionar_no_fim('Sophia', 24)
lista2.adicionar_no_fim('Lionel', 25)
lista2.adicionar_no_fim('Messi', 26)
lista2.adicionar_no_fim('Neymar', 27)
lista2.adicionar_no_fim('Ronaldo', 28)
lista2.adicionar_no_fim('Ronaldinho', 29)
lista2.adicionar_no_fim('Gaucho', 30)
lista2.adicionar_no_fim('Cristiano', 31)

print(mesclar_listas(lista1, lista2))