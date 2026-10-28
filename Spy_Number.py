def Sumofdigit(n):
    if n <=9:
        return n
    t = 0 
    while n > 0:
        t += n%10
        n//=10
    return t
def Productofdigit(n):
    if n <=9:
        return n
    t = 1 
    while n > 0:
        t *= n%10
        n//=10
    return t 
def SpyNumber(n):
    x = n 
    a = Sumofdigit(n)
    b = Productofdigit(n) 
    if a == b :
        return True 
    else :
        return False
def SpyNumberRange(a,b):
    for i in range(a,b+1):
        if SpyNumber(i):
            print(i,end=" ")
def NearstSpyNumber(n):
    if SpyNumber(n):
        print("given n is a Spy number",n)
    l = n-1
    r = n+1
    while not SpyNumber(r):
        r+=1
    while not SpyNumber(l):
        l -=1
    print("\n Left Spy number is :",l)
    print("\n Right Spy number is :",r)
    if (r-n) > (n-l):
        print("\n Nearest Spy number is :",l)
    else:
        print("\n Nearest Spy number is :",r)
def NthSpyNumber(n):
    i=1
    count = 0
    while count < n:
        if SpyNumber(i):
            count+=1
        if count == n:
            break
        i += 1
    print("\n Nth Spy number is :",i)
n = int(input("enter n :"))
print(SpyNumber(n))
SpyNumberRange(a = int(input("enter lower bound: ")), b = int(input("enter upper bound: ")))
NearstSpyNumber(n)
NthSpyNumber(n=int(input("enter n: ")))
print(SpyNumber(n))
