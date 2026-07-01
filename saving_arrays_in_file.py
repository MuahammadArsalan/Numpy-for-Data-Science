import numpy as np
import matplotlib.pyplot as plb


'''arr1= np.array([[1,2,3],[4,5,6]])
arr2 = np.random.rand(3,3)
arr3 = np.zeros((4,4))
print("Arr1",arr1)
print("Arr2",arr2)
print("Arr3",arr3)
'''
'''
np.save("arr1.npy",arr1)
np.save("arr2.npy",arr2)
np.save("arr3.npy",arr3)
'''
'''print_Saved_arr = np.load("arr1.npy")
print("Saved arr",print_Saved_arr)
'''
'''load_image =  np.load("numpy_logo.npy")


plb.figure(figsize=(6,10))
plb.subplot(121)
plb.imshow(load_image)
plb.grid(False)'''
import os

from PIL import Image
import numpy as np

img = Image.open("numpy-logo.png")
arr = np.array(img)

np.save("numpy-logo.npy", arr)
logo = np.load('numpy-logo.npy')

    # Display
plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.imshow(logo)
plt.title("Numpy logo")
plt.grid(False)
