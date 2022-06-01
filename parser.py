from tokenizer import Tokenizer
from node import *
import sys
class Parser:
    tokens= None


    def parseProgram():
        list_defs = []
        while Parser.tokens.actual.type != 'EOF':
            list_defs.append(Parser.parseDeclaration())
        return Block('Block',list_defs)
    
    def parseDeclaration():
        if Parser.tokens.actual.type in ["STRING","INT","VOID"]:
            
            type_func = Parser.tokens.actual.type
            Parser.tokens.selectNext()
            if Parser.tokens.actual.type == "IDENTIFIER":
                
                iden_func = Parser.tokens.actual
                name_func = VarDec(type_func,[iden_func])
                list_childrens = []
                list_childrens.append(name_func)
                
                Parser.tokens.selectNext()
                if Parser.tokens.actual.type == "OPEN_PAREN":
                    
                    Parser.tokens.selectNext()
                    if Parser.tokens.actual.type == "CLOSE_PAREN":
                        
                        Parser.tokens.selectNext()
                        list_childrens.append(Parser.parseBlock())
                        return FuncDec(iden_func.value,list_childrens)
                    elif Parser.tokens.actual.type in ["STRING","INT","VOID"]:
                        
                        type_arg = Parser.tokens.actual.type
                        Parser.tokens.selectNext()
                        if Parser.tokens.actual.type == "IDENTIFIER":
                            
                            iden_arg = Parser.tokens.actual
                            Parser.tokens.selectNext()
                            arg_func = VarDec(type_arg,[iden_arg])
                            list_childrens.append(arg_func)
                            while Parser.tokens.actual.type == "COMMA":
                                
                                Parser.tokens.selectNext()
                                if Parser.tokens.actual.type in ["STRING","INT","VOID"]:
                                    
                                    type_arg = Parser.tokens.actual.type
                                    Parser.tokens.selectNext()
                                    if Parser.tokens.actual.type == "IDENTIFIER":
                                        
                                        iden_arg = Parser.tokens.actual
                                        Parser.tokens.selectNext()
                                        arg_func = VarDec(type_arg,[iden_arg])
                                        list_childrens.append(arg_func)
                                        
                                    else:
                                        sys.exit(f"ERROR PARSEDECLARATION: expect a second IDENTIFIER, received {Parser.tokens.actual.type}")    
                                else:
                                    sys.exit(f"ERROR PARSEDECLARATION: expect STRING or INT or VOID, received {Parser.tokens.actual.type}")
                            if Parser.tokens.actual.type == "CLOSE_PAREN":
                                Parser.tokens.selectNext()
                                
                                list_childrens.append(Parser.parseBlock())
                                return FuncDec(iden_func.value,list_childrens)
                                    

                        else:
                            sys.exit(f"ERROR PARSEDECLARATION: expect a second IDENTIFIER, received {Parser.tokens.actual.type}")    
                    else:
                        sys.exit(f"ERROR PARSEDECLARATION: expect a Close Paren or a type of identifier, received {Parser.tokens.actual.type}")    

                else:
                    sys.exit(f"ERROR PARSEDECLARATION: expect a OPEN_PAREN, received {Parser.tokens.actual.type}")    
            else:
                sys.exit(f"ERROR PARSEDECLARATION: expect a IDENTIFIER, received {Parser.tokens.actual.type}")

        else:
            sys.exit(f"ERROR PARSEDECLARATION: expect STRING or INT or VOID, received {Parser.tokens.actual.type}")

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
            sys.exit(f"ERROR PARSER BLOCK: Open Brackets not find, finded {Parser.tokens.actual.type}")
        


    def parseStatement():
        if Parser.tokens.actual.type == 'SEMICOLON':
            node = NoOp('',[])
            Parser.tokens.selectNext()
            return node
        
        elif Parser.tokens.actual.type == 'IDENTIFIER':
            name_function = Parser.tokens.actual.value #if function
            node = Identifier(Parser.tokens.actual.value,[])
            Parser.tokens.selectNext()
            if Parser.tokens.actual.type == 'EQUAL':
                Parser.tokens.selectNext()
                node = Assignment('=',[node,Parser.relativeExpression()])
                if Parser.tokens.actual.type == 'SEMICOLON':
                    Parser.tokens.selectNext()
                    return node
                else:
                    sys.exit(f"ERROR STATEMENT IDENTIFIER: Expected SEMICOLON, readed {Parser.tokens.actual.type} {Parser.tokens.actual.value} ")
            elif Parser.tokens.actual.type == "OPEN_PAREN":
                list_childrens = []
                Parser.tokens.selectNext()
                if Parser.tokens.actual.type == "CLOSE_PAREN":
                    Parser.tokens.selectNext()
                    if Parser.tokens.actual.type == 'SEMICOLON':
                        Parser.tokens.selectNext()
                        return FuncCall(name_function,[])
                else:
                    list_childrens.append(Parser.relativeExpression())
                    while Parser.tokens.actual.type == "COMMA":
                        Parser.tokens.selectNext()
                        list_childrens.append(Parser.relativeExpression())
                    if Parser.tokens.actual.type == "CLOSE_PAREN":
                        Parser.tokens.selectNext()
                        if Parser.tokens.actual.type == 'SEMICOLON':
                            Parser.tokens.selectNext()
                            return FuncCall(name_function,list_childrens)
                    else:
                        sys.exit(f"ERROR STATEMENT: expect a CLOSE_PAREN, receive {Parser.tokens.actual.type}")
            else:
                sys.exit(f"ERROR STATEMENT IDENTIFIER: expected a equal or open paren, receive {Parser.tokens.actual.type}")
        
        elif Parser.tokens.actual.type == 'PRINT':
            Parser.tokens.selectNext()
            if Parser.tokens.actual.type == 'OPEN_PAREN':
                Parser.tokens.selectNext()
                node = Print('Print',[Parser.relativeExpression()])
                if Parser.tokens.actual.type == 'CLOSE_PAREN':
                    Parser.tokens.selectNext()
                    if Parser.tokens.actual.type == 'SEMICOLON':
                        Parser.tokens.selectNext()
                        return node

                    else:
                        sys.exit(f"ERROR STATEMENT: Expected SEMICOLON, readed {Parser.tokens.actual.type} {Parser.tokens.actual.value} ")
                else:
                    sys.exit(f"ERROR STATEMENT: There are open parentheses {Parser.tokens.actual.value}")
            
        elif Parser.tokens.actual.type in ["STRING","INT"]:
            type_iden = Parser.tokens.actual.type
            Parser.tokens.selectNext()
            lista_tokens = []
            if Parser.tokens.actual.type == 'IDENTIFIER':
                token_iden = Parser.tokens.actual
            else:
                sys.exit(f"ERROR STATEMENT: Invalid token type {Parser.tokens.actual.type} in type")
            Parser.tokens.selectNext()
            lista_tokens.append(token_iden)

            while Parser.tokens.actual.type == "COMMA":
                Parser.tokens.selectNext()
                if Parser.tokens.actual.type == 'IDENTIFIER':
                    token_iden = Parser.tokens.actual
                else:
                    sys.exit(f"ERROR STATEMENT: Invalid token type {Parser.tokens.actual.type} in type")
                lista_tokens.append(token_iden)
                Parser.tokens.selectNext()
            if Parser.tokens.actual.type == 'SEMICOLON':
                Parser.tokens.selectNext()
                return VarDec(type_iden,lista_tokens)
            else:
                sys.exit(f"ERROR STATEMENT TYPE: semicolon expected, finded {Parser.tokens.actual.type}")
        
        elif Parser.tokens.actual.type == 'RETURN':
            Parser.tokens.selectNext()
            if Parser.tokens.actual.type == "OPEN_PAREN":
                Parser.tokens.selectNext()
                node = Return('return',[Parser.relativeExpression()])
                if Parser.tokens.actual.type == "CLOSE_PAREN":
                    Parser.tokens.selectNext()
                    if Parser.tokens.actual.type == 'SEMICOLON':
                        Parser.tokens.selectNext()
                        return node
                    else:
                        sys.exit(f"ERROR STATEMENT RETURN: Expected SEMICOLON, readed {Parser.tokens.actual.type} {Parser.tokens.actual.value} ")
                else:
                    sys.exit(f"ERROR STATEMENT RETURN: There are open parentheses {Parser.tokens.actual.value}")
            else:
                sys.exit(f"ERROR STATEMENT RETURN: Expected open parentheses {Parser.tokens.actual.value}")
                        
        
        elif Parser.tokens.actual.type == 'WHILE':
            Parser.tokens.selectNext()
            if Parser.tokens.actual.type == 'OPEN_PAREN':
                Parser.tokens.selectNext()
                node = Parser.relativeExpression()
                if Parser.tokens.actual.type == "CLOSE_PAREN":
                    Parser.tokens.selectNext()
                    node = While('while',[node,Parser.parseStatement()])
                    return node
                else:
                    sys.exit(f"ERROR STATEMENT: There are open parentheses {Parser.tokens.actual.value}")
            else:
                sys.exit(f"ERROR STATEMENT: while expect a open parentheses")
        elif Parser.tokens.actual.type == "IF":
            Parser.tokens.selectNext()
            if Parser.tokens.actual.type == "OPEN_PAREN":
                Parser.tokens.selectNext()
                node = Parser.relativeExpression()
                if Parser.tokens.actual.type == "CLOSE_PAREN":
                    Parser.tokens.selectNext()
                    node_1 = Parser.parseStatement()
                    if Parser.tokens.actual.type == "ELSE":
                        Parser.tokens.selectNext()
                        node = If('if',[node,node_1,Parser.parseStatement()])
                        return node
                    else:
                        node = If('if',[node,node_1])
                        return node
                else:
                    sys.exit(f"ERROR STATEMENT IF: There are open parentheses {Parser.tokens.actual.value}")
            else:
                sys.exit(f"ERROR STATEMENT IF: if expect a open parentheses")
        else:
            node = Parser.parseBlock()
            return node

    def relativeExpression():
        node = Parser.parseExpression()
        
        while Parser.tokens.actual.type in ["EQUAL_TO","MINOR","GREATER"]:
            if Parser.tokens.actual.type == "EQUAL_TO":
                Parser.tokens.selectNext()
                node = BinOp('==',[node,Parser.parseExpression()])
            elif Parser.tokens.actual.type == "MINOR":
                Parser.tokens.selectNext()
                node = BinOp('<',[node,Parser.parseExpression()])
            elif Parser.tokens.actual.type == "GREATER":
                Parser.tokens.selectNext()
                node = BinOp('>',[node,Parser.parseExpression()]) 
        return node

    def parseExpression():
        
        # resultado = Parser.parseTerm()
        node = Parser.parseTerm()
        
        while Parser.tokens.actual.type in ["PLUS","MINUS","OR","DOT"]:
            if Parser.tokens.actual.type == "PLUS":
                Parser.tokens.selectNext()
                # resultado += Parser.parseTerm()
                node = BinOp('+',[node,Parser.parseTerm()])
            elif Parser.tokens.actual.type == "MINUS":
                Parser.tokens.selectNext()
                # resultado -= Parser.parseTerm()
                node = BinOp('-',[node,Parser.parseTerm()])
            elif Parser.tokens.actual.type == "OR":
                Parser.tokens.selectNext()
                node = BinOp('||',[node,Parser.parseTerm()])
            elif Parser.tokens.actual.type == "DOT":
                Parser.tokens.selectNext()
                node = BinOp('.',[node,Parser.parseTerm()])
        return node    


    def parseTerm():
        node = Parser.parseFactor()
        while Parser.tokens.actual.type in ["TIMES","DIVISION", "AND"]:
            if Parser.tokens.actual.type == "TIMES":
                Parser.tokens.selectNext()
                # resultado *=Parser.parseFactor()
                node = BinOp('*',[node,Parser.parseFactor()])
            if Parser.tokens.actual.type == "DIVISION":
                Parser.tokens.selectNext()
                # resultado //=Parser.parseFactor()
                node = BinOp('/',[node,Parser.parseFactor()])
            if Parser.tokens.actual.type == "AND":
                Parser.tokens.selectNext()
                node = BinOp('&&',[node, Parser.parseFactor()])
        return node

    def parseFactor():
        
        if Parser.tokens.actual.type == 'NUMBER':
            
            # resultado += Parser.tokens.actual.value
            node = IntVal(Parser.tokens.actual.value,[])
            Parser.tokens.selectNext()
        
        elif Parser.tokens.actual.type == 'STRING':
            node = StrVal(Parser.tokens.actual.value,[])
            Parser.tokens.selectNext()
        

        elif Parser.tokens.actual.type == "PLUS":
            Parser.tokens.selectNext()
            node = UnOp('+',[Parser.parseFactor()])
            # resultado += Parser.parseFactor()
    
        elif Parser.tokens.actual.type == "MINUS":
            Parser.tokens.selectNext()
            node = UnOp('-',[Parser.parseFactor()])
            # resultado -= Parser.parseFactor()
    
        elif Parser.tokens.actual.type == "NOT":
            Parser.tokens.selectNext()
            node = UnOp('!',[Parser.parseFactor()])

        elif Parser.tokens.actual.type == "OPEN_PAREN":
            Parser.tokens.selectNext()
            node = Parser.relativeExpression()
            # resultado = Parser.parseExpression()
            if Parser.tokens.actual.type == "CLOSE_PAREN":
                Parser.tokens.selectNext()
            else:
                sys.exit("ERROR: There are open parentheses")

        elif Parser.tokens.actual.type == "SCANF":
            Parser.tokens.selectNext()
            node = Scanf("",[])
            if Parser.tokens.actual.type == "OPEN_PAREN":
                Parser.tokens.selectNext()
                if Parser.tokens.actual.type == "CLOSE_PAREN":
                    Parser.tokens.selectNext()
                else:
                    sys.exit("ERROR: There are open parentheses")
            else:
                sys.exit(f"ERROR Factor Scanf: scanf expect a open parentheses")


        elif Parser.tokens.actual.type == "IDENTIFIER":
            node = Identifier(Parser.tokens.actual.value, [])
            name_function = Parser.tokens.actual.value #if function
            Parser.tokens.selectNext()
            if Parser.tokens.actual.type == "OPEN_PAREN":
                list_childrens = []
                Parser.tokens.selectNext()
                if Parser.tokens.actual.type == "CLOSE_PAREN":
                    Parser.tokens.selectNext()
                    if Parser.tokens.actual.type == 'SEMICOLON':
                        Parser.tokens.selectNext()
                        node = FuncCall(name_function,[])
                else:
                    list_childrens.append(Parser.relativeExpression())
                    while Parser.tokens.actual.type == "COMMA":
                        Parser.tokens.selectNext()
                        list_childrens.append(Parser.relativeExpression())
                    if Parser.tokens.actual.type == "CLOSE_PAREN":
                        Parser.tokens.selectNext()
                        node = FuncCall(name_function,list_childrens) 
                    else:
                        sys.exit(f"ERROR FACTOR: expect a CLOSE_PAREN, receive {Parser.tokens.actual.type}")
        else:
            sys.exit("ERROR: The code must start with a number, or '+','-','('")
        return node



    def run(code):
        Parser.tokens = Tokenizer(code)
        Parser.tokens.selectNext()
        node = Parser.parseProgram()
        if Parser.tokens.actual.type !="EOF":
            sys.exit("Error: the compiler didn't finish the code")
        node.children.append(FuncCall('main',[]))
        return node