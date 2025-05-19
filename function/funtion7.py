def reversed():
    num = int(input("enter any number:"))
    rem = 0
    result = 0
    while num != 0:
        rem = num % 10
        result = result * 10 + rem
        num = num // 10
    print(f"tne reversed number is: {result}")

reversed()