import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load the dataset
data = pd.read_csv('newjs1.csv')

# Perform data preprocessing
data['交易年月'] = pd.to_datetime(data['交易年月']).dt.year

# Extract the required features and target variable
X = data[['總價(萬元)', '交易年月']]
y = data['單價']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a random forest regression model
random_forest = RandomForestRegressor()

# Fit the model to the training data
random_forest.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = random_forest.predict(X_test)

# Calculate the average price increase
average_increase = (y_pred - y_test) / y_test * 100

# Create a new DataFrame for visualization
df_visualize = pd.DataFrame({'House Price': y_test, 'Average Increase': average_increase, 'Year': X_test['交易年月']})

# Plot the visualization
sns.set(style="whitegrid")
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()

sns.lineplot(x='Year', y='House Price', data=df_visualize, ax=ax1, color='b', marker='o')
sns.lineplot(x='Year', y='Average Increase', data=df_visualize, ax=ax2, color='r', marker='o')

ax1.set_xlabel('Year')
ax1.set_ylabel('House Price')
ax2.set_ylabel('Average Increase (%)')
ax1.set_title('House Price and Average Increase over Years')

plt.show()
