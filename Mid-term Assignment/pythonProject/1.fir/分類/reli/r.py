import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv('combined_file.csv')

# Create a DataFrame containing housing types
data = pd.DataFrame({'Type': ['Apartment (5 floors or less, no elevator)', 'Studio (1 bedroom, 1 living room, 1 bathroom)', 'Residential Building (11 floors or more, with elevator)', 'Mansion (10 floors or less, with elevator)', 'Apartment (5 floors or less, no elevator)', 'Studio (1 bedroom, 1 living room, 1 bathroom)', 'Residential Building (11 floors or more, with elevator)', 'Mansion (10 floors or less, with elevator)', 'Apartment (5 floors or less, no elevator)', 'Studio (1 bedroom, 1 living room, 1 bathroom)']})

# Use crosstab to calculate the frequency of different housing types
cross_tab = pd.crosstab(index=data['Type'], columns='count')

# Visualize the frequency using a heatmap
sns.heatmap(cross_tab, annot=True, fmt='d', cmap='YlGnBu')

# Set the title and axis labels
plt.title('Housing Type Heatmap')
plt.xlabel('Housing Type')
plt.ylabel('Count')

# Display the plot
plt.show()
