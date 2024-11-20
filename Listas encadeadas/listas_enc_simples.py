class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Lista_encadeada():
    def __init__(self):
        self.head = None

    def append_init(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            no_atual = self.head
            while no_atual.next is not None:
                no_atual = no_atual.next
            no_atual.next = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)
        
        # **Modificação 1**: Caso especial - Inserção no início da lista
        if position == 0:  
            new_node.next = self.head
            self.head = new_node
            return
        
        no_atual = self.head
        counter = 0
        
        # **Modificação 2**: Percorrer a lista até a posição desejada ou até o final da lista
        while no_atual is not None and counter < position - 1:
            no_atual = no_atual.next
            counter += 1
        
        # **Modificação 3**: Verificação se a posição está fora dos limites da lista
        if no_atual is None:  
            print('Posição fora do alcance da lista')
        else:
            # Inserir o novo nó na posição correta
            new_node.next = no_atual.next
            no_atual.next = new_node

    def display(self):
        elementos_lista = []
        no_atual = self.head
        while no_atual:
            elementos_lista.append(no_atual.data)
            no_atual = no_atual.next
        print(elementos_lista)

# Teste do código
lista = Lista_encadeada()
lista.append_init(10)
lista.append_init(11)
lista.append_init(12)
lista.append_end(14)
lista.append_end(15)        
lista.insert_at_position(70, 2)  # Inserir o valor 70 na posição 2
lista.display()  # Saída esperada: [12, 11, 70, 10, 14, 15]
lista.insert_at_position(100, 10)  # Tentativa de inserção fora dos limites