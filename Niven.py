def Niven(n):
 x = n 
 total = 0
 while x > 0:
    temp = x%10
    total +=temp 
    x//=10
 if n%total == 0:
    return True
 else:
    return False
n = int(input())
print(Niven(n))