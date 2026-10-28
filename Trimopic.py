def Zeros(n):
    t = 1
    while n > 0:
        t*=10
        n-=1
    return t
def len_n(n):
    x = n 
    c = 0 
    while x > 0 :
        c += 1 
        x //=10
    return c     
def Trimophic(n):
    if n == 1 or n == 0 :
        return True
    x = len_n(n) 
    temp = n**3 
    digit = temp % Zeros(len_n(n))
    if digit == n :
        return True 
    else :
        return False
def TrimophicRange(a,b):
    for i in range(a,b+1):
        if Trimophic(i):
            print(i,end = " ")
def TrimophicNear(n):
    if Trimophic(n):
        print("\ngiven number is Trimophic",n)
    l = n-1
    r = n+1
    while not Trimophic(l):
        l -= 1
    while not Trimophic(r):
        r += 1
    print("Left Trimophic",l)
    print("Right Trimophic",r)
    if (r-n) > (n-l):
        print("Near Trimophic",l)
    else :
        print("Near Trimorphic",r)
def nthTrimophic(n):
    count = 0
    i = 1
    while count < n:
        if Trimophic(i):
            count += 1
        if count == n:
            break
        i+=1
    print("nth Trimophic",i)

n = int(input("Enter a Number:"))
TrimophicRange(a = int(input("enter lower bound:")), b = int(input("enter upper bound:")))
TrimophicNear(n)
nthTrimophic(n=int(input("enter n value:")))
print(Trimophic(n))
