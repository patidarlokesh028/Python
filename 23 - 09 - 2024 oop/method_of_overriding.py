# class base:
#     def fun(self):
#         print("hello form base class")

# class child(base):
#     def fun(self):
#         print("hello form child class")

# obj = child()
# obj.fun()

#print("==================================")

# DUCK TYPING

# class duck():
#     def quack(self):
#         print("quack")

    
#     def fly(self):
#         print("the duck is flying")


# class airplane:
#     def quack(self):
#         print("the airpalane can't quack, but let's pretend it can")

    
#     def fly(self):
#         print("the airplane is flying")

# def make_it_fly_and_quack(thing):
#     thing.quack()
#     thing.fly()

# Duck = duck()
# Airplane = airplane()

# make_it_fly_and_quack(Duck)
# make_it_fly_and_quack(Airplane)

# print("==============================================")

