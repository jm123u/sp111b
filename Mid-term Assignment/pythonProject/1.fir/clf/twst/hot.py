import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.kernel_ridge import KernelRidge
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

data = pd.read_csv('../newjs1.csv', delimiter='\t', encoding='utf-8')

features = ['Location', 'transaction Year', 'Price', 'Total Area', 'Type']
target = ['Total Price (million)']

data['Year of transaction'] = pd.to_datetime(data['Year of transaction'], format='%Y/%m/%d', errors='coerce')


X_train, X_test, y_train, y_test = train_test_split(data[features], data[target], test_size=0.3, random_state=120)

combined_data = pd.concat([X_train, X_test])

combined_data_encoded = pd.get_dummies(combined_data, columns=['Type', 'Location'])

X_train_encoded = combined_data_encoded[:len(X_train)]
X_test_encoded = combined_data_encoded[len(X_train):]

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_encoded)
X_test_scaled = scaler.transform(X_test_encoded)

param_grid = {
    'kernel': ['linear', 'rbf', 'poly', 'sigmoid'],
    'alpha': [0.1, 1, 10],
}

grid_search = GridSearchCV(estimator=KernelRidge(), param_grid=param_grid, scoring='neg_mean_squared_error', cv=5)
grid_search.fit(X_train_scaled, y_train)

print("Best hyperparameters: ", grid_search.best_params_)
print("Best score: ", -grid_search.best_score_)

best_krr = KernelRidge(**grid_search.best_params_)
best_krr.fit(X_train_scaled, y_train)

y_pred = best_krr.predict(X_test_scaled)

y_test = y_test.values.ravel()
y_pred = y_pred.ravel()

mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)

rmse = np.sqrt(mse)
print('Root Mean Squared Error:', rmse)

# Calculate mean absolute percentage error (MAPE)
mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
print('Mean Absolute Percentage Error:', mape)

# Calculate mean absolute error (MAE)
mae = np.mean(np.abs(y_test - y_pred))
print('Mean Absolute Error:', mae)

# Calculate symmetric mean absolute percentage error (SMAPE)
smape = 2 * np.mean(np.abs(y_test - y_pred) / (np.abs(y_test) + np.abs(y_pred))) * 100
print('Symmetric Mean Absolute Percentage Error:', smape)

# Calculate coefficient of determination (R-squared score)
r2 = r2_score(y_test, y_pred)
print('R-squared Score:', r2)

results = pd.DataFrame({'Actual Value': y_test, 'Predicted Value': y_pred})

# Display the first 20 predicted results
print(results.head(20))
