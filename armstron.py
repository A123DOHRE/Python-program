for num1 in range(1,10000):
    num = list(str(num1))

    if len(num)==3:
        digit1=int(num[0])**3
        digit2=int(num[1])**3
        digit3=int(num[2])**3
        sum = digit1+digit2+digit3
        if sum==num1:
            print sum
    elif len(num)==4:
        digit1=int(num[0])**4
        digit2=int(num[1])**4
        digit3=int(num[2])**4
        digit4=int(num[3])**4
        sum = digit1+digit2+digit3+digit4
        if sum==num1:
            print sum
    
        
        
        
        
        
        
