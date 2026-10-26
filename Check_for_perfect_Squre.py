n = int(input())
perfect = False
for i in range(1,int(n*0.5)+1):
    if i*i == n :
        perfect = True 
        break 
if perfect:
    print("True")
else:
    print("False")
        
    