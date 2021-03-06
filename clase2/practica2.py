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

# print(p.is_empty())
# p.push(1)
# print(p)
# p.pop()
# print(p)
# p.push(23)
# print(p)

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

nodo = Nodo("peras", "banana")



class ListaEnlazada(object):
    #Modela una lista enlazada, compuesta por nodos

    def __init__(self):
        #crea una lista enlazada vacia
        
        #apuntara al primero nodo - None con la lista vacia
        self.primero = None

        #len: longitud de la lista = 0 con la lista vacia
        self.len = 0


    def pop(self, indice=None):
        """Elimina el nodo de la posicion del indice y devuelve el dato contenido
        si esta fuera del rango, levanta la excepcion de IndexError"""

        if indice == None:
            #Si no recibo un indice por parametro, se elimina y devuelve el ultimo (indice -1)
            indice = self.len = -1
            if not (0 <= indice < self.len):
                raise IndexError("El indice esta fuera de rango")

        #Caso particular, si es el primero
        # HAY QUE SALTEAR LA CABECERA DE LA LISTA
        if indice == 0: #o sea, si el indice a eliminar es el primer elemento (el enganche) #tengo que hacer el enganche nuevo del segundo elemento que toma su lugar
            dato = self.primero.dato
            self.primero = self.primero.prox

        else: #Para todos los demas elementos, busca la posicion
            nodo_anterior = self.primero
            nodo_actual = nodo_anterior.prox

            for posicion in range(1, indice):
                nodo_anterior = nodo_actual
                nodo_actual = nodo_anterior.prox
                #Guardar el dato y eliminar el nodo anterior
                dato = nodo_actual.dato
                nodo_anterior.prox = nodo_actual.prox
                #hay que restar 1 de len
                self.len -= 1
                #y devolver el valor borrado
                return dato
    
    def remove(self, x):
        """Borra la primera aparicion del valor x en la lista. Si x no esta, levanta un ValueError"""
        if self.len == 0:
            raise ValueError("La lista esta vacia")
        elif self.primero.dato == x:
            #se descarta la cabecera de la lista
            self.primero = self.primero.prox

        #En cualquier otro caso hay q buscar a x
        else:
            # obntiene el nodo anterior al que contiene x (nodo_ant) nodo_ant = self.prim
            nodo_actual = self.primero.prox
            while nodo_actual != None and nodo_actual != x:
                nodo_anterior = nodo_actual
                nodo_actual = self.primero.prox
            #si no se encotnro X en la lista, levanta una excepcion
        if nodo_actual == None:
            raise ValueError("El valor no esta en la lista")
            
    #si se encontro a x, debe pasar de nodo_anterior -> n_x -> n_x-prox # a nodo_anterior a -> n_x.prox
        else: 
            nodo_anterior.prox = nodo_actual.prox
            #Si no levanto excepcion, hay q restar 1 al largo
            self.len -= 1

    def insert(self, indice, x):
        """Inserta el elemento x en la posicion indice.
        si la posicion es invalida, levanta un error"""

        if (indice > self.len) or (indice < 0):
            raise IndexError("Posicion invalida") #crea un nuevo nodo con x 
        nuevo = Nodo(x) #en el ejemplo llevaba parentesis

        #insertar al principio (caso particular)
        if indice == 0:
            #El siguientedel nuevo pasa a ser el que era primero
             nuevo.prox = self.primero

             # El primero apasa a ser el nuevo
             self.primero = nuevo

        #Insertar en cualquier lugar > 0 
        else: 
            #recorre la lista hasta llegar a la posicion deseada nodo_anterior = self.primero 
            for posicion in range(1, indice):
                nodo_anterior = nodo_anterior.prox
                #Intercala el nuevo y obtiene nodo_anterior -> nuevo -> nodo_anterior.prox
                nuevo.prox = nodo_anterior.prox
                nodo_anterior.prox = nuevo
                
                #En cualquier caso incrementar en 1 la longitud
        self.len += 1


