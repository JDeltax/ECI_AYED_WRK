"""La idea es utilizar la pila como estructura de datos para ir pusheando los
valores y popeando los mismos si se encuentran claves, si al final la pila es vacia
entonces estara organizado, de resto pues no
y mas alla de eso es el hecho de que al popear un elemento debe tener otro
esperado que se debe encontrar el la pila
si esto no sucede, pues hay error

JUAN PABLO VEGA VILLAMIL
"""



from sys import stdin 

class Stack:
    def __init__(self):
        self.pStack = []
    
    def push(self, Element):
        self.pStack.append(Element)  # Agregar al final
    
    def pop(self):
        if self.pStack:
            return self.pStack.pop()  # Sacar el ultimo elemento
    
    def peek(self):
        return self.pStack[-1] if self.pStack else None  # Ver el ultimo elemento
    
    def is_empty(self):
        return len(self.pStack) == 0  # Ver si la pila esta vacia



def check(s):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}  #VALOR/CLAVE IDEA DE IAGEN

    for char in s:
        if char in pairs.values():  # Si es un parentesis de apertura
            stack.push(char)
        elif char in pairs.keys():  # Si es un parentesis de cierre
            if stack.is_empty() or stack.pop() != pairs[char]:  
                return "NO"
    
    return "YES" if stack.is_empty() else "NO"

def main():
    q = int(stdin.readline().strip())  # Numero de casos
    for _ in range(q):
        s = stdin.readline().strip()
        print(check(s))

main()
