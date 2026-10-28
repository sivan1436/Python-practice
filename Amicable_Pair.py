def Amicable(a, b):
    Sum1 = 0
    Sum2 = 0
    i = 1

    while i < a:
        if a % i == 0:
            Sum1 += i
        i += 1

    i = 1
    while i < b:
        if b % i == 0:
            Sum2 += i
        i += 1

    if Sum1 == b and Sum2 == a:
        print("Amicable pairs")
    else:
        print("Not amicable pairs")
Amicable(a=int(input("Enter a number: ")),b=int(input("Enter b number: ")))