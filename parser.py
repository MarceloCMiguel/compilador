from tokenizer import Tokenizer
import sys
class Parser:
    tokens= None

    def parseTerm():
        resultado = 0
        if Parser.tokens.actual.type == 'NUMBER':
            resultado += Parser.tokens.actual.value
            Parser.tokens.selectNext()
            while Parser.tokens.actual.type == "TIMES" or Parser.tokens.actual.type == "DIVISION":
                if Parser.tokens.actual.type == "TIMES":
                    Parser.tokens.selectNext()
                    if Parser.tokens.actual.type == "NUMBER":
                        resultado *= Parser.tokens.actual.value
                    else:
                        sys.exit(f"Error: the token in position {Parser.tokens.position} must be a number")
                if Parser.tokens.actual.type == "DIVISION":
                    Parser.tokens.selectNext()
                    if Parser.tokens.actual.type == "NUMBER":
                        resultado //= Parser.tokens.actual.value
                    else:
                        sys.exit(f"Error: the token in position {Parser.tokens.position} must be a number")
                Parser.tokens.selectNext()
            return resultado

        else:
            sys.exit("Error: The code must start with a number")



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
        if Parser.tokens.actual.type !="EOF":
            sys.exit("Error: the compiler didn't finish the code")
        print(resultado)
        return resultado


    def run(code):
        Parser.tokens = Tokenizer(code)
        Parser.parseExpression()