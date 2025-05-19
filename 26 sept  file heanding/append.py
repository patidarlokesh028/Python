# with open('file.txt', 'a') as f:
#     f.write("this is append")
#     f.close()



#   two file are open 

# f1 = open('file.txt', 'r')
# f2 = open('file.txt', 'w')

# for i in f1:
#     f2.write(i)

# f1.close()
# f2.close()




#   image open file 

# f1 = open('img.jpg', 'rb')
# f2 = open('img2.jpg', 'wb')
# print(f.read())

# for i in f1:
#     f2.write(i)

# f1.close()
# f2.close()



#    seek formula in python for the raducs the elements for the given to file



# f = open('file.txt', 'rb')
# f.seek(3)
# print(f.read())

f = open('file.txt', 'rb')
f.seek(-5, 2)
print(f.read())

f.close()