import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load your dataset (replace 'your_data.csv' with your actual file)
file_path = "4_treeSample.csv"
df = pd.read_csv(file_path)

# Identify categorical columns
categorical_columns = ['education','capital']

# One-hot encode categorical columns
df_encoded = pd.get_dummies(df, columns=categorical_columns)

# Separate features (X) and target variable (y)
X = df_encoded.drop('marital_status', axis=1)
y = df_encoded["marital_status"]

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a RandomForestClassifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the random forest on the training data
rf_classifier.fit(X_train, y_train)

# Make predictions on the test data
y_pred = rf_classifier.predict(X_test)

print(y_test,y_pred)
