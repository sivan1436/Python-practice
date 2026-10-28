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
def NivenRange(a,b):
    for i in range(a,b+1):
        if Niven(i):
            print(i,end = " ")
def NivenNear(n):
    if Niven(n):
        print("\ngiven number is Niven",n)
    l = n-1
    r = n+1
    while not Niven(l):
        l -= 1
    while not Niven(r):
        r += 1
    print("Left Niven",l)
    print("Right Niven",r)
    if (r-n) > (n-l):
        print("Near Niven",l)
    else :
        print("Near Niven",r)
def nthNiven(n):
    count = 0
    i = 1
    while count < n:
        if Perfect(i):
            count += 1
        if count == n:
            break
        i+=1
    print("nth Niven",i)

n = int(input("Enter a Number:"))
NivenRange(a = int(input("enter lower bound:")), b = int(input("enter upper bound:")))
NivenNear(n)
nthNiven(n=int(input("enter n value:")))
print(Niven(n))
