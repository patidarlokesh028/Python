dic1 = {'a': 200, 'b': 100, 'c': 300}
dic2 = {'a': 100, 'c': 500, 'd': 400}

dic3 = dic1.copy()
for i, value in dic2.items():
    if i in dic3:
        dic3[i] += value

    else:
        dic3[i] = value

print(dic3)