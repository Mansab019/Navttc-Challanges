# Task 54 - Support Vector Machine (SVM)
# Reference: https://stackabuse.com/implementing-svm-and-kernel-svm-with-pythons-scikit-learn/

import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler

# Load dataset
data = load_wine()
X, y = data.data, data.target

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features (important for SVM)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train - Linear Kernel
model_linear = SVC(kernel='linear')
model_linear.fit(X_train, y_train)
print(f"Linear Kernel Accuracy: {accuracy_score(y_test, model_linear.predict(X_test)):.4f}")

# Train - RBF Kernel
model_rbf = SVC(kernel='rbf')
model_rbf.fit(X_train, y_train)
print(f"RBF Kernel Accuracy: {accuracy_score(y_test, model_rbf.predict(X_test)):.4f}")

print("\nClassification Report (RBF):\n", classification_report(y_test, model_rbf.predict(X_test)))
