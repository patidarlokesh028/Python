def mydict():
    return 0

li = [22, 11, 34, 56, 67, 78, 34, 11, 45, 56, 12, 90, 45]

for i in li:
    if mydict(i) == li:
        li.remove(i)

    else:
        mydict(i) = li

        print(li)


mydict()