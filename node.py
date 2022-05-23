import sys
from symboltable import SymbolTable
from asm import Asm
class Node():
    #constructor

    def __init__(self, value, children):
        self.value = value
        self.children = children
    
    def Evaluate(self,st: SymbolTable, asm: Asm):
        pass


class BinOp(Node):
    def __init__(self,value,children):
        super().__init__(value,children)
    def Evaluate(self,st, asm):
        (value_child1, type_child1, id_child1) =self.children[0].Evaluate(st,asm)
        asm.write("PUSH EBX ;")
        (value_child2, type_child2, id_child2) =self.children[1].Evaluate(st,asm)
        asm.write("POP EAX ;")
        value = 0
        if self.value == '+':
            asm.write("ADD EAX, EBX ;")
            value = value_child1 + value_child2
        elif self.value == '-':
            asm.write("SUB EAX, EBX ;")
            value = value_child1 - value_child2
        elif self.value == '*':
            asm.write("IMUL EAX, EBX ;")
            value = value_child1 * value_child2
        elif self.value == '/':
            asm.write("IDIV EAX, EBX ;")
            value = value_child1 // value_child2
        asm.write("MOV EBX, EAX")
        return (value, 'INT','-1')
        # if (self.value == '.'):
        #     value = str(value_child1) + str(value_child2)
        #     return (value,"STRING")
        
        # value = 0
        # if self.value in ['==','<','>']:
        #     if self.value == '==':
        #             bool_value = value_child1 == value_child2
        #             if bool_value == True:
        #                 value = 1
        #             else:
        #                 value = 0
                    
        #     elif self.value == '<':
        #         bool_value = value_child1 < value_child2
        #         if bool_value == True:
        #             value = 1
        #         else:
        #             value = 0    
        #     elif self.value == '>':
        #         bool_value = value_child1 > value_child2
        #         if bool_value == True:
        #             value = 1
        #         else:
        #             value = 0

        # elif type_child1 == "INT":
        #     if self.value == '*':
        #         value = value_child1 * value_child2
        #     elif self.value == '/':
        #         value = value_child1 // value_child2

        #     elif self.value == '+':
        #         value = value_child1 + value_child2
        #     elif self.value == '-':
        #         value = value_child1 - value_child2
        #     elif self.value == '||':
        #         value = value_child1 or value_child2
        #         if value >0:
        #             value = 1
        #     elif self.value == '&&':
        #         value = value_child1 and value_child2
        #         if value > 0:
        #             value = 1
        #     else:
        #         sys.exit("ERROR BINOP EVALUATE: INT operator f{self.value} invalid")
            
        # elif type_child1 == "STRING":
        #     if self.value == '.':
        #         value = value_child1 + value_child2
        # else:
        #     sys.exit("Error BINOP Evaluate: else trigger")
        # return (value,type_child1)

class UnOp(Node):
    def Evaluate(self,st, asm):
        print(self.children[0].Evaluate(st, asm))
        (value_child, type_child) = self.children[0].Evaluate(st, asm)
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
    def Evaluate(self, st,asm):
        return (self.value,"STR")

class IntVal(Node):
    
    def Evaluate(self,st, asm):
        assembly = f"MOV EBX {self.value} ; EVALUATE DO INTVAL"
        asm.write(assembly)
        return (self.value, "INT","-1")

class VarDec(Node):
    def Evaluate(self, st, asm):
        for child in self.children:
            asm.write("PUSH DWORD 0 ;")
            name = child.value
            st.create(name,self.value)

class NoOp(Node):
    
    def Evaluate(self,st, asm):
        pass  

class Identifier(Node):
    def Evaluate(self,st, asm):
        (value, type_, id) = st.getter(self.value)
        asm.write(f"MOV EBX, [EBP-{id}]")
        return (value, type_, id)

class Assignment(Node):
    def Evaluate(self, st, asm):
        variable_name = self.children[0].value
        value = self.children[1].Evaluate(st, asm)
        st.setter(variable_name,value[0])
        (variable_value,type_,id) =st.getter(variable_name)
        asm.write(f"MOV [EBP-{id}], EBX; resultado da atribuição")



class Print(Node):
    def Evaluate(self, st, asm):
        print(self.children[0].Evaluate(st,asm)[0])

class Block(Node):
    def Evaluate(self, st, asm):
        for children in self.children:
            children.Evaluate(st,asm)

class While(Node):
    def Evaluate(self, st,asm):
        while self.children[0].Evaluate(st,asm)[0]:
            self.children[1].Evaluate(st, asm)

class If(Node):
    def Evaluate(self, st, asm):
        if self.children[0].Evaluate(st, asm)[0]:
            self.children[1].Evaluate(st, asm)
        elif len(self.children)>2:
            self.children[2].Evaluate(st, asm)

class Scanf(Node):
    def Evaluate(self, st, asm):
        var = int(input())
        return (var,"INT")

 

# node = IntVal(5,[])
# node = BinOp('+',[node,node])
# node = UnOp('-',[node])
# print(node.Evaluate())