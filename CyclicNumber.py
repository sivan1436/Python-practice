def SumOfDigits(n):
    digits = []
    while n>0:
        t= n%10
        digits.append(t)
        n=n//10
    return digits
def CyclicNumber(n):
    for i in range(1,6+1):
        temp = n*i
        if SumOfDigits(n) != SumOfDigits(temp):
            return False
    return True
print(CyclicNumber(n=int(input("Enter a number: "))))

