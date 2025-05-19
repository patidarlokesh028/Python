li = (5, 3, 65, 324, 78, 34, 7, 43, 23, 56,89, 54, 23, 23, 56, 87, 56)

Min = li[0]
Max = li[0]
for i in range(1, len(li)):
    if li[i] < Min:
        Min = li[i]

    if li[i] > Max:
        Max = li[i]

print(f"the minimum number in list is: {Min}")
print(f"the maximum number in list is: {Max}")