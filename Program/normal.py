# -*- coding: utf-8 -*-
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats, integrate
sns.set(style="whitegrid", palette="muted", color_codes=True)
data = pd.read_csv('/Users/macair/Desktop/红包数据/1.csv')


mu,sigma=10,5.8498
x1=[]
for i in range(0,180):
    x=np.random.normal(mu,sigma)
    if x<1:
        x=1
    x1.append(x)
sns.kdeplot(x1)
sns.distplot(data['1'])
plt.show()
