def Perfect(n):
 x = n 
 total = 0
 for i in range(1,int(n/2)+1):
     if n%i == 0 :
         total +=i 
 if total == n:
    return True
 else:
    return False
def PerfectRange(a,b):
    for i in range(a,b+1):
        if Perfect(i):
            print(i,end = " ")
def PerfectNear(n):
    if Perfect(n):
        print("\ngiven number is perfect",n)
    l = n-1
    r = n+1
    while not Perfect(l):
        l -= 1
    while not Perfect(r):
        r += 1
    print("Left Perfect",l)
    print("Right Perfect",r)
    if (r-n) > (n-l):
        print("Near Perfect",l)
    else :
        print("Near Perfect",r)
def nthPerfect(n):
    count = 0
    i = 1
    while count < n:
        if Perfect(i):
            count += 1
        if count == n:
            break
        i+=1
    print("nth Perfect",i)

n = int(input("Enter a Number:"))
PerfectRange(a = int(input("enter lower bound")), b = int(input("enter upper bound")))
PerfectNear(n)
nthPerfect(n=int(input("enter n value:")))
print(Perfect(n))
    