import pandas as pd

# Sample DataFrame with a categorical field
data = {'Fruit': ['Apple', 'Orange', 'Banana', 'Orange', 'Apple', 'Banana']}

df = pd.DataFrame(data)
df_original = df.copy()

# Mapping categorical values to numerical categories
# Creating a mapping dictionary
mapping = {'Apple': 1, 'Orange': 2, 'Banana': 3}

# Replacing categorical values with numerical categories
df['Fruit'] = df['Fruit'].map(mapping)

print("Original DataFrame:")
print(df_original)

print("\nReexpressed DataFrame:")
print(df)