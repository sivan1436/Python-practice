def fact(n):
    if n == 1 or n == 0 :
        return 1
    return n*fact(n-1)
def Strong(n):
 x = n
 total = 0
 while x > 0:
    temp = x%10
    total = total + fact(temp)
    x//=10
 if total == n:
    return True
 else:
    return False
def StrongRange(a,b):
    for i in range(a,b+1):
        if Strong(i):
            print(i,end=" ")
def StrongNear(n):
    if Strong(n):
        print("\nn is a strong number:",n)
    l = n-1
    r = n+1
    while not Strong(l):
        l -=1
    while not Strong(r):
        r +=1
    print("\nleft Strong :",l)
    print("\nright Strong :",r)
    if (r-n)>(n-l):
        print("\nnearest Strong Number:",l)
    else:
        print("\nNearest Strong Number:",r)
def nthStrong(n):
    count = 0
    i = 0
    while True:
        if Strong(i):
            count += 1
        if  count == n:
            break
        i +=1
    print("nth Strong Number:",i)
n = int(input("Enter a number:"))
Strong(n)
StrongRange(a = int(input("Enter a Lower Bound:")),b = int(input("Enter a Lower Bound:")))
StrongNear(n)
nthStrong(n=int(input("Enter nth term number:")))

