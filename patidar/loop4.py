for i in range(1, 501):
    q = i
    rem = 0
    result = 0

    while q != 0:
        rem = q % 10
        result = result * 10 + rem
        q = q// 10

        if result == i:
            print(f"{i} is palindrome")
        else:
             print(f"{i} is not palindrome")