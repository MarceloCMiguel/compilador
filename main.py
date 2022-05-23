import sys

from parser import Parser
from unicodedata import name
from asm import Asm
from prepro import PrePro
from symboltable import SymbolTable
x = sys.argv[1]
name_file = x[:-2]
name_file+=".asm"
f = open(x,"r")
contents = f.read()
f.close()
# print(contents)
node = Parser.run(PrePro.filter(contents))
st = SymbolTable()
asm = Asm(name_file)
node.Evaluate(st, asm)
asm.dump()
