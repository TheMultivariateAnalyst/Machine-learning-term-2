import numpy as np
import random

def generate_random_quad_func():
    a = random.uniform(-10, 10)
    b = random.uniform(-10, 10)
    c = random.uniform(-10, 10)
    d = random.uniform(-10, 10)
    e = random.uniform(-10, 10)
    f = random.uniform(-10, 10)
    return lambda x, y: a * x**2 + b * x * y + c * y**2 + d * x + e * y + f, a, b, c, d, e, f

def grad_f(x, y, a, b, c, d, e):
    return np.array([2 * a * x + b * y + d, b * x + 2 * c * y + e])

f, a, b, c, d, e, f = generate_random_quad_func()

# Set initial values for x and y
x = 2
y = 2

# Set learning rate
learning_rate = 0.1

# Perform gradient descent until the gradient is equal to 0
iteration = 0
while True:
    # Compute the gradient of f at (x, y)
    grad = grad_f(x, y, a, b, c, d, e)

    # If the gradient is equal to 0, we have reached the minimum
    if np.allclose(grad, 0):
        break

    # Update x and y using the gradient descent rule
    x = x - learning_rate * grad[0]
    y = y - learning_rate * grad[1]

    # Print the current iteration and the values of x and y
    if iteration < 3:
        print(f"Iteration {iteration}: x = {x}, y = {y}")

    iteration += 1

# Print the minimum value of f
print(f(x, y))
