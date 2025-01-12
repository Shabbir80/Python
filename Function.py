# # Syntax of Functions
# def print_1(): # difination of Function
#     print("Hello World")
#
# print_1() # Calling of Function
#
#
# def add():
#     x = 30
#     y = 70
#     print(x+y)
#
# add()
#
#
# def add(a,b): # a and b are Parameter of the function
#      print(a+b)
#
# add(34,66) # 34 and 66 are Argument of the function
# add(20,45)
# add(5,5)
#
#
# def rec(l,b):
#     print("The area of the rectangle is",l*b)
#
# rec(40,20)
# rec(6,9)
#
#
# def a(*name):
#     print("Hello,my name is",name[0])
#
# a("Asif","John","Raja")



# def sum(x,y):
#     sum = x+ y
#     return sum
#
# a = float(input("Enter a number here"))
# b = float(input("Enter a another here"))
# tol = sum(a,b)
# print("The sum is",tol)


# def hello():
#     print("Hello")
#     return hello()
# hello()


# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     elif n < 0:
#         return "None"
#     else:
#         return (n * factorial(n-1))
#
# n = int(input("Enter a number here to get factorial of the number"))
# fact = factorial(n)
# print("Factorial of the number is",fact)



# #  Lambda Function
#
# a = lambda b : b * 6
# print(a(5))
#
#
# x = lambda p,q,r,s : p * q + r * s
# print(x(2,3,5,4))



# Globle function

# a = 34
# print("First value of a is",a)
#
# def b() :
#     global a
#     a = 35
#     print(a)
# b()
# print(a)


# Using function find maximum number

# def num(x,y,z):
#     if x > y and x > z:
#         return x
#     elif y > x and y > z:
#         return y
#     else:
#         return z
# print("The maximum number is",num(78,45,999))



# Printing Prime Number using Function

# def num(n):
#     if n <= 1 :
#         return "is not a prime number"
#     elif n == 2:
#         return "is a prime number"
#     else:
#         for i in range (2,n):
#            if n % i == 0:
#              return "is not a prime number"
#         return "is a prime number"
#
# n = int(input("Enter number here to check Prime or Not:"))
# m = num(n)
# print(n,m)



# Printing list which is square of no. 1 to 30

# def list_square():
#     l = []
#     for i in range (1,31):
#         l.append(i ** 2)
#     print(l)
#
# list_square()



# To add all number in list

# def add(list):
#     sum = 0
#     for i in list:
#         sum += i
#     return sum
#
# # print(add([5,10,8,2,5,]))
#
# def sum(l):
#     if len(l) == 0:
#         return 0
#     else:
#         return l[0] + sum(l[1:])
#
# print(sum([5,10,8,2,5,]))
#
#
#
# def fibonacci(n):
#     fib_sequence = []  # To store the Fibonacci sequence
#     a, b = 0, 1  # Initial two numbers in the sequence
#     for i in range(n):
#         fib_sequence.append(a)
#         a, b = b, a + b  # Update a and b
#     return fib_sequence
#
# n = int(input("Enter the number of Fibonacci numbers to print: "))
# print(fibonacci(n))













