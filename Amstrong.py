def power(x,n):
    t = 1 
    while n > 0 :
        t = t*x 
        n-=1 
    return t    


def Amstrong(n):
 count = 0 
 x = n 
 while x > 0:
    count += 1 
    x//=10 
 total = 0 
 x = n 
 while x > 0:
    temp = x%10 
    total = total + power(temp,count)
    x//=10
 if total == n:
    return True
 else:
    return False
n = int(input())
print(Amstrong(n))
    