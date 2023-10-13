import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# load data from file poll_responses.csv column 'Response'
data = np.loadtxt('cache/poll_responses.csv',delimiter=',',skiprows=1,usecols=2)
df = pd.read_csv('cache/poll_responses.csv')
participants = df['Participant Name'].unique() 

fig, ax = plt.subplots(1, len(participants) + 1, figsize=(20, 5))
for i, person in enumerate(participants):
    data = df[df['Participant Name'] == person]['Response'].values

    # Calculate center of bins
    bins = np.histogram(data,bins=5)
    loc = [-2,-1,0,1,2]

    # Plot
    ax[i].bar(loc,bins[0])
    ax[i].set_title(f'Rating Distribution for {person}')
    ax[i].set_xlabel('Value')
    ax[i].set_ylabel('Counts')

bins = np.histogram(df['Response'],bins=5)
loc = [-2,-1,0,1,2]

# Plot
ax[-1].bar(loc,bins[0])
ax[-1].set_title('Mean Rating Distribution')
ax[-1].set_xlabel('Value')
ax[-1].set_ylabel('Counts')
plt.tight_layout()
plt.savefig('Images/histogram.png',dpi=300, bbox_inches='tight')
plt.show()

print(f'mean rating: {np.mean(data):.2f}')