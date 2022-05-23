class Asm:
    def __init__(self, code_name) -> None:
        self.code = ""
        self.code_name = code_name

    def write(self,code):
        self.code+= code + '\n'
    def dump(self):
        with open(self.code_name,'w+') as f:
            f.write(self.code)
        # def dump():