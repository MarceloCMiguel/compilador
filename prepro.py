import sys
class PrePro:

    def filter(code):
        i = 0
        open_comments = False
        start_position = 0
        last_position = 0
        while i < len(code):
            if open_comments == False:
                if i + 1<=len(code):
                    if code[i] == '/' and code[i+1] == '*':
                        open_comments = True
                        start_position = i
            else:
                if i+1 <=len(code):
                    if code[i] == '*' and code[i+1] == '/':
                        last_position = i+2
                        open_comments = False
                        l = list(code)
                        del(l[start_position:last_position])
                        code = "".join(l)
                        i-=4
            i+=1
        if open_comments == True:
            sys.exit("Error: Comments")
        return code