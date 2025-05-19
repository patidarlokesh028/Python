def fun(choice):
    if choice == 1:
        num = int(input("enter any number:"))

        a = -1
        b = 1
        c = 0

        for i in range(1, num + 1):
            c = a + b
            print(c)
            a = b
            b = c

        print("===================================================")

    elif choice == 2:
         num = int(input("enter any number:"))
         flag = False

         for i in range(2, num):
             if num % i == 0:

                 flag = True
                 break

         if flag:
             print(f"{num} is composite")

         else:
             print(f"{num} is prime")


         print("=================================================")

    elif choice == 3:
        num = int(input("enter any number:"))
        rem = 0
        result = 0
        q = num

        while q != 0:
            rem = q % 10
            result = result + 10 + rem
            q = q // 10

        if result == num:
            print(f"{num} is palindrome")

        else:
            print(f"{num} is not plindorme")

        print("=================================")

print("choose from below options")
print("1 for fibonaci series")
print("2 for prime number")
print("3 for palindrome number")
print("4 for exit")

print("========================================")

while True:
    choice = int(input("enter your choice:"))

    print("============================================")


    if choice == 1:
        fun(choice)

    elif choice == 2:
        fun(choice)

    elif choice == 3:
        fun(choice)

    elif choice == 4:
        print("code exited")

        break

    else:
        print("invalid choice\ntry again")

    print("=======================================")