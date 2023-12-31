import pandas as pd

# Creating a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [25, -1, 30, 40, 20],
        'Gender': ['F', 'M', 'M', 'F', 'F']}

df = pd.DataFrame(data)
df_orginial = df.copy()
# Replace negative age values with NaN (missing value)
df['Age'] = df['Age'].apply(lambda x: x if x > 0 else pd.NA)

print("Original DataFrame:")
print(df_orginial)

print("\nModified DataFrame:")
print(df)