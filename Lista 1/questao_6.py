class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Fila():
    def __init__(self):
        self.head = None
        
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

class Pilha():
    def __init__(self):
        self.head = None
    
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def pop(self):
        if self.head is None:
            print('Nao e possivel desempilhar uma pilha vazia')
        else:
            aux = self.head
            self.head = self.head.next
            return aux.data
    def peek(self):
        if self.head is None: 
            print('Pilha vazia')
        else:
            return(self.head.data)
        
    def is_empty(self):
        return self.head is None

    def display(self):
        elements = []
        atual = self.head
        while atual != None:
            elements.append(atual.data)
            atual = atual.next
        return print('Os elementos da pilha agora sao:',elements)
    
pilha = Pilha()
fila = Fila()

def transferir_pilha_para_fila(pilha, fila):
    pilha_temp = Pilha()
    while not pilha.is_empty():
        elemento = pilha.pop()
        pilha_temp.push(elemento)
    while not pilha_temp.is_empty():
        elemento = pilha_temp.pop()
        fila.enqueue(elemento)

pilha.push(40)
pilha.push(60)
pilha.push('Rafael')
pilha.push('Pedro Cria')
pilha.display()
transferir_pilha_para_fila(pilha, fila)
fila.display()


