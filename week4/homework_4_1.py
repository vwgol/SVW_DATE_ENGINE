# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 17:15:48 2020

@author: Administrator
"""


import pandas as pd
import numpy as np
from efficient_apriori import apriori

def main():
    dataset = pd.read_csv('./Market_Basket_Optimisation.csv', header=None)
    transacations = []
    for myrow in dataset.values:
        transacations.append(list(filter(lambda x:x is not np.nan, myrow)))
    itemsets, rules = apriori(transacations, min_support=0.05, min_confidence=0.25)
    print('频繁项集：', itemsets)
    print('关联规则：', rules)
        
if __name__ == '__main__':
    main()