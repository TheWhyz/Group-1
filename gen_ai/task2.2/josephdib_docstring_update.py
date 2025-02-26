import tensorflow as tf
from sklearn.model_selection import KFold
import pandas as pd

dataMNIST = pd.read_csv("MNIST.csv")

X=dataMNIST.drop('label', axis=1)
y = dataMNIST.iloc[:, 0]

kf = KFold(n_splits=5)
train = 0
test = 0

for train, test in kf.split(dataMNIST):

    tra_X = X.iloc[train, :]
    tra_y = y.iloc[train]
    tst_X = X.iloc[test, :]
    tst_y = y.iloc[test]

    tst_X, tra_X = tst_X / 255.0, tra_X / 255.0

    mdl = tf.keras.models.Sequential([
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10)
    ])

    pred = mdl(tra_X[:1]).numpy()

    tf.nn.softmax(pred).numpy()

    loss_func = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

    loss_func(tra_y[:1], pred).numpy()

    mdl.compile(optimizer='adam',
              loss=loss_func,
              metrics=['accuracy'])
    

    mdl.fit(tra_X, tra_y, epochs=5)

    mdl.evaluate(tst_X,  tst_y, verbose=2)


#---------------------------------------------------------------------

import tensorflow as tf
from sklearn.model_selection import KFold
import pandas as pd

# Load the MNIST dataset from a CSV file
dataMNIST = pd.read_csv("MNIST.csv")

# Separate features (X) and labels (y)
X = dataMNIST.drop('label', axis=1)  # Drop the 'label' column from features
y = dataMNIST.iloc[:, 0]  # The 'label' column as the target variable

# Initialize KFold cross-validation with 5 splits
kf = KFold(n_splits=5)

# Variables to store train and test indices in each fold
train = 0
test = 0

# Iterate through each fold for training and evaluation
for train, test in kf.split(dataMNIST):

    # Split the dataset into training and testing sets based on the current fold
    tra_X = X.iloc[train, :]  # Training features
    tra_y = y.iloc[train]     # Training labels
    tst_X = X.iloc[test, :]   # Testing features
    tst_y = y.iloc[test]      # Testing labels

    # Normalize the pixel values to be between 0 and 1 by dividing by 255
    tst_X, tra_X = tst_X / 255.0, tra_X / 255.0

    # Build a neural network model using TensorFlow Keras
    mdl = tf.keras.models.Sequential([
        tf.keras.layers.Dense(128, activation='relu'),  # Dense layer with 128 neurons and ReLU activation
        tf.keras.layers.Dropout(0.2),  # Dropout layer to prevent overfitting
        tf.keras.layers.Dense(10)  # Output layer with 10 neurons (for 10 classes)
    ])

    # Perform a quick prediction using the first sample of the training set
    pred = mdl(tra_X[:1]).numpy()  # Make a prediction for the first sample

    # Apply softmax to get probability distribution from raw logits (model output)
    tf.nn.softmax(pred).numpy()  # This step is to convert logits to probabilities

    # Define the loss function: SparseCategoricalCrossentropy for multi-class classification
    loss_func = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

    # Compute the loss for the first sample in the training set (just for demonstration)
    loss_func(tra_y[:1], pred).numpy()  # Calculate the loss for a single prediction

    # Compile the model with the Adam optimizer and the defined loss function
    mdl.compile(optimizer='adam',  # Optimizer used during training
                loss=loss_func,  # Loss function used to optimize the model
                metrics=['accuracy'])  # Metrics to evaluate model performance

    # Train the model using the training data for 5 epochs
    mdl.fit(tra_X, tra_y, epochs=5)

    # Evaluate the model on the test data and print the results
    mdl.evaluate(tst_X, tst_y, verbose=2)  # Evaluate performance on the test set

