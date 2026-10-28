def Squre_of_digits(n):
    if n <=9 :
        return n
    x = n 
    sum = 0 
    while x > 0 :
        sum += (x%10)**2
        x //=10
    return Squre_of_digits(sum)    
def HappyNumber(n):
    temp = Squre_of_digits(n)
    if temp == 1:
        return True 
    else :
        return False
def HappyNuberRange(a,b):
    for i in range(a,b+1):
        if HappyNumber(i):
            print(i,end=" ")
def NearstHappyNumber(n):
    if HappyNumber(n):
        print("given n is a magic number",n)
    l = n-1
    r = n+1
    while not HappyNumber(r):
        r+=1
    while not HappyNumber(l):
        l -=1
    print("\n Left happy number is :",l)
    print("\n Right Happy number is :",r)
    if (r-n) > (n-l):
        print("\n Nearest Happy number is :",l)
    else:
        print("\n Nearest Happy number is :",r)
def NthHappyNumber(n):
    i=1
    count = 0
    while count < n:
        if HappyNumber(i):
            count+=1
        if count == n:
            break
        i += 1
    print("\n Nth Happy number is :",i)
n = int(input("enter n :"))
print(HappyNumber(n))
HappyNuberRange(a = int(input("enter lower bound: ")), b = int(input("enter upper bound: ")))
NearstHappyNumber(n)
NthHappyNumber(n=int(input("enter n: ")))
