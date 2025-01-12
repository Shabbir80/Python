# List difining syntax
fruit = ["Apple","Mango","Orange"]
print(fruit)
print(type(fruit))


a = ["asif","shabbir",23,1.23]
print(a)
print(type(a))

# Slicing List
b = ["Spider Man","Captain America","Hulk","Thor"]

#way of printing list b
print(b)
print(b[:])
print(b[:4])
print(b[0::])
print(b[-4::])
print(b[0:4])

print(b[:2])
print(b[2:])
print(b[1:3])
print(b[0:4:2])
print(b[::-1])
print(b[-1:-4:-1])



# iteration using for Loop
x = ["Spider Man","Captain America","Hulk","Thor"]
for i in x:
    print(i)

# iteration using for loop with range and length function
for i in range (len(x)):
    print(x[i])

# iteration using while loop
j = 0
while j < (len(x)):
    print(x[j])
    j+=1


# Using short-hand for loop
[print(k) for k in x]


# List Function

a = ["Spider Man","Captain America","Hulk","Thor","Hulk"]

b = len(a)
print(b)

print(a.count("Hulk"))

a.append("Iron Man")
print(a)

a.insert(1,"Groot")
print(a)

a.remove("Hulk")
print(a)

a.pop(1)
print(a)


# List Function Part 2

my_list = [25,56]
my_list[0:2] = [99, 100]
print(my_list)

v = ["spider",34,"love",21]
v[1] = "yu"
print(v)

v.reverse()
print(v)

a = [12,45,67,19,99,32]
b = ["Spider Man","Captain America","Hulk","Thor","Hulk"]
print(b.index("Thor"))

a.sort()
print(a)
b.sort()
print(b)

print("the largest no. in the list",a[-1])
print("the smallest no. in the list",a[0])

c = []
c = b.copy()
print(c)

a,b =b,a #swaping element of list
print(a)
print(b)

d = ["asif","saif",23,45]
e = ["hulk","thor",34,23]
d.extend(e)
print(d)

d.clear()
print(d)


#List comprehenshion

l1 = [20,19,46,70,54,12]
l2 = []

for i in l1:
    if i > 45:
     l2.append(i)
print(l1,"\n",l2)


l3 = [i for i in l1 if i < 50]
print(l3)


# Problem Solving

l = ["physic","chemistry","math","bio"] # swaping first and fourth element
l[0],l[3] = l[3],l[0]
print(l)


a = ["physic","chemistry","math","bio"] # inserting new element at second position
a.insert(1,"economy")
print(a)


b = [20,19,46,70,54,12]
b.pop(2)
print(b)

x = 1      # multiply all element in list
c = [20,12,10,5]
for i in c:
     x *= i
print(x)


d = [20,19,46,70,54,12]
d.sort()
print("The largest number in the list is",d[-1])
print("The smallest number in the list is",d[0])




