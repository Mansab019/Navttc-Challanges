# Task 64 - CNN on CIFAR-10 Dataset
# Reference: https://www.analyticsvidhya.com/blog/2020/02/learn-image-classification-cnn-convolutional-neural-networks-3-datasets/

try:
    import tensorflow as tf
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
    from tensorflow.keras.datasets import cifar10
    from tensorflow.keras.utils import to_categorical

    # Class names
    class_names = ['airplane','automobile','bird','cat','deer',
                   'dog','frog','horse','ship','truck']

    # Load data
    (X_train, y_train), (X_test, y_test) = cifar10.load_data()

    # Preprocess
    X_train = X_train / 255.0
    X_test = X_test / 255.0
    y_train = to_categorical(y_train, 10)
    y_test = to_categorical(y_test, 10)

    # Build model
    model = Sequential([
        Conv2D(32, (3,3), activation='relu', padding='same', input_shape=(32,32,3)),
        BatchNormalization(),
        MaxPooling2D(2,2),
        Conv2D(64, (3,3), activation='relu', padding='same'),
        BatchNormalization(),
        MaxPooling2D(2,2),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.summary()

    # Train (3 epochs for demo)
    model.fit(X_train, y_train, epochs=3, batch_size=64,
              validation_split=0.1, verbose=1)

    # Evaluate
    loss, acc = model.evaluate(X_test, y_test)
    print(f"\nCIFAR-10 Test Accuracy: {acc:.4f}")

except ImportError:
    print("TensorFlow not installed. Run: pip install tensorflow")
