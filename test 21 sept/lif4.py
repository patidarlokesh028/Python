li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newli = list(filter(lambda x: x % 2 != 0, li))

print(newli)