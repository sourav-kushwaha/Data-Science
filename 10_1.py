import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as sns

# Load the iris dataset from Seaborn
iris = sns.load_dataset('iris')

# Display the first few rows of the dataset
print(iris.head())

# Create a DataFrame 'data' with the iris dataset
data = pd.DataFrame(iris.drop(columns='species'))  # Excluding the 'species' column for multicollinearity check

# Display the first few rows of the 'data' DataFrame
print(data.head())

# Create a correlation matrix
correlation_matrix = data.corr()

# Display the correlation matrix
print(correlation_matrix)

# Check for high correlations (threshold can be adjusted)
threshold = 0.7
high_correlations = np.where(np.abs(correlation_matrix) > threshold)

# Filter for pairs of features with high correlations
high_corr_list = [(correlation_matrix.columns[x], correlation_matrix.columns[y]) for x, y in zip(*high_correlations) if x != y and x < y]

# Print pairs of highly correlated features
print("Pairs of highly correlated features:")
for pair in high_corr_list:
    print(pair)
