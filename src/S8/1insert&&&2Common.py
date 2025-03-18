#Solamente pegue estas lineas en hackerrank en su respectivo campo:

    def insert(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if val < current.info:
                if current.left is None:
                    current.left = new_node
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                else:
                    current = current.right



##################################


def lca(root, v1, v2):
    while root:
        if v1 < root.info and v2 < root.info:
            root = root.left
        elif v1 > root.info and v2 > root.info:
            root = root.right
        else:
            return root
    return None
