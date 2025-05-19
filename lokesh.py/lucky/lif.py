year = int(input("enter any year:"))

if year % 100 == 0:
    if year % 400 == 0:
        print("century year and leap year")
    else:
        print("century year not a leap year")
else:
    if year % 4 == 0:
        print("non_century year and leap year")
    else:
        ("non-century year not a leap year")