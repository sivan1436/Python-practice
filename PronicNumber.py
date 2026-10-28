def Pronic(n):
    if n == 2 :
        return True
    pronic = False
    i = 0 
    j = 1 
    while j < (int(n/2)+1):
        if i*j == n :
            pronic = True 
            break 
        else:
            i+=1 
            j +=1
    if pronic :
        return True 
    return pronic
def PronicNumberRange(a,b):
    for i in range(a,b+1):
        if Pronic(i):
            print(i,end=" ")
def NearstPronicNumber(n):
    if Pronic(n):
        print("given n is a pronic number",n)
    l = n-1
    r = n+1
    while not Pronic(r):
        r+=1
    while not Pronic(l):
        l -=1
    print("\n Left Pronic number is :",l)
    print("\n Right pronic number is :",r)
    if (r-n) > (n-l):
        print("\n Nearest pronic number is :",l)
    else:
        print("\n Nearest pronic number is :",r)
def NthPronicNumber(n):
    i=1
    count = 0
    while count < n:
        if Pronic(i):
            count+=1
        if count == n:
            break
        i += 1
    print("\n Nth pronic number is :",i)
n = int(input("enter n :"))
print(Pronic(n))
PronicNumberRange(a = int(input("enter lower bound: ")), b = int(input("enter upper bound: ")))
NearstPronicNumber(n)
NthPronicNumber(n=int(input("enter n: ")))
print(Pronic(n))