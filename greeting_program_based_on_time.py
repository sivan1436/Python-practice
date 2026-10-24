time = input()
time = time.split(" ")
mins = time[0].split(".")
print(mins)
if int(mins[1]) > 59:
    print("invalid time")

else:
 if time[1] == 'am':
    if float(time[0]) > 5.00 :
        if float(time[0])<=12.59:
            print("good morning")
    else :
        print("good night")
 if  time[1] == "pm":
    if float(time[0]) >=1:
        if float(time[0]) <= 4.59:
            print("good afternoon")
        if float(time[0]) > 4:
            if float(time[0]) <=7:
                print("good evening")
        if float(time[0]) > 7 :
            if float(time[0]) <=10 :
                print("good night")
