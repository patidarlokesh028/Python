#Dic1 = {"Name": "jhon", "Age": 23, "email": "Jhon@test.com"}
#print(type(Dic1))
#print(Dic1)
#print(Dic1["Age"]

#dic1 = {"name": "jhon", "age": 23, "email": "jhon@test.com"}
#dic2 = {"profession": "developer", "language": "python", "contact": "5456445157"}

#dic1.update(dic2)
#dic1.popitem()
#dic1.pop("name")
#dic2 = dic1.copy()
#dic1.clear()
#print(dic1.get("A"))
#print(dic1['A'])
#print(dic1.key())
#print(dic1.value())
#print(dic1.items())
#print(dic1)


#for key in dic1.keys():
#   print(f"the value on {key} is: {dic1[key]}")


#for value in dic1.values():
#    print(f"the value is: {value}")

#for key, value in dic1.items():
#    print(f"the value on {key} is: {value}")


#li = [1, 2, 3]
#dic2 = dict().fromkeys(li,"none")
#print(dic2)

#dic1.setdefault('A', 56)
#del dic1["age"]
#print(dic1)

#value = dic1.pop("name", "this key does not exist")
#print(value)


dic1 = {"name": "jhon", "age":23, "email": "jhon@test.com"}
key = input("enter any key:")

if key in dic1:
    print("yes")

else:
    print("no")
