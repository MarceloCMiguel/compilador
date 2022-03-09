import sys

from parser import Parser
from prepro import PrePro
x = sys.argv[1]

Parser.run(PrePro.filter(x))