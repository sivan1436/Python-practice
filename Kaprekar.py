def Zeros(n):
    t = 1
    while n > 0 :
        t *=10
        n -=1
    return t
def len_n(n):
    t = 0
    while n > 0 :
        t +=1
        n //=10
    return t
def Kaprekar(n):
    x = n*n
    rem = x % Zeros(len_n(n))
    Div = x//Zeros(len_n(n))
    if rem+Div == n :
        return True
    else :
        return False
def KaprekarRange(a,b):
    if a % 2 ==0:
        a +=1
    for i in range(a,b+1,2) :
        if Kaprekar(i) :
            print(i,end=" ")
KaprekarRange(a=int(input("Enter a number:")),b=int(input("Enter b  number:")))