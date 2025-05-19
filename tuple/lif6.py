tup = (23, 45, 67, 8, 14, 55, 43, 68, 34, 11, 7, 9, 6, 5, 4, 22)

num = int(input("enter the number you want to append:"))

temp = list(tup)
temp.append(num)
tup = tuple(temp)

print(tup)