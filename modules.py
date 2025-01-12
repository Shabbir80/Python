import datetime

x = datetime.datetime.now()
print(x)


y = datetime.datetime(1999,12,19)
print(y.strftime("%A"))
print(y.strftime("%a"))
print(y.strftime("%B"))
print(y.strftime("%b"))
print(y.strftime("%m"))
print(y.strftime("%D"))
print(y.strftime("%d"))
print(y.strftime("%Y"))
print(y.strftime("%y"))



import random

a = random.randint(1,6)
print(a)

l = ["Heads","Tails"]
b = random.choice(l)
print(b)



import math

c = pow(2, 5)
print(c)

d = max(23,12,1001,45,999)
print(d)

e = math.sqrt(81)
print(e)

f = math.cbrt(27)
print(f)

g = abs(-24)
print(g)

h = math.factorial(5)
print(h)

i = math.ceil(2.3)
print(i)

j = math.floor(2.3)
print(j)



