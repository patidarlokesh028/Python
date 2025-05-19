def check_palindorme():
    num = int(input("enter any number:"))
    flag = False
    rem = 0
    result = 0
    q = num


    while q != 0:
        rem = q % 10
        result = result * 10 + rem
        q = q // 10
        flag = True
        break

    if flag:
        return True
    
    else:
        return False
    

X = check_palindorme()