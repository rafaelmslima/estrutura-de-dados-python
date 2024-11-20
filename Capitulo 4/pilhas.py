#pilha de pratos em uma cozinha, ou seja LIFO (Last in, first out)
#dados so podem ser inseridos no fim da pilha (push)
#dados so podem ser excluidos do fim da pilha (pop)
#so o ultimo elemento de dados pode ser lido na pilha(peek)
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        novo_no = Node(data)
        if self.head is None:
            self.head = novo_no
            return
        else:
            novo_no.next = self.head
            self.head = novo_no
        self.size += 1

    def pop(self):
        if self.head is None:
            print('Nao e possivel apagar dados de uma lista vazia')
        else:
            if self.head.next is None:
                valor = self.head.data
                self.head = None
                print('Data retirada:', valor)
                return valor
            else:
                valor = self.head.data
                self.head = self.head.next
                print('Data retirada: ', valor)
                return valor
        self.size -= 1

    def peek (self):
        if self.head is None:
            print('Lista vazia')
        else:
            valor = self.head.data
            print(valor)
            return valor

    def display(self):
        elementos = []
        atual = self.head
        while atual:
            elementos.append(atual.data)
            atual = atual.next
        print(elementos)

#teste
dll = Stack()
dll.push(30)
dll.push('Rafael')
dll.push('Couto')
dll.peek()