# #Syntax of set
# a = {"a","b",5,"c",10,"d"}
# print(a)
# print(type(a))
#
# #iteration in set
# for i in a:
#     print(i)
#
#
# # set function part 1
# b = {"a","b","c","d"}
# b.add('x')
# print(b)
#
#
# b.pop()
# print(b)
#
#
# b.remove("x") #remove & discard are same
# print(b)
# b.discard("a")
# print(b)
#
#
# c = {"a","b",5,"c",10,"d"}
# x = c.copy()
# print(x)
#
#
# # set function part 2
# x = {"a","b",5,"c",10,"d"}
# y = {"e","f","g","h"}
# z = {"e","f",5}
# s = {"b",5,"c",10}
#
#
# print(x.isdisjoint(y)) # Returns True if two sets have no common elements.
# print(x.isdisjoint(z))
#
#
# print(s.issubset(x)) # Returns True if all elements of the set are in another set.
# print(x.issubset(s))
#
#
# print(x.issuperset(s)) # Returns True if the set contains all elements of another set.
# print(s.issuperset(x))
#
#
# x.update(z) # Adds elements from another set or iterable to the set.
# print(x)
# print(z)
#
#
# x.clear() #  Removes all elements from the set, leaving it empty.
# print(x)


# set function part 3

x = {"a","b",5,"c",10,"d"}
z = {"e","f",5}

print(x.union(z))


print(x.difference(z))
print(z.difference(x))

a = {"a","b",5,"c",10,"d"}
b = {"e","f",5}

a.difference_update(b)
print(a)


c = {"a","b",5,"c",10,"d"}
d = {"a","f",5}

print(c.intersection(d))


c.intersection_update(d)
print(c)


e = {"a","b",5,"c",10,"d"}
f = {"a","f",5}

print(e.symmetric_difference(f))

e.symmetric_difference_update(f)
print(e)


# Problem Solving

set1 = {67,43,35,89,12,5,99,34}

maximum = max(set1)
minimum = min(set1)
print("The maximum number in set1 is",maximum)
print("the minimum numbere in set1 is",minimum)


a = {67,43,35,89,12,5,99,34}
b = {6,43,30,89,12,5,90,34}
c =  {43,89,34,35}
print("The comman element in the sets are",a&b&c)


a = list(set1)
print(a)







