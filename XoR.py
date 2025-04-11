# Write a program to build and display a Neural network using Tenser flow Keres. 

import tensorflow as tf
import numpy as np

# Define XORNet with Keras
class XORNet(tf.keras.Model):
    def __init__(self):
        super(XORNet, self).__init__()
        self.fc1 = tf.keras.layers.Dense(16, activation='tanh')  # Increased neurons and changed activation
        self.fc2 = tf.keras.layers.Dense(8, activation='tanh')   # Added another hidden layer
        self.fc3 = tf.keras.layers.Dense(1, activation='sigmoid')

    def call(self, inputs):
        x = self.fc1(inputs)
        x = self.fc2(x)
        x = self.fc3(x)
        return x

def validate_input(input_pair):
    for value in input_pair:
        if (value != 0) and (value != 1):
            return False
    return True

# XOR inputs and outputs
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
outputs = np.array([[0], [1], [1], [0]], dtype=np.float32)

# Instantiate model
model = XORNet()

# Compile the model with Binary Crossentropy Loss and Adam Optimizer
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
epochs = 100  # Increased epochs for better training
model.fit(inputs, outputs, epochs=epochs, verbose=0)

# Predict function
def predict(x):
    if not validate_input(x):
        return np.nan  # Return NaN for invalid inputs
    input_tensor = np.array([x], dtype=np.float32)
    output = model.predict(input_tensor, verbose=0)[0, 0]
    return 1 if output >= 0.5 else 0

# Test cases
test_cases = [(1, 1), (0, 0), (1, 0), (0, 1), (0.25, 0.75), (0.5, 0.5), (0.75, 0.25)]
true_outputs = [0, 0, 1, 1, np.nan, np.nan, np.nan]
predicted_outputs = []

for test in test_cases:
    result = predict(test)
    predicted_outputs.append(result)
    print(f"Input: {test}, Predicted Output: {result}")

# Calculate accuracy
def calculate_accuracy(y_true, y_pred):
    correct_predictions = 0
    total_predictions = 0
    for true, pred in zip(y_true, y_pred):
        if true == pred:
            correct_predictions += 1
        elif np.isnan(true) and np.isnan(pred):  # Handle NaN cases
            correct_predictions += 1
        total_predictions += 1
    return correct_predictions / total_predictions

accuracy = calculate_accuracy(true_outputs, predicted_outputs)
print(f"Accuracy of the XOR gate neural network: {accuracy * 100:.2f}%")
''' 
Input: (1, 1), Predicted Output: 0
Input: (0, 0), Predicted Output: 0
Input: (1, 0), Predicted Output: 1
Input: (0, 1), Predicted Output: 1
Input: (0.25, 0.75), Predicted Output: nan
Input: (0.5, 0.5), Predicted Output: nan
Input: (0.75, 0.25), Predicted Output: nan
Accuracy of the XOR gate neural network: 100.00%
'''
