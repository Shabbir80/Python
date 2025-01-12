# syntax of distionaries
from itertools import product
from os.path import pardir

# a = {"Name":"Asif","Age":20,"Gender":"Male"}
#
# print(a)
# print(type(a))
# print(a["Name"])
# print(a["Age"])
#
#
# # iteration in ditionaries
#
# student = {"Name":"Asif","Age":20,"Gender":"Male"}
# for i in student:
#     print(i) # it give keys
#
# # using keys function
# for i in student.keys():
#     print(i)
#
#
# for i in student:
#     print(student[i]) # it gives value
#
# # using values function
# for i in student.values():
#     print(i)
#
#
# # using items function for printing keys and values
# for i,j in student.items():
#     print(i,"-",j)
#
#
# # Distionaries function Part 1

# student = {"Name":"Asif","Roll No.":45,"Age":20,"Gender":"Male"}
#
# print(student.get("Name"))
# print(student.keys())
# print(student.values())
# print(student.items())
#
# x = student.copy()
# print(x)


# # Distionaries function Part 2
#
# student1 = {"Name":"Asif","Roll No.":45,"Age":20,"Gender":"Male"}
#
# x = student1.setdefault("Roll No.",40) #Roll no. already exist so no change
# print(student1)
#
# y = student1.setdefault("Class",10) #Class does not exist so it`s added with value 10
# print(student1)
#
#
# student1.update({"Class":11,"Age":21,"Roll No.":30})
# print(student1)
#
# student1.update({"Class":11,"Age":21,"Roll No.":30,"Father Name":"Md Tahir Hussain"})
# print(student1)
#
#
# x = student1.pop("Age")
# print(student1)
# print(x)
#
#
# key_value = student1.popitem()
# print(student1)
# print(key_value)
#
#
# student1.clear()
# print(student1



# Nested Distionaries

students = {1:{"Name":"Asif","Roll No.":45,"Age":20,"Gender":"Male"},
            2:{"Name":"Arif","Roll No.":30,"Age":19,"Gender":"Male"},
            3:{"Name":"Lisa","Roll No.":12,"Age":20,"Gender":"Female"},
            4:{"Name":"Danish","Roll No.":3,"Age":20,"Gender":"Male"}}
print(students)
print(students[2])
print(students[3]["Gender"])



# Problem solving

a = {"a":2,"b":5,"c":10,"d":12}
x = sorted(a.values())
print(x)
z = sorted(a.keys())
print(z)


b = {}
for i in range (1,16) :
    b[i] = i ** 2
print(b)


c = {"a":2,"b":5,"c":10,"d":12}
product = 1
for i in c.values():
    product *= i

print(product)


d = {"d":2,"z":5,"a":10,"f":12}
d = sorted(d.keys())
print(d)


# Problem Solving 2

import json

student = {"Name":"Asif","Age":20,"Gender":"Male"}
print(type(student))

student1 = json.dumps(student)
print(student1)
print(type(student1))



person1 = '{"Name":"Asif","Age":20,"Gender":"Male"}'
print(type(person1))
data1 = json.loads(person1)
print(type(data1))
print(data1["Age"])



person2 = {"Name":"Asif","Age":20,"Gender":"Male"}
data2 = json.dumps(person2,indent=4,separators=(",","="))
print(data2)


# demo1.json
person3 = {"Name":"Asif","Age":20,"Gender":"Male"}
f = open("demo1.json","w")
data3 = json.dumps(person3,indent=4,sort_keys=True)
f.write(data3)
f.close()


person4 = """{"Name":{"Asif":{"Son of":{"Father_Name":"Md Tahir hussain","Age":48,"Gender":"Male"}}}}"""
data4 = json.loads(person4)
print(data4["Name"]["Asif"]["Son of"]["Father_Name"])


