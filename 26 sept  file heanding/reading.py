f = open("file.txt", 'r')
#print(f.read())
#print(f.readline())
#print(f.readable())



#f.close()

with open('file.txt', 'a') as f:
    print(f.read())
    f.close()