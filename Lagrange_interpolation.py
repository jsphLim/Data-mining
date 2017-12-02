import pandas as pd
from scipy.interpolate import lagrange

#数据补缺 运用拉格朗日插值法
inputfile = 'catering_sale.xlsx'

outfile = 'sales.xlsx'

data = pd.read_excel(inputfile)

data[u'sale'][(data[u'sale']<400) | (data[u'sale']>5000)] = None #过滤

def ployinterp_column(s,n,k=5):  # s为列向量 n为被插值的位置 k代表取前后五个数据
    y = s[list(range(n-k,n))+list(range(n+1,n+1+k))] #取数
    y = y[y.notnull()]  #剔除空值
    return lagrange(y.index,list(y))(n) #插值并返回结果

for i in data.columns: #遍历找到空的地方就插入
    for j in range(len(data)):
        if(data[i].isnull())[j]:
            data[i][j] = ployinterp_column(data[i],j)

data.to_excel(outfile)
