# class bussiness:
#     name = "jhon"
#     expense = 3000
#     profit = 1000
#     marketing_expense = 500

#     def show_data(self):
#         print(f"name = {self.name}")
#         print(f"expense = {self.expense}")
#         print(f"profit = {self.profit}")
#         print(f"marketing_expense = {self.marketing_expense}")

# b1 = bussiness()
# b2 = bussiness()

# b2.name = "rahul"
# b2.expense = 5000
# b2.profit = 1000
# b2.marketing_expense = 500

# b1.show_data()
# b2.show_data()

#     print("================================")


class student():
    def __init__(self):
        self.name = input("enter any name")
        self.age = int(input("enter any age"))
        self.roll_number = int(input("enter any roll_number"))


    def show_data(self):
        print(f"the name is: {self.name}")
        print(f"the age is: {self.age}")
        print(f"the roll_number is: {self.roll_number}")

s1 = student()
s2 = student()

s1.show_data()
s2.show_data()


print("===========================================")


# class employee:
 
#     def __init__(self, name, emp_id, salary):
#         self.name = name
#         self.emp_id = emp_id
#         self.salary = salary

#     def show_data(self):
#         print(f"the name is : {self.name}")
#         print(f"the emp_id is: {self.emp_id}")
#         print(f"the salary is: {self.salary}")

# em1 = employee("vinay", 101, 20000)
# em2 = employee("rahul", 102, 15000)

# em1.show_data()
# em2.show_data()

#print("=======================================")


# Types of variables

# class fun():
#     school = "THE PRIME STEP"
#     def __init__(self, name):
#         self.name = name

#     def show_data(self):
#         print(f"the name is: {self.name}")

# f1 = fun("jhon");
# f2 = fun("rahul")

# fun.school = "PRIME STEP"

# print(f1.school)
# print(f2.school)


#  print("=====================================")

# types of methods

# class fun:
#     def show(self):
#         print("I am a intance method")

#         @classmethod
#         def clfun(cls):
#             print("I am a class method")

#         @staticmethod
#         def add(a, b):
#             print(f"the addition is: {a + b}")

# f1 = fun()
# f2 = fun()

# f1.show()
# fun.clfun()
# f1.add(10, 20)

#    print("===============================================================")

# Constructor

# class student:
#     def __init__(self, name, age, roll_number):
#         self.name = name
#         self.age = age
#         self.roll_number = roll_number

#     def show_data(self):
#         print(f"the name is: {self.name}")
#         print(f"the age is: {self.age}")
#         print(f"the roll_number is: {self.roll_number}")


# s1 = student("jhon", 12, 1)
# s2 = student("rahul", 20, 2)

# s1.show_data()
# s2.show_data()



