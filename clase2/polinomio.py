class Nodo: # TERMINO 
        def __init__(self, coeficiente= None, grado= None, prox=None):
            self.coeficiente = coeficiente
            self.grado = grado
            self.prox = prox

        def __str__(self):
            return str(f"{self.coeficiente} x {self.grado}")



class Polinomio(object):
    "Modela una polinomio, compuesta por terminos"

    def __init__(self):
        #crea una polinomio vacio

        #apuntara al primero nodo - None con la lista vacia
        self.primero = None # El termino de mayor grado

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

    def addTermino(self, coeficiente, potencia):
        """Inserta el elemento x en la posicion indice.
        si la posicion es invalida, levanta un error"""

        nuevo = Nodo(coeficiente, potencia) #en el ejemplo llevaba parentesis

        #insertar al final (caso particular)
        if potencia == 0:
            #El siguiente del ultimo pasa a ser el nuevo nodo
            #buscamos el ultimo termino
            actual = self.primero
            while actual.prox != None:
                actual = actual.prox

        # Llegamos al final de la lista e insertamos el termino aca
            actual.proximo = nuevo
        
        # Insertar en cualquier lugar mas al frente, potencia != 0
        else:       
            actual = self.primero

            ################################## MINUTO  3:32 ########################
        
        #Insertar en cualquier lugar > 0 
        # else: 
        #     #recorre la lista hasta llegar a la posicion deseada nodo_anterior = self.primero 
        #     for posicion in range(1, indice):
        #         nodo_anterior = nodo_anterior.prox
        #         #Intercala el nuevo y obtiene nodo_anterior -> nuevo -> nodo_anterior.prox
        #         nuevo.prox = nodo_anterior.prox
        #         nodo_anterior.prox = nuevo
                
        #         #En cualquier caso incrementar en 1 la longitud
        # self.len += 1


