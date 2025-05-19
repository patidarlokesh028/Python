class base_class:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class child_class1(base_class):
    def __init__(self, a, b):
        super().__init__(a, b)


    def product(self):
        print(f"Product = {self.a * self.b}")

class child_class2(base_class):
    def __init__(self, a, b):
        super().__init__(a, b)


    def add(self):
        print(f"the sum is: {self.a + self.b}")


obj1 = child_class1(10, 2)
obj2 = child_class2(90, 40)

obj1.product()
obj2.add()