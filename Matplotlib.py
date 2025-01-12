from itertools import groupby

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy.ma.core import right_shift, left_shift
from numpy.ma.extras import median

"""BAR PLOT"""

# x = [2000,2001,2002,2003,2004]
# y = [1000,800,2000,1700,3000]
# colors = ["red","green","yellow","blue","orange"]
# plt.bar(x,y,color =colors,width= 0.5,edgecolor="black")
# plt.xlabel("Years",fontsize =15)
# plt.ylabel("Production Of The Car",fontsize =15)
# plt.title("A Company Produce No. Of Car Per Year",fontsize =20)
# plt.show()



# data = pd .read_csv("employee_data_with_salary.csv")
# df = pd.DataFrame(data)
# print(df)
# grouped_by = df.groupby("Department")["Salary"].mean()
# print(grouped_by)
#
# plt.bar(grouped_by.index,grouped_by.values)
# plt.show()





"""LINE PLOT"""

# x = ["mon","tue","wed","thu","fri","sat","sun"]
# y = [600,500,120,300,500,300,1000]
# y1 = [700,450,500,600,300,400,800]
#
# plt.plot(x, y, marker = ".", ls = "--", color = "blue", label = "Week1")
# plt.plot(x, y1, marker = ".", ls = "-", color = "green", label = "Week2")
# plt.xlabel("Days")
# plt.ylabel("Number Of People")
# plt.title("People Visit Patna Zoo In The Month Of December")
# plt.legend()
# plt.show()



# x = ["2000","2001","2002","2003","2004"]
# y = [1000,800,2000,1700,3000]
# y1 = [1500,2500,3000,1000,4000]
# plt.plot(x,y,color ="green", marker = ".", ls = ":", label = "Car")
# plt.plot(x,y1,color="yellow", marker = ".", ls = "-", label = "Bike")
# plt.xlabel("Years", color = "black", fontsize = 12)
# plt.ylabel("Numbers Of Production", color = "black", fontsize = 12)
# plt.title("Production Of A Company", color = "black")
# plt.legend()
# plt.show()


# data = pd.read_csv("december_family_expenses.csv")
# print(data)
#
# grouped_by = data.groupby("Category").agg({"Amount":"sum"})
# print(grouped_by)
#
# plt.plot(grouped_by.index,grouped_by.values)
# plt.show()





"""SCATTER PLOT"""

# x = np.random.randint(1,10,50)
# y = np.random.randint(1,100,50)
# plt.scatter(x, y, marker=",", color =  np.random.choice(["red","black","blue"]))
# plt.show()


# data = pd.read_csv("employee_info_random_with_age.csv")
# print(data)
# plt.scatter(data["EmployeeID"],data["Salary"],s = data["Age"])
# plt.show()




"""PIE CHART"""

# brands = ["Apple","OnePlus","Redmi","Vivo","Nokhia"]
# popularity = [20,15,25,35,5]
# ex = [0.1,0,0,0.1,0]
# plt.pie(popularity, labels= brands, shadow= True, startangle= 180, explode= ex, autopct= "%.f")
# plt.title("Popularity Of Smart Phone in India in Percentage")
# plt.show()


# data = pd.read_csv("december_family_expenses.csv")
# print(data)
# grouped_by = data.groupby("Payment Mode")["Amount"].sum()
# print(grouped_by)
# plt.pie(grouped_by.values, labels = grouped_by.index, autopct = "%.2f")
# plt.show()



# sizes = [15, 30, 45, 10]  # Values for each section
# labels = ['Category A', 'Category B', 'Category C', 'Category D']  # Labels for each section
# colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']  # Colors for each section
# ex = [0,0,0.1,0]
# # Plot
# plt.figure(figsize=(8, 8))
# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90,
#         wedgeprops={'width': 0.3}, shadow = True, explode = ex)  # Adjust width for the donut effect
# plt.gca().set_aspect('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
#
# plt.show()





"""BOX PLOT"""

# l1 = [1,3,4,7,12,2,8,9,24]
# Q1 = np.percentile(l1, 25)
# Q3 = np.percentile(l1, 75)
# print("Q1 = ",Q1)
# print("Q3 = ",Q3)
# plt.boxplot(l1)
# plt.show()


# l2 = [1,3,4,7,12,2,8,9,24]
# l3 = [5,7,27,56,33,20,40,42,90]
# plot_value = [l2,l3]
# plt.boxplot(plot_value)
# plt.show()


