m = int(input()) 
n = int(input())
op = 127734 
rem = 0
term = 0
def zeros(tp):
    t = 1 
    while tp > 0:
        t=t*10 
        tp -=1 
    return t        
    
term = 0 
rem = 0
nt = 0
x=n 
while x > 0:
    nt += 1
    x = x//10 
mt = 0 
y = m 
mt = 0 
while y > 0 :
    mt += 1 
    y = y//10
if mt %2 == 0:   
 rem = m%zeros(nt)
 term = m//zeros(nt)
 print(rem)
 print(term)
 term = term*zeros(nt) + n 
 print(term)
 term = term*zeros(nt) + rem 
 print(term)
else :
 rem = m%zeros(nt+1)
 term = m//zeros(nt+1)
 print(rem)
 print(term)
 term = term*zeros(nt) + n 
 print(term)
 term = term*zeros(nt+1) + rem 
 print(term)
        
# program for n natural number
n = int(input())
total = int((n*(n+1))/2)
print(total)  
#print 1/n! by using recursion 
#factorial by using recursion
def fact(t):
    if t == 1 or t==0:
        return 1
    return t*fact(t-1)
n = int(input())
print(f"1/{fact(n)}")


#print x^n/n! by using recursion 
def fact(t):
    if t == 1 or t== 0:
        return 1 
    return t*fact(t-1)
def power(x,n):
   if n == 0:
       return 1 
   return x*power(x,n-1)   
n = int(input())
x = int(input())
print(f"{power(x,n)}/{fact(n)}")    
       
       

       
       
   