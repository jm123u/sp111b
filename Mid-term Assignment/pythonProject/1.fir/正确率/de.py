import pandas as pd

# 读取CSV文件
data = pd.read_csv('js1.csv')

# 删除包含百分号的数据
data_without_percent = data.replace('%', '', regex=True)

# 保存修改后的数据到新的CSV文件
data_without_percent.to_csv('newjs1.csv', index=False)
