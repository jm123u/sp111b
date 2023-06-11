import pandas as pd
import numpy  as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, mean_squared_log_error
from sklearn.preprocessing import LabelEncoder

# Read the CSV file
data = pd.read_csv('newjs1.csv')

# Convert the date column to datetime type
data['交易年月'] = pd.to_datetime(data['交易年月'], format='%Y/%m/%d')

# Calculate the number of days relative to a reference date
ref_date = pd.to_datetime('2000-01-01')
data['交易年月'] = (data['交易年月'] - ref_date).dt.days

# Extract the features and target variable
X = data[['交易年月', '型態']]
y = data['總價(萬元)']

# Label encode the categorical feature
label_encoder = LabelEncoder()
X['型態'] = label_encoder.fit_transform(X['型態'])

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the decision tree regressor model
decision_tree = DecisionTreeRegressor()

# Fit the model on the training set
decision_tree.fit(X_train, y_train)

# Make predictions on the test set
y_pred = decision_tree.predict(X_test)

# Calculate performance metrics
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
msle = mean_squared_log_error(y_test, y_pred)

# Print the performance metrics
print("Mean Squared Error:", mse)
print("Mean Absolute Error:", mae)
print("R2 Score:", r2)
print("Root Mean Squared Error:", rmse)
print("Mean Absolute Percentage Error:", mape)
print("Mean Squared Log Error:", msle)
