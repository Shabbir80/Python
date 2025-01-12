import numpy as np
# Syntax of Array
# arr_1 = np.array([23,78,4,67,23,0])
# print(arr_1)
# print(type(arr_1))
#
#
# #Array in Matrix form
# arr_2 = np.array([[23,78,4,67],[55,46,34,65],[41,56,87,523]])
# print(arr_2)
#
#
# #Slicing Array
# arr_3 = np.array([10,20,30,40,50])
# print(arr_3[0:])
# print(arr_3[2:])
# print(arr_3[3])
# print(arr_3[::-1])
# print(arr_3[::2])


# arr_4 = np.array([[20,70,40,60],[50,10,33,66],[44,55,80,10]])
# print(arr_4[0,0:2])
# print(arr_4[1,0:3])
# print(arr_4[2,1:])
# print(arr_4[1:4,0:3])
# print(arr_4[0,2])
#
# # Attributes of Array
# print(np.shape(arr_4))
# print(arr_4.dtype)
# print(np.size(arr_4))
# print(np.ndim(arr_4))
#
# print(len(arr_4))
# print(type(arr_4))
# print(arr_4.astype(float))




# # Mathematical Operation on Array
# arr1 = np.array([10,20,30,40])
# arr2 = np.array([50,60,70,80])
# print(arr1 + arr2)
# print(np.add(arr1,arr2))
#
# print(arr2-arr1)
# print(np.subtract(arr2,arr1))
#
# print(arr1*arr2)
# print(np.multiply(arr1,arr2))
#
# print(arr1/arr2)
# print(np.divide(arr1,arr2))
#
#
#
# arr3 = np.array([[10,20],[30,40]])
# arr4 = np.array([[50,60],[70,80]])
# print(arr3+arr4)
# print(np.add(arr3,arr4))
#
# print(arr4-arr3)
# print(np.subtract(arr3,arr4))
#
# print(arr3*arr4)
# print(np.multiply(arr3,arr4))
#
# print(arr3/arr4)
# print(np.divide(arr3,arr4))
#
#
#
# arr5 = np.array([1,2,3,4])
# arr6 = np.array([3])
# print(np.pow(arr5,arr6))
# print(arr5**arr6)
#
#
#
# arr7 = np.array([1,4,25,81])
# print(np.sqrt(arr7))
# print(arr7**0.5)



# # Combinig And Spliting Array
#
# arr_5 = np.array([10,20,30,40])
# arr_6 = np.array([50,60,70,80])
# print(np.concatenate([arr_5,arr_6]))
#
#
# arr_7 = np.array([[10,20],[30,40]])
# arr_8 = np.array([[50,60],[70,80]])
# print(np.concatenate([arr_7,arr_8],axis = 0))
# print()
# print(np.vstack([arr_7,arr_8]))
# print()
# print(np.concatenate([arr_7,arr_8],axis = 1))
# print()
# print(np.hstack([arr_7,arr_8]))
#
#
#
# arr_9 = np.array([10,20,30,40,50,60,70,80])
# print(np.array_split(arr_9,4))
#
# arr_10 = np.array([10,20,30,40,50,60,70,80])
# a = (np.array_split(arr_10,4))
# print(a)
# print(a[2])
#
#
#
# # Adding And Removing
# arr_11 = np.array([10,20,30,40])
# print(np.append(arr_11,90))
# print(np.append(arr_11,[33,55]))
#
# print(np.insert(arr_11,1,100))
# print(np.insert(arr_11,[2,0],[111,123]))
#
#
arr_12 = np.array([[10,20],[30,40]])
print(np.vstack(arr_12))

print(np.hstack(arr_12))

print(np.append(arr_12,222))
print(np.append(arr_12,[333,444]))

# print(np.insert(arr_12,1,777))
# print(np.insert(arr_12,[1,2],[999,555]))
# print(np.insert(arr_12,[1,2],[5] , axis = 0))
# print(np.insert(arr_12,[1,2],[99,55],axis = 1))
# print()
# print(np.delete(arr_12,1))
# print()
# print(np.delete(arr_12,1,axis = 0))
# print()
# print(np.delete(arr_12,1,axis = 1))



# # Sort , Search and Filter
#
# arr_13 = np.array([7,12,4,1,9])
# print(np.sort(arr_13))
# x = np.where(arr_13 == 1)
# print(x)
# z = np.where(arr_13 % 2 == 0)
# print(z)
#
#
# arr_14 = np.array([[7,12,4,1,],[6,30,19,22]])
# print(np.sort(arr_14))
#
#
# arr_15 = np.array([2,5,9,11,22,45])
# y = np.searchsorted(arr_15,9)
# print(y)
#
#
# arr_16 = np.array([2,3,4,5])
# fa1 = [True,False,True,True]
# new1 = arr_16[fa1]
# print(new1)
#
# fa2 = arr_16 % 2 == 0
# new2 = arr_16[fa2]
# print(new2)
#
# fa2 = arr_16 % 2 == 1
# new2 = arr_16[fa2]
# print(new2)
#
# fa2 = arr_16 > 3
# new2 = arr_16[fa2]
# print(new2)


# # Aggregating Functions
# arr_17 = np.array([10, 30, 10, 50])
# print(np.sum(arr_17))
# print(np.min(arr_17))
# print(np.max(arr_17))
# print(np.size(arr_17))
# print(np.cumsum(arr_17))
# print(np.cumprod(arr_17))
#
# arr_18 = np.array([[10,20],[30,40]])
# print(np.sum(arr_18))
# print(np.sum(arr_18,axis = 0))
# print(np.sum(arr_18,axis = 1))


a = [200,150,100,300,250]
b = [4,5,100,6,50]

price = np.array([a])
quantity = np.array([b])
c = (np.cumprod([price,quantity],axis = 0))
print(c)
print(np.sum(c[1]))


# # Statistical Function
# import statistics as st
#
# arr_19 = np.array([10, 30, 10, 50])
# print(np.min(arr_19))
# print(np.max(arr_19))
# print(np.mean(arr_19))
# print(np.median(arr_19))
# print(st.mode(arr_19))
# print(np.std(arr_19))
# print(np.var(arr_19))
#
#
# Values range from -1 to 1:
# 1 indicates a strong positive correlation (when one value increases, the other also increases).
# -1 indicates a strong negative correlation (when one value increases, the other decreases).
# 0 means no correlation.
tobacco_cunsumption = np.array([30,40,50,60,70,80])
death = np.array([110,150,160,180,190,200])
print(np.corrcoef(tobacco_cunsumption,death))

price = np.array([110,150,160,180,190,200])
sale = np.array([80,70,60,50,40,30])
print(np.corrcoef(price,sale))


