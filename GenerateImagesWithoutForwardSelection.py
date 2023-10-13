import numpy as np
import pandas as pd
np.random.seed(21)
import sklearn.linear_model
import matplotlib.pyplot as plt

# Alternative method without forward selection
# Change the following
first_component_to_use = 3
last_component_to_use = 17
alpha_scaling = 0.2


# Do not change this
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


# Linear Regression
PCs = np.load("cache/PCs.npy")
PCs = PCs[:,first_component_to_use:last_component_to_use]
# Load ratings
poll_responses = pd.read_csv("cache/poll_responses.csv")
# Find Respons for all images with same image id and take the mean
ratings = poll_responses.groupby("Image")["Response"].mean()

model = sklearn.linear_model.LinearRegression()
model = model.fit(PCs, ratings)

# Generating images
ratings_generate = [-10,-2,-1,0,1,2,10]
synthetic_images = generate_images(model,ratings_generate)

components = np.load("cache/components.npy")
loading_matrix = components[first_component_to_use:last_component_to_use,:]
mean_image = np.load("cache/mean.npy")

im_size = (254,187)

plt.figure(figsize=(20, 10))
for i in range(len(synthetic_images)):
    image = synthetic_images[i]@loading_matrix * alpha_scaling + mean_image
    plt.subplot(1, len(synthetic_images), i+1)
    plt.imshow(image.reshape(im_size), cmap="gray")
    plt.title(ratings_generate[i])
    plt.axis("off")
plt.show()
