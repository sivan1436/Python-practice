def Pronic(n):
    if n == 2 :
        return True
    pronic = False
    i = 0 
    j = 1 
    while j < (int(n/2)+1):
        if i*j == n :
            pronic = True 
            break 
        else:
            i+=1 
            j +=1
    if pronic :
        return True 
    return pronic    
        
n = int(input()) 
print(Pronic(n))