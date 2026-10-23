n = int(input())
if n < 99: #checking if the 3 digit or not 
  print("please enter a 3 digit number")
  
else :  
 prime = True
 for i in range(2,int(n/2)+1):
   if n%i == 0:
    prime = False
    break
 if prime : #checking given num is prime or not
  print(" given number is prime : ",n)
 else:
  x = n-1
  while n>2:
    l_prime = True # checking for left prime
    for i in range(2,int(x/2)+1):
      if x%i == 0:
        l_prime = False
        break
    if l_prime:
      l=x
      break
    else:
      x=x-1
  print(l) 
  r=0
  y=n+1 #cheking for right prime
  while y > 1:
    r_prime = True
    for i in range(2,int(y/2)+1):
      if y%i == 0:
        r_prime = False
        break
    if r_prime:
      r=y
      break
    else:
      y=y+1
  print(r) 
  if (n-l)<(r-n):#checking for nearest prime
      prime = l
  else:
      prime = r
  print(prime)  # printing nearest prime         
      
        
      
        
    
    