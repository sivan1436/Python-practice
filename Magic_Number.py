def Sumofdigit(n):
    if n <=9:
        return n
    t = 0 
    while n > 0:
        t += n%10
        n//=10
    n = t  
    return Sumofdigit(n)
def MagicNumber(n) :
 x=(Sumofdigit(n))
 if x == 1:
    return True 
 else :
    return False 
n = int(input()) 
print(MagicNumber(n))