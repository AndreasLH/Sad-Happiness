import numpy as np
import pandas as pd
np.random.seed(21)
import sklearn.linear_model
import sklearn.feature_selection
import pickle as pkl
import matplotlib.pyplot as plt

# Linear Regression using forward selection
PCs = np.load("cache/PCs.npy")
PCs = PCs[:,:25]
# Load ratings
poll_responses = pd.read_csv("cache/poll_responses.csv")
# Find Respons for all images with same image id and take the mean
ratings = poll_responses.groupby("Image")["Response"].mean()

n_features = 25
model = sklearn.linear_model.LinearRegression()

print("Performing forward selection...")
forward_selection = sklearn.feature_selection.SequentialFeatureSelector(model)#, n_features_to_select=n_features,tol=0.01,n_jobs=-1)
selected_features = forward_selection.fit(PCs,ratings).support_
print('number of selected features:',sum(selected_features))

model = model.fit(PCs[:, selected_features], ratings)

def mask_to_idx(mask):
    return np.where(mask)[0]

plt.figure(figsize=(12, 4))
plt.bar(mask_to_idx(selected_features), model.coef_)
plt.xticks(mask_to_idx(selected_features))
plt.title("Coefficients of selected features")
plt.xlabel("Feature index")
plt.ylabel("Coefficient")
plt.savefig('Images/linear_regression.png',dpi=300, bbox_inches='tight')

# Save selected features
np.save("cache/selected_features.npy", selected_features)
# Save model
with open("cache/linear_regression_model.pkl", "wb") as f:
    pkl.dump(model, f)