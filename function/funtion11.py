def palindorme():
    num = int(input("enter any number:"))
    q = num
    rem = 0
    result = 0

    while num != 0:
        rem = num % 10
        result = result % 10 + rem
        num = num // 10

    if result == q:
        print(f"the number is palindorme")

    else:
        print(f"the number is not palindorme")

palindorme()