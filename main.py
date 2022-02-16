import sys

def check_args():
    if len(sys.argv) > 2:
        sys.exit("Error: More than one arguments was passed")
    x = sys.argv[1]
    #x = '1+1-2'
    i=0
    number = ""
    is_number = False
    y= None
    #print(len(x))
    while i < len(x):
        if x[i].isnumeric():
            temp = ''
            while x[i].isnumeric():
                
                temp +=x[i]
                #print(temp)
                if i+1 == len(x):
                    break
                
                i+=1
            if number == "" and i+1 != len(x):
                is_number = True
                number = int(temp)
            else:
                var = int(temp)
                if operator !='+' and operator !='-':
                    sys.exit("Error: Invalid operator")
                if operator =='+':
                    if y!= None:
                        y += var
                    else:
                        y = number + var
                else:
                    if y!=None:
                        y-= var
                    else:    
                        y = number - var
                if i+1 == len(x):
                    i+=1
        else:
            operator = x[i]  
            i+=1
    if y == None:
        sys.exit("Error: no result")

    # if number != "" and var != None:
    #     sys.exit("Error: no Operator was detected")
    print(y)

            

check_args()
#x = sys.argv[1]
# print(x)