import matplotlib.pyplot as plt

# Sample data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
data1 = [100, 150, 70, 120]
data2 = [80, 110, 60, 100]

plt.bar(categories, data1, label='Data 1', color='blue')
plt.bar(categories, data2, label='Data 2', color='red')

# Adding labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Graph with Overlay')

plt.show()