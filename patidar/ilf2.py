num = int(input("enter any number:"))

i = 1
while i <= num:
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
    i += 1