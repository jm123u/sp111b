import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, mean_squared_log_error, mean_absolute_percentage_error
from sklearn.preprocessing import LabelEncoder

# Load the dataset
data = pd.read_csv('newjs1.csv')

# Perform data preprocessing
data['交易年月'] = pd.to_datetime(data['交易年月']).dt.year

# Extract the required features and target variable
X = data[['總價(萬元)', '交易年月', '型態']]
y = data['單價']

# Apply label encoding to the '型態' feature
label_encoder = LabelEncoder()
X['型態'] = label_encoder.fit_transform(X['型態'])

# Sort the data by '交易年月'
data_sorted = data.sort_values(by='交易年月')

# Extract the sorted '交易年月' and corresponding prices
sorted_dates = data_sorted['交易年月']
sorted_prices = data_sorted['單價']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a random forest regression model
random_forest = RandomForestRegressor()

# Fit the model to the training data
random_forest.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = random_forest.predict(X_test)

# 获取最早和最晚时间点的房价数据
earliest_price = sorted_prices.iloc[0]
latest_price = sorted_prices.iloc[-1]

# 计算价格涨幅百分比
price_change = (latest_price - earliest_price) / earliest_price * 100

# 打印平均涨幅
print("房价平均涨幅: {:.2f}%".format(price_change))

price_change_over_time = sorted_prices - earliest_price

# 绘制矩形图
plt.figure(figsize=(10, 6))
plt.bar(sorted_dates, price_change_over_time)
plt.xlabel('Trading Year')
plt.ylabel('Price Change')
plt.title(' Average increase in house prices (rectangular graph)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 绘制线性图
plt.figure(figsize=(10, 6))
plt.plot(sorted_dates, price_change_over_time)
plt.xlabel('Trading Year')
plt.ylabel('Price Change')
plt.title('Average house price increase (linear graph)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Calculate performance metrics
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
msle = mean_squared_log_error(y_test, y_pred)
mape = mean_absolute_percentage_error(y_test, y_pred) * 100

# Print the performance metrics
print("Mean Squared Error:", mse)
print("Mean Absolute Error:", mae)
print("R-squared Score:", r2)
print("Root Mean Squared Error:", rmse)
print("Mean Squared Log Error:", msle)
print("Mean Absolute Percentage Error:", mape)
