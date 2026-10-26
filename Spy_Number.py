def Sumofdigit(n):
    if n <=9:
        return n
    t = 0 
    while n > 0:
        t += n%10
        n//=10
    return t
def Productofdigit(n):
    if n <=9:
        return n
    t = 1 
    while n > 0:
        t *= n%10
        n//=10
    return t 
def SpyNumber(n):
    x = n 
    a = Sumofdigit(n)
    b = Productofdigit(n) 
    if a == b :
        return True 
    else :
        return False 
        
n = int(input()) 
print(SpyNumber(n)) 