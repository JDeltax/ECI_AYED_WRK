class Stack:
    def _init_(self, n: int) -> None:
        assert n > 0
        self.top: int = -1
        self.items: list[str | None] = [None] * n

    def is_empty(self) -> bool: # T(n) = O(1)
        if self.top == -1:
            return True
        else:
            return False

    def is_full(self) -> bool: # T(n) = O(1)
        return self.top + 1 == len(self.items)

    def push(self, x: str): # T(n) = O(1)
        assert not self.is_full()

        self.top += 1
        self.items[self.top] = x

    def pop(self) -> str: # T(n) = O(1)
        assert not self.is_empty()

        self.top -= 1
        v =  self.items[self.top + 1]
        assert v is not None
        return v

    # en vez de crear un stack nuevo, podemos resetearlo para que sea vacio en O(1)
    def clear(self):
        self.top = -1

    def _str_(self) -> str:
        return f"Stack(top: {self.top} - array: {self.items[0: max(self.top+1, 0)]})"
    

    #OR
    class Stack:
        def __init__(self, a):
            self.pStack = a[::-1]
        def push(self, Element):
            self.pStack.append(Element)
        def pop(self):
            if len(self.pStack) == 0:
                return
            self.pStack.pop(len(self.pStack)-1)
        def getlast(self):
            if len(self.pStack) == 0:
                return float('inf')
            return self.pStack[-1]
        def show(self):
            print(*self.pStack)
        def size(self):
            return len(self.pStack)
    
