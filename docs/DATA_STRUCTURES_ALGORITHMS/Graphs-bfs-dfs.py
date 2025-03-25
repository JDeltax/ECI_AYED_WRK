from sys import stdin

class Node:
    def __init__(self, k, color = 'white', time=0):
        self.__value = k
        self.__distance = float('inf')
        self.__color = color
        self.__time = time
        self.__predecesor = None

    def set_value(self, k) -> None:
        self.__value = k

    def get_value(self) -> int:
        return self.__value

    def set_distance(self, d: int) -> None:
        self.__distance = d

    def get_distance(self) -> int:
        return self.__distance

    def set_color(self, c) -> None:
        self.__color = c

    def get_color(self) -> str:
        return self.__color

    def set_time(self, t: int) -> None:
        self.__time = t

    def get_time(self) -> int:
        return self.__time

    def set_predecesor(self, p) -> None:
        if isinstance(p, Node):
            self.__predecesor = p
        #else:
            #raise ValueError("Invalid predecessor")

    def get_predecesor(self):
        return self.__predecesor

class Graph:
    def __init__(self, directed: bool, umatrix: bool):
        self.__arcos = set()
        self.__nodes = set()
        self.__is_directed = directed
        self.__uses_matrix = umatrix
        self.__valuesonly = set()

    def join(self, node1, node2):
        if self.__is_directed:
            self.__arcos.add((node1, node2))
        else:
            self.__arcos.add((node1, node2))
            self.__arcos.add((node2, node1))

        self.__valuesonly.add(node1.get_value())
        self.__valuesonly.add(node2.get_value())

        self.__nodes.add(node1)
        self.__nodes.add(node2)

    def show_connections(self):
        for arco in self.__arcos:
            print(arco[0].get_value(), arco[1].get_value())

    def get_representation(self):
        if self.__uses_matrix:
            return self.__create_matrix()
        else:
            return self.__create_list()

    def __create_matrix(self):
        print("Matriz de adyacencia:")

        # Crear un mapeo del valor del nodo a un índice
        order = {value: index for index, value in enumerate(sorted(self.__valuesonly))}

        # Crear una matriz de tamaño adecuado
        n = len(self.__valuesonly)
        matrix = [[0] * n for _ in range(n)]

        # Llenar la matriz con las aristas
        for arco in self.__arcos:
            row = order[arco[0].get_value()]
            col = order[arco[1].get_value()]
            matrix[row][col] = 1

        # Imprimir la matriz
        for row in matrix:
            print(row)

        return matrix

    def __create_list(self):
        print("Lista de adyacencia:")
        for node in sorted(self.__nodes, key=lambda x: x.get_value()):
            toprint = {arco[1].get_value() for arco in self.__arcos if arco[0].get_value() == node.get_value()}
            print(f"{node.get_value()} : {{", ', '.join(map(str, toprint)), "}")
    # Funcion que retorna las conexiones por nodo
    def get_paths(self,Anode):
        queue = []
        for item in self.__arcos:
            if item[0] == Anode:
                queue.append(item[1])
        return queue

    # Start representa un nodo ---> recuerde que el nodo tiene color --> se le es asignado un color de tres posibles
    # Negro: Visitado, Gtis: En proceso a visitar, Blanco: Sin visitar
    """Funcionamiento algoritmo --> El BFS Funciona manteniendo 3 posibles estados: Visitado, Sin Visitar, En cola
        Se empieza desde el nodo indicado -> lo marca de negro -> Pone en Queue ambas ramas tanto derecha como izquierda (Las marca de gris) -> pasa a la ramas y las marca de negro ->
        Vuelve a realizar el mismo proceso por ramas.
        
        Este proceso se hace rama a rama (En una estructura de datos tipo árbol, qué, también es un grafo)""
        Tocaría primero extraer todas las conexiones que nazcan del nodo --> digamos que se quiere empezar de un nodo A
        entonces, de todas las parejas de Nodos (arcos) de la forma (A,X) -> se extrae el X para lista de enqeue
        ejemplo
        (A,B) (A,C) (A,D) ---> ENQEUE [B,C,D] ---> Como es nivel a nivel, entonces se hace uno a uno el recorrido -> Recorremos una vez y nada más que una vez para obtener otro nivel en
        B, C y D. Así;

        Si (B,E) (B,F) (B,K) ---> ENQEUE [E,F,K]  De aqui se analiza E y en C ya pasará a ser visitado, por ende, se omite
        si (C,E) (C,H) (C,N) ---> ENQEUE [E,H,N]     
        si (D,E) (D,V) (D,B) ---> ENQEUE [E,V,B]  --> B ya fué visitado ¿Que procede Hacer? --> ¿INFINITAS MANERAS?
        
        """
    def bfs(self, s,target):
        toret = []
        for u in self.__nodes:
            u.set_color("White")
        s.set_color("Gray")
        q = []
        q.append(s)
        while q:
            u = q[0]
            q.pop(0)
            #if u == target:
                #return True
            for v in self.get_paths(u):
                if v.get_color() == "White":
                    v.set_color("Gray")
                    q.append(v)
            u.set_color("Black")
            toret.append(u.get_color())
        return toret

    def dfs(self):
        time = [0] 
        for u in self.__nodes:
            u.set_color("White")
            u.set_predecesor(None)

        for u in sorted(self.__nodes, key=lambda x: x.get_value()):
            if u.get_color() == "White":
                self.dfs_visit(u, time)

    def dfs_visit(self, u, time):
        time[0] += 1
        u.set_time(time[0])  # Discovery time
        u.set_color("Gray")

        for v in sorted(self.get_paths(u), key=lambda x: x.get_value()):
            if v.get_color() == "White":
                v.set_predecesor(u)
                self.dfs_visit(v, time)

        u.set_color("Black")
        time[0] += 1
        u.set_time(time[0]) 




def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    g = Graph(False, False) 
    g.join(node1, node2)
    g.join(node2, node3)
    g.join(node3, node4)
    g.join(node1, node4)

    g.dfs()

    # muestra los tiempos de finalizacion
    # for node in [node1, node2, node3, node4]:
        # print(f"Node {node.get_value()}: Time = {node.get_time()}, Color = {node.get_color()}")

    g.get_representation()
main()
