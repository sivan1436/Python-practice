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
def EvilNumberRange(a,b):
    for i in range(a,b+1):
        if Evil(i):
            print(i,end=" ")
def NearstEvilNumber(n):
    if Evil(n):
        print("given n is a Evil number",n)
    l = n-1
    r = n+1
    while not Evil(r):
        r+=1
    while not Evil(l):
        l -=1
    print("\n Left Magic Evil is :",l)
    print("\n Right Evil number is :",r)
    if (r-n) > (n-l):
        print("\n Nearest Evil number is :",l)
    else:
        print("\n Nearest Evil number is :",r)
def NthEvilNumber(n):
    i=1
    count = 0
    while count < n:
        if Evil(i):
            count+=1
        if count == n:
            break
        i += 1
    print("\n Nth Evil number is :",i)
n = int(input("enter n"))
print(Evil(n))
EvilNumberRange(a = int(input("enter lower bound: ")), b = int(input("enter upper bound: ")))
NearstEvilNumber(n)
NthEvilNumber(n=int(input("enter n: "))    )
