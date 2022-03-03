from token import Token

class Tokenizer:
    def __init__(self,origin):
        self.origin = origin
        self.position = 0
        self.actual = None
    def selectNext(self):
        # se for +

        if self.position >= len(self.origin):
            self.actual = Token('EOF','')
            return self.actual 

        elif self.origin[self.position] == '+':
            self.actual = Token('PLUS','')
            self.position +=1
            return self.actual
        
        # se for -
        elif self.origin[self.position] == '-':
            self.actual = Token('MINUS','')
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

        else:
            pass
