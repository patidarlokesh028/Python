num1 = int(input("enter any number:"))
num2 = int(input("enter any number:"))

for i in range(num1, num2 + 1):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")

    print("=====================")