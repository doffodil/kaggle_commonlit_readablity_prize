import pandas as pd

# 运行此文件，将替覆盖原有数据集

# 设置pandas显示格式
pd.set_option("display.max_columns", 10, "display.max_colwidth", 40, "display.width", 200)

# 设置数据地址
train_path = '../input/commonlitreadabilityprize/train.csv'
enhance_path = "../input/enhance-data/Google_backtrans.csv"
vaild_path = '../input/commonlitreadabilityprize/valid.csv'

# 读取数据
train_df = pd.read_csv(train_path)
enhance_df = pd.read_csv(enhance_path)

# 新的的训练集、验证集大小
train_len = 2500
valid_len = len(train_df) - train_len

# 从增强数据中删除对应数据
index = []
for start in range(valid_len, len(enhance_df), len(train_df)):
    index.extend([i for i in range(start, start + train_len)])
enhance_df = enhance_df.iloc[index].reindex()

# 从训练集中划分出验证集
valid_df = train_df.loc[0:valid_len - 1].reindex()
train_df = train_df.loc[valid_len::].reindex()

# 将新的数据集保存
train_df.to_csv(train_path, index=False)
valid_df.to_csv(vaild_path, index=False)
enhance_df.to_csv(enhance_path, index=False)

print()