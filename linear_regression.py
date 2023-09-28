import numpy as np
from matplotlib import pyplot as plt
from scipy.linalg import eigh
from sklearn import datasets
np.random.seed(21)
import os
from PIL import Image
from tqdm import tqdm
import sklearn

# Linear Regression using forward selection
PCs = np.load("PCs.npy")

n_features = 10
model = sklearn.linear_model.LinearRegression()

forward_selection = sklearn.feature_selection.SequentialFeatureSelector(model, n_features_to_select=n_features)
selected_features = forward_selection.get_support()

model = model.fit(PCs[:, selected_features])


# Generating images
def generate_images(model,ratings):
    """
    Generates an image based on the ratings provided.

    Input:
    model:               The linear regression model
    ratings:             A list of ratings for each feature

    Output:
    generated_images:    A list of generated images
    """
    
    generated_images = []
    intercept = model.intercept_
    weights = model.coef_
    scaling = weights/np.linalg.norm(weights)
    for x0 in ratings:
        generated_images.append((x0-intercept) * scaling)
    return generated_images

ratings = [-4,-2,-1,0,1,2,4]
synthetic_images = generate_images(model,ratings)

plt.figure(figsize=(20, 10))
for i in range(len(synthetic_images)):
    plt.subplot(1, len(synthetic_images), i+1)
    plt.imshow(synthetic_images[i].reshape(450, 610), cmap="gray")
    plt.title(ratings[i])
    plt.axis("off")
plt.show()
