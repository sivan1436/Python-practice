def zeros(n):
    temp = 1 
    while n > 0 :
        temp *=10 
        n -= 1 
    return temp    
m = int(input())
def EVENSFIRST_ODDSAFTER(m): 
 E = 0
 O = 0
 x =m
 c = 0 
 while x > 0 :
    c +=1 
    x //=10
 i = 1    
 while m > 0 :
    
     temp = m // zeros(c-i) 
     print("DIGIT: " ,temp)
     if temp % 2 == 0 :
         if E == 0 :
             E = temp
             print("EVEN:" ,E)
         else :     
           E = E*10 + temp 
           print("EVEN:",E)00
     else : 
         if O == 0:
             O = temp 
             print("ODDS:",O)
         else :
             O = O*10 + temp
             print("OODS:",O)
     m =m%zeros(c-i)
     i+=1
 y = O 
 print("OODS",O)
 print("EVENS :",E)
 a = 0 
 while y > 0 :
    a += 1 
    y //=10 
 print("OOD counts ",a)    
 E = E*zeros(a) + O 
 return E  
    