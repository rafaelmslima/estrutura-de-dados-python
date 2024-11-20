class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Fila():
    def __init__(self):
        self.head = None
        self.tamanho = 0
        
    def enqueue(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif self.head.next is None:
            self.head.next = new_node
        else:
            atual = self.head
            while atual.next != None:
                atual = atual.next
            atual.next = new_node
        self.tamanho += 1

    def dequeue(self):
        if self.head is None:
            print('Nao e possivel retirar elementos de uma lista vazia')
        elif self.head.next is None:
            aux = self.head.data
            print('Removendo', self.head.data)
            self.head = None
            print('A lista agora é vazia')
            return aux
        else:
            aux = self.head.data
            print('Removendo', self.head.data)
            self.head = self.head.next
            print('Nova cabeca é',self.head.data)
            return aux

    def is_empty(self):
        return self.head is None

    def peek (self):
        return print(self.head.data)

    def display(self):
        elements = []
        atual = self.head
        while atual is not None:
            elements.append(atual.data)
            atual = atual.next
        print('Os elementos da Fila sao:', elements)

fila1 = Fila()
fila2 = Fila()

def verifica_igualdade_filas(fila1, fila2):
    atual1 = fila1.head
    atual2 = fila2.head
    if fila1.tamanho == fila2.tamanho:
        while atual1 is not None and atual2 is not None:
            if atual1.data == atual2.data:
                atual1 = atual1.next
                atual2 = atual2.next
            else:
                print('filas diferentes!')
                return False
        print('Filas iguais!')
        return True
    else:
        print('Filas com tamanhos diferentes!')
        return False

fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)
fila1.enqueue(30)

fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)
fila2.enqueue(30)

verifica_igualdade_filas(fila1,fila2)