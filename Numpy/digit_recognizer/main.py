import numpy as np
import urllib.request
import os

# -----------------------------
# Download MNIST automatically
# -----------------------------
URL = "https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz"
FILE = "mnist.npz"

if not os.path.exists(FILE):
    print("Downloading MNIST...")
    urllib.request.urlretrieve(URL, FILE)
    print("Download complete.")

# -----------------------------
# Load data
# -----------------------------
data = np.load(FILE)

X_train = data["x_train"]
y_train = data["y_train"]
X_test = data["x_test"]
y_test = data["y_test"]

# -----------------------------
# Preprocess
# -----------------------------
X_train = X_train.reshape(-1, 784) / 255.0
X_test = X_test.reshape(-1, 784) / 255.0

def one_hot(y):
    out = np.zeros((y.size, 10))
    out[np.arange(y.size), y] = 1
    return out

y_train_oh = one_hot(y_train)

# smaller dataset for speed
X_train = X_train[:10000]
y_train_oh = y_train_oh[:10000]

# -----------------------------
# Initialize weights
# -----------------------------
np.random.seed(0)
W = np.random.randn(784, 10) * 0.01
b = np.zeros((1, 10))

# -----------------------------
# Functions
# -----------------------------
def softmax(z):
    e = np.exp(z - np.max(z, axis=1, keepdims=True))
    return e / np.sum(e, axis=1, keepdims=True)

def loss(y_true, y_pred):
    return -np.mean(np.sum(y_true * np.log(y_pred + 1e-9), axis=1))

# -----------------------------
# Training
# -----------------------------
lr = 0.1
epochs = 15

for i in range(epochs):

    logits = X_train @ W + b
    probs = softmax(logits)

    L = loss(y_train_oh, probs)

    dZ = probs - y_train_oh
    dW = X_train.T @ dZ / len(X_train)
    db = np.mean(dZ, axis=0, keepdims=True)

    W -= lr * dW
    b -= lr * db

    print(f"Epoch {i+1}, Loss: {L:.4f}")

# -----------------------------
# Test
# -----------------------------
preds = np.argmax(softmax(X_test @ W + b), axis=1)
acc = np.mean(preds == y_test)

print("\nFinal Test Accuracy:", acc)

# Show first 10 predictions
print("\nSample Predictions:")
for i in range(10):
    print("Predicted:", preds[i], "Actual:", y_test[i])
