import numpy as np
import matplotlib.pyplot as plt

# Generate a random dataset
np.random.seed(0)
X = 5* np.random.rand(100, 1)
y = 6 + 3 * X + np.random.randn(100, 1)

# Add a column of ones to X to account for the bias term
X_b = np.c_[np.ones((100, 1)), X]


# Use the normal equation to find the optimal values of theta
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
print("Normal equation:", theta_best)

# Set the number of iterations and the learning rate
n_iterations = 1000
learning_rate = 0.01

# Initialize theta to zero
theta = np.random.randn(2, 1)

# Use gradient descent to find the optimal values of theta
for iteration in range(n_iterations):
    gradients = 2/len(X_b) * X_b.T.dot(X_b.dot(theta) - y)
    theta = theta - learning_rate * gradients
print("Gradient descent:", theta)

# Calculate the difference between the two sets of theta values
print("Difference:", theta - theta_best)

# Plot the data and the models
X_new = np.array([[0], [2]])
X_new_b = np.c_[np.ones((2, 1)), X_new]
y_predict = X_new_b.dot(theta)
y_predict_best = X_new_b.dot(theta_best)
plt.plot(X_new, y_predict, "r-", linewidth=2, label="Predictions with GD")
plt.plot(X_new, y_predict_best, "b--", linewidth=2, label="Predictions with NE")
plt.plot(X, y, "g.", markersize=5)
plt.xlabel("$x_1$", fontsize=18)
plt.ylabel("$y$", rotation=0, fontsize=18)
plt.legend(loc="upper left", fontsize=14)
plt.show()
