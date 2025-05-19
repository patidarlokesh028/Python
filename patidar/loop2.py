num = int(input("enter any number:"))
q = 0
rem = 0
result = 0

while num != 0:
    rem = num % 10
    result = result * 10 + rem
    num = num // 10

if result == q:
    print(f"palindrome")
else:
    print(f"not palindome")