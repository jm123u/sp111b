import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer
import numpy as np
import matplotlib.pyplot as plt

# 加载房价数据集
data = pd.read_csv('newjs1.csv')

data_filtered = data.drop(['地段位置或門牌',  '交易年月', '型態'], axis=1)


# 提取特征和目标变量
X = data_filtered[['主建物佔比', '總價(萬元)', '單價']]
y = data_filtered['總價(萬元)']  # 只保留目标变量 '總價(萬元)'

# 数据预处理
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X_imputed)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 训练线性回归模型
model = LinearRegression()
model.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = model.predict(X_test)

# 计算回归模型的评估指标
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error (MSE):", mse)
print("R-squared (R2):", r2)

# 绘制拟合图
fig, ax = plt.subplots()
ax.scatter(y_test, y_pred, color='blue', label='Actual vs. Predicted')
ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--', label='Perfect Fit')
ax.set_xlabel('Actual Price')
ax.set_ylabel('Predicted Price')
ax.set_title('Linear Regression - Actual vs. Predicted Price')
ax.legend()
plt.show()

