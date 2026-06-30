import numpy as np

'''arr = np.arange(1,11)
print("arr",arr)
print("Slicing",arr[2:7])
print("Slicing Specifically after 2",arr[2:7:2])
print("Negative Indexing", arr[-2])
'''


#Sorting

arr_1D = np.array([1,2,3,4,6,5,9,8,7])
print("Sorted Array " ,np.sort(arr_1D))


# axis ==0 column and axis=1 for row arrangement

'''arr_2D = np.array([[1,2],[7,8],[5,3]])
print("Simple Array",arr_2D)
print("Sorted Array",np.sort(arr_2D,axis=0))
print("Sorted Array",np.sort(arr_2D,axis=1))
'''

#Filter 
'''numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
even_num = numbers % 2 == 0
print("Filtering",numbers[even_num])

#Filter with mask

mask = numbers > 3
print("mask filter",numbers[mask])
'''


#Fancy indexing and where method

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

indices = [0,2,4]
