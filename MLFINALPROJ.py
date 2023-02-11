import numpy as np
import matplotlib.pyplot as plt

# input data
X = np.random.rand(50,1)
y = np.random.rand(50,1)

# add column of ones to X for bias term
X = np.column_stack((np.ones(len(X)), X))

# Print the input variables before normal equation calculation
print("X:", X)
print("y:", y)
print("X transpose:", X.T)
print("X transpose * X:", X.T @ X)
print("Inverse of X transpose * X:", np.linalg.inv(X.T @ X))

# calculate theta using normal equation method
theta = np.linalg.inv(X.T @ X) @ X.T @ y
print("Theta:", theta)

# plot the line
plt.scatter(X[:,1], y)
plt.plot(X[:,1], X @ theta, 'r')
plt.xlabel('X')
plt.ylabel('y')
plt.show()
print("Independent Variables:", X[:,1:])
