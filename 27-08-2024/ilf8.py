def fun(li1, li2):
    flag = False
    for i in li1: 
        for j in li2:
            if i == j:
                flag = True
    
    if flag:
        return True
    
    else:
        return False

li1 = [32, 67, 45, 77, 42, 565, 23, 11]
li2 = [32, 76, 23, 112, 42, 645, 1, 11]

if fun(li1,li2):
    print("there is a same element in both list")

else:
    print("there is no same element in both list")