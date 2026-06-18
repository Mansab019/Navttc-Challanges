# Task 59 - Loss Functions in Neural Networks
# Reference: https://www.analyticsvidhya.com/blog/2019/08/detailed-guide-7-loss-functions-machine-learning-python-code/

import numpy as np

y_true = np.array([1, 0, 1, 1, 0])
y_pred = np.array([0.9, 0.1, 0.8, 0.6, 0.3])

# Mean Squared Error
mse = np.mean((y_true - y_pred) ** 2)
print(f"MSE: {mse:.4f}")

# Mean Absolute Error
mae = np.mean(np.abs(y_true - y_pred))
print(f"MAE: {mae:.4f}")

# Binary Cross Entropy
epsilon = 1e-15
y_pred_clipped = np.clip(y_pred, epsilon, 1 - epsilon)
bce = -np.mean(y_true * np.log(y_pred_clipped) + (1 - y_true) * np.log(1 - y_pred_clipped))
print(f"Binary Cross Entropy: {bce:.4f}")

# Hinge Loss (for SVM)
y_true_hinge = np.array([1, -1, 1, -1])
y_pred_hinge = np.array([0.8, -0.5, 0.3, 0.2])
hinge = np.mean(np.maximum(0, 1 - y_true_hinge * y_pred_hinge))
print(f"Hinge Loss: {hinge:.4f}")
