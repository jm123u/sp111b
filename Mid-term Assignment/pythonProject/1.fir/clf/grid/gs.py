import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression

# 加载数据集
data = pd.read_csv('js1.csv')

# Convert the date column to datetime type
data['交易年月'] = pd.to_datetime(data['交易年月'], format='%Y/%m/%d')

# Calculate the number of days relative to a reference date
ref_date = pd.to_datetime('2000-01-01')
data['交易年月'] = (data['交易年月'] - ref_date).dt.days

# 提取特征和目标变量
X = data[['交易年月', '單價']]
y = data['總價(萬元)']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建线性回归模型
linear_regression = LinearRegression()

# 定义参数网格
param_grid = {
    'fit_intercept': [True, False]
}

# 创建网格搜索对象
grid_search = GridSearchCV(estimator=linear_regression, param_grid=param_grid, cv=5)

# 在训练集上进行网格搜索
grid_search.fit(X_train, y_train)

# 打印最佳超参数
print("Best Parameters:", grid_search.best_params_)

# 在测试集上评估模型
score = grid_search.score(X_test, y_test)
print("Score:", score)

# 获取网格搜索结果
results = pd.DataFrame(grid_search.cv_results_)

# 打印网格搜索结果
print(results[['params', 'mean_test_score', 'rank_test_score']])