# data = pd.read_csv("december_family_expenses.csv")
# df = pd.DataFrame(data)
# print(df)
# plt.boxplot(df["Amount"])
# plt.show()




"""HISTOGRAM PLOT"""

# x = [2,4,55,65,5,6,9,10,70,77,89,90,91,22,22,33,55]
# plt.hist(x, bins= 10, color = "skyblue", edgecolor = "black") #bins=10: Number of intervals (bins) to divide the data.
# plt.show()


# data = pd.read_csv("december_family_expenses.csv")
# print(data)
#
# plt.hist(data["Amount"], bins = 10, edgecolor = "red", color = "pink")
# plt.xlabel("Spent")
# plt.ylabel("Frequency")
# plt.title("Expenses Of A Family In DECEMBER Month")
# plt.show()



"""VOILIN PLOT"""

# l = [4,95,97,34,32,40,43,43,34,42,90,89,87,18,]
# plt.violinplot(l, showmedians = True, showmeans= True)
# plt.show()



# data = pd.read_csv("december_family_expenses.csv")
# print(data)
# df = pd.DataFrame(data)
#
# plt.violinplot(df["Amount"], showmedians= True, showmeans= True, showextrema= True)
# plt.show()




"""STEM PLOT"""

# l = [22,44,55,19,77,40,90,60]
# plt.stem(l, linefmt= "--", markerfmt= "^")
# plt.show()


# data = pd.read_csv("december_family_expenses.csv")
# df = pd.DataFrame(data)
# print(df)
# plt.stem(df["Amount"], markerfmt= ".")
# plt.plot(df["Amount"], color = "violet")
# plt.xlabel("Payment")
# plt.ylabel("Amount")
# plt.show()




"""STACK PLOT"""

# days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
# nop_week1 = [45,36,54,39,44,23,16]
# nop_week2 = [23,10,16,20,22,50,70]
# nop_week3 = [45,65,76,89,90,100,120]
#
# plt.stackplot(days,nop_week1,nop_week2,nop_week3, labels= ("week1","week2","week3"))
# plt.xlabel("DAYS")
# plt.ylabel("NUMBER OF PEOPLE")
# plt.title("NUMBER OF PEOPLE COME IN RESTAURENT")
# plt.legend()
# plt.show()




# data = pd.read_excel("Food_Calorie_Data_Realistic.xlsx")
# df = pd.DataFrame(data)
# print(df)
#
# grouped_by = df.groupby("Category").agg({"Calories":"mean","Protein":"mean","Fat":"mean","Fibre":"mean"})
# print(grouped_by)
#
# plt.stackplot(grouped_by.index,grouped_by["Calories"],grouped_by["Protein"],
#               grouped_by["Fat"],grouped_by['Fibre'],
#               labels= ("Calories","Protein","Fat","Fibre"),
#               colors = ["#5E757F","#CD2783","#D694E9","#833049"])
# plt.legend()
# plt.show()





"""STEP PLOT"""

# days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
# y = [2,5,25,9,22,32,8]
#
# plt.step(days, y, marker= ".", color= "red", where= "post")
# plt.show()



# data = pd.read_csv("december_family_expenses.csv")
# df = pd.DataFrame(data)
# print(df)
#
# group_by = df.groupby("Category")["Amount"].sum()
# print(group_by)
#
# plt.step(group_by.index, group_by.values, marker = ".", color = "#2E8B75")
# plt.xticks(rotation = 30, color = "#2E8B75")
# plt.yticks(color = "#2E8B75")
# plt.show()




"""SUB PLOT"""

# employee = ["A","B","C","D"]
# age = [34,56,27,60]
# plt.subplot(2,2,1)      # Rows, Columns, Chartnum
# plt.plot(employee,age, marker = "o")
# plt.title("Age")
#
#
# employee = ["A","B","C","D"]
# weight = [40,80,55,76]
# plt.subplot(2,2,2)
# plt.stem(employee,weight)
# plt.title("Weight In Kg")
#
# employee = ["A","B","C","D"]
# height = [160,150,170,147]
# plt.subplot(2,2,3)
# plt.bar(employee,height)
# plt.title("Height In (cm)")
#
#
# employee = ["A","B","C","D"]
# salary = [45000,70000,35000,100000]
# plt.subplot(2,2,4)
# plt.step(employee,salary, marker = "o")
# plt.title("Salary In (Rs)")
# plt.suptitle("Employee Information")
# plt.tight_layout()
# plt.savefig("subplot.png", facecolor = "skyblue")
# plt.show()