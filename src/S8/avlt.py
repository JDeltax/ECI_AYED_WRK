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
#
#
# Arbol AVL de balanceo

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
    
class AVLTree:
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


        current = new
        while current:
            current = self.balance(current)  # Aplica balanceo
            if current.get_parent() is None:
                self.__root = current  # Si la raíz cambió después de una rotación, actualizarla
            current = current.get_parent()  # Subir al padre para seguir balanceando

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
        
    def inorder(self, root, result = None):
        if result is None:
            result = []  # Inicializar la lista en la primera llamada

        if root is None:
            return result  # Devolver la lista cuando no hay más nodos

        # Primero, visitar la izquierda
        self.inorder(root.get_left(), result)

        # Luego, agregar el valor actual a la lista
        result.append(root.get_value())

        # Finalmente, visitar la derecha
        self.inorder(root.get_right(), result)

        return result  # Devuelve la lista con los valores del arbol

    def preorder(self, root, result = None):
        if result is None:
            result = []
        
        if root is None:
            return result # Devolver la lista cuando no hay más nodos
        
        """ Primero se añade el root, de ahí en adelante, visitar izquierdas y derechas"""

        result.append(root.get_value())

        # Primero Visitar la izquierda
        self.preorder(root.get_left(), result)

        # Finalmente, visitar la derecha 
        self.preorder(root.get_right(), result)

        return result
    
    def postorder(self, root, result = None):
        if result == None:
            result = []
        
        if root is None:
            return result
        
        # Primero visita la izquierda
        self.postorder(root.get_left(), result)
        

        # Visitamos la derecha
        self.postorder(root.get_right(), result)

        # Añadimos valores
        result.append(root.get_value())

        return result

    def setAVL(self, node):
        """Calcula el factor de balance de cada nodo en el árbol."""
        if node is None:
            return

        # Aplicar recursión a la izquierda y derecha
        self.setAVL(node.get_left())
        self.setAVL(node.get_right())

        # Calcular el factor de balance del nodo actual
        left_height = self.height(node.get_left())
        right_height = self.height(node.get_right())
        node.balance_factor = right_height - left_height

    def getAVL(self, node):
        """Obtiene el factor de balance de un nodo."""
        return node.balance_factor if node else 0

    def rotateLeft(self, node):
        """Rotación simple a la izquierda."""
        if node is None or node.get_right() is None:
            return node  # No se puede rotar si no hay subárbol derecho

        right_child = node.get_right()
        node.set_right(right_child.get_left())

        if right_child.get_left():
            right_child.get_left().set_parent(node)

        right_child.set_parent(node.get_parent())

        if node.get_parent() is None:
            self.__root = right_child
        elif node == node.get_parent().get_left():
            node.get_parent().set_left(right_child)
        else:
            node.get_parent().set_right(right_child)

        right_child.set_left(node)
        node.set_parent(right_child)

        return right_child  # Retorna la nueva raíz del subárbol

    def rotateRight(self, node):
        """Rotación simple a la derecha."""
        if node is None or node.get_left() is None:
            return node  # No se puede rotar si no hay subárbol izquierdo

        left_child = node.get_left()
        node.set_left(left_child.get_right())

        if left_child.get_right():
            left_child.get_right().set_parent(node)

        left_child.set_parent(node.get_parent())

        if node.get_parent() is None:
            self.__root = left_child
        elif node == node.get_parent().get_left():
            node.get_parent().set_left(left_child)
        else:
            node.get_parent().set_right(left_child)

        left_child.set_right(node)
        node.set_parent(left_child)

        return left_child  # Retorna la nueva raíz del subárbol

    def rotateLeftRight(self, node):
        """Rotación doble izquierda-derecha."""
        if node is None:
            return node

        node.set_left(self.rotateLeft(node.get_left()))
        return self.rotateRight(node)

    def rotateRightLeft(self, node):
        """Rotación doble derecha-izquierda."""
        if node is None:
            return node

        node.set_right(self.rotateRight(node.get_right()))
        return self.rotateLeft(node)

    def balance(self, node):
        """Balancea el árbol después de la inserción/eliminación."""
        if node is None:
            return node

        self.setAVL(node)  # Actualiza los factores de balance
        balance_factor = self.getAVL(node)

        # Casos de desbalance
        if balance_factor > 1:  # Desbalance hacia la derecha
            if self.getAVL(node.get_right()) >= 0:
                return self.rotateLeft(node)  # Rotación simple izquierda
            else:
                return self.rotateRightLeft(node)  # Rotación doble derecha-izquierda

        if balance_factor < -1:  # Desbalance hacia la izquierda
            if self.getAVL(node.get_left()) <= 0:
                return self.rotateRight(node)  # Rotación simple derecha
            else:
                return self.rotateLeftRight(node)  # Rotación doble izquierda-derecha

        return node  # Si no hay desbalance, devuelve el nodo tal cual



def main():
    """
    #CASO 1

    tree = AVLTree(Node(50, None))
    tree.insert(30)
    tree.insert(70)
    tree.insert(20)
    tree.insert(40)
    tree.insert(60)
    tree.insert(80)
    tree.insert(10)
    tree.insert(25)
    tree.insert(35)
    tree.insert(45)
    tree.insert(55)
    tree.insert(65)
    tree.insert(75)
    tree.insert(85)

    print("Inorder:", tree.inorder(tree.get_root()))  # Para verificar el orden
    print("Preorder:", tree.preorder(tree.get_root()))  # Para ver la estructura del árbol
    print("Postorder:", tree.postorder(tree.get_root()))  # Para ver cómo se visitan los nodos
    """  
    tree = AVLTree(Node(10, None))
    tree.insert(20)
    tree.insert(30)

    print("Inorder:", tree.inorder(tree.get_root()))  
    print("Preorder:", tree.preorder(tree.get_root()))  
    print("Postorder:", tree.postorder(tree.get_root()))  

main()