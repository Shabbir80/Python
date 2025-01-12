import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.pyplot import legend
from seaborn import set_palette

"""LINE PLOT"""

# data = ({"Days":["mon","tue","wed","thu","fri","sat","sun"],
#          "NOP":[34,65,46,75,34,53,53]})
# df = pd.DataFrame(data)
# print(df)
#
# sns.lineplot(data = data , x = "Days", y = "NOP")
# plt.show()




# data = pd.read_excel("ESD.xlsx")
#
# pd.set_option("display.max_columns",None)
# print(data.head(10))
#
# color = sns.color_palette("muted6")
# sns.lineplot(data = data, x = "Business Unit", y = "Age", hue = "Ethnicity",  marker = ".", palette = color)
# plt.legend(loc = 1)
# plt.show()





"""BAR PLOT"""

# data = sns.load_dataset("tips")
# print(data)
#
# sns.barplot(data = data, x = "day", y = "tip", hue= "sex", estimator= "sum", palette= "GnBu")
# plt.show()




"""HISTOGRAM PLOT"""

# data = sns.load_dataset("titanic")
# pd.set_option("display.max_columns",None)
# print(data)
#
# sns.histplot(data = data, x = "age", hue = "who", bins = 16, kde = True)
# plt.show()



"""SCATTER PLOT"""

# data = pd.read_excel("ESD.xlsx")
# pd.set_option("display.max_columns", None)
# print(data.head(10))
#
# plt.figure(figsize=(8, 6))
# sns.scatterplot(data = data, x = "Age", y = "Annual Salary", hue = "Department", size = "Bonus %")
# plt.legend(bbox_to_anchor = (1,1.01)) # (x, y)
# plt.tight_layout()
# plt.show()





"""HEATMAP"""

#data = sns.load_dataset("tips")
# print(data)

# gp = data.groupby("day").agg({"total_bill":"sum"})
# print(gp)

# sns.heatmap(gp)
# plt.show()




# data = pd.read_excel("ESD.xlsx")
# pd.set_option("display.max_columns",None)
# print(data.head(5))
#
# gp = data.groupby(["Job Title"]).agg({"Annual Salary":"mean"})
# print(gp)
# sns.heatmap(gp, annot= True, linewidths= 2)
# plt.title("Mean Salary")
# plt.tight_layout()
# plt.show()





"""COUNT PLOT"""

# df = pd.read_excel("ESD.xlsx")
# pd.set_option("display.max_columns", None)
# print(df.head(5))
#
# sns.countplot(data = df, x = "Business Unit", hue = "Gender", palette="viridis")
# plt.tight_layout()
# plt.show()



# data = sns.load_dataset("titanic")
# pd.set_option("display.max_columns", None)
# print(data)
#
# sns.countplot(data = data, x= "who", hue = "alive", palette= "GnBu")
# plt.title("People on Titanic")
# plt.xlabel("People")
# plt.show()




"""VIOLIN PLOT"""


# df = sns.load_dataset("tips")
# print(df)
#
# sns.violinplot(data= df, x = "day", y = "total_bill",palette= "viridis", legend= False,hue="day")
# plt.show()




# data = pd.read_excel("ESD.xlsx")
# pd.set_option("display.max_columns",None)
# print(data)
#
#
# sns.violinplot(data = data, y = "Annual Salary", color = "skyblue", inner="quartz")
# plt.show()





"""PAIR PLOT"""

# df = sns.load_dataset("tips")
# print(df)
#
# sns.pairplot(df,hue= "day", kind  = "reg")
# plt.show()





"""STRIP PLOT"""

# data = sns.load_dataset("tips")
# print(data)
#
# sns.stripplot(data = data, x = "day", y = "tip", hue = "sex", dodge= True, jitter= 0.3)
# plt.show()




"""BOX PLOT"""

# data = sns.load_dataset("tips")
# print(data)
# sns.boxplot(data=data, y = "tip", x = "day", hue= "sex", saturation= 0.5)
# plt.show()





"""CAT PLOT"""

# data = sns.load_dataset("tips")
# print(data)
#
# # cat plot stand for categorical plot
# sns.catplot(data = data, x = "day", y = "tip", hue = "sex", kind= "bar", estimator= "mean") # default is strip plot
# plt.show()





"""style and color in plot"""

# data = sns.load_dataset("tips")
# print(data)
#
# sns.set_style(style= "whitegrid")
# sns.barplot(data = data, x= "day", y= "tip")
# plt.show()




# sns.palplot(sns.color_palette("viridis",3))
# plt.show()






"""Multiple Plot"""

# data = sns.load_dataset("tips")
# print(data)
#
# a = sns.FacetGrid(data = data, col= "day", hue= "sex", legend_out= False)
# a.map(sns.stripplot, "smoker", "tip", dodge= True, jitter = 0.3)
# a.add_legend(title= "sex")
# plt.tight_layout()
# plt.show()




"""Relational Plot"""

# data = sns.load_dataset("tips")
# print(data)
#
# sns.relplot(data= data, x = "tip",  y = "total_bill", hue = "sex", col = "time", size= "smoker") # scatter plot
# plt.show()





"""Swarm Plot"""

# data = sns.load_dataset("tips")
# print(data)
#
# sns.swarmplot(data = data, x  ="day", y ="total_bill", hue = "sex", dodge = True, formatter= None)
# plt.show()




"""KDE Plot"""

# data = sns.load_dataset("tips")
# print(data)
#
# sns.kdeplot(data = data, x = "total_bill", hue= "day", multiple= "stack")
# plt.show()

