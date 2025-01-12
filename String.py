# # String manupulation Part 1
# a = "Why fit in, When you are Born to Stand Out!"
#
# b = len(a) # length
# print(b)
#
# print(a.count("o")) # counting how many times occure
#
# x = a.lower() # converting text into lower and upper case
# print(x)
# print(a.casefold()) #lower case
#
# z = a.upper()
# print(z)
#
# e = a.title()
# print(e)
#
# print(a.find("When")) # index of When and find and index are same
#
# print(a.index("W",10,18))
#
# print(a.capitalize()) #capitalize first alphabet of string
#
# name = "Asif"
# age = 20
# n = "My name is {}.and my age is {}"
# print(n.format(name,age))
#
# print(name.center(24,"-"))



# # String function Part 2
#
# a = "hello"
# b = "hello123"
# c = "12345"
# d = "HELLO"
# e = " "
# f = "Hello 123@"
# g = "123.45"
# h = "HELLO123@"
# i = "Why fit in, When you are Born to Stand Out!"
# j = "Why Fit In, When You Are Born To Stand Out!"
#
# print(a, a.isalnum())
# print(b, b.isalnum())
# print(g, g.isalnum())
# print(c,c.isalnum())
#
#
# print(g, g.isdecimal())
# print(c, c.isdecimal())
#
# print(g, g.isdigit())
# print(c, c.isdigit())
# print(b, b.isdigit())
#
# print(g, g.isnumeric())
# print(c, c.isnumeric())
#
# print(a, a.islower())
# print(d, d.islower())
# print(b, b.islower())
#
# print(a, a.isupper())
# print(d, d.isupper())
# print(h, h.isupper())s
#
# print(e, e.isspace())
# print(f, f.isspace())
#
# print(i, i.istitle())
# print(j, j.istitle())


# # String function Part 3
#
# a = "Hary Potter"
# print(a.endswith("r"))
# print(a.endswith("y",0,4))
#
#
# print(a.startswith("H"))
# print(a.startswith("h"))
# print(a.startswith("P",5))
#
#
# print(a.swapcase())
#
#
# b = "     Harry Potter        "
# c = "***********harry potter     ---------------------"
# print(a.strip())
# print(c.strip("*, ,-"))
#
#
# d = "dddf#0001#you#adr"
# e ="Hello.My name is Asif.I am 20 yrs old"
# print(d.split("#"))
# print(e.split("."))
#
#
# f = "Harry Potter"
# x = f.rjust(20,"#")
# print(x,"is my favorite movie")
#
# y = f.ljust(20)
# print(y,"is my favorite movie")
#
# name = "My name is Asif"
# print(name)
# print(name.replace("Asif","Shabbir"))
#
#
# s = "doda is a nothing" # rindex and rfind are same
# print(s.rfind("o",5,))
# print(s.rindex("a",0,5))


# Slicing of String

# a = "Harry Potter and the Goblet Of fire"
# print(a)
# b = "0123456789"
#
# print(a[0:5])
# print(a[-4:])
# print(a[:5])
# print(a[0:12])
#
# print(b)
# print(b[::3])
# print(b[:7:2])
# print(b[::-1])
# print(b[6::-2])



## Problem solving of String

# a = "ASD.YOU.DOP.AWER.CRFH"
# print(a.split("."))
#
#
# b = input("enter here anything:")
# print(sorted(b))
#
#
# c = "hello"
# d = "F.R.I.E.N.D"
#
# print(c.replace("e",""))
#
# print(d.replace(".",""))
#
#
# e = "she is selling sea food at sea shore"
# print(e.count("sea"))


# f = input("Enter here anything :")
# x = f[::-1]
# print(x)
#
# print(f.isdigit())
#
# n = input("Enter (no./word) to check it is palindrome:")
# if n == n[::-1]:
#     print("It is a plindrome")
#
# else:
#     print("it is not a palindrome")


a = input("Enter here string to check number of vowel:")
vowels = 0
for i in a:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U" :
        vowels += 1


print("Number of vowel in the string are" , vowels)

print(a.istitle())















