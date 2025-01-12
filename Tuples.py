# # Syntax of tuple and it is mutable
#
# a = "boi","che","phy",12,56,98
# print(type(a))
# print(a)
#
# b = "asif",
# print(type(b))
#
#
# # Slicing tuples
#
# c = "boi","che","phy",12,56,98
#
# print("Print element at 2nd and 3rd position",c[1:3])
# print(c[:3])
# print(c[3:])
# print(c[::])
# print(c[::2])
# print(c[1::2])
# print(c[::-1])
# print(c[::-1])
# print(c[-1:-4:-1])
#
#
# # coversion of tuples into list
# t = "boi","che","phy",12,56,98
# print(t)
#
# t = list(t)
# print(type(t))
# print(t)
#
# t.append("eco")
# print(t)
#
# t = tuple(t)
# print(t)

# Iteration in tuples with for loop

m = "boi","che","phy",12,56,98
for j in m: #with for loop
    print(j)

for i in range(len(m)): #along in range and lenght in for loop
    print(m[i])


print(m.count("che"))
print(m.index("phy"))


# iteration in tuples in while

n = "boi","che","phy",12,56,98

p = 0
while len(n) > p:
    print(n[p])
    p += 1






