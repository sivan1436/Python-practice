def Reverse(n,rev = 0):
    if n ==0:
        return rev
    return Reverse(n//10,rev*10+n%10)
print(Reverse(n=int(input("enter n: "))))
