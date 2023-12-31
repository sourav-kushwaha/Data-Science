import pandas as pd
from sklearn.model_selection import train_test_split
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri

# Creating a sample DataFrame
data = {
    'feature1': [1, 2, 3, 4, 5],
    'feature2': ['A', 'B', 'C', 'D', 'E'],
    'target_column': [0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

# Saving the DataFrame to a CSV file
df.to_csv('my_data.csv', index=False)

# Activate automatic conversion of pandas objects to R objects
pandas2ri.activate()

# Load your dataset (replace 'your_data.csv' with your actual file)
file_path = "my_data.csv"
df = pd.read_csv(file_path)

# Assuming 'target' is the column you want to predict
X = df.drop("target_column", axis=1)  # Features
y = df["target_column"]  # Target variable

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Import the C5.0 package from R
c50 = importr('C50')

# Convert pandas DataFrames to R data.frames
X_train_r = pandas2ri.py2rpy(X_train)
y_train_r = pandas2ri.py2rpy(y_train)

# Train the C5.0 decision tree
c5_model = c50.C5_0(x=X_train_r, y=y_train_r)