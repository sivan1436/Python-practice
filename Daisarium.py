def Daisarium(n):
    if n <= 9:
        return True
    c = 0
    x = n 
    while x > 0 :
        c += 1 
        x//=10 
    sum = 0 
    x = n 
    i = c 
    while x > 0 :
        temp = x%10
        sum +=temp**i
        i-=1
        x //=10
    if sum == n :
        return True 
    else :
        return False
n = int(input()) 
print(Daisarium(n))