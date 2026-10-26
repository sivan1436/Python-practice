def Squre_of_digits(n):
    if n <=9 :
        return n
    x = n 
    sum = 0 
    while x > 0 :
        sum += (x%10)**2
        x //=10
    return Squre_of_digits(sum)    
def HappyNumber(n):
    temp = Squre_of_digits(n)
    if temp == 1:
        return True 
    else :
        return False
n = int(input()) 
print(HappyNumber(n)) 