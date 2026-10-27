def len_n(n):
    x = n 
    c = 0 
    while x > 0 :
        c += 1 
        x //=10
    return c     
def Trimophic(n):
    if n == 1 or n == 0 :
        return True
    x = len_n(n) 
    temp = n**3 
    digit = temp % Zeros(len_n(n))
    if digit == n :
        return True 
    else :
        return False 
n = int(input()) 
print(Trimophic(n)) 