tup = (24, 56, 234, 77, 89, 36, 56, 66, 452)
num = int(input("enter the number you want to  append:"))

temp = list(tup)
temp.append(num)
tup = tuple(temp)

print(tup)