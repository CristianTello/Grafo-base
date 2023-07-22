class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = []

    def agregar_arista(self, origen, destino):
        if origen in self.grafo:
            self.grafo[origen].append(destino)
        else:
            self.grafo[origen] = [destino]

        if destino not in self.grafo:
            self.grafo[destino] = []

    def obtener_nodos(self):
        return list(self.grafo.keys())

    def obtener_aristas(self):
        aristas = []
        for nodo, destinos in self.grafo.items():
            for destino in destinos:
                aristas.append((nodo, destino))
        return aristas

    def __str__(self):
        return str(self.grafo)

# Crear un grafo, agregar nodos y aristas
mi_grafo = Grafo()
mi_grafo.agregar_nodo("A")
mi_grafo.agregar_nodo("B")
mi_grafo.agregar_nodo("C")
mi_grafo.agregar_arista("A", "B")
mi_grafo.agregar_arista("A", "C")
mi_grafo.agregar_arista("B", "C")

# Obtener los nodos y aristas
nodos = mi_grafo.obtener_nodos()
aristas = mi_grafo.obtener_aristas()

print("Nodos:", nodos)
print("Aristas:", aristas)

# Impresión
print("Representación del grafo:")
print(mi_grafo)