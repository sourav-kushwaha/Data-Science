import pandas as pd

# Sample data
data = {'Gender': ['Male', 'Female', 'Male', 'Male', 'Female'],
        'Smoker': ['Yes', 'No', 'No', 'Yes', 'Yes']}

df = pd.DataFrame(data)

# Create a contingency table using the crosstab function
contingency_table = pd.crosstab(df['Gender'], df['Smoker'])

# Display the contingency table
print(contingency_table)
