import pandas as pd

data = {"Name":["Lisa","Peter","john"],
        "Age":[20,16,25],
        "Salary":[70000,50000,100000]}
df = pd.DataFrame(data)
print(df)


"""Opening csv and excel file in pycharm"""
data_1 = pd.read_csv("customer_billing.csv")
print(data_1)

data_2 = pd.read_excel("C:/Users/SHABBIR HUSSAIN/Downloads/customer_billing_data.xlsx")
print(data_2)


data_3 = pd.read_excel("Sample_Data.xlsx")
print(data_3)
print()
print(data_3.head(10))
print()
print(data_3.tail(20))
print()
print(data_3.info())
print()
print(data_3.describe())
print()

print(data_3.isnull())
print(data_3.isnull().sum())
print()



data_4 = pd.read_csv("employee_data_with_duplicates.csv")
print(data_4)

"""handling with duplicates value"""
print(data_4["EmployeeID"].duplicated())
print()
print(data_4["EmployeeID"].duplicated().sum())
print()

"""Removing duplicates"""
print(data_4.drop_duplicates("EmployeeID"))



"""Dealing with null value"""
data_5 = pd.read_csv("employee_data_with_null.csv")
print(data_5)
print()
print(data_5.isnull())
print()
print(data_5.isnull().sum())
print()
print(data_5.dropna())

import numpy as np

data_5 = pd.read_csv("employee_data_with_null.csv")
print(data_5)
print()

print(np.mean(data_5["Salary"]))

data_5["Salary"] = data_5["Salary"].replace(np.nan,80862.03)
print(data_5)
print()
data_5["Department"] = data_5["Department"].fillna(method ="bfill")
print(data_5)
print()
data_5["Age"] = data_5["Age"].fillna(method ="ffill")
print(data_5)
print()
data_5["Name"] = data_5["Name"].fillna(method ="ffill")
print(data_5)
print()
print(data_5.dropna())



"""Column Transformation Part 1"""

df = pd.read_csv("employee_data_bonus.csv")
print(df)
print()

df.loc[(df["Bonus"] == 0, "GetBonus")] = "No"
df.loc[(df["Bonus"] > 0, "GetBonus")] = "Yes"
print(df)
print()

df["FullName"] = df["FirstName"].str.upper() +" "+ df["LastName"].str.upper()
print(df)

"""Column Transformation Part 2"""

data_6 = pd.read_csv("employee_data_with_salary.csv")
print(data_6)
print()

data_6["Bonus"] = (data_6["Salary"]/100) * 20
print(data_6)
print()



x = {"Months":["January","Feburary","March","April","May"]}
df1 = pd.DataFrame(x)
print(df1)
print()

df1["Months(short)"] = df1["Months"].str[0:3]
print(df1)




"""Groupby and agg Function"""

data_7 = pd.read_csv("employee_info_random_with_age.csv")
print(data_7)


gp1 = data_7.groupby(["Department","Gender"]).agg({"EmployeeID":"count"})
print(gp1)
print()

gp2 = data_7.groupby(["Country","Gender"]).agg({"Salary":"max"})
print(gp2)
print()

gp3 = data_7.groupby(["Country"]).agg({"Salary":"mean"})
print(gp3)
print()

gp4 = data_7.groupby(["Country"]).agg({"Salary":"mean","Age":"min"})
print(gp4)
print()

gp5 = data_7.groupby(["Department"]).agg({"Age":"min"})
print(gp5)
print()

gp6 = data_7.groupby(["Department","Gender"]).agg({"Salary":"max"})
print(gp6)
print()




"""Merge or Join and Concatenate in pandas"""

data1 = {"EmployeeID":["E01","E02","E03","E04","E05","E06"],
         "Name":["JOHN","LISA","RIYA","RAM","SAAM","KELLY"],
         "Age":[23,43,21,33,37,29]}

data2  = {"EmployeeID":["E01","E02","E03","E04","E05","E06"],
          "Salary":[87000,50000,55000,90000,84000,65000]}

