import numpy as np
import pandas as pd
np.random.seed(21)
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

# Save selected features
np.save("selected_features.npy", selected_features)
# Save model
with open("linear_regression_model.pkl", "wb") as f:
    pkl.dump(model, f)