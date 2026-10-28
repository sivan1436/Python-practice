def Abundant(n):
 x = n 
 total = 0
 for i in range(2,int(n/2)+1):
  if n%i == 0:
    total +=i
 if total > n:
     return True
 else:
    return False
def AbundantNumberRange(a,b):
    for i in range(a,b+1):
        if Abundant(i):
            print(i,end=" ")
def NearstAbundantNumber(n):
    if Abundant(n):
        print("\n given n is a Abundant number:",n)
    l = n-1
    r = n+1
    while not Abundant(r):
        r+=1
    while not Abundant(l):
        l -=1
    print("\n Left Abundant number is :",l)
    print("\n Right Abundant number is :",r)
    if (r-n) > (n-l):
        print("\n Nearest Abundant number is :",l)
    else:
        print("\n Nearest Abundant number is :",r)
def NthAbundantNumber(n):
    i=1
    count = 0
    while count < n:
        if Abundant(i):
            count+=1
        if count == n:
            break
        i += 1
    print("\n Nth Abundant number is :",i)
n = int(input("enter n:"))
print(Abundant(n))
AbundantNumberRange(a = int(input("enter lower bound: ")), b = int(input("enter upper bound: ")))
NearstAbundantNumber(n)
NthAbundantNumber(n=int(input("enter n: "))    )
