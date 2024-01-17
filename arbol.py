class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.padre = None
        self.hijos = list()

    def __repr__(self):
        return str(self.valor)


class Arbol:
    def __init__(self, nodo):
        self.raiz = nodo

    def es_ancestro(self, ancestro, descendiente):
        explorador = descendiente
        while True:
            if explorador is ancestro:
                return True
            if explorador is self.raiz:
                break
            explorador = explorador.padre
        return False

    def es_decendiente(self, descendiente, ancestro):
        return self.es_ancestro(ancestro, descendiente)

    def lista_ancestros(self, nodo):
        resultado = 1
        # Agregar a los demas ancestros
        while True:
            if nodo is not self.raiz:
                resultado += 1
                nodo = nodo.padre
            if nodo is self.raiz:
                resultado += 1
                break
        return resultado


def padre_hijo(n1, n2):
    n1.hijos.append(n2)
    n2.padre = n1


def es_hoja(nodo):
    return not nodo.hijos


def es_hijo(hijo, padre):
    return hijo in padre.hijo


def es_padre(padre, hijo):
    return hijo.padre is padre


def enlistar_nodos(nodo):
    lista = [nodo]
    for hijo in nodo.hijos:
        lista += enlistar_nodos(hijo)
    return lista


def altura(nodo):
    contador = 0
    if nodo.hijos:
        contador += 1
        for i in nodo.hijos:
            altura(i)
    return contador


def profundidad(nodo):
    contador = 0
    while True:
        if nodo.padre:
            nodo = nodo.padre
            contador += 1
        else:
            break
    return contador
