import pandas as pd
import numpy as np
import math
import random
from catboost import Pool, CatBoostRegressor
from sklearn.metrics import mean_squared_error, r2_score, roc_auc_score, auc, roc_curve, mean_absolute_error
from pycaret.regression import *
import io
import sys

# Redirecting the standard output to a file
sys.stdout = open('stack1.docx', 'w')

k: int
for k in range(1, 2):
    ##1读原始数据
    dat = pd.read_excel('I:\\xxls_data\\ml_data\\市数据2.xlsx')
    sub_df = pd.DataFrame(dat)
    # rad = random.randint(1, 9)
    rad = k
    ##3 数据划分
    if rad == 1:
        sub_df1 = sub_df.query('大豆分区==1')
    elif rad == 2:
        sub_df1 = sub_df.query('大豆分区==2')
    elif rad == 3:
        sub_df1 = sub_df.query('大豆分区==3')
    elif rad == 4:
        sub_df1 = sub_df
    ##2处理离散数据-哑变量处理
    sub_df = pd.get_dummies(


        sub_df1,
        columns=['亚区'],
        prefix=['亚区'],
        prefix_sep="_",
        dummy_na=False,
        drop_first=False
    )


    ## 删除不需要的列  名称 日期等
    # df_sit = sub_df1.query('site==58918')
    # ne = sub_df1.query('site!=58918')
    sub_df1 = sub_df1.drop(['市', '大豆分区'], axis=1)
    # sub_df2 = ne.drop(['site', 'year', 'agriculture'], axis=1)
    # sub_df3 = df_sit.drop(['site', 'year', 'agriculture'], axis=1)
    # 查看列名称
    # clf = setup(data=sub_df2, target='SPEI', train_size=0.9, use_gpu=True)

    # clf = setup(data=sub_df1, target='市级数据', train_size=0.75, use_gpu=False)
    if rad == 1:
        clf = setup(data=sub_df1, target='市级数据', session_id=4, train_size=0.75, data_split_shuffle=True)
    elif rad == 2:
        clf = setup(data=sub_df1, target='市级数据', session_id=2, train_size=0.75, data_split_shuffle=True)
    elif rad == 3:
        clf = setup(data=sub_df1, target='市级数据', session_id=16, train_size=0.75, data_split_shuffle=True)
    elif rad == 4:
        clf = setup(data=sub_df1, target='市级数据', session_id=90, train_size=0.75, data_split_shuffle=True)

    # 列出所有回归模型
    # print(models())
    print('roundn',rad)
    # top5 = compare_models(n_select=5, include=['lr', 'lasso', 'ridge', 'en', 'llar', 'br', 'ard', 'tr',
    #                                            'huber', 'kr', 'knn', 'dt', 'rf', 'et', 'ada', 'gbr',
    #                                            'mlp', 'xgboost', 'lightgbm', 'catboost'])
    # # print('catboost')
    # catboost = create_model('catboost')
    # stacker = stack_models(estimator_list=top5[0:], meta_model=catboost)
    # print('et_stacker')



    lr = create_model('lr')
    print('lr')
    lasso = create_model('lasso')
    print('lasso')
    ridge = create_model('ridge')
    print('ridge')
    en = create_model('en')
    print('en')
    llar = create_model('llar')
    print('llar')
    br = create_model('br')
    print('br')
    ard = create_model('ard')
    print('ard')
    tr = create_model('tr')
    print('tr')
    huber = create_model('huber')
    print('huber')
    kr = create_model('kr')
    print('kr')
    knn = create_model('knn')
    print('knn')
    dt = create_model('dt')
    print('dt')
    rf = create_model('rf')
    print('rf')
    et = create_model('et')
    print('et')
    ada = create_model('ada')
    print('ada')
    gbr = create_model('gbr')
    print('gbr')
    mlp = create_model('mlp')
    print('mlp')
    xgboost = create_model('xgboost')
    print('xgboost')
    lightgbm = create_model('lightgbm', verbose=False)
    print('lightgbm')
    catboost = create_model('catboost')
    print('catboost')
    #
    # modeldt_bagged = ensemble_model(catboost)
    # top4 = compare_models(n_select=4, exclude='lar')
    # top5 = compare_models(n_select=5, include=['et', 'catboost', 'xgboost', 'rf', 'lightgbm', 'gbr', 'dt', 'ada',
    #                                            'ridge', 'lr', 'br', 'knn', 'omp', 'en', 'lasso', 'huber', 'llar',
    #                                            'dummy', 'par'])
    #
    # # stacker = stack_models(estimator_list=top5[0:])
    # print('et_stacker')


    lr_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=lr)
    print('lr_stacker')
    lasso_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=lasso)
    print('lasso_stacker')
    ridge_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=ridge)
    print('ridge_stacker')
    en_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=en)
    print('en_stacker')
    llar_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=llar)
    print('llar_stacker')
    br_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=br)
    print('br_stacker')
    ard_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=ard)
    print('ard_stacker')
    tr_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=tr)
    print('tr_stacker')
    huber_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=huber)
    print('huber_stacker')
    kr_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=kr)
    print('kr_stacker')
    knn_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=knn)
    print('knn_stacker')
    dt_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=dt)
    print('dt_stacker')
    rf_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=rf)
    print('rf_stacker')
    et_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=et)
    print('et_stacker')
    ada_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=ada)
    print('ada_stacker')
    gbr_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=gbr)
    print('gbr_stacker')
    mlp_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=mlp)
    print('mlp_stacker')
    xgboost_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=xgboost)
    print('xgboost_stacker')
    lightgbm_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=lightgbm)
    print('lightgbm_stacker')
    catboost_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=catboost)
    print('catboost_stacker')



    # result = pd.concat([df_sit['year'], df_sit['SPEI'], catboost_predict['Label'],
    #                     et_predict['Label'], lightgbm_predict['Label'], rf_predict['Label'], xgboost_predict['Label'],
    #                     stacker_predict['Label']], axis=1)
    # result.to_csv('E:\\气象数据未解压\\spei\\analyse\\58918.csv',
    #               index_label=['id', 'year', 'SPEI', 'catboost', 'et', 'lightgbm', 'rf', 'xgboost', 'stacker'])
