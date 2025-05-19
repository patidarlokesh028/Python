num = int(input("enter any number:"))
evensum = 0
oddsum = 0

for i in range(1, num+1):
    if i % 2 == 0:
        evensum = evensum + i
    else:    
        oddsum = oddsum + i

print(f"the sum of all even numbers is: {evensum}")
print(f"the sum of all odd number is: {oddsum}")