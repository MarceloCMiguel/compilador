from select import select
from tokenizer import Tokenizer
from node import BinOp,UnOp,IntVal,NoOp
import sys
class Parser:
    tokens= None

    def parseFactor():
        # resultado = 0
        # node = 0
        if Parser.tokens.actual.type == 'NUMBER':
            # resultado += Parser.tokens.actual.value
            node = IntVal(Parser.tokens.actual.value,[])
            Parser.tokens.selectNext()
        
        elif Parser.tokens.actual.type == "PLUS":
            Parser.tokens.selectNext()
            node = UnOp('+',[Parser.parseFactor()])
            # resultado += Parser.parseFactor()
    
        elif Parser.tokens.actual.type == "MINUS":
            Parser.tokens.selectNext()
            node = UnOp('-',[Parser.parseFactor()])
            # resultado -= Parser.parseFactor()
    
        elif Parser.tokens.actual.type == "OPEN_PAREN":
            node = Parser.parseExpression()
            # resultado = Parser.parseExpression()
            if Parser.tokens.actual.type == "CLOSE_PAREN":
                Parser.tokens.selectNext()
            else:
                sys.exit("ERROR: There are open parentheses")
        else:
            sys.exit("ERROR: The code must start with a number, or '+','-','('")
        return node


    def parseTerm():

        node = Parser.parseFactor()
        while Parser.tokens.actual.type == "TIMES" or Parser.tokens.actual.type == "DIVISION":
            if Parser.tokens.actual.type == "TIMES":
                Parser.tokens.selectNext()
                # resultado *=Parser.parseFactor()
                node = BinOp('*',[node,Parser.parseFactor()])
            if Parser.tokens.actual.type == "DIVISION":
                Parser.tokens.selectNext()
                # resultado //=Parser.parseFactor()
                node = BinOp('/',[node,Parser.parseFactor()])
        return node


    def parseExpression():
        Parser.tokens.selectNext()
        # resultado = Parser.parseTerm()
        node = Parser.parseTerm()
        
        while Parser.tokens.actual.type == "PLUS" or Parser.tokens.actual.type == "MINUS":
            if Parser.tokens.actual.type == "PLUS":
                Parser.tokens.selectNext()
                # resultado += Parser.parseTerm()
                node = BinOp('+',[node,Parser.parseTerm()])
            if Parser.tokens.actual.type == "MINUS":
                Parser.tokens.selectNext()
                # resultado -= Parser.parseTerm()
                node = BinOp('-',[node,Parser.parseTerm()])
        return node


    def run(code):
        Parser.tokens = Tokenizer(code)
        node = Parser.parseExpression()
        if Parser.tokens.actual.type !="EOF":
            sys.exit("Error: the compiler didn't finish the code")
        # print(node.value)
        print(node.Evaluate())
        return node