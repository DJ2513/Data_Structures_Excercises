# Ejercicio:
"""Generar una clase ArregloDinamico que herede de Arreglo. 
La clase AgrregloDinamico debe incluir los algoritmos de:
- Agregar
-Eliminar
Con propiedades denámicas (doblar capacidad y reducir la capacidad) que se activen al llenarse o vaciarse a más de la mitad.

Generar pruebas que verifiquen las pruebas de las nuevas funciones."""

class Arreglo:
    def __init__(self, inicial):
        self.capacidad= inicial
        self.arreglo=[0]*self.capacidad
        self.cantidad =0
    def __repr__(self):
        return str(self.arreglo)
    def agregar(self, elemento):
        if self.cantidad<self.capacidad:
            self.arreglo[self.cantidad]= elemento
            self.cantidad+=1
        else:
            print('El arreglo ya está lleno')
            print('No se puedo agregar: ', elemento)
    def eliminar(self):  #Se elimina el último elemento
        if self.cantidad>0:
            self.cantidad-=1
    
class ArregloDinamico (Arreglo):    
    def DoblarCapacidad(self):
        if self.cantidad==self.capacidad:
            temp=[0]
            for i in range(self.cantidad):
                temp[i]= self.cantidad[i]
            self.capacidad*=2
            self.arreglo=[0]*self.capacidad
            for i in range(self.cantidad):
                self.cantidad[i]=temp[i]

a =ArregloDinamico(4)
a.agregar('a')
a.agregar('b')
a.agregar('c')
a.agregar('d')
print(a)
a.DoblarCapacidad
print(a)