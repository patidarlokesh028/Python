def fun_check():
    my_string = input("enter any number:")
    ucount = 0
    lcount = 0

    for i in my_string:
        if 'A' <= i <= 'Z':
            ucount += 1

        elif 'a' <= i <= 'z':
            lcount += 1

    print(f"the number of uppercase letters in string is: {ucount}")
    print(f"the number of lowercase letters in string is: {lcount} ")

fun_check()