df1 = pd.DataFrame(data1)
df2 =pd.DataFrame(data2)

print(df1)
print()
print(df2)
print()
print(pd.merge(df1,df2, on= "EmployeeID"))




data3 = {"EmployeeID":["E01","E02","E03","E04","E05","E011"],
         "Name":["JOHN","LISA","RIYA","RAM","SAAM","KELLY"],
         "Age":[23,43,21,33,37,29]}

data4  = {"EmployeeID":["E01","E09","E03","E04","E010","E06"],
          "Salary":[87000,50000,55000,90000,84000,65000]}

df3 = pd.DataFrame(data3)
df4 =pd.DataFrame(data4)

print(df3)
print()
print(df4)
print()
print(pd.merge(left = df3, right = df4, on = "EmployeeID", how = "left" ))
print()
print(pd.merge(df3,df4, on = "EmployeeID", how = "right" ))
print()
print(pd.merge(df3,df4, on = "EmployeeID", how = "inner" ))
print()
print(pd.merge(df3,df4, on = "EmployeeID", how = "outer" ))
print()




data5 = {"EmployeeID":["E01","E02","E03","E04","E05","E06"],
         "Name":["JOHN","LISA","RIYA","RAM","SAAM","KELLY"],
         "Age":[23,43,21,33,37,29]}

data6 = {"EmployeeID":["E07","E08","E09","E010","E011","E012"],
         "Name":["ASIF","SITA","SAAD","FARIHA","SOOD","KIRAN"],
         "Age":[20,33,28,43,47,27]}

df5 = pd.DataFrame(data5)
df6 = pd.DataFrame(data6)
print(df5)
print()
print(df6)
print()

print(pd.concat([df5,df6]))




"""Compare Data Frame"""

df7 = pd.DataFrame({"Fruits":["Apple","Orange","Grapes","Papaya"],
                    "Price(per kg)":[150,80,100,50],
                    "Quantity(box of 10 kg)":[20,35,15,40]})

print(df7)
print()

df8 = df7.copy()

df8.loc[0,"Price(per kg)"] = 200
df8.loc[1,"Price(per kg)"] = 120
df8.loc[3,"Price(per kg)"] = 40
df8.loc[2,"Price(per kg)"] = 80

df8.loc[0,"Quantity(box of 10 kg)"] = 10
df8.loc[1,"Quantity(box of 10 kg)"] = 20
df8.loc[3,"Quantity(box of 10 kg)"] = 15

print(df7.compare(df8))
print()
print(df7.compare(df8, align_axis= 0))
print()
print(df7.compare(df8, keep_equal= True))
print()
print(df7.compare(df8, keep_equal= False))
print()
print(df7.compare(df8, keep_shape= True))
print()
print(df7.compare(df8, keep_shape= False))
print()




"""Pivoting and Melting Dataframes"""

Dic = {"Keys":["k1","k2","k1","k2"],
       "Name":["John","Alice","Lisa","Peter"],
       "House":["Red","BLue","Green","Black"]}

df = pd.DataFrame(Dic)
print(df)
print()
x = df.pivot(index="Keys", columns="Name", values="House")
print(x)
print()

Dic1 = {"Keys":["k1","k2","k1","k2"],
       "Name":["John","Alice","Lisa","Peter"],
       "House":["Red","BLue","Green","Black"],
       "Std":["8th","9th","7th","5th"]}

df1 = pd.DataFrame(Dic1)
print(df1)
print()
print(df1.pivot(index="Keys", columns="Name", values=["House","Std"]))



Dic2 = {
       "Name":["John","Alice","Lisa","Peter"],
       "House":["Red","BLue","Green","Black"],
       "Std":["8th","9th","7th","5th"]
        }

df2 = pd.DataFrame(Dic2)
print(df2)
print()
print(df2.melt(id_vars="Name", value_vars="House"))
print()
print(df2.melt(id_vars="Name", value_vars=["House","Std"]))


