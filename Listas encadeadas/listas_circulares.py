class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Lista_circular():
    def __init__(self):
        self.head = None
        self.tail = None

    def append_init(self, data):
        novo_no = Node(data)
        if self.head is None:
            self.head = novo_no
            self.tail = novo_no
            self.tail.next = self.head
        else:
            novo_no.next = self.head
            self.head = novo_no
            self.tail.next = self.head
            
    def append_at_posicion(self,data, position):
        novo_no = Node(data)
        if position == 0:
            self.append_init(data)
            return
        else:
            atual = self.head
            contador = 0
            while contador < position - 1:
                atual = atual.next
                contador += 1
                if atual == self.head:
                    break
            if atual == self.tail:
                self.append_end(data)
            if atual == self.head and contador < position - 1:
                print('Posicao fora de alcance')
            else:
                #[3, 4, 5]
                novo_no.next = atual.next
                atual.next = novo_no

    def append_end(self, data):
        novo_no = Node(data)
        if self.head is None:
            self.head = novo_no
            self.tail = novo_no
            self.tail.next = novo_no
        else:
            self.tail.next = novo_no
            self.tail = novo_no
            self.tail.next = self.head

    def remove(self, data):
        if self.head is None:
            print('Essa lista ja esta vazia')
            return
        
        if self.head.data == data:
            self.head = self.head.next
            self.tail.next = self.head
            return
        
        atual = self.head

        while atual.next.data != data and atual.next != self.head:
            atual = atual.next
        
        if atual.next == self.head:
            print("Elemento nao encontrado na lista")
            return

        if self.tail.data == atual.next.data:
            self.tail = atual
            self.tail.next = self.head
        else: 
            #[3,2,5,4]
            atual.next = atual.next.next
            

    def display (self):
        elementos = []
        atual = self.head
        while True:
            elementos.append(atual.data)
            atual = atual.next
            if atual == self.head:
                break
        print(elementos)

#testando

dll = Lista_circular()
dll.append_init(10)
dll.append_init(20)
dll.append_end(30)
dll.append_end(60)
dll.display()
dll.append_at_posicion(79,1)
dll.display()
dll.remove(30)
dll.remove(15)
dll.display()