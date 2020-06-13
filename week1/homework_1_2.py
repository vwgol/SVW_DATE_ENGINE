# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 16:29:17 2020

@author: Administrator
"""

import numpy as np
persontype=np.dtype({
                    'names':['name','语文','数学','英语'],
                    'formats':['U32','i','i','i']})
people=np.array([
                    ("张飞",68,65,30),
                    ("关羽",95,76,98),
                    ("刘备",98,86,88),
                    ("典韦",90,88,77),
                    ("许褚",80,90,90)
                ],dtype=persontype)

for subject in people.dtype.names[1:]:
    print("%s平均分:%.1f"%(subject,np.mean(people[subject])))
    print("%s最低分:%.1f"%(subject,np.min(people[subject])))
    print("%s最高分:%.1f"%(subject,np.max(people[subject])))
    print("%s方差:%.1f"%(subject,np.var(people[subject])))
    print("%s标准差:%.1f"%(subject,np.std(people[subject])))
    print("")    


total=[]
for each in map(list,people[:]):    
    total.append((each[0],sum(each[1:])))
print("总分名次")
print(sorted(total,key=lambda item:item[1],reverse=True))