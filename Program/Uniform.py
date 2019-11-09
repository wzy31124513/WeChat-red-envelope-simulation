# -*- coding: utf-8 -*-
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats, integrate
sns.set(style="whitegrid", palette="muted", color_codes=True)
data = pd.read_csv('/Users/macair/Desktop/红包数据/1.csv')

x1=[]
x2=[]
x3=[]
x4=[]
x5=[]
x6=[]
for i in range(0,180):
    x=np.random.uniform(0,20)
    if x<1:
        x=1
    x1.append(x)
for i in x1:
    x=np.random.uniform(0.01,(60-i)*2/5)
    if x<(60-i)/50:
        x=(60-i)/50
    x2.append(x)
for i in range(0,180):
    x=np.random.uniform(0.01,(60-x1[i]-x2[i])/2)
    if x<(60-x1[i]-x2[i])/40:
        x=(60-x1[i]-x2[i])/40
    x3.append(x)
for i in range(0,180):
    x=np.random.uniform(0.01,(60-x1[i]-x2[i]-x3[i])*2/3)
    if x<(60-x1[i]-x2[i]-x3[i])/30:
        x=(60-x1[i]-x2[i]-x3[i])/30
    x4.append(x)
for i in range(0,180):
    x=np.random.uniform(0.01,60-x1[i]-x2[i]-x3[i]-x4[i])
    if x<(60-x1[i]-x2[i]-x3[i]-x4[i])/20:
        x=(60-x1[i]-x2[i]-x3[i]-x4[i])/20
    while (x==60-x1[i]-x2[i]-x3[i]-x4[i]):
        x=np.random.uniform(0.01,60-x1[i]-x2[i]-x3[i]-x4[i])
    x5.append(x)
for i in range(0,180):
    x6.append(60-x1[i]-x2[i]-x3[i]-x4[i]-x5[i])
sns.distplot(data['1'])
sns.kdeplot(x1)
'''sns.distplot(data['2'])
sns.kdeplot(x2)'''
'''sns.distplot(data['3'])
sns.kdeplot(x3)'''
'''sns.distplot(data['4'])
sns.kdeplot(x4)'''
'''sns.distplot(data['5'])
sns.kdeplot(x5)'''
'''sns.distplot(data['6'])
sns.kdeplot(x6)'''
plt.show()

'''print([max(x1),max(x2),max(x3),max(x4),max(x5),max(x6)])
print([min(x1),min(x2),min(x3),min(x4),min(x5),min(x6),])
print([sum(x1)/len(x1),sum(x2)/len(x1),sum(x3)/len(x1),sum(x4)/len(x1),sum(x5)/len(x1),sum(x6)/len(x1)])
print([np.var(x1),np.var(x2),np.var(x3),np.var(x4),np.var(x5),np.var(x6)])'''
