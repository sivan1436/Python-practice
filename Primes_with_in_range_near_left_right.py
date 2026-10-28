def isprimes(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i =5
    while i*i <= n:
        if n % i == 0:
            return False
        i +=2
    return True
def primesWithInRange(a,b):
 for i in range(a, b + 1):
    if isprimes(i):
        print(i,end=" ")
def NearestPrime(n):
    if isprimes(n):
        print(n,end="")
    l = n - 1
    r = n + 1
    while not isprimes(l):
        l -= 1
    while not isprimes(r):
        r += 1
    print("Left primes",l)
    print("Right primes",r)
    if (r-n) > (n-l):
        print("Nearest Prime",n,"is",l)
    else :
        print("Nearest Prime",n,"is",r)
n = int(input("Enter a number: "))
NearestPrime(n)
primesWithInRange(a=int(input("Enter a Lower Bound: ")), b=int(input("Enter a Lower Bound: ")))
print(f"\n {isprimes(n)} ")