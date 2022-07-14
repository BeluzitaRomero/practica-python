class Pila:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        return str(self.items)
    
    def push(self, x):
        self.items.append(x)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila esta vacia")
    
    def is_empty(self):
        return self.items == []

    def top(self):
        x= self.items.pop()
        self.items.append(x)
        return x

p = Pila()

# p.is_empty()
# p.push(1)
# print(p)
# p.pop()
# print(p)
# p.push(23)
# print(p.top())

class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        try:
            self.items.pop(0)
        except IndexError:
            raise ValueError("La cola esta vacia")
    
    def is_empty(self):
        return self.items == []


class Nodo:
    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)



class ListaEnlazada(object):
    def __init__(self):
        #apunta al primero nodo - None con la lista vacia
        self.primero = None

        #len: lingitud de la lista = 0 con la lista vacia
        self.len = 0
