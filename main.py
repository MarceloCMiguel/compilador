import sys

def check_args():
    if len(sys.argv) > 2:
        sys.exit("Error: More than one arguments was passed")
    x = sys.argv[1]
    i=0
    number = ""
    while i < len(x):
        if x[i].isnumeric():
            number = x[i]
        if i+1 == len(x):
            var = int(x[i])
            #faz operação
            if operator =='+':
                y = int(number) + var
            else:
                y = int(number) - var


        else:
            operator = x[i]        
        
        
        
        i+=1
    print(y)

            

check_args()
x = sys.argv[1]
# print(x)