import pandas as pd
from catboost import CatBoostRegressor
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split

# 读取训练数据
train_data_path = r'I:\xxls_data\ml_data\市数据.xlsx'
train_df = pd.read_excel(train_data_path)

# 读取测试数据
test_data_path = r'I:\xxls_data\ml_data\县数据.xlsx'
test_df = pd.read_excel(test_data_path)

# 定义X和Y数据
X_train = train_df[['CEC_SOIL', 'CLAY', 'GOSIF', 'LSTd', 'NDVI', 'OC', 'pH', 'pre', 'REF_BULK', 'SILT', 'tc_pdsi', 'tc_soil', 'tc_srad', 'tc_tmax', 'tc_tmin', 'TPDC_AS', 'TPDC_MA', 'TPDC_NPK', 'TPDC_ONS', 'TPDC_Urea']]
Y_train = train_df['市级数据']

X_test = test_df[['CEC_SOIL', 'CLAY', 'GOSIF', 'LSTd', 'NDVI', 'OC', 'pH', 'pre', 'REF_BULK', 'SILT', 'tc_pdsi', 'tc_soil', 'tc_srad', 'tc_tmax', 'tc_tmin', 'TPDC_AS', 'TPDC_MA', 'TPDC_NPK', 'TPDC_ONS', 'TPDC_Urea']]
Y_test = test_df['县级数据']

# 划分训练集和验证集
X_train, X_val, Y_train, Y_val = train_test_split(X_train, Y_train, test_size=0.2, random_state=42)
print("划分训练集和验证集")

# 初始化CatBoost回归模型
model = CatBoostRegressor(iterations=1000, depth=6, learning_rate=0.1, loss_function='RMSE', random_seed=42)
print("初始化CatBoost回归模型")

# 拟合模型
model.fit(X_train, Y_train, eval_set=(X_val, Y_val), early_stopping_rounds=50, verbose=100)
print("拟合模型")

# 预测测试集
Y_pred = model.predict(X_test)
print("预测测试集")

# 计算R方值
r2 = r2_score(Y_test, Y_pred)

# 计算RMSE值
rmse = mean_squared_error(Y_test, Y_pred, squared=False)

print(f'R方值 (R-squared): {r2}')
print(f'RMSE值 (Root Mean Squared Error): {rmse}')
