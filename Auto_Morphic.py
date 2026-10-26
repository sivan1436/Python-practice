def Zeros (n):
    t = 1 
    while n > 0 :
        t *=10
        n-=1
    return t    
def AutoMoprphic(n):
 x = n 
 number_of_Digits_in_n = 0
 while x > 0 :
     number_of_Digits_in_n +=1 
     x //=10
 temp = n*power(n,2)
 x = temp % Zeros(number_of_Digits_in_n)
  
 if x == n:
     return True
 else:
    return False
n = int(input())
print(AutoMoprphic(n))