def Perfect(n):
 x = n 
 total = 0
 for i in range(1,int(n/2)+1):
     if n%i == 0 :
         total +=i 
 if total == n:
    return True
 else:
    return False
n = int(input())
print(Perfect(n))
    