

def sqrt(num:int):


    iterations = 100
    x = num
    i = 0
    while(True ):

        print("num =",num)
        num = ( num + x / num ) / 2 
    
        if i > iterations :
            break

        i+=1
    print(num)
    return int(num)




print(sqrt(4))



