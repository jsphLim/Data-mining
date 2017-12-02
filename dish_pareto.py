
from __future__ import print_function
#菜品盈利数据 帕累托图
import pandas as pd
dish_profit = 'catering_dish_profit.xlsx'

data = pd.read_excel(dish_profit,index_col=u'菜品名')
data = data[u'盈利'].copy()
data.sort_values(ascending = False)


import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure()
data.plot(kind='bar')
plt.ylabel(u'盈利')
p = 1.0*data.cumsum()/data.sum()
p.plot(color = 'r',secondary_y=True,style = '-o',linewidth=2)
plt.annotate(format(p[6],'.4%'),xy=(6,p[6]),xytext=(6*0.9,p[6]*0.9),arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))

plt.ylabel(u'盈利(比例)')
plt.show()


#分析结果  前七个菜品占种类书70% 盈利占85% 所以应该重点投入前七个菜品
