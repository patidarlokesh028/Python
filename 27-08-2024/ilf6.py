list = [34, 67, 89, 523, 45, 254, 562, 623, 322, 1221]

num = int(input("enter any number:"))

if num in list:
    q = num
    rem = 0
    result = 0

    while q != 0:
        rem = q % 10
        result = result * 10 + rem
        q = q // 10

    if result == num:
        print("palindrome")

    else:
        print("not palindrome")

else:
    print("number is not list") 

