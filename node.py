import sys
from symboltable import SymbolTable

class Node():
    #constructor

    def __init__(self, value, children):
        self.value = value
        self.children = children
    
    def Evaluate(self,st):
        pass


class BinOp(Node):
    def __init__(self,value,children):
        super().__init__(value,children)
    def Evaluate(self,st):
        if self.value == '*':
            return self.children[0].Evaluate(st) * self.children[1].Evaluate(st)
        elif self.value == '/':
            return self.children[0].Evaluate(st) // self.children[1].Evaluate(st)

        elif self.value == '+':
            return self.children[0].Evaluate(st) + self.children[1].Evaluate(st)
        elif self.value == '-':
            return self.children[0].Evaluate(st) - self.children[1].Evaluate(st)
        else:
            sys.exit("Error Valuate")

class UnOp(Node):
    def Evaluate(self,st):
        if self.value == '+':
            return self.children[0].Evaluate(st)
        elif self.value == '-':
            return - self.children[0].Evaluate(st)
        sys.exit(f"Error UnOp: {self.value} not supported")

class IntVal(Node):
    
    def Evaluate(self,st):
        return self.value

class NoOp(Node):
    
    def Evaluate(self,st):
        pass  

class Identifier(Node):
    def Evaluate(self,st):
        return st.getter(self.value)

class Assignment(Node):
    def Evaluate(self, st):
        variable_name = self.children[0].value
        value = self.children[1].Evaluate(st)
        st.setter(variable_name,value)

class Print(Node):
    def Evaluate(self, st):
        print(self.children[0].Evaluate(st))

class Block(Node):
    def Evaluate(self, st):
        for children in self.children:
            children.Evaluate(st)


# node = IntVal(5,[])
# node = BinOp('+',[node,node])
# node = UnOp('-',[node])
# print(node.Evaluate())
# return 
