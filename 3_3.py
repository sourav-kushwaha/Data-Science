import matplotlib.pyplot as plt
import numpy as np

# Sample data
data1 = np.random.randn(1000)  # Random data for histogram 1
data2 = np.random.randn(800)   # Random data for histogram 2

plt.hist(data1, bins=30, alpha=0.5, label='Data 1', color='blue')
plt.hist(data2, bins=30, alpha=0.5, label='Data 2', color='orange')

# Adding labels and title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram with Overlay')

plt.legend()

plt.show()