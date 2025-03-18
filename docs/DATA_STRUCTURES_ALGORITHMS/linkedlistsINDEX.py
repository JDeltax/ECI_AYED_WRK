
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, data=[]):
        self.head = None
        self.len = 0
        for e in data:
            self.append(e)

    def __len__(self):
        return self.len

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.len += 1

    def delete_by_index(self, index):
        if index < 0 or index >= self.len:
            raise IndexError("Index out of range")
        
        current = self.head
        if index == 0:
            self.head = current.next
        else:
            prev = None
            for _ in range(index):
                prev = current
                current = current.next
            prev.next = current.next
        
        self.len -= 1
        return current.value

    def compare(self):
        disparador = True
        ltac = []
        current = self.head
        i = 0

        while current is not None and current.next is not None:
            if current.value >= current.next.value:
                pass
            else:
                ltac.append(i + 1)  # Guardar el indice del nodo a eliminar
                disparador = False
            current = current.next
            i += 1
        return ltac, disparador

    def printeo(self):
        current = self.head
        while current:
            print(f"({current.value})", end=" --> ")
            current = current.next
        print("x")
