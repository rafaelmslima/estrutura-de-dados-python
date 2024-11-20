class Node ():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly_linked_list():
    def __init__(self):
        self.head = None

    def append_inicio(self, data):
        novo_no = Node(data)
        if self.head is None:
            self.head = novo_no

        else:
            novo_no.next = self.head
            self.head.prev = novo_no
            self.head = novo_no

    def append_fim(self, data):
        novo_no = Node(data)
        if self.head is None:
            self.head = novo_no
        else:
            no_atual = self.head
            while no_atual.next:
                no_atual = no_atual.next
            no_atual.next = novo_no
            novo_no.prev = no_atual

    def remover(self, data):
        if self.head is None: #verifiquei se a cabeca existe
            print('Nao existem elementos na lista')
        atual = self.head

        if atual.data == data: #verifiquei se o valor a ser removido é a cabeca e existem outros nós
            if atual.next:
                self.head = atual.next
                self.prev = None
            else: #caso nao existam outros nos
                self.head = None

        while atual and atual.data != data: #percorre a lista e verifica se o elemento está na lista
            atual = atual.next
        
        if atual == None:
            print('Nao existe esse valor na lista')

        if atual.next:#verifica se o proximo existe e modifica o ponteiro do anterior do proximo para o anterior do atual
            atual.next.prev = atual.prev
        if atual.prev: #verifica se o anterior existe e modifica o ponteiro do proximo do anterior para o proximo do atual
            atual.prev.next = atual.next

    def insert_at_posicion(self, data, position):
        novo_no = Node(data)
        if position == 0:
            self.append_inicio(data)
            return

        atual = self.head
        contador = 0
        while atual is not None and contador < position - 1:
            atual = atual.next
            contador += 1
        
        if atual is None:
            print('Elemento nao existe na lista')
        else:
            novo_no.next = atual.next
            novo_no.prev = atual
            if atual.next is not None:
                atual.next.prev = novo_no
            atual.next = novo_no

    def display(self):
        elementos = []
        no_atual = self.head
        while no_atual:
            elementos.append(no_atual.data)
            no_atual = no_atual.next
        print(elementos)
    
    def display_fim_inicio(self):
        elementos = []
        no_atual = self.head
        while no_atual.next:
            no_atual = no_atual.next
        while no_atual:
            elementos.append(no_atual.data)
            no_atual = no_atual.prev
        print(elementos)

#Testando a lista
dll = Doubly_linked_list()
dll.append_inicio(10)
dll.append_inicio(50)
dll.append_fim(30)
dll.append_fim(80)
dll.remover(50)
dll.insert_at_posicion(34, 2)
dll.display()