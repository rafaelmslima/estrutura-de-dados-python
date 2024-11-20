class Node():
    def __init__ (self, data):
        self.data = data
        self.next = None

class Deque():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 10
        self.count = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.count += 1
        else:
            if self.count < self.size:
                self.tail.next = new_node
                self.tail = new_node
                self.tail.next = self.head
                self.count += 1
            elif self.count == self.size:
                self.head = self.head.next
                self.tail.next = new_node
                self.tail = new_node
                self.tail.next = self.head

    def display (self):
        elements = []
        atual = self.head
        elements.append(atual.data)
        atual = atual.next
        while atual != self.head:
            elements.append(atual.data)
            atual = atual.next
        print(elements)


######### TESTES ##########

lista = Deque()
lista.enqueue(30)
lista.enqueue(40)
lista.enqueue(70)
lista.enqueue(70)
lista.enqueue(70)
lista.enqueue(70)
lista.enqueue(70)
lista.enqueue(70)
lista.enqueue(70)
lista.enqueue(70)
lista.enqueue(900)
lista.enqueue(100)


lista.display()