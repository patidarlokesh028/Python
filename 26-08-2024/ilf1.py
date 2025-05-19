def fun():
    my_string = input("enter the string:")
    vcount = 0
    ccount = 0

    for i in my_string:
         if i == 'A' or 'E' or 'I' or 'O' or 'u' or 'a' or 'e' or 'i' or 'o' or 'o':
           vcount += 1

    else:
         ccount += 1


    print("the number of vowel letters in string is: {vcount}")
    print("the number of consonents letters in string is: {ccount}")

fun()