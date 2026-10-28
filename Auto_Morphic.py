def Zeros (n):
    t = 1 
    while n > 0 :
        t *=10
        n-=1
    return t
def AutoMorphic(n):
 x = n 
 number_of_Digits_in_n = 0
 while x > 0 :
     number_of_Digits_in_n +=1 
     x //=10
 temp = n**2
 x = temp % Zeros(number_of_Digits_in_n)
  
 if x == n:
     return True
 else:
    return False

def AutoMorphicRange(a, b):
     for i in range(a, b + 1):
         if AutoMorphic(i):
             print(i, end=" ")

def AutoMorphicNear(n):
     if AutoMorphic(n):
         print("\ngiven number is Automorphic", n)
     l = n - 1
     r = n + 1
     while not AutoMorphic(l):
         l -= 1
     while not AutoMorphic(r):
         r += 1
     print("Left AutoMorphic", l)
     print("Right Automophic", r)
     if (r - n) > (n - l):
         print("Near Automophic", l)
     else:
         print("Near Automorphic", r)

def nthAutomophic(n):
     count = 0
     i = 1
     while count < n:
         if AutoMorphic(i):
             count += 1
         if count == n:
             break
         i += 1
     print("nth Trimophic", i)

n = int(input("Enter a Number:"))
AutoMorphicRange(a=int(input("enter lower bound:")), b=int(input("enter upper bound:")))
AutoMorphicNear(n)
nthAutomophic(n=int(input("enter n value:")))
print(AutoMorphic(n))
