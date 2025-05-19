def  digits_count():
    num = int(input("enter any number:"))
    count = 0
    while num != 0:
        num = num // 10
        count += 1
    print(f"the number is digits: {count}")

digits_count()