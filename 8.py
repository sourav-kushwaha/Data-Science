#8 "k mean clustering"
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("8_incomee.csv")

# Drop unnecessary columns
df = df.drop(columns=['Name', 'Unnamed: 3'], errors='ignore')

# Visualize the data
plt.scatter(df.Age, df['Income($)'])
plt.xlabel('Age')
plt.ylabel('Income($)')
plt.title('Scatter plot of Age vs Income')
plt.show()

# Use KMeans for clustering
numeric_cols = df.select_dtypes(include=['number']).columns
kmeans = KMeans(n_clusters=3, n_init=10)
kmeans.fit(df[numeric_cols])

# Add a new column 'Cluster' to the dataframe to store the cluster assignment
df['Cluster'] = kmeans.labels_

# Visualize the clusters
plt.scatter(df.Age, df['Income($)'], c=df['Cluster'], cmap='rainbow')
plt.xlabel('Age')
plt.ylabel('Income($)')
plt.title('KMeans Clustering Result')
plt.show()

# Display the clustered data
print(df)

