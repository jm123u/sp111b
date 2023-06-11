import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error, median_absolute_error, mean_squared_log_error, explained_variance_score

# Load the dataset
data = pd.read_csv('newjs1.csv')

# Perform data preprocessing
data['交易年月'] = pd.to_datetime(data['交易年月']).dt.year

# Extract the required features and target variable
X = data[['交易年月']]
y = data['總價(萬元)']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
linear_reg = LinearRegression()

# Fit the model to the training data
linear_reg.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = linear_reg.predict(X_test)

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# Calculate MAPE
mape = mean_absolute_percentage_error(y_test, y_pred)

# Calculate SMAPE
smape = 2 * np.mean(np.abs(y_test - y_pred) / (np.abs(y_test) + np.abs(y_pred))) * 100

# Calculate MedAE
medae = median_absolute_error(y_test, y_pred)

# Calculate MSLE
msle = mean_squared_log_error(y_test, y_pred)

# Calculate EV
ev = explained_variance_score(y_test, y_pred)

# Create a new DataFrame for visualization
df_visualize = pd.DataFrame({'Price': y_test, 'Year': X_test['交易年月'], 'Predicted Price': y_pred})

# Plot the visualization
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Year', y='Price', data=df_visualize, color='b')
sns.lineplot(x='Year', y='Predicted Price', data=df_visualize, color='r')
plt.xlabel('Year')
plt.ylabel('Price (萬元)')
plt.title('Price over Years with Linear Regression')
plt.legend(['Regression Line', 'Actual Price'])

# Print the evaluation metrics
print("RMSE:", rmse)
print("MAPE:", mape)
print("SMAPE:", smape)
print("MedAE:", medae)
print("MSLE:", msle)
print("EV:", ev)

plt.show()
