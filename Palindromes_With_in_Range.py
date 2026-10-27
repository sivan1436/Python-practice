def reverse(n):
    x = n
    rev = 0
    while (n > 0):
        temp = n % 10
        rev = rev * 10 + temp
        n = n // 10
    return rev
a = int(input("Enter the lower bound: "))
b = int(input("Enter upper bound: "))
for i in range (a, b + 1):
    if reverse(i) == i:
        print(i)

