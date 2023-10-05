import numpy as np
from matplotlib import pyplot as plt
np.random.seed(21)
import pickle as pkl

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

components = np.load("components.npy")
selected_features = np.load("selected_features.npy")
loading_matrix = components[selected_features,:]
mean_image = np.load("mean.npy")

im_size = (254,187)

plt.figure(figsize=(20, 10))
for i in range(len(synthetic_images)):
    image = synthetic_images[i]@loading_matrix + mean_image
    plt.subplot(1, len(synthetic_images), i+1)
    plt.imshow(image.reshape(im_size), cmap="gray")
    plt.title(ratings_generate[i])
    plt.axis("off")
plt.show()



 # Visualize part 5
n_components = 10
plt.figure(figsize=(15, 5))
for i in range(n_components):
    plt.subplot(3, n_components, i + 1)
    plt.imshow(components[i].reshape(im_size), cmap='gray')
    plt.title(f'PC {i + 1}')
    plt.axis('off')
plt.tight_layout()
plt.show()



""" 2.4
tmp = np.linalg.pinv(PCs)@ratings
weights = tmp[:-1]
intercept = tmp[-1]
scaling = weights/np.linalg.norm(weights)**2
tmp = (0-intercept) * scaling
plt.imshow(tmp.reshape(x,y), cmap="gray")
plt.axis("off")
plt.show()
"""
