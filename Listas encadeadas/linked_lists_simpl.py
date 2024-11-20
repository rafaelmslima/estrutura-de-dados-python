class Node:
    def __init__(self, data=None):
        self.data = data  # Armazenando o dado
        self.next = None  # Ponteiro apontando para o nó seguinte

class LinkedList:
    def __init__(self):
        self.head = None  # Inicializando a lista vazia

    def append_init(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append_any(self, data, position):
        new_node = Node(data)
        if position == 0:  # Inserir no início
            new_node.next = self.head
            self.head = new_node
        else:
            no_atual = self.head
            count = 0
            while no_atual is not None and count < position - 1:
                no_atual = no_atual.next
                count += 1
            if no_atual is None:
                print('Não é possível adicionar, posição fora do alcance')
            else:
                # Parte corrigida começa aqui:
                new_node.next = no_atual.next  # O novo nó deve apontar para o próximo nó correto
                no_atual.next = new_node  # O nó anterior agora aponta para o novo nó
                # Parte corrigida termina aqui.

    def append_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  # Percorre até o último nó
            last_node = last_node.next
        last_node.next = new_node  # O último nó agora aponta para o novo nó

    # Exibindo a lista
    def display(self):
        elements = []
        current_node = self.head
        while current_node:  # Percorre a lista até o final
            elements.append(current_node.data)
            current_node = current_node.next
        print(elements)


# Teste do código
lista = LinkedList()
lista.append_init(5)  # [5]
lista.append_end(20)  # [5, 20]
lista.append_init(20)  # [20, 5, 20]
lista.append_init(55)  # [55, 20, 5, 20]
lista.append_any(40, 2)  # Inserindo 40 na posição 2 [55, 20, 40, 5, 20]

lista.display()  # Saída esperada: [55, 20, 40, 5, 20]