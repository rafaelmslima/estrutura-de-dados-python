class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque():
    def __init__(self):
        self.head = None
        self.tail = None

    def inser_at_beggining(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
    def remove_at_beggining(self):
        if self.head is None:
            print('Nao e possivel remover dados de uma lista vazia')
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next

    def remove_at_end(self):
        if self.tail is None:
            print('Nao e possivel retirar dados de uma lista vazia')
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev

    def display (self):
        elements = []
        atual = self.head
        while atual is not None:
            elements.append(atual.data)
            atual = atual.next
        return print(elements)
    
teste = Deque()
teste.inser_at_beggining(30)
teste.inser_at_beggining(60)
teste.inser_at_beggining(90)
teste.insert_at_end('Rafael')
teste.insert_at_end('Sousa')
teste.insert_at_end('Pedro')
teste.display()