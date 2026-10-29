def Zeros(n):
    t = 1
    while n > 0:
        t*=10
        n-=1
    return t
def DuckNum(n):
    count = 0
    x = n
    while x > 0:
        count+=1
        x//=10
    if n//Zeros(count-1) == 0:
        return False
    else:
        return True
print(DuckNum(n=int(input("Enter a number: "))))