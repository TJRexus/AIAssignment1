import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
housing = fetch_california_housing()
X = housing.data
y = housing.target

# Split data into training and testing sets (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=42) #Set test_size to 0.8 to state the 80/20 split

# Build and train the model
model = LinearRegression()
model.fit(X_train, y_train) #Use .fit() to train the model

# Make predictions on the test set
y_pred = model.predict(X_test) #.predict() is used to predict the other 20% test set

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R^2 Score:", r2)