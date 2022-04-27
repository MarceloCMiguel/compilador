from token import Token
import sys
class Tokenizer:
    def __init__(self,origin):
        self.origin = origin
        self.position = 0
        self.actual = None
    def selectNext(self):
        reserved_words = {
            'printf': 'PRINT',
            'if':'IF',
            'else':'ELSE',
            'while':'WHILE',
            '<':'MINOR',
            '>':'GREATER',
            '||':'OR',
            '&&':'AND',
            'scanf':'SCANF',
            '!': 'NOT'
        }

        if self.position >= len(self.origin):
            self.actual = Token('EOF','')
            return self.actual 

        elif self.origin[self.position] in reserved_words:
            temp = self.origin[self.position]
            self.actual = Token(reserved_words[temp],temp)
            self.position += 1
            return self.actual
        
        elif self.origin[self.position] == '&':
            self.position +=1
            if self.origin[self.position] == '&':
                self.position +=1
                self.actual = Token(reserved_words['&&'],'&&')
                return self.actual
            else:
                sys.exit(f"ERROR TOKENIZER: Expect a & but receive {self.origin[self.position]}")
            
        elif self.origin[self.position] == '|':
            self.position +=1
            if self.origin[self.position] == '|':
                self.position +=1
                self.actual = Token(reserved_words['||'],'||')
                return self.actual
            else:
                sys.exit(f"ERROR TOKENIZER: Expect a || but receive {self.origin[self.position]}")

        elif self.origin[self.position] == ';':
            self.actual = Token('SEMICOLON','')
            self.position +=1
            return self.actual

        elif self.origin[self.position] == '{':
            self.actual = Token('OPEN_BRACKETS','')
            self.position +=1
            return self.actual

        elif self.origin[self.position] == '}':
            self.actual = Token('CLOSE_BRACKETS','')
            self.position +=1
            return self.actual

        # IDENTIFIER

        elif self.origin[self.position].isalpha():
            temp = self.origin[self.position]
            self.position +=1
            if self.position>=len(self.origin):
                if temp in reserved_words:
                    self.actual = Token(reserved_words[temp],temp)
                    return self.actual
                self.actual = Token('IDENTIFIER',temp)
                return self.actual
            while self.origin[self.position].isalpha() or self.origin[self.position].isnumeric() or self.origin[self.position]=='_':
                temp += self.origin[self.position]
                self.position +=1
                if self.position>=len(self.origin):
                    if temp in reserved_words:
                        self.actual = Token(reserved_words[temp],temp)
                        return self.actual
                    self.actual = Token('IDENTIFIER',temp)
                    return self.actual
            if temp in reserved_words:
                self.actual = Token(reserved_words[temp],temp)
                return self.actual
            self.actual = Token('IDENTIFIER',temp)
            return self.actual

        #enter
        elif self.origin[self.position] == '\n':
            self.position +=1
            return self.selectNext()

        elif self.origin[self.position] == '=':
            self.actual = Token('EQUAL','')
            self.position +=1
            if self.origin[self.position] == '=':
                self.actual = Token('EQUAL_TO','')
                self.position +=1
            return self.actual
            
        # se for +
        elif self.origin[self.position] == '+':
            self.actual = Token('PLUS','')
            self.position +=1
            return self.actual
        
        # se for -
        elif self.origin[self.position] == '-':
            self.actual = Token('MINUS','')
            self.position +=1
            return self.actual

        # se for *
        elif self.origin[self.position] == '*':
            self.actual = Token('TIMES','')
            self.position +=1
            return self.actual

        # se for /
        elif self.origin[self.position] == '/':
            self.actual = Token('DIVISION','')
            self.position +=1
            return self.actual

        # se for (
        elif self.origin[self.position] == '(':
            self.actual = Token('OPEN_PAREN','')
            self.position +=1
            return self.actual

        # se for )
        elif self.origin[self.position] == ')':
            self.actual = Token('CLOSE_PAREN','')
            self.position +=1
            return self.actual
        
        # se for numero
        elif self.origin[self.position].isnumeric():
            #percorre até o origin[position] não ser número
            temp = self.origin[self.position]
            self.position +=1
            if self.position>=len(self.origin):
                self.actual = Token('NUMBER',int(temp))
                return self.actual
            while self.origin[self.position].isnumeric():
                temp += self.origin[self.position]
                self.position +=1
                if self.position>=len(self.origin):
                    self.actual = Token('NUMBER',int(temp))
                    return self.actual
            self.actual = Token('NUMBER',int(temp))
            return self.actual
        # caso de espaços
        else:
            while self.origin[self.position] == " ":
                self.position += 1
                if self.position>=len(self.origin):
                    self.actual = Token('EOF','')
                    return self.actual
            return self.selectNext()

