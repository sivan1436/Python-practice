def power(x,n):
    t = 1
    while n > 0 :
        t = t*x
        n-=1
    return t


def Amstrong(n):
    count = 0
    x = n
    while x > 0:
        count += 1
        x//=10
    total = 0
    x = n
    while x > 0:
        temp = x%10
        total = total + power(temp,count)
        x//=10
    if total == n:
        return True
    else:
        return False
def NearestAmstrong(n):
        if Amstrong(n):
            Print("n is an amstrong number",n)
        i = n-1
        r = n+1
        while not Amstrong(i):
            i -=1
        while not Amstrong(r):
            r+=1
        print("left prime is:",i)
        print("right prime is:",r)
        if (r-n)> (n-l):
            print("near prime is:",l)
        else:
            print("near prime is:",r)
def AmstrongRange(a,b):
        for i in range(a,b+1):
            if Amstrong(i):
                print(i,end=" ")
def nthAmstrong(n):
        i=0
        count = 0
        while True:
            if Amstrong(i):
                count += 1
            if count == n:
                print("n is an amstrong number",i)
                break
            i += 1
       print(f"{n}th term Amstrong number is: {i}")
n = int(input("enter the number"))
Amstrong(n)
AmstrongRange(a=int(input("enter lower bound")), b=int(input("enter the number upper bound")))
nthAmstrong(a=int(input("enter the number of term :")))