li = [4, 34, 7, 34, 32, 7, 5, 34, 32, 54, 87]

n = len(li)
for i in range(0, n-1):
    for j in range(0, n- i - 1):
        if li[j] > li[j + 1]:
            temp = li[j]
            li[j] = li[j + 1]
            li[j + 1] = temp


print("sorted list")
print(li)