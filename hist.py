import numpy as np
from matplotlib import pyplot as plt

# load data from file poll_responses.csv column 'Response'
data = np.loadtxt('poll_responses.csv',delimiter=',',skiprows=1,usecols=2)

# Calculate center of bins
bins = np.histogram(data,bins=5)
loc = [-2,-1,0,1,2]

# Plot
plt.figure()
plt.bar(loc,bins[0])
plt.title('Distribution')
plt.xlabel('Value')
plt.ylabel('Counts')
plt.show()