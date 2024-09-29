import pandas as pd
import numpy as np
import math
import random
from sklearn.metrics import mean_squared_error, r2_score, roc_auc_score, auc, roc_curve, mean_absolute_error
from pycaret.regression import *


# 读取训练数据
train_data_path = r'I:\xxls_data\ml_data\市数据.xlsx'
train_df = pd.read_excel(train_data_path)

# 读取测试数据
test_data_path = r'I:\xxls_data\ml_data\县数据.xlsx'
test_df = pd.read_excel(test_data_path)

# 定义X和Y数据
X_train = train_df[['大豆单产', 'CEC_SOIL', 'CLAY', 'GOSIF', 'LSTd', 'NDVI', 'OC', 'pH', 'pre', 'REF_BULK', 'SILT', 'tc_pdsi', 'tc_soil', 'tc_srad', 'tc_tmax', 'tc_tmin', 'TPDC_AS', 'TPDC_MA', 'TPDC_NPK', 'TPDC_ONS', 'TPDC_Urea', '大豆分区']]
Y_train = train_df['大豆单产']
print(X_train)

X_test = test_df[['大豆单产', 'CEC_SOIL', 'CLAY', 'GOSIF', 'LSTd', 'NDVI', 'OC', 'pH', 'pre', 'REF_BULK', 'SILT', 'tc_pdsi', 'tc_soil', 'tc_srad', 'tc_tmax', 'tc_tmin', 'TPDC_AS', 'TPDC_MA', 'TPDC_NPK', 'TPDC_ONS', 'TPDC_Urea', '大豆分区']]
Y_test = test_df['大豆单产']


sub1 = X_train.query("大豆分区 == 3")
sub1 = sub1.drop(['大豆分区'], axis=1)

sub2 = X_test.query("大豆分区 == 3")
sub2 = sub2.drop(['大豆分区'], axis=1)
# sub_df2 = pd.get_dummies(
#     X_test,
#     columns=['大豆分区'],
#     prefix=['大豆分区'],
#     prefix_sep="_",
#     dummy_na=False,
#     drop_first=False
# )


# Create and set up the model with X_train data
clf = setup(data=sub1, target='大豆单产', train_size=0.9, use_gpu=False)

# Create models
catboost = create_model('catboost')
et = create_model('et')
# lightgbm = create_model('lightgbm', log_level=-1)
rf = create_model('rf')
xgboost = create_model('xgboost')

# Use X_test data for validation
catboost_predict = predict_model(catboost, data=sub2)
et_predict = predict_model(et, data=sub2)
# lightgbm_predict = predict_model(lightgbm, data=X_test)
rf_predict = predict_model(rf, data=sub2)
xgboost_predict = predict_model(xgboost, data=sub2)

stacker = stack_models(estimator_list=[catboost, et, rf, xgboost], meta_model=catboost)
stacker_predict = predict_model(stacker, data=sub2)
