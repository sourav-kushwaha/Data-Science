import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, export_graphviz
import graphviz

# Load your dataset (replace 'your_data.csv' with your actual file)
file_path = "4_treeSample.csv"
df = pd.read_csv(file_path)

# Assuming 'target' is the column you want to predict
X = df.drop("capital", axis=1)  # Features
y = df["capital"]  # Target variable

# Convert categorical variables to numerical using one-hot encoding
X = pd.get_dummies(X, columns=["marital_status", "education"])

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a DecisionTreeClassifier
tree_classifier = DecisionTreeClassifier(random_state=42)

# Train the decision tree on the training data
tree_classifier.fit(X_train, y_train)

# Display text representation of the decision tree rules
tree_rules = export_text(tree_classifier, feature_names=X.columns.tolist())
print("Decision Tree Rules:\n", tree_rules)

# Visualize the decision tree using graphviz
dot_data = export_graphviz(
    tree_classifier,
    out_file=None,
    feature_names=X.columns.tolist(),
    class_names=list(map(str, tree_classifier.classes_)),
    filled=True,
    rounded=True,
    special_characters=True
)

graph = graphviz.Source(dot_data)

