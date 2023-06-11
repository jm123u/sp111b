import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.kernel_ridge import KernelRidge
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('../newjs1.csv', delimiter='\t', encoding='utf-8')

features = ['Location', 'Transaction Year', 'Price', 'Total Area', 'Type']
target = ['Total Price (million)']

data['Transaction Year'] = pd.to_datetime(data['Transaction Year'], format='%Y/%m/%d', errors='coerce')

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
