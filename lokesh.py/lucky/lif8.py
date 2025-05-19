# 0 1 1 2 3 5 8 13
# a      b       c
# -1      1       0
#   1     0       1
#   0     1       1
#  1      1       2
#   1     2       3
#  2      3       5

num = int(input("enter any number:"))
a = -1
b =  1
c =  0

for i in range(1, num + 1):
    c = a + b
    print(c)