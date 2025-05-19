def evenodd():
    evensum = 0
    oddsum = 0

    num = int(input("enter any number:"))
    for i in range(1 , num + 1):
        if i % 2 == 0:
            evensum = evensum + i

        else:
            oddsum = oddsum + i

    print(f"the sum of all number is: {evensum}")
    print(f"the sum of all number is: {oddsum}")

    
evenodd()