# -*- coding: utf-8 -*-
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats, integrate
sns.set(style="whitegrid", palette="muted", color_codes=True)
numbers=np.arange(0,40)
data = pd.read_csv('/Users/macair/Desktop/红包数据/1.csv')
data2 = pd.read_csv('/Users/macair/Desktop/红包数据/11.csv')


sns.distplot(data['1'])
#sns.distplot(data['2'])
#sns.distplot(data['3'])
#sns.distplot(data['4'])
#sns.distplot(data['5'])
#sns.distplot(data['6'])

#sns.kdeplot(data['1'])
#sns.kdeplot(data['2'])
#sns.kdeplot(data['3'])
#sns.kdeplot(data['4'])
#sns.kdeplot(data['5'])
#sns.kdeplot(data['6'])
#sns.barplot(x=data2['counts'],y=data2['1'])
#sns.barplot(x=data2['counts'],y=data2['2'])
#sns.barplot(x=data2['counts'],y=data2['3'])
#sns.barplot(x=data2['counts'],y=data2['4'])
#sns.barplot(x=data2['counts'],y=data2['5'])
#sns.barplot(x=data2['counts'],y=data2['6'])
plt.show()
