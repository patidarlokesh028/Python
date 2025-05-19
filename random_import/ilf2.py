def evenodd():
    num = int(input("enter any number:"))
    for i in range(1, num+1):
        if i % 2 == 0:
             print("{i} is even")

        else:
            print("{i} is odd")

evenodd()