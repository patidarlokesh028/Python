a = int(input("enter any frist number:"))
b = int(input("enter any sencond number:"))
c = int(input("enter any third number:"))

if a > b:
    if a > c:
        print(f"{a} is greatest")
    else:
        print(f"{c} is greatest")

else:
    if b > c:
        print(f"{b} is greatest")
    else:
        print(f"{c} is greatest")