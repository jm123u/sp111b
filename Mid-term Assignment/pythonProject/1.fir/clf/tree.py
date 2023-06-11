import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 加载房价数据集
data = pd.read_csv('combined_file.csv')

# 转换日期列为日期类型
# 转换日期列为日期类型
data['交易年月'] = pd.to_datetime(data['交易年月'], format='mixed')


# 根据每年的数据计算总成交量和平均单价
yearly_data = data.groupby(data['交易年月'].dt.year).agg({'總價(萬元)': 'sum', '單價': 'mean'}).reset_index()

# 提取特征和目标变量
X = yearly_data[['交易年月']]
y_volume = yearly_data['總價(萬元)']
y_price = yearly_data['單價']

# 划分训练集和测试集
X_train, X_test, y_train_volume, y_test_volume = train_test_split(X, y_volume, test_size=0.2, random_state=42)
_, _, y_train_price, y_test_price = train_test_split(X, y_price, test_size=0.2, random_state=42)

# 训练成交量的决策树模型
model_volume = DecisionTreeRegressor()
model_volume.fit(X_train, y_train_volume)

# 在测试集上进行成交量预测
y_pred_volume = model_volume.predict(X_test)

# 计算成交量模型的评估指标
mse_volume = mean_squared_error(y_test_volume, y_pred_volume)
r2_volume = r2_score(y_test_volume, y_pred_volume)

print("Volume - Mean Squared Error (MSE):", mse_volume)
print("Volume - R-squared (R2):", r2_volume)

# 训练单价的决策树模型
model_price = DecisionTreeRegressor()
model_price.fit(X_train, y_train_price)

# 在测试集上进行单价预测
y_pred_price = model_price.predict(X_test)

# 计算单价模型的评估指标
mse_price = mean_squared_error(y_test_price, y_pred_price)
r2_price = r2_score(y_test_price, y_pred_price)

print("Price - Mean Squared Error (MSE):", mse_price)
print("Price - R-squared (R2):", r2_price)

# 绘制成交量预测结果
plt.figure(figsize=(10, 5))
plt.scatter(X_test, y_test_volume, color='blue', label='Actual')
plt.plot(X_test, y_pred_volume, color='red', linestyle='--', label='Predicted')
plt.xlabel('Year')
plt.ylabel('Volume')
plt.title('Volume Prediction - Decision Tree Regression')
plt.legend()
plt.show()

# 绘制单价预测结果
plt.figure(figsize=(10, 5))
plt.scatter(X_test, y_test_price, color='blue', label='Actual')
plt.plot(X_test, y_pred_price, color='red', linestyle='--', label='Predicted')
plt.xlabel('Year')
plt.ylabel('Price')
plt.title('Price Prediction - Decision Tree Regression')
plt.legend()
plt.show()
