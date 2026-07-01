import numpy as np
import matplotlib.pyplot as plt
# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],  # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites
    [3, 200000, 230000, 260000, 300000],  # Pizza Hub
    [4, 180000, 210000, 240000, 270000],  # Burger Point
    [5, 160000, 185000, 205000, 230000]   # Chai Point
])


'''print("****==== Zomato sales analysis ==== ****")
print("Sale data",sales_data)
print("\n Sales data shape",sales_data.shape)
print(" Sample data for 1st 3 restau: ",sales_data[0:3])
'''

# total sales per year

'''total_sell = np.sum(sales_data[0:,1:],axis=0)
print("Total sales",total_sell)

# Minimum sales per restaurant
min_sales = np.min(sales_data[:, 1:], axis=1)
print(min_sales)
# maximum sales per restaurant
max_sales = np.max(sales_data[:, 1:], axis=0)
print(max_sales)

avg_Sale = np.mean(sales_data[0:,1:],axis=1)
print("Avg",avg_Sale)


cumsum = np.cumsum(sales_data[:, 1:], axis=1)
print("Cumulative sum",cumsum)

plt.figure(figsize=(6,10))
plt.plot(np.mean(cumsum,axis=0))
plt.title("Graph representation")
plt.xlabel("years")
plt.ylabel("Sales")
plt.grid("true")
plt.show()


'''
'''vector1 = np.array([1, 2, 3, 4, 5])
vector2 = np.array([6, 7, 8, 9, 10])

print("Addition of vector",vector1+vector2)
print("Multiplication of vector",vector1*vector2)
print("Dot product of vector",np.dot(vector1,vector2))

angle = np.arccos(np.dot(vector1,vector2) / np.linalg.norm(vector1*np.linalg.norm(vector2)))
print("Angle",angle)
'''



restaurant_types = np.array(['biryani', 'chinese', 'pizza', 'burger', 'cafe'])
vectorized = np.vectorize(str.upper)
print("Vectorized Upper Case", vectorized(restaurant_types))

#here 12 is scale it indivisually divide by all element called broadcasting


avg_mont_sale = sales_data[0:,1:] /12
print("Avg month sale",avg_mont_sale)

