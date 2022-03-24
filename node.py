import sys


class Node():
    #constructor
    def __init__(self, value, children):
        self.value = value
        self.children = children
    
    def Evaluate(self):
        pass


class BinOp(Node):
    def __init__(self,value,children):
        super().__init__(value,children)
    def Evaluate(self):
        if self.value == '*':
            return self.children[0].Evaluate() * self.children[1].Evaluate()
        elif self.value == '/':
            return self.children[0].Evaluate() // self.children[1].Evaluate()

        elif self.value == '+':
            return self.children[0].Evaluate() + self.children[1].Evaluate()
        elif self.value == '-':
            return self.children[0].Evaluate() - self.children[1].Evaluate()
        else:
            sys.exit("Error Valuate")

class UnOp(Node):
    def Evaluate(self):
        if self.value == '+':
            return self.children[0].Evaluate()
        elif self.value == '-':
            return - self.children[0].Evaluate()
        sys.exit(f"Error UnOp: {self.value} not supported")

class IntVal(Node):
    
    def Evaluate(self):
        return self.value

class NoOp(Node):
    
    def Evaluate(self):
        pass  

# node = IntVal(5,[])
# node = BinOp('+',[node,node])
# node = UnOp('-',[node])
# print(node.Evaluate())
# return 
