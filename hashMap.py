class Mapa:
    '''Recibe el tamaño del Mapa'''
    def __init__(self, n: int) -> None:
        self.buckets=[[] for _ in range(n)] #El _ es una variable que no usaras en otro lugar, simplemente recorre el arreglo.
        self.n =n
    def insertar(self, elemento):
        posicion= hash(elemento)%self.n
        self.buckets[posicion].append(elemento)
    def buscar(self, elemento):
        posicion= hash(elemento)%self.n
        casilla= self.buckets[posicion]
        if elemento in casilla:
            return True
        else:
            return False

            #Las famosas 'Funciones Mágicas'

    def __getitem__(self, elemento):
        return self.buscar(elemento)  #Te permite Buscar de una manera mas eficiente.
    def __contains__(self, elemento):
        return self.buscar(elemento)  #Te permite usar la Palabra "In" en la busqueda del elemento.

from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str
    edad: int

    def __hash__(self) -> int:
        return hash(self.nombre)+hash(self.edad)
    

m= Mapa(10)
print(m.buckets)
m.insertar("Armando")
m.insertar(1.1)
m.insertar(254)
m.insertar(Persona("Daniel", 19))
print(m.buckets)
print(m.buscar("Daniel"))
print(m.buscar(Persona("Daniel", 19)))
print(m.buscar(1.1))
print(m.buscar(9999))
#Las siguentes lineas vienen del  def __getitem__
print(m["Armando"])
print(m[1.2])
#Las siguientes lineas vienen del def __contains__
print("Armando" in m)
print(253 in m)