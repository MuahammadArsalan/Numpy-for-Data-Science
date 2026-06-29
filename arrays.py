import numpy as np
'''
arr_1D =np.array( [1,2,3])
print(arr_1D)

arr_2D = np.array([[1,2,3],[1,2,3]])
print("\n",arr_2D)'''


#List vs numpy array
'''
py_lsit = [1,2,3]
print("Python list multiplication ", py_lsit * 2)

num_arr = np.array([1,2,3])

print("Numpy array multiplication ", num_arr * 2)
'''

# checking time taken numpy array is effeicient in calculation

'''import time

inital = time.time()

py_lsit  = [i*2 for i in range(1000000)]
print("time taken py list  == ", time.time()-inital)

inital = time.time()
num_arr = np.arange(1000000) * 2

print("time taken numpy arr == ", time.time()-inital)'''


#creating arrays  using methods


'''zeros = np.zeros((2,3))
print(zeros)

#unit matrix
onse = np.ones((3,3))
print(onse)

full = np.full((3,2),7)
print(full)

rand = np.random.random((2,3))
print(rand)

sequencial = np.arange(0,21,2)
print(sequencial)
'''



#Vector, Matrix and Tensor

'''vector = np.array([1, 2, 3])
print("\n","\n","\n","Vector: ", vector)

matrix = np.array([[1,2,3],[4,5,6]])
print("\n","\n","\n","Matrix: ", matrix)

tensor = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

print("Tensor: ", tensor)
'''

#Array properties

'''arr = np.array([[1,2,3],[4,5,6]])
print("Shape", arr.shape )
print("dimension",arr.ndim)
print("size",arr.size)
print("data type",arr.dtype)
'''


#Array Reshaping

'''arr = np.arange(12)
print(arr)

reshape = arr.reshape((4,3))
print("reshape",reshape)'''

#differnce b/w ravel and flatten is that ravel returns original array which affect the main array when changes in ravel becomes while flatten()
#Hamesha NEW array (copy) banata hai original array pe koi effect nahi hotaSafe operation hai

'''flatten = reshape.flatten()
print("flatten",flatten)

raveled = reshape.ravel()
print("raveled",raveled)

transpose = reshape.T
print("Transpose",transpose)
'''




