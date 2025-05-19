li = [11, 56, 77, 66, 66, 78, 23, 77, 56]
num = int(input("enter any number:"))

count = 0
flag = False

for i in li:
    if num == i:
        flag = True
        count += 1

if flag:
    print(f"{num} is in the list and was repeated {count} times")

else:
    print(f"{num} is not in the list")       