def Digits(n):
    Max1 = -1
    Max2 = -1
    Min1 = float("inf")
    Min2 = float("inf")
    Ones = 0
    Odds = 0
    Evens = 0
    Zeros = 0
    while n > 0:
        temp = n % 10
        if temp % 2 == 0:
            Evens += 1
        if temp % 2 == 1:
            Odds += 1
        if temp > Max1:
            Max2 = Max1
            Max1 = temp
        elif temp > Max2 and temp < Max1:
            Max2 = temp

        if temp < Min1:
            Min2 = Min1
            Min1 = temp
        elif temp < Min2 and temp > Min1:
            Min2 = temp

        if temp == 1:
            Ones += 1

        if temp == 0:
            Zeros += 1

        n //= 10

    print("Max digit:", Max1)
    print("Min digit:", Min1)
    print("Ones count:", Ones)
    print("Zeros count:", Zeros)
    print("Second max digit:", Max2)
    print("Second min digit:", Min2)
    print("Odds count:", Odds)
    print("Evens count:", Evens)

Digits(int(input("Enter a number: ")))