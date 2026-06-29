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

import time

inital = time.time()

py_lsit  = [i*2 for i in range(1000000)]
print("time taken py list  == ", time.time()-inital)

inital = time.time()
num_arr = np.arange(1000000) * 2

print("time taken numpy arr == ", time.time()-inital)
