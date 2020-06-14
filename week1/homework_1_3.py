# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 22:27:05 2020

@author: Administrator
"""


import pandas as pd
result=pd.read_csv('car_complain.csv')
problems=result.problem.str.get_dummies(',')
tags=problems.columns
result = result.drop('problem', 1).join(problems)
df1=result.groupby(['brand'])[tags].agg(['sum'])
df1.reset_index(inplace=True)
df1['品牌投诉问题总数']=df1.sum(axis=1)
df1=df1.drop(tags,1)
print(df1)
df2=result.groupby(['brand','car_model'])[tags].agg(['sum'])
df2.reset_index(inplace=True)
df2['车型投诉问题总数']=df2.sum(axis=1)
df2=df2.drop(tags,1)
print(df2)
df3=result.groupby(['brand'])['car_model'].agg(['nunique'])
df3.reset_index(inplace=True)
df4 = pd.merge(df1, df3, on=['brand'],how='left')
df4['车型平均投诉问题数']=round(df4.apply(lambda x:x[('品牌投诉问题总数','')]/x['nunique'],axis=1),2)
df4=df4.sort_values(by='车型平均投诉问题数',ascending=False)
print(df4)
