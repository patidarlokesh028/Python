def check_digits():
    num = int(input("enter any number:"))
    count = 0

    while num != 0:
        num = num // 10
        count += 1


    return count

X = check_digits()

