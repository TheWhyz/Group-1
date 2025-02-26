from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#read data from csv file
data = pd.read_csv("MNIST_100.csv")

#drop labels and read into variables
x=data.drop('label', axis=1)
y=data.iloc[:, 0]

#construct the PCA
pca=PCA(n_components=2)
pca.fit(x)
PCAX=pca.transform(x)

#create the 10 data sets
plt.scatter(PCAX[0:100, 0], PCAX[0:100, 1])
plt.scatter(PCAX[100:200, 0], PCAX[100:200, 1])
plt.scatter(PCAX[200:300, 0], PCAX[200:300, 1])
plt.scatter(PCAX[300:400, 0], PCAX[300:400, 1])
plt.scatter(PCAX[400:500, 0], PCAX[400:500, 1])
plt.scatter(PCAX[500:600, 0], PCAX[500:600, 1])
plt.scatter(PCAX[600:700, 0], PCAX[600:700, 1])
plt.scatter(PCAX[700:800, 0], PCAX[700:800, 1])
plt.scatter(PCAX[800:900, 0], PCAX[800:900, 1])
plt.scatter(PCAX[900:1000, 0], PCAX[900:1000, 1])

#create the legend for PCA graph
plt.legend('0123456789')

#show PCA graph
plt.show()

##------------------------------------------------------

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd

# Read data from CSV file
data = pd.read_csv("MNIST_100.csv")

# Drop labels and assign to variables
x = data.drop('label', axis=1)
y = data['label']

# Perform PCA
pca = PCA(n_components=2)
PCAX = pca.fit_transform(x)

# Create scatter plot for each label (0 to 9)
plt.figure(figsize=(8, 6))  # Optional: Adjust figure size for better readability

# Loop through each unique label (0 to 9)
for label in range(10):
    # Select the points belonging to the current label
    label_data = PCAX[y == label]
    # Plot the points for this label
    plt.scatter(label_data[:, 0], label_data[:, 1], label=str(label))

# Add legend to the plot
plt.legend(title="Digit", loc="upper right")

# Show the plot
plt.title("PCA of MNIST Data")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()