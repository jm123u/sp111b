import pandas as pd
import opencc

# 创建繁体字转简体字的实例
converter = opencc.OpenCC('t2s.json')  # t2s.json 是将繁体字转换为简体字的配置文件

# 读取 CSV 文件，使用繁体字编码 'big5'
df = pd.read_csv('jc.csv', encoding='utf-8')

# 移除不需要的列
df = df.drop(['社區簡稱'], axis=1)

# 将 '備註' 列中的缺失值填充为空字符串
df['備註'] = df['備註'].fillna('')

df = df.dropna(subset=['主要用途'])
# 过滤基于条件的行
df = df[~df['備註'].str.contains('親友')]
df = df[df['主要用途'].str.contains('住家用')]
print(df.columns)
# 过滤 '交易年月' 列中包含 '104' 的行
df = df[~df['交易年月'].str.contains('104')]
# 过滤 '單價' 列不等于 0 的行
df = df[df['單價'] != 0]

# 将 DataFrame 中的繁体字转换为简体字
df['備註'] = df['備註'].apply(lambda x: converter.convert(x))

# 删除 '備註' 列
df = df.drop(['備註'], axis=1)

# 将修改后的数据保存到新的 CSV 文件
df.to_csv('./js1.csv', index=False)

# 打印修改后的 DataFrame 的形状
print("Shape of modified DataFrame:", df.shape)

# 打印修改后的 DataFrame 的前几行
print("First few rows of modified DataFrame:")
print(df.head())
