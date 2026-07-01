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




from PIL import Image
import numpy as np





try:
    img = Image.open("numpy_logo.png")
    arr = np.array(img)

    np.save("numpy_logo.npy", arr)
    Logo_Load = np.load('numpy_logo.npy')

    Logo_Load = np.load('numpy-logo.npy')

    # Display
    plb.figure(figsize=(10, 5))
    plb.subplot(121)
    plb.show(Logo_Load)
    plb.title("Numpy logo")
    plb.grid(False)
    plb.show()
    #dark_logo = 1 - logo



except FileNotFoundError:
    print("numpy logo file not found")