class Node():
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Dupla_circular():
    def __init__(self):
        self.head = None
        self.tail = None

    def append_init(self, data):
        novo_no = Node(data)
        if self.head is None:
            self.head = novo_no
            self.tail = novo_no
            return
        else:
            novo_no.next = self.head
            self.head.prev = novo_no
            self.head = novo_no
            self.tail.next = self.head
            self.head.prev = self.tail

    def insert_at_position(self, data, position):
        novo_no = Node(data)
        if self.head is None:
            self.head = novo_no
            self.tail = novo_no
            novo_no.next = novo_no
            novo_no.prev = novo_no
            return
        else:
            atual = self.head
            while atual.next != 

    def append_end(self, data):
        novo_no = Node(data)
        if self.head is None:
            self.head = novo_no
            self.tail = novo_no
            self.head.prev = self.tail
            self.tail.next = self.head
            return
        else:
            atual = self.head
            while atual.next is not self.head:
                atual = atual.next

            #[3,4,2,6,9]
            novo_no.prev = self.tail
            self.tail.next = novo_no
            self.tail = novo_no
            self.tail.next = self.head
            self.head.prev = self.tail

    def display(self):
        elementos = []
        atual = self.head
        while True:
            elementos.append(atual.data)
            atual = atual.next
            if atual == self.head:
                break
        print(elementos)

#testando
dll = Dupla_circular()
dll.append_init(30)
dll.append_init(60)
dll.append_init(80)
dll.append_end(108)
dll.append_end(353)
dll.display()