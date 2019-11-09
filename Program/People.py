# -*- coding: utf-8 -*-
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats, integrate
sns.set(style="whitegrid", palette="muted", color_codes=True)
data = pd.read_csv('/Users/macair/Desktop/红包数据/2.csv')
data2 = pd.read_csv('/Users/macair/Desktop/红包数据/average.csv')

sns.stripplot(x=data['name'],y=data['number'],jitter=True)
sns.pointplot(x=data2['name'],y=data2['Max'])
sns.pointplot(x=data2['name'],y=data2['avg'])
sns.pointplot(x=data2['name'],y=data2['Min'])

plt.show()
