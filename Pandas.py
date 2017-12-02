import pandas as pd

s = pd.Series([1,2,3],index=['a','b','c'])
d = pd.DataFrame([[1,2,3], [4,5,6],],columns=['a','b','c'])
d2 = pd.DataFrame(s)

d.head()
d.describe()

# print(d)
# print(d2)


stock = pd.read_excel('C:/Users/sd/Documents/WeChat Files/cherstalst/Files/data.xlsx')
print(stock)

#pd.read_csv('data.csv',encoding = 'utf-8')
#pandas 主要特征函数 sum() 按列求和
#mean 算术平均数
#var 方差
#std 标准差
#corr 计算样本相关系数矩阵
#cov 协方差矩阵
#shew 样本值的偏度
#kurt 样本值的峰度
# describe() 给出样本的基本描述
