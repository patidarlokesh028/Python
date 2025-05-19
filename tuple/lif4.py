tup = (34, 23, 67, 32, 'Hello', 56.8, 90)

#print(tup.count(34))
#print(tup.index(90))

temp = list(tup)
temp.append(40)
temp.remove('Hello')
temp.extend([80, 60, 50])

tup = tuple(temp)
print(tup)