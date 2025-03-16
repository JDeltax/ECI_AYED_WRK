from random import randint
class BinaryTree:
    def __init__(self, root = None):
        self.clear()
        self.setRoot(root)

    def clear(self):
        self.setRoot(None)
        self.setRight(None)
        self.setLeft(None)
        self.setParent(None)
        self.setHeight()
        self.setAVL()

    def insertMany(self, elements = []):
        for e in elements:
            self.insert(e)
    
    def getRoot(self):
        return self.root
    
    def setRoot(self, value):
        self.root = value
    
    def isEmpty(self):
        return self.root is None
    
    def isLeaf(self):
        return self.left is None and self.right is None
    
    def setLeft(self, tree):
        if isinstance(tree, BinaryTree) or tree is None :
            self.left = tree
    
    def setRight(self, tree):
        if isinstance(tree, BinaryTree) or tree is None :
            self.right = tree
    
    def setParent(self, tree):
        if isinstance(tree, BinaryTree) or tree is None :
            self.parent = tree
    
    def getRight(self):
        return self.right
    
    def getLeft(self):
        return self.left
    
    def getParent(self):
        return self.parent
    
    def getHeight(self):
        return self.height
    
    def setHeight(self):
        if self.isEmpty() :
            self.height = 0
        else:
            left, right = self.left, self.right
            if left : left.setHeight()
            if right : right.setHeight()
            leftHeight, rightHeight = 0 if left is None else left.getHeight(), 0 if right is None else right.getHeight()
            self.height = 1 + max(leftHeight, rightHeight)

            
    def setAVL(self):
        if self.isEmpty():
            self.avl = 0
        else:
            left, right = self.left, self.right
            if left : left.setAVL()
            if right : right.setAVL()
            leftHeight, rightHeight = 0 if left is None else left.getHeight(), 0 if right is None else right.getHeight()
            self.avl = rightHeight - leftHeight

    def getAVL(self):
        return self.avl
        
        
    def __str__(self):
        preorder, inorder = [], []
        self.preOrder(preorder)
        self.inOrder(inorder)
        return "BinTree("+str(list(map(str,preorder)))+", "+str(list(map(str,inorder)))+" )"
    
    def insert(self, value):
        if self.isEmpty():
            self.setRoot(value)
        else:
            root, left, right = self.getRoot(), self.left, self.right
            direction = value >= root
            treeToInsert = right if direction else left
            if treeToInsert is None:
                #Crear el nuevo arbol binario
                treeToInsert = BinaryTree()
                treeToInsert.insert(value)
                if direction:
                    self.setRight(treeToInsert)
                else:
                    self.setLeft(treeToInsert)
            else:
                treeToInsert.insert(value)
        self.setHeight()
        self.setAVL()
        if abs(self.getAVL()) > 1:
            self.balance(value)
        self.setHeight()
        self.setAVL()
        
    def search(self, value):
        if not self.isEmpty():
            if self.getRoot() == value:
                return self
            else:
                root, left, right = self.getRoot(), self.left, self.right
                direction = value > root
                treeToSearch = right if direction else left
                if treeToSearch is not None:
                    return treeToSearch.search(value)
        return None
    
    def maximum(self):
        print(self.getRight())
        

    def minimum(self):
        self.root = self.getRoot()        

    """
    def preOrder(self, buffer = []):

    def posOrder(self, buffer = []):

    def inOrder(self, buffer = []):
    """

    #_________________

def rotateLeft(self):
    root, left, right, avl, rl = self.getRoot(), self.left, self.right, self.avl, self.right.getLeft()
    self.setRoot(right.getRoot())
    self.setRight(right.getRight())
    self.setLeft(BinaryTree(root))
    self.left.setRight(rl)
    self.left.setLeft(left)
    self.setHeight()
    self.setAVL()


def rotateRight(self):
    root, left, right, avl, lr = self.getRoot(), self.left, self.right, self.avl, self.left.getRight()
    self.setRoot(left.getRoot())
    self.setLeft(left.getLeft())
    self.setRight(BinaryTree(root))
    self.right.setLeft(lr)
    self.right.setRight(right)
    self.setHeight()
    self.setAVL()


def rotateLeftRight(self):
    root, left, right, avl = self.getRoot(), self.left, self.right, self.avl
    # Rotate Right
    lRoot, lvr, lvl, ll = left.getRoot(), left.right.right, left.right.left, left.left
    left.setRoot(left.right.getRoot())
    left.setLeft(BinaryTree(lRoot))
    left.setRight(lvr)
    left.left.setLeft(ll)
    left.left.setRight(lvl)
    self.rotateRight()


def rotateRightLeft(self):
    root, left, right, avl = self.getRoot(), self.left, self.right, self.avl
    # Rotate Right
    rRoot, rr, lvr, lvl = right.getRoot(), right.right, right.left.right, right.left.left
    right.setRoot(right.left.getRoot())
    right.setRight(BinaryTree(rRoot))
    right.setLeft(lvl)
    right.right.setLeft(lvr)
    right.right.setRight(rr)
    self.rotateLeft()


def balance(self, lastValue):
    root, left, right, avl = self.getRoot(), self.left, self.right, self.avl
    #Rightmost corner case
    if avl > 1 and right.getRoot() <= lastValue:#Unbalanced Right
        self.rotateLeft()
    if avl > 1 and right.getRoot() > lastValue:  # Unbalanced Right
        self.rotateRightLeft()
        #Leftmost corner case
    if avl < -1 and left.getRoot() > lastValue: #Unbalanced Left
        self.rotateRight()
    if avl < -1 and left.getRoot() <= lastValue: #Unbalanced Left
        self.rotateLeftRight()
        self.setHeight()
        self.setAVL()
def printTree(tree):
    pre, inO, pos = [], [], []
    tree.preOrder(pre)
    tree.inOrder(inO)
    tree.posOrder(pos)
    print("PreOrder", pre)
    print("InOrder", inO)
    print("PosOrder", pos)
    print("height", tree.getHeight())
    print("AVL Factor", tree.getAVL())
def main():
    rand = [randint(0,100) for i in range(30)]
    tree = BinaryTree()
    tree.insertMany(rand)
    for val in rand:
        t = tree.search(val)
        print(t, 'AVL:', t.getAVL(), 'Height:', t.getHeight())
    print(tree, tree.getAVL())
main()