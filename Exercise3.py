import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Assume X_train is already defined and has shape (num_samples, num_features)
num_features = X_train.shape[1]

# Create a simple neural network model for regression
model = Sequential([
    Dense(64, activation='relu', input_shape=(num_features,)),  #Input layer; set input_shape to num_features since it holds the shape
    Dense(64, activation='relu'),
    Dense(1, activation='linear')  # Output layer for regression
])

model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=1)