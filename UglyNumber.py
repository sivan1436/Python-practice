def UglyNumber(n):
    if n < 0 :
        return False
    x = n
    Factors = []
    while x%2 == 0 :
        Factors.append(2)
        x //= 2
    factor = 3
    while factor * factor < n :
        while x%factor == 0 :
            Factors.append(factor)
            x //= factor
        factor += 2
    print(Factors)
    if factor <=n:
        return True
    else:
        return False

print(UglyNumber(int(input("Enter a number: "))))
