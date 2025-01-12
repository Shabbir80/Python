# for loop
# for i in range (1,6):
#     print(i)
#
# for i in range(1, 6, 2):
#     print(i)
#
# # table of 7
# num =7
# for i in range (1, 11):
#     print(num ,"*", i, "=", num * i )
#
#
# # whiie loop
# n = 2
# while n<=10:
#     print(n)
#     n+=2
#
# # table
# a =1
# b = int(input("Enter any for printing table of the number:"))
# while a<=10:
#     print(b,"*",a,"=",b*a)
#     a+=1
from unicodedata import digit

# # while True loop is infinite loop
# while True:
#   num1 = int(input("enter a no. here"))
#   num2 = int(input("enter another no. here"))
#   print(num1 + num2)
#
#   repeat = input("if you want to stop it type yes: ")
#   if repeat == "yes":
#     break


# # Nested for loop
# for i in range (1,4):
#   for j in range (1,11):
#     print(j, end="")
#   print()
#
# # pattern
# for i in range (1,6):
#   for j in range (1,i+1):
#     print(j, end=" ")
#   print()


# # loop with conditional statement
#
# for i in range (1,101):
#   if i % 8 == 0 and i % 12 == 0:
#     print(i)
#
#
# # continue is used skipe part and break is used to terminate loop
#
# for i in range (1,11):
#   if i == 4 :
#     continue
#   else:
#     print(i)
#
#
# for i in range (1,11):
#   if i == 4 :
#     break
#   else:
#     print(i)


# problem solving

# # to find sum of even number up to 50
# sum = 0
# for i in range (2, 51, 2):
#   sum += i
# print(sum)



# # write first 20 no. and their square no.
# for i in range (1, 21):
#   print(i,"^ 2 =",i * i)

# # to find sum of first 10 odd no. using for and while loop
# sum = 0
# for i in range (1 ,20, 2):
#   sum += i
# print(sum)


# sum = 0
# n = 0
# while n <= 20:
#   if n % 2 == 1:
#     sum += n
#   n += 1
# print(sum)
#
#
# # write program to calculate billing amount
# while True:
#   name = input("Enter name of the coustomer: ")
#   total = 0
#
#   while True:
#     price = float(input("Enter the price of item: "))
#     quantity = int(input("Enter the quantity of the item: "))
#     total += price * quantity
#     repeat = input("Do you not want to add more item?(yes/no):")
#     if repeat == "no" or repeat == "No":
#       break
#
#   print("NAME = ",name)
#   print("-" * 45)
#   print("The total amount is:",total)
#   print("-" * 45)
#   print("**************** THANK YOU ******************")
#
#   repeat1 = input("Do you want to go next coustomer?(yes/no):")
#   if repeat1 == "no" or repeat =="No":
#     break


# # to find fibonacci to given range
# a = 0
# b = 1
# num = int(input("Enter no. here  where do want to get fibonacci series:"))
# if num == 1:
#     print(0)
# else:
#     print(a)
#     print(b)
#     for i in range (2,num):
#         c = a + b
#         a = b
#         b = c
#         print(c)22


# # to check a no. is prime or not
# n = int(input("Enter a no. here to check it is prime or not: "))
# if n <= 1:
#     print("It is not prime number")
# else:
#      for i in range(2,n):
#          if n % i == 0:
#           print("It is not prime number")
#           break
#      else:
#         print("it is prime number")



# # to find Palindrome
# num = (input("Enter a text : "))
# if num == num[::-1]:
#     print("it is palindrome")
#
# else:
#     print("its not palindrome")


# n = int(input("Enter number here to check it is palindrome:"))
# temp = n
# rev =  0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n//10
#
# if temp == rev :
#     print("It is a palindrome")
#
# else:
#     print("It is not palindrome")


#
# # Area calculater
# print("************AREA CALCULATER****************")
#
# while True:
#         print("""
# Enter 1 for square area
# Enter 2 for rectangle area
# Enter 3 for triangle area
# Enter 4 for circle area""")
#
#         choice = int(input("Enter number:"))
#
#
#         if choice == 1:
#             while True:
#                 side = float(input("Enter side:"))
#                 print("Area of the square is",side*side)
#                 repeat = input("do you want to stay with area of square(yes/no):")
#                 if repeat.lower() == "no":
#                     break
#
#
#         elif choice == 2:
#             while True:
#                 len = float(input("Enter lenght:"))
#                 breath = float(input("Enter breath:"))
#                 print("Area of the rectangle",len * breath)
#                 repeat = input("do you want to stay with area of rectangle(yes/no):")
#                 if repeat.lower() == "no":
#                     break
#
#
#         elif choice == 3:
#             while True:
#                 lenght = float(input("Enter lenght:"))
#                 width = float(input("Enter base:"))
#                 print("Area of the triangle:",0.5 * lenght * width)
#                 repeat = input("do you want to stay with area of triangle(yes/no):")
#                 if repeat == "no" or repeat == "NO":
#                     break
#
#
#         elif choice == 4 :
#             while True:
#                 radius = float(input("Enter radius:"))
#                 print("Area of circle:",3.14 * radius * radius)
#                 repeat = input("do you want to stay with area of circle(yes/no):")
#                 if repeat == "no" or repeat == "NO":
#                     break
#
#         else:
#             print("Invaled input")
#
#         repeat1 = input("do you want to continue menu(yes/no)")
#         if repeat1 == "no" or repeat1 == "NO":
#            break




# # pattern problem
#
# for i in range(1,6): # rows
#     for j in range(1,i+1): # column
#         print(i,end=" ")
#     print()
#
#
# for i in range(1,6): # rows
#     for j in range(6,i,-1): # column
#         print(j,end=" ")
#     print()
#
#
# for i in range(1,6): # rows
#     for j in range(5,i,-1): # column
#         print(" ",end=" ")
#     for k in range(i):
#         print(i, end=" ")
#     print()


# for i in range(1,6): # rows
#     for j in range(i,0,-1): # column
#         print(j,end=" ")
#     print()



#
# for i in range (1,9):
#     for j in range (1,i+1):
#         print(i *j,end=" ")
#     print()

#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()
#
# for k in range(1,5):
#     for l in range(5,k,-1):
#         print("*", end=" ")
#     print()













