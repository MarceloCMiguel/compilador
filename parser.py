from select import select
from tokenizer import Tokenizer
from node import BinOp,UnOp,IntVal,NoOp,Assignment,Block,Identifier,Print
import sys
class Parser:
    tokens= None



    def parseBlock():
        
        if Parser.tokens.actual.type == 'OPEN_BRACKETS':
            Parser.tokens.selectNext()
            lista_node = []
            while Parser.tokens.actual.type !='CLOSE_BRACKETS':
                node = Parser.parseStatement()
                lista_node.append(node)
            node = Block('Block',lista_node)
            Parser.tokens.selectNext()
            return node
        else:
            sys.exit("ERROR PARSER BLOCK: Open Brackets not find")
        


    def parseStatement():
        if Parser.tokens.actual.type == 'SEMICOLON':
            node = NoOp('',[])
            Parser.tokens.selectNext()
        if Parser.tokens.actual.type == 'IDENTIFIER':
            node = Identifier(Parser.tokens.actual.value,[])
            Parser.tokens.selectNext()
            if Parser.tokens.actual.type == 'EQUAL':
                Parser.tokens.selectNext()
                node = Assignment('=',[node,Parser.parseExpression()])
                if Parser.tokens.actual.type == 'SEMICOLON':
                    Parser.tokens.selectNext()
                    return node
                else:
                    sys.exit(f"ERROR STATEMENT: Expected SEMICOLON, readed {Parser.tokens.actual.type} {Parser.tokens.actual.value} ")

        elif Parser.tokens.actual.type == 'PRINT':
            Parser.tokens.selectNext()
            if Parser.tokens.actual.type == 'OPEN_PAREN':
                Parser.tokens.selectNext()
                node = Print('Print',[Parser.parseExpression()])
                if Parser.tokens.actual.type == 'CLOSE_PAREN':
                    Parser.tokens.selectNext()
                    if Parser.tokens.actual.type == 'SEMICOLON':
                        Parser.tokens.selectNext()
                        return node
                    else:
                        sys.exit(f"ERROR STATEMENT: Expected SEMICOLON, readed {Parser.tokens.actual.type} {Parser.tokens.actual.value} ")
                else:
                    sys.exit(f"ERROR STATEMENT: There are open parentheses {Parser.tokens.actual.value}")
            else:
                sys.exit("ERROR STATEMENT: no open parentheses find")
        else:
            sys.exit(f"ERROR STATEMENT: Token {Parser.tokens.actual.type} not valid")

    def parseExpression():
        
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
        elif Parser.tokens.actual.type == "IDENTIFIER":
            node = Identifier(Parser.tokens.actual.value, [])
            Parser.tokens.selectNext()
        else:
            sys.exit("ERROR: The code must start with a number, or '+','-','('")
        return node



    def run(code):
        Parser.tokens = Tokenizer(code)
        Parser.tokens.selectNext()
        node = Parser.parseBlock()
        if Parser.tokens.actual.type !="EOF":
            sys.exit("Error: the compiler didn't finish the code")
        return node