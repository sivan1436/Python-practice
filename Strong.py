def fact(n):
    if n == 1 or n == 0 :
        return 1 
    return n*fact(n-1)    
def Strong(n):
 x = n 
 total = 0
 while x > 0:
    temp = x%10 
    total = total + fact(temp)
    x//=10
 if total == n:
    return True
 else:
    return False
n = int(input())
print(Strong(n))