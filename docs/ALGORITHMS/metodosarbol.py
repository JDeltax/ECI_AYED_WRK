"""def rotateLeft(self):
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
    # Rightmost corner case
    if avl > 1 and right.getRoot() <= lastValue:  # Unbalanced Right
        self.rotateLeft()
    if avl > 1 and right.getRoot() > lastValue:  # Unbalanced Right
        self.rotateRightLeft()
    # Leftmost corner case
    if avl < -1 and left.getRoot() > lastValue:  # Unbalanced Left
        self.rotateRight()
    if avl < -1 and left.getRoot() <= lastValue:  # Unbalanced Left
        self.rotateLeftRight()
    self.setHeight()
    self.setAVL()

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
"""