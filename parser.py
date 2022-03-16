from select import select
from tokenizer import Tokenizer
import sys
class Parser:
    tokens= None

    def parseFactor():
        resultado = 0
        if Parser.tokens.actual.type == 'NUMBER':
            resultado += Parser.tokens.actual.value
            Parser.tokens.selectNext()
        
        elif Parser.tokens.actual.type == "PLUS":
            Parser.tokens.selectNext()
            resultado += Parser.parseFactor()
    
        elif Parser.tokens.actual.type == "MINUS":
            Parser.tokens.selectNext()
            resultado -= Parser.parseFactor()
    
        elif Parser.tokens.actual.type == "OPEN_PAREN":
            resultado = Parser.parseExpression()
            if Parser.tokens.actual.type == "CLOSE_PAREN":
                Parser.tokens.selectNext()
            else:
                sys.exit("ERROR: There are open parentheses")
        else:
            sys.exit("ERROR: The code must start with a number, or '+','-','('")
        return resultado


    def parseTerm():

        resultado = Parser.parseFactor()
        while Parser.tokens.actual.type == "TIMES" or Parser.tokens.actual.type == "DIVISION":
            if Parser.tokens.actual.type == "TIMES":
                Parser.tokens.selectNext()
                resultado *=Parser.parseFactor()
            if Parser.tokens.actual.type == "DIVISION":
                Parser.tokens.selectNext()
                resultado //=Parser.parseFactor()
        return resultado


    def parseExpression():
        Parser.tokens.selectNext()
        resultado = Parser.parseTerm()
        
        while Parser.tokens.actual.type == "PLUS" or Parser.tokens.actual.type == "MINUS":
            if Parser.tokens.actual.type == "PLUS":
                Parser.tokens.selectNext()
                resultado += Parser.parseTerm()
            if Parser.tokens.actual.type == "MINUS":
                Parser.tokens.selectNext()
                resultado -= Parser.parseTerm()
        return resultado


    def run(code):
        Parser.tokens = Tokenizer(code)
        v = Parser.parseExpression()
        if Parser.tokens.actual.type !="EOF":
            sys.exit("Error: the compiler didn't finish the code")
        print(v)
        return v