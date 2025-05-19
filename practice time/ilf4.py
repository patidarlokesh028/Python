a = int(input("enter any number:"))
b = int(input("enter any number:"))
c = int(input("enter any number:"))

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