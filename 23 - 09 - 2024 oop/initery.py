# single leval Inheritance

# class base:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print(f"the name is: {self.name}")
#         print(f"the age is: {self.age}")

# class derived(base):
#     def __init__(self, name, age, salary, propession):
#         super().__init__(name, age)

#         self.salary = salary
#         self.propession = propession

#     def getdata(self):
#         print(f"the salary is: {self.salary}")
#         print(f"the profession is: {self.propession} ")


# obj = derived("nayan", 24, 25000, "teacher")
# obj.show()
# obj.getdata()


#  multilevel Inheritance
# class animal:
#     def __init__(self):
#         print("I am an animal")

# class dog(animal):
#     def __init__(self):
#         print("Barking...")
#         super().__init__()

# class babydog(dog):
#     def __init__(self):
#         print("Weeping...")
#         super().__init__()

# bd = babydog()


#    print("===========================================")


# class animal:
#     def animal(self):
#         print("I am an animal")

# class dog(animal):
#     def bark(self):
#         print("Barking...")

# class babydog(dog):
#     def weep(self):
#         print("weeping...")

# db = babydog()
# db.animal() 
# db.bark()
# db.weep()



#   print("============================")

# class base_class1:
#     def show1(self):
#         print("This is the first function of base class")

# class base_class2:
#     def show2(self):
#         print("this is the second function of base class")

# class child_class(base_class1, base_class2):
#     def show3(self):
#         print("this is the function of child class")


# obj = child_class()
# obj.show1()
# obj.show2()
# obj.show3()

#print("=================================")

# class base_class1:
#      def __init__(self):
#          print("This is the first function of base class")

# class base_class2:
#      def __init__(self):
#          print("this is the second function of base class")
# class child_class(base_class1, base_class2):
#      def __init__(self):
#          print("this is the function of child class")
#          super().__init__()
         
# obj = child_class()

# print("=======================================")


#  Decorator

# def fun(fn):
#     def mod_fun():
#         print("Hello")
#         fn()

#     return mod_fun

# @fun
# def greet():
#     print("Good Morning")

# greet()