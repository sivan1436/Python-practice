def Daisarium(n):
    if n <= 9:
        return True
    c = 0
    x = n 
    while x > 0 :
        c += 1 
        x//=10 
    sum = 0 
    x = n 
    i = c 
    while x > 0 :
        temp = x%10
        sum +=temp**i
        i-=1
        x //=10
    if sum == n :
        return True 
    else :
        return False
def DaisariumNumberRange(a,b):
    for i in range(a,b+1):
        if Daisarium(i):
            print(i,end=" ")
def NearstDaisariumNumber(n):
    if Daisarium(n):
        print("given n is a Daisarium number",n)
    l = n-1
    r = n+1
    while not Daisarium(r):
        r+=1
    while not Daisarium(l):
        l -=1
    print("\n Left Daisarium is :",l)
    print("\n Right Daisarium number is :",r)
    if (r-n) > (n-l):
        print("\n Nearest Daisarium number is :",l)
    else:
        print("\n Nearest Daisarium number is :",r)
def NthDaisariumNumber(n):
    i=1
    count = 0
    while count < n:
        if Daisarium(i):
            count+=1
        if count == n:
            break
        i += 1
    print("\n Nth Daisarium number is :",i)
n = int(input("enter n :"))
print(Daisarium(n))
DaisariumNumberRange(a = int(input("enter lower bound: ")), b = int(input("enter upper bound: ")))
NearstDaisariumNumber(n)
NthDaisariumNumber(n=int(input("enter n: "))    )