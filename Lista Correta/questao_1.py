class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque():
    def __init__(self):
        self.head = None
        self.tail = None

    def inserir_inicio(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def inserir_fim(self,data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def remove_inicio(self):
        if self.head is None:
            print('Nao e possivel retirar elementos de uma lista vazia')
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            print('A lista agora esta vazia')
        else:
            self.head.next.prev = None
            self.head = self.head.next

    def remove_fim(self):
        if self.tail is None:
            print('Nao e possivel retirar elementos de uma lista vazia')
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            print('Lista agora vazia')
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
    
    def display(self):
        elements = []
        atual = self.head
        while atual != None:
            elements.append(atual.data)
            atual = atual.next
        print(elements)

############# TESTES ###############
lista = Deque()
lista.inserir_inicio(30)
lista.inserir_inicio(20)
lista.inserir_inicio(80)
lista.inserir_fim(100)
lista.inserir_fim(200)
lista.inserir_fim(460)
lista.display()
lista.remove_fim()
lista.display()
lista.remove_fim()
lista.display()
lista.remove_fim()
lista.display()
lista.remove_fim()
lista.display()
lista.remove_fim()
lista.display()
lista.remove_fim()
lista.display()