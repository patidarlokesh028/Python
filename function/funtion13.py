a = int(input("enter the frist number:"))
b = int(input("enter the second number:"))
c = int(input("enter the third number:"))

if a > b:
    if a > c:
        print(f"{a} is maximum")

    else:
        print(f"{c} is maximum")

else:
    if b > c:
        print(f"{b} is maximum")

    else:
        print(f"{c} is maximum")

