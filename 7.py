import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

# Build the model
model = models.Sequential()
model.add(layers.Dense(1, input_dim=1))
model.compile(optimizer='sgd', loss='mean_squared_error')

# Generate data
X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 6, 8, 10], dtype=float)

# Train the model
model.fit(X, y, epochs=1000, verbose=0)

# Make a prediction
new_data = np.array([6], dtype=float)
prediction = model.predict(new_data)

print("Prediction for input 6:", prediction[0, 0])
