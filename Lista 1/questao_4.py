#Receber uma pilha como entrada e inverter a ordem dos elementos com apenas uma pilha adicional

class Pilha:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("A pilha está vazia")

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("A pilha está vazia")

    def size(self):
        return len(self.items)
    
    def display(self):
        return print(self.items[::-1])
    
    def inverter_pilha(self):
        pilha_auxiliar = Pilha()
        while not self.is_empty():
            elemento = self.pop()
            pilha_auxiliar.push(elemento)
            
        for i in range(pilha_auxiliar.size()):
            self.push(pilha_auxiliar.items[i])
    


pilha_original = Pilha()
pilha_original.push(40)
pilha_original.push(90)
pilha_original.push(70)
pilha_original.push(10)
pilha_original.push(20)
pilha_original.push(30)
pilha_original.push(40)
pilha_original.push(80)
pilha_original.push(180)
pilha_original.push(420)
pilha_original.display()
pilha_original.inverter_pilha()
pilha_original.display()