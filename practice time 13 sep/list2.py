li = [5, 34,  12, 56, 78, 89, 90, 30, 22, 33, 45]

num = int(input("enter any number:"))

flag = False

for i in li:
    if num == i:
        flag = True
        print(f"{num} is in the list")
        break

if not flag:
    print(f"{num} is not in the list")