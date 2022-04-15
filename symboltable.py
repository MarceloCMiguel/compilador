import sys

class SymbolTable():
    def __init__(self) -> None:
        self.table = {}

    def getter(self,name):
        if name in self.table:
            return self.table[name]
        sys.exit(f"ERROR SYMBOLTABLE: variable {name} not in dict")
    
    def setter(self,name,value):
        
        self.table[name]= value