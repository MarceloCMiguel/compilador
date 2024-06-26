import sys

class SymbolTable():
    def __init__(self) -> None:
        self.table = {}
        self.id = 0

    def getter(self,name):
        if name in self.table:
            return self.table[name]
        sys.exit(f"ERROR SYMBOLTABLE: variable {name} not in dict")
    
    def create(self,name,type_):
        if name in self.table:
            sys.exit(f"ERROR SYMBOLTABLE: variable {name} already created")
        if type_ == "STRING" or type_ == "INT":
            self.id += 4
            self.table[name] = (None,type_, self.id)
        else:
            sys.exit(f"ERROR SYMBOLTABLE: type {type_} invalid")

    def setter(self,name,value):
        if name not in self.table:
            sys.exit(f"ERROR SYMBOLTABLE: setter invalid name")
        type_in_dict = self.table[name][1]
        id_in_dict = self.table[name][2]
        if type_in_dict == "STRING":
            if type(value) == str:
                self.table[name] = (value, type_in_dict, id_in_dict)
            else:
                sys.exit(f"ERROR SYMBOLTABLE STRING: setter value {value} invalid for type {type_in_dict}")
        elif type_in_dict == "INT":
            if type(value) == int:
                self.table[name] = (value,type_in_dict, id_in_dict)
            else:
                sys.exit(f"ERROR SYMBOLTABLE INT: setter value {value} invalid for type {type_in_dict}")
        else:
            sys.exit(f"ERROR SYMBOLTABLE: setter variable {name} error")