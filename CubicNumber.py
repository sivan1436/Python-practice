def Cube(n):
    if n==1:
        return True
    i = 2
    while i*i*i <=n:
        if i*i*i ==n :
            return True
        i += 1
    return False
print(Cube(n=int(input("Enter the number : "))))