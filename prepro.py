import sys
class PrePro:

    def filter(code):
        i = 0
        open_comments = False
        start_position = 0
        last_position = 0
        new_code = ''
        while i < len(code):
            if open_comments == False:
                if i + 1<=len(code):
                    if code[i] == '/' and code[i+1] == '*':
                        open_comments = True
                    else:
                        new_code+=code[i]

            else:
                if i+1 <=len(code):
                    if code[i] == '*' and code[i+1] == '/':
                        open_comments = False
                        i+=1
            i+=1
        if open_comments == True:
            sys.exit("Error: Comments are open")
        return new_code

