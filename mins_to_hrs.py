mins = int(input())
hr = ""
while mins > 0 :
    if mins > 59:
        hr +=str((mins//60))
        mins=mins%60
    else:
        hr+="."+str(mins)
        mins = 0
hrs = list(hr)
if hrs[0]==".":
    hr = "12"+hr
if float(hr) > 24 :
    print("mins has exceed then 24hr")
else:
    hr = hr.replace(".",":")
    print(f"{hr} mins")
    
