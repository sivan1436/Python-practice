def reverse(n):
    x = n
    rev = 0
    palindrome = False
    while (x > 0):
        temp = x % 10
        rev = rev * 10 + temp
        x = x // 10
    if rev == n :
        palindrome = True
    return palindrome
n = int(input("Enter a number: "))
if reverse(n):
    print("given number is a palindrome")
else:
 r = n + 1
 l = n-1
 while not reverse(r):
    r+=1
 while not reverse(l):
    l-=1
 if ((r-n) > (n-l)):
    print(l,end=" ")
 else:
    print(r,end=" ")
 print("\nPrevious palindrome:",l)
 print("\nNext palindrome:",r)


