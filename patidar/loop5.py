q = 0
flag = False
for i in range(1, 501):
    if q % i == 0:
        flag = True

if flag:
    print(f"{q} is prime")

    
