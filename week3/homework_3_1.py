# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 18:22:24 2020

@author: Administrator
"""


from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd

def main():
    data = pd.read_csv('car_data.csv', encoding='gbk')
    train_x = data[["人均GDP","城镇人口比重","交通工具消费价格指数","百户拥有汽车量"]]
    min_max_scaler = preprocessing.MinMaxScaler()
    train_x = min_max_scaler.fit_transform(train_x)
    kmeans = KMeans(n_clusters=4)
    kmeans.fit(train_x)
    predict_y = kmeans.predict(train_x)
    result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
    p_col = list(result.columns)
    p_col[-1] = '聚类结果'
    result.columns = p_col
    result.sort_values(by='聚类结果',inplace=True)
    print(result)
    result.to_csv("result_KMeans.csv")


if __name__ == '__main__':
    main()