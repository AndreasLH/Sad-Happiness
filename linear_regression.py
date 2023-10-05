import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.linalg import eigh
from sklearn import datasets
np.random.seed(21)
import os
from PIL import Image
from tqdm import tqdm
import sklearn.linear_model
import sklearn.feature_selection
import pickle as pkl

# Linear Regression using forward selection
PCs = np.load("PCs.npy")

# Load ratings
poll_responses = pd.read_csv("poll_responses.csv")
# Find Respons for all images with same image id and take the mean
ratings = poll_responses.groupby("Image").mean()["Response"].values

n_features = 10
model = sklearn.linear_model.LinearRegression()

print("Performing forward selection...")
forward_selection = sklearn.feature_selection.SequentialFeatureSelector(model, n_features_to_select=n_features)
selected_features = forward_selection.fit(PCs,ratings).get_support()

model = model.fit(PCs[:, selected_features], ratings)

# Save model
with open("linear_regression_model.pkl", "wb") as f:
    pkl.dump(model, f)


#%%
# Load model
with open("linear_regression_model.pkl", "rb") as f:
    model = pkl.load(f)

print('Generating images...')
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
    scaling = weights/np.linalg.norm(weights)**2
    for x0 in ratings:
        generated_images.append((x0-intercept) * scaling)
    return generated_images

ratings_generate = [-4,-2,-1,0,1,2,4]
synthetic_images = generate_images(model,ratings_generate)

plt.figure(figsize=(20, 10))
for i in range(len(synthetic_images)):
    plt.subplot(1, len(synthetic_images), i+1)
    plt.imshow(synthetic_images[i], cmap="gray")
    plt.title(ratings[i])
    plt.axis("off")
plt.show()

#%%
tmp = np.linalg.pinv(PCs)@ratings
weights = tmp[:-1]
intercept = tmp[-1]
scaling = weights/np.linalg.norm(weights)**2
tmp = (0-intercept) * scaling
plt.imshow(tmp.reshape(x,y), cmap="gray")
plt.axis("off")
plt.show()

