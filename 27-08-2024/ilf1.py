list = [2, 45, 67, 55, 595, 447, 74, 23, 57]

evensum = 0
oddsum = 0

for i in list:
    if i % 2 == 0:
        evensum = evensum + 1

    else:
        oddsum = oddsum + 1

print(f"the evensum of the elements list is: {evensum}")
print(f"the oddsum of the elements list is: {oddsum} ")
        