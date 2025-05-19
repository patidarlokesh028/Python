year = int(input("enter any year:"))

if year % 100 != 0:
    if year % 400 == 0:
        print("this is leap year")
    else:
        print("this is not leap year")

else:
    if year % 4 == 0:
        print("this is leap year")

    else:
        print("this is not leap year")