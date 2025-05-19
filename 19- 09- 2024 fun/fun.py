# Required Arguments and Dfault Arguments

def sum(a, b, c = 10):
    print(f"the sum is: {a + b + c}")

sum(20, 30)

print("=================================")

# Keyword Arguments

def fun(name, age):
    print(f"Hello {name} your age is: {age}")


fun(age = 20, name = "jhon")

print("=================================")

# Variable Length Argument

def fun(*args):
    print(args)

    add = 0
    for i in args:
        add = add + 1

    print(f"Sum = {add}")

fun(10, 20, 30)

print("===============================")

# keyword Arbitery Arguments
def fun(**Kwargs):
    print(Kwargs)

    for key, value in Kwargs.items():
        print(f"the value on {key} is: {value}")

fun(name= "jhon", age=20, email="jhon@test.com")


print("==================================")

#Positional Only Arguments
def fun(name, /, age):
    print(f"Hello {name} your age is: {age}")

fun("jhon",20)


print("===================================")

# Keyword Only Arguments

def fun(*, name, age):
    print(f"Hello {name} your age is: {age}")

fun(name= "jhon", age= 20)

print("=================================")

def fun(name, age, email):
    print(f"name = {name}")
    print(f"age = {age}")
    print(f"email = {email}")

dic1 = {"name": "jhon", "age": 20, "email":"jhon@test.com"}

fun(**dic1)

print("===========================================")


def fun(x):
    n = 0

    if x == 1:
        return x
    
    else:
        n = x + fun(x - 1)
        return n
    
z = fun(3)
print(z)

print('=================================================')


a = 10

def fun():
    global a
    a = 5

    print(f"in funtion = {a}")


fun()
print(f"Outside function = {a}")

print("=============================================")