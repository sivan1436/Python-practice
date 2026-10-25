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

        
        
       
       
       
   