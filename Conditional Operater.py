# if else statement

# marks = 87
# if marks >= 90 :
#     print("you will marks get phone")
# else:
#   print("you will not get phone for a week")
#   print("thank you")

#if elif else statement

# mark = 56
# if mark >= 90:
#     print("get a car")
# elif mark >= 80:
#     print("get a bike")
# elif mark >= 70:
#     print("get a bycycle")
# else:
#   print(" you will not get phone for a week")


# nested if statement

# mark = 78
# if mark >= 95:
#     print(" you get iphone ")
# if mark >= 80:
#         print(" you get redmi phone ")
# else:
#         print(" you will not get phone for a week ")


# short hand if statement
"""mark = 99
if mark >= 90: print("you will get iphone")


# short hand if else statement

mark = 90
print("you will go to trip") if mark >= 90 else print("no phone for a month")

# problem solving ------- print positive no.

num = int(input("enter no."))
if num >= 0 :
    print("it is a positive no.")
else:
    print("it is not positive no.")"""


# write a program to check even or odd

# num = int(input("enter a number"))
# if num % 2 == 1:
#     print("it is a odd number")
# else:
#     print("it is even number")


# write a program to check vowel

# b = input(" enter a letter")
# if b in "aeiou" or b in "AEIOU":
#     print("it ia a vowel")
# else:
#     print("it is not a vowel")


# write a program to check digit of a no. up to 5 digit no.

num = int(input("enter number up to 5 digit no."))
if num >= 0 and num <= 9:
    print("it is one digit no.")

elif num >= 10 and num <= 99:
        print("it is two digit no.")

elif num >= 100 and num <= 999:
    print("it is three digit no.")

elif num >= 1000 and num <= 9999:
    print("it is four digit no.")
    
elif num >= 10000 and num <= 99999:
    print("it is five digit no.")

else:
    print("invalde no.")



