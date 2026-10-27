def Evil(n):
    if n < 1:
        return 0 
    if n == 1 :
     return 1 
    x = n 
    bin = 0 
    a=1
    while x > 0 :
        bit = x%2 
        bin = bin + bit *a
        a=a*10
        x //=2 
    x = 0 
    while bin > 0 :
        temp = bin%10 
        if temp == 1 :
            x +=1 
        bin //=10
    if x % 2 == 0 :
        return True 
    else :
        return False
n = int(input()) 
print(Evil(n))