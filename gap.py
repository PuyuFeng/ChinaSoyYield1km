import pandas as pd

# 读取Excel表格
df = pd.read_excel('C:/Users/cau/Desktop/xxls/数据/现有数据集/SPAM.xlsx')
df1 = pd.read_excel('I:/xxls_data/ml_data/县数据1_test.xlsx')

# 获取行和列的名称
columns = df.columns
index = df.index

# 生成空DataFrame
empty_df = pd.DataFrame(index=index, columns=columns)
empty_df1 = pd.DataFrame(index=df1.index, columns=df1.columns)


empty_df['county'] = df['county']
empty_df1['县'] = df1['县']
empty_df1['年份'] = df1['年份']
empty_df1['县级数据'] = df1['县级数据']
print(empty_df1)

n = 0
for i in range(0, len(df1)):
    for j in range(0, len(df)):
        if df1.iloc[i, 0] == df.iloc[j, 0]:
            for k in range(0, 2):
                if k*5 + 2005 == df1.iloc[i, 1]:
                    if pd.notnull(df.at[j, columns[k+1]]):
                        n += 1
                        if n % 10 == 0:
                            print(n)
                            print(empty_df)
                        empty_df.at[j, columns[k+1]] = df.iloc[j, k+1] - df1.iloc[i, 2]
                        empty_df1.at[i, df1.columns[3]] = df.iloc[j, k+1]



# for i in range(0, 371):
#     if
#     for j in range(1, 21):
#         for k in range(0, 13855):
#             if df.iloc[i, 0] == df1.iloc[k, 0] and j + 2000 == df1.iloc[k, 1]:
#                 n += 1
#                 if n % 10 == 0:
#                     print(n)
#                 empty_df.at[i, columns[j]] = df.iloc[i, j] - df1.iloc[k, 2]

# 保存结果到Excel文件
empty_df.to_excel('C:/Users/cau/Desktop/xxls/数据/现有数据集/SPAM_差.xlsx', index=False)
empty_df1.to_excel('C:/Users/cau/Desktop/xxls/数据/现有数据集/SPAM_对比.xlsx', index=False)
