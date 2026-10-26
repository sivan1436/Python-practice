def primefact(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n//2
    factor = 3 
    while factor * factor <= n :
        while n%factor == 0 :
            factors.append(factor)
            n //= factor
        factor += 2 
    if n > 2 :
        factors.append(n)
    return factors 
def prime(n):
    p = True 
    for i in range(2,int(n/2) + 1):
        if n % i == 0:
            p = False
            break
    if p:
        return True
    return False    
    
n = int(input())
check = []
result = []
if n < 2 :
    print("No factors")
else :
    result = (primefact(n))
    for i in result:
        check.append(prime(i))
print(result)
print(check)
        
        
        
    
    
    
    
    
    