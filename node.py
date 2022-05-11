import sys
from symboltable import SymbolTable

class Node():
    #constructor

    def __init__(self, value, children):
        self.value = value
        self.children = children
    
    def Evaluate(self, st):
        pass


class BinOp(Node):
    def __init__(self,value,children):
        super().__init__(value,children)
    def Evaluate(self,st):
        (value_child1, type_child1) = self.children[0].Evaluate(st)
        (value_child2, type_child2) = self.children[1].Evaluate(st)
        if (type_child1 != type_child2 and self.value != '.'):
            sys.exit("ERROR BINOP EVALUEATE:")
        if (self.value == '.'):
            value = str(value_child1) + str(value_child2)
            return (value,"STRING")
        
        value = 0
        if self.value in ['==','<','>']:
            if self.value == '==':
                    bool_value = value_child1 == value_child2
                    if bool_value == True:
                        value = 1
                    else:
                        value = 0
                    
            elif self.value == '<':
                bool_value = value_child1 < value_child2
                if bool_value == True:
                    value = 1
                else:
                    value = 0    
            elif self.value == '>':
                bool_value = value_child1 > value_child2
                if bool_value == True:
                    value = 1
                else:
                    value = 0

        elif type_child1 == "INT":
            if self.value == '*':
                value = value_child1 * value_child2
                return (value,value_child1)
            elif self.value == '/':
                value = value_child1 // value_child2

            elif self.value == '+':
                value = value_child1 + value_child2
            elif self.value == '-':
                value = value_child1 - value_child2
            elif self.value == '||':
                value = value_child1 or value_child2
                if value >0:
                    value = 1
            elif self.value == '&&':
                value = value_child1 and value_child2
                if value > 0:
                    value = 1
            else:
                sys.exit("ERROR BINOP EVALUATE: INT operator f{self.value} invalid")
            
        elif type_child1 == "STRING":
            if self.value == '.':
                value = value_child1 + value_child2
        else:
            sys.exit("Error BINOP Evaluate: else trigger")
        return (value,type_child1)

class UnOp(Node):
    def Evaluate(self,st):
        (value_child, type_child) = self.children[0].Evaluate(st)
        if type_child == "STRING":
            sys.exit(f"ERROR EVALUATE UNOP: STRING type don't support this operation")
        if self.value == '+':
            return (value_child, type_child)
        elif self.value == '-':
            return (- value_child, type_child)
        elif self.value == '!':
            return  (not value_child, type_child)
        sys.exit(f"Error UnOp: {self.value} not supported")

class StrVal(Node):
    def Evaluate(self, st):
        return (self.value,"STR")

class IntVal(Node):
    
    def Evaluate(self,st):
        return (self.value,"INT")

class VarDec(Node):
    def Evaluate(self, st):
        for child in self.children:
            name = child.value
            st.create(name,self.value)

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
        st.setter(variable_name,value[0])

class Print(Node):
    def Evaluate(self, st):
        print(self.children[0].Evaluate(st)[0])

class Block(Node):
    def Evaluate(self, st):
        for children in self.children:
            children.Evaluate(st)

class While(Node):
    def Evaluate(self, st):
        while self.children[0].Evaluate(st)[0]:
            self.children[1].Evaluate(st)

class If(Node):
    def Evaluate(self, st):
        if self.children[0].Evaluate(st)[0]:
            self.children[1].Evaluate(st)
        elif len(self.children)>2:
            self.children[2].Evaluate(st)

class Scanf(Node):
    def Evaluate(self, st):
        return int(input())

 

# node = IntVal(5,[])
# node = BinOp('+',[node,node])
# node = UnOp('-',[node])
# print(node.Evaluate())
# return 
