li = [2, 56, 34, 32, 78, 33, 99, 11, 77, 29, 23]

num = int(input("enter any number:"))

flag = False

if num in li:
    for i in range(2, num):
        if num % i == 0:
            flag = True
            break
    if flag:
        print("composite")

    else:
        print("prime")

else:
    print("number is not list")
