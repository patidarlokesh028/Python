li = [55, 67, 676, 73, 55, 67, 22, 78, 42, 73]

uni = []
dup = []

for ele in li:
    if ele not in uni:
        uni.append(ele)

    elif ele not in dup:
        dup.append(ele)

print(dup)
print(uni)