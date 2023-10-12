import numpy as np
from matplotlib import pyplot as plt
import pickle as pkl
import os
np.random.seed(23)
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
'''
ratings_generate = [-3,-2,-1,0,1,2,3]
synthetic_images = generate_images(model,ratings_generate)

components = np.load("components.npy")
selected_features = np.load("selected_features.npy")
selected_features = np.concatenate((selected_features,np.zeros(933-len(selected_features),dtype=bool)))
loading_matrix = components[selected_features,:]
mean_image = np.load("mean.npy")

im_size = (254,187)

plt.figure(figsize=(20, 10))
for i in range(len(synthetic_images)):
    image = synthetic_images[i]@loading_matrix * 0.2 + mean_image
    plt.subplot(1, len(synthetic_images), i+1)
    plt.imshow(image.reshape(im_size), cmap="gray")
    plt.title(ratings_generate[i])
    plt.axis("off")
#plt.show()



 # Visualize part 5
n_components = 10
plt.figure(figsize=(15, 5))
for i in range(n_components):
    plt.subplot(3, n_components, i + 1)
    plt.imshow(loading_matrix[i].reshape(im_size), cmap='gray')
    plt.title(f'PC {i + 1}')
    plt.axis('off')
plt.tight_layout()
#plt.show()



# 2.4
tmp = np.linalg.pinv(PCs)@ratings
weights = tmp[:-1]
intercept = tmp[-1]
scaling = weights/np.linalg.norm(weights)**2
tmp = (0-intercept) * scaling
plt.imshow(tmp.reshape(x,y), cmap="gray")
plt.axis("off")
plt.show()
'''
def generate_dataset(scale_factor=0.2):
    # generate folders if not there
    if not os.path.exists("dataset2/"):
        os.makedirs("dataset2/")
        print("dataset2 folder created")
        
    # generate the images
    ratings_generate = [-3,-2,-1,0,1,2,3]
    synthetic_images = generate_images(model,ratings_generate)

    # prepare the model
    components = np.load("components.npy")
    selected_features = np.load("selected_features.npy")
    selected_features = np.concatenate((selected_features,np.zeros(933-len(selected_features),dtype=bool)))
    loading_matrix = components[selected_features,:]
    mean_image = np.load("mean.npy")
    print("Model loaded")
    
    # save the images
    print("Saving images...")
    im_size = (254,187)
    for i in range(len(synthetic_images)):
        plt.figure(figsize=(im_size[1]*3/im_size[0], im_size[0]*3/im_size[0]), )
        image = synthetic_images[i]@loading_matrix * scale_factor + mean_image
        plt.imshow(image.reshape(im_size), cmap="gray")
        #plt.title(ratings_generate[i])
        plt.axis("off")
        plt.tight_layout()
        plt.savefig(f"dataset2/image_{i-3}.png")
                    
if __name__ == "__main__":
    generate_dataset()