# Task 58 - Feed Forward Neural Network using Keras
# Reference: https://builtin.com/data-science/feedforward-neural-network-intro

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

try:
    import tensorflow as tf
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense

    # Load data
    data = load_breast_cancer()
    X, y = data.data, data.target

    # Split & Scale
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Build model
    model = Sequential([
        Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.summary()

    # Train
    history = model.fit(X_train, y_train, epochs=20, batch_size=16,
                        validation_split=0.1, verbose=1)

    # Evaluate
    loss, acc = model.evaluate(X_test, y_test)
    print(f"\nTest Accuracy: {acc:.4f}")

except ImportError:
    print("TensorFlow not installed. Run: pip install tensorflow")
