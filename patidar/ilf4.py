num = int(input("enter any number:"))
flag = False
for i in range(2, num):
    if num % i == 0:
        flag = True

if flag:
    print(f"{num} is composite")

else:
    print(f"{num} is prime")