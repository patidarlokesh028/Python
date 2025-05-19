li = [23, 76, 88, 34, 56, 223, 12, 9, 967, 44, 77]

num = int(input("enter any number:"))
flag = False

for i in li:
    if num == i:
        flag = True
        print(f"{num} is the list")

if not flag:
    print(f"{num} is not in list")