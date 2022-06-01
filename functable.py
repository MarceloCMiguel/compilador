import sys
class FuncTable:
    
    table = {}

    def getter(name):
        if name in FuncTable.table:
            return FuncTable.table[name]
        sys.exit(f"ERROR FUNCTABLE: variable {name} not in dict")
    
    def create(name,address):
        if name in FuncTable.table:
            sys.exit(f"ERROR FUNCTABLE: function {name} already created")
        
        FuncTable.table[name] = address
        # else:
        #     sys.exit(f"ERROR SYMBOLTABLE: type {type_} invalid")

    # def setter(self,name,value):
        # if name not in self.table:
        #     sys.exit(f"ERROR SYMBOLTABLE: setter invalid name")
        # type_in_dict = self.table[name][1]
        # if type_in_dict == "STRING":
        #     if type(value) == str:
        #         self.table[name] = (value, "STRING")
        #     else:
        #         sys.exit(f"ERROR SYMBOLTABLE STRING: setter value {value} invalid for type {type_in_dict}")
        # elif type_in_dict == "INT":
        #     if type(value) == int:
        #         self.table[name] = (value,"INT")
        #     else:
        #         sys.exit(f"ERROR SYMBOLTABLE INT: setter value {value} invalid for type {type_in_dict}")
        # else:
        #     sys.exit(f"ERROR SYMBOLTABLE: setter variable {name} error")