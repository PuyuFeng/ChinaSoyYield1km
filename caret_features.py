import pandas as pd
import numpy as np
import math
import random
from catboost import Pool, CatBoostRegressor
from sklearn.metrics import mean_squared_error, r2_score, roc_auc_score, auc, roc_curve, mean_absolute_error
from pycaret.regression import *
import sys

# Redirecting the standard output to a file
sys.stdout = open('zuhe33.docx', 'w')

c = ['pre', 'tc_pdsi', 'tc_srad', 'tc_tmax', 'tc_tmin', 'tc_vpd']
r = ['GOSIF', 'LSTd', 'NDVI', 'NPP']
m = ['TPDC_AS', 'TPDC_MA', 'TPDC_NPK', 'TPDC_ONS', 'TPDC_Urea', '年份']
s = ['tc_soil', 'CEC_SOIL', 'CLAY', 'OC', 'pH', 'REF_BULK', 'SILT']

k: int
for k in range(3, 4):
    ##1读原始数据
    dat = pd.read_excel('I:\\xxls_data\\ml_data\\市数据2.xlsx')
    sub_df = pd.DataFrame(dat)
    print(sub_df)

    fixed_cols = ['大豆分区', '市级数据', '亚区']

    # 组合所有可能的列组合
    g = [
        c,
        r,
        m,
        s,
        c + r,
        c + m,
        c + s,
        r + m,
        r + s,
        m + s,
        c + r + m,
        c + r + s,
        c + m + s,
        r + m + s,
        c + r + m + s
    ]

    # 输出以检查
    for i, combo in enumerate(g, 1):
        print(f"组合 {i}: {combo}")

    for n in g:
        sub_df = dat[n + fixed_cols]
        print(sub_df)

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
        #2处理离散数据-哑变量处理
        if '亚区' in n:
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
        sub_df1 = sub_df1.drop(['大豆分区'], axis=1)
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

        print('catboost')
        catboost = create_model('catboost')
        print('et')
        et = create_model('et')
        print('ridge')
        ridge = create_model('ridge')

        print('ridge_stacker')
        print(n)
        huber_stacker = stack_models(estimator_list=[catboost, et], meta_model=ridge)

    # 列出所有回归模型
    # print(models())
    # print('roundn',rad)
    # top5 = compare_models(n_select=5, include=['lr', 'lasso', 'ridge', 'en', 'llar', 'br', 'ard', 'tr',
    #                                            'huber', 'kr', 'knn', 'dt', 'rf', 'et', 'ada', 'gbr',
    #                                            'mlp', 'xgboost', 'lightgbm', 'catboost'])
    # print('catboost')
    # catboost = create_model('catboost')
    # stacker = stack_models(estimator_list=top5[0:], meta_model=catboost)
    # print('et_stacker')


    # print('catboost')
    # catboost = create_model('catboost')
    # print('et')
    # et = create_model('et')
    # print('lightgbm')
    # lightgbm = create_model('lightgbm')
    # print('rf')
    # rf = create_model('rf')
    # print('xgboost')
    # xgboost = create_model('xgboost')
    # print('gbr')
    # gbr = create_model('gbr')
    # print('dt')
    # dt = create_model('dt')
    # print('ada')
    # ada = create_model('ada')
    # print('ridge')
    # ridge = create_model('ridge')
    # print('lr')
    # lr = create_model('lr')
    # print('br')
    # br = create_model('br')
    # print('knn')
    # knn = create_model('knn')
    # print('omp')
    # omp = create_model('omp')
    # print('en')
    # en = create_model('en')
    # print('lasso')
    # lasso = create_model('lasso')
    # print('huber')
    # huber = create_model('huber')
    # print('llar')
    # llar = create_model('llar')
    # print('dummy')
    # dummy = create_model('dummy')
    # print('par')
    # par = create_model('par')
    #
    # # modeldt_bagged = ensemble_model(catboost)
    # # top4 = compare_models(n_select=4, exclude='lar')
    # # top5 = compare_models(n_select=5, include=['et', 'catboost', 'xgboost', 'rf', 'lightgbm', 'gbr', 'dt', 'ada',
    # #                                            'ridge', 'lr', 'br', 'knn', 'omp', 'en', 'lasso', 'huber', 'llar',
    # #                                            'dummy', 'par'])
    #
    # # stacker = stack_models(estimator_list=top5[0:])
    # print('et_stacker')
    # et_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=et)
    # print('catboost_stacker')
    # catboost_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=catboost)
    # print('xgboost_stacker')
    # xgboost_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=xgboost)
    # print('rf_stacker')
    # rf_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=rf)
    # print('lightgbm_stacker')
    # lightgbm_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=lightgbm)
    # print('gbr_stacker')
    # gbr_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=gbr)
    # print('dt_stacker')
    # dt_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=dt)
    # print('ada_stacker')
    # ada_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=ada)
    # print('ridge_stacker')
    # ridge_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=ridge)
    # print('lr_stacker')
    # lr_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=lr)
    # print('br_stacker')
    # br_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=br)
    # print('knn_stacker')
    # knn_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=knn)
    # print('omp_stacker')
    # omp_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=omp)
    # print('en_stacker')
    # en_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=en)
    # print('lasso_stacker')
    # lasso_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=lasso)
    # print('huber_stacker')
    # huber_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=huber)
    # print('llar_stacker')
    # llar_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=llar)
    # print('dummy_stacker')
    # dummy_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=dummy)
    # print('par_stacker')
    # par_stacker = stack_models(estimator_list=[catboost, et, lightgbm, rf, xgboost], meta_model=par)

    # result = pd.concat([df_sit['year'], df_sit['SPEI'], catboost_predict['Label'],
    #                     et_predict['Label'], lightgbm_predict['Label'], rf_predict['Label'], xgboost_predict['Label'],
    #                     stacker_predict['Label']], axis=1)
    # result.to_csv('E:\\气象数据未解压\\spei\\analyse\\58918.csv',
    #               index_label=['id', 'year', 'SPEI', 'catboost', 'et', 'lightgbm', 'rf', 'xgboost', 'stacker'])
