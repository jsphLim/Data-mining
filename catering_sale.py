import pandas as pd


data = pd.read_excel('D:\pycharmproject\dataScience\catering_sale.xlsx',index_col= u'date')
data = data[(data[u'sale']>400)&(data[u'sale'])<5000] #筛选数据
statistics = data.describe()
statistics.loc['range'] = statistics.loc['max']-statistics.loc['min'] #极差
statistics.loc['var'] = statistics.loc['std']/statistics.loc['mean'] #变异系数
statistics.loc['dis'] = statistics.loc['75%']-statistics.loc['25%'] #四分位数间距

print(statistics)
