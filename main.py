import sys

from parser import Parser
from prepro import PrePro
x = sys.argv[1]
f = open(x,"r")
contents = f.read()
f.close()

# print(contents)
Parser.run(PrePro.filter(contents))