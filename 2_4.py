import numpy as np

# Sample numeric field
numeric_field = [10, 20, 30, 40, 50]

# Calculate mean and standard deviation
mean_value = np.mean(numeric_field)
std_dev = np.std(numeric_field)

# Standardize the numeric field using Z-score
z_scores = [(x - mean_value) / std_dev for x in numeric_field]

print("Original numeric field:", numeric_field)
print("Z-scores:", z_scores)
