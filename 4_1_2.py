import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.under_sampling import RandomUnderSampler

# Loading CSV file into a Pandas DataFrame
file_path = "4_employees.csv"
df = pd.read_csv(file_path)

# 'target' is the column which we want to predict
X = df.drop("Salary", axis=1)  # axis=1 for column
y = df["Salary"]  # Target variable

# Split the data into training and test sets
test_size = 0.2 # set the ratio based on requirements 20%
random_state = 40  # Set a seed for reproducibility
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

# Print the shapes of the resulting sets
print("Training set shape - X:", X_train.shape, "y:", y_train.shape)
print("Test set shape - X:", X_test.shape, "y:", y_test.shape)

# printing the actual data form after spliting
print(X_train,y_train)
print(X_test, y_test)

print("------------------------------    P4-02    -----------------------------------------------")
rus = RandomUnderSampler(random_state=40)
X_resampled, y_resampled = rus.fit_resample(X_train, y_train)
print(X_resampled,y_resampled)
