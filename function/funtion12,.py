num = int(input("enter any number:"))

rem = 0
result = 0
q = num


while num != 0:
    rem = num % 10
    result = result % 10 + rem
    num = num // 10


if result == q:
    print(f"{num} is palindorme")

else:
    print(f"{num} is not palindorme")