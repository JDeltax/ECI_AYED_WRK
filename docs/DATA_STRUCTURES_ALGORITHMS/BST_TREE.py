#    ______________________________
#   < Deltax & SinXCosX were here... >
#    ------------------------------
#       \
#        \
#                                    .::!!!!!!!:.
#     .!!!!!:.                        .:!!!!!!!!!!!!
#     ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$
#         :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P
#         $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#
#         $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*
#         ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R"
#           "*$bd$$$$      '*$$$$$$$$$$$o+#"
#                """"          """""""
# Juan Pablo Vega Villamil
# Juan Diego Patiño Muñoz

class Node:
    # Constructor de la clase nodo, recibe un valor entero
    # para almacenar como valor y un nodo padre.
    def __init__(self, k: int, parent):
        self.__value = k
        self.__left = None
        self.__right = None
        self.__parent = parent
        self.__times = 1
    
    # Define el nodo de la izquierda
    def set_left (self, to) -> None:
        self.__left = to
    
    # Define el nodo de la derecha
    def set_right(self, to) -> None:
        self.__right = to

    def set_parent (self, to) -> None:
        self.__parent = to
    
    def set_value (self, to) -> None:
        self.__value = to
    
    # Obtiene el valor del nodo
    def get_value(self) -> int:
        return self.__value
    
    # Obtiene el nodo de la derecha
    def get_right(self):
        return self.__right
        
    # Obtiene el nodo de la izquierda
    def get_left(self):
        return self.__left
    
    # Obtiene el padre del nodo
    def get_parent(self):
        return self.__parent

    # Verifica si el nodo tiene al menos un hijo
    def children(self):
        return (self.get_left() != None or self.get_right() != None)
    
class BSTree:
    # Inicializacion del arbol, recibe como root el primer nodo insertado
    def __init__(self, root: Node):
        self.__root = root
        self.__height = 0

    def insert (self, k: int) -> bool:
        thisroot = self.__root
        prevroot = None

        # Recorre el arbol almacenando el parent por el que acabamos de pasar
        # Cuando llegue a un parent sin hijos --> None, entonces ya sabemos que el padre era
        # Prevroot, por ende se le asigna el nodo con el valor k a insertar y se hace el ingreso
        # del nuevo nodo
        while thisroot:
            prevroot = thisroot
            if k < thisroot.get_value():
                thisroot = thisroot.get_left()
            else:
                thisroot = thisroot.get_right()
        # Asigna Nodo
        new = Node(k, prevroot)

        # Evaluacion con k para su respectiva insercion
        if k < prevroot.get_value():
            prevroot.set_left(new)
        else:
            prevroot.set_right(new)
    
    def search (self, k: int) -> tuple:
        # Iniciamos el root a buscar
        thisroot = self.__root
        side = 0
        
        # Mientras que el root contenga un valor y sea diferente al valor buscado, ejecuta el bucle de busqueda
        while thisroot and k != thisroot.get_value():
            
            # Una condicion de parada cuando ya el root es None, es decir el parent que analizamos no tiene hijos
            if thisroot == None:
                return None
            
            # Nuevas asignaciones de thisroot para evaluar por derecha o izquierda respectivamente
            if k > thisroot.get_value():
                thisroot = thisroot.get_right()
                side = 1
            else:
                thisroot = thisroot.get_left()
                side = -1

        return (thisroot, side)

    def delete (self, k: int) -> bool:
        # busca el elemento a eliminar 
        thatroot, at = self.search(k)
        
        # CASOS 1) Si el root no tiene hijos
        if thatroot.get_left() == None and thatroot.get_right() == None:
            parent = thatroot.get_parent()
            if at == 1: parent.set_right(None)
            else: parent.set_left(None)
            thatroot = None

            return True
        
        # CASO 2) Si el root tiene solamente un hijo a la izquierda
        elif thatroot.get_left() != None and thatroot.get_right() == None:
            parent = thatroot.get_parent()
            if at == 1: parent.set_right(thatroot.get_left())
            else: parent.set_left(thatroot.get_left())
            thatroot.get_left().set_parent(parent)
            thatroot = None
            return True
        # CASO 3) Si el root tiene solamente un hijo a la derecha
        elif thatroot.get_left() == None and thatroot.get_right() != None:
            parent = thatroot.get_parent()
            if at == 1: parent.set_right(thatroot.get_right())
            else: parent.set_left(thatroot.get_right())
            thatroot.get_right().set_parent(parent)
            thatroot = None
            return True
        # CASO 4) Si el root tiene 2 hijos.
        else:
            minode = self.__get_min(thatroot.get_right())
            minval = minode.get_value()
            self.delete(minval)
            thatroot.set_value(minval)
            return True

    def get_root (self) -> Node:
        return self.__root
    
    def __get_min (self, root):
        minx = root
        while minx.get_left():
            minx = minx.get_left()
        return minx

    def height(self, root):
        if root is None:
            return -1
        else:
            lt_height = self.height(root.get_left())
            rt_height = self.height(root.get_right())
            return max(lt_height, rt_height) + 1


def main():
    root = Node(31, None)
    tree = BSTree(root)
main()
