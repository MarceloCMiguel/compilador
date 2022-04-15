import sys

from parser import Parser
from prepro import PrePro
from symboltable import SymbolTable
x = sys.argv[1]
f = open(x,"r")
contents = f.read()
f.close()
# print(contents)
node = Parser.run(PrePro.filter(contents))
st = SymbolTable()
node.Evaluate(st)