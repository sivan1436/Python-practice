def MerseneNumber(n):
    i = 0
    while 2**i != n+2:
        if 2**i - 1 == n:
            return True
        i += 1
    return False
print(MerseneNumber(n=int(input("Enter a number: "))))