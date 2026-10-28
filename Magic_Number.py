def Sumofdigit(n):
    if n <=9:
        return n
    t = 0 
    while n > 0:
        t += n%10
        n//=10
    n = t  
    return Sumofdigit(n)
def MagicNumber(n) :
 x=(Sumofdigit(n))
 if x == 1:
    return True 
 else :
    return False
def MagicNuberRange(a,b):
    for i in range(a,b+1):
        if MagicNumber(i):
            print(i,end=" ")
def NearstMagicNumber(n):
    if MagicNumber(n):
        print("given n is a magic number",n)
    l = n-1
    r = n+1
    while not MagicNumber(r):
        r+=1
    while not MagicNumber(l):
        l -=1
    print("\n Left Magic number is :",l)
    print("\n Right Magic number is :",r)
    if (r-n) > (n-l):
        print("\n Nearest Magic number is :",l)
    else:
        print("\n Nearest Magic number is :",r)
def NthMagicNumber(n):
    i=1
    count = 0
    while count < n:
        if MagicNumber(i):
            count+=1
        if count == n:
            break
        i += 1
    print("\n Nth Magic number is :",i)
n = int(input("enter n"))
print(MagicNumber(n))
MagicNuberRange(a = int(input("enter lower bound: ")), b = int(input("enter upper bound: ")))
NearstMagicNumber(n)
NthMagicNumber(n=int(input("enter n: "))    )