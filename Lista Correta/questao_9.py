class Node():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.next = None

class ListaCircular():
    def __init__(self):
        self.head = None
        self.tail = None

    def nova_pessoa(self, nome, idade):
        pessoa = Node(nome, idade)
        if self.head == None:
            self.head = pessoa
            self.tail = pessoa
            self.tail.next = self.head
        elif self.head.idade > pessoa.idade:
            pessoa.next = self.head
            self.head = pessoa
            self.tail.next = self.head
        else:
            atual = self.head
            while atual.next != self.head and atual.next.idade < pessoa.idade:
                atual = atual.next
            pessoa.next = atual.next
            atual.next = pessoa
            if atual == self.tail:
                self.tail = pessoa
    def display(self):
        elementos = []
        atual = self.head.next
        elementos.append((self.head.nome, self.head.idade))
        while atual is not self.head:
            elementos.append((atual.nome, atual.idade))
            atual = atual.next
        return elementos


############# TESTE ############
lista = ListaCircular()
lista.nova_pessoa('Rafael', 18)
lista.nova_pessoa('Pedro', 20)
lista.nova_pessoa('Rafael', 18)
lista.nova_pessoa('Lucas', 17)
lista.nova_pessoa('Ricardo', 16)
lista.nova_pessoa('Jonatas', 18)
print(lista.display())



