def fun():
    ncounts = 0
    pcounts = 0
    zcounts = 0

    while True:
        num = int(input("enter any  number:"))
        
        if num > 0:
            pcounts += 1

        elif num == 0:
            zcounts += 1

        else:
            ncounts += 1

        choice = input("do you want to countine:")

        if choice == 'no':
            break
print("===============================")

print(f"the number of positive digits are:{'pcounts'}")
print(f"the number of negative digits are:{'ncounts'} ")
print(f"the number of zero are:{'zcounts'}")

fun()