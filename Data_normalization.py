import pandas as pd
import numpy as np
datafile = '########.xlsx'
data = pd.read_excel(datafile,header=0)

(data-data.min())/(data.max()-data.min()) #最小-最大规范化 x* = x-min/max-min
(data-data.mean())/data.std()  #零-均值规范化 x* = x-x"/σ
data/10**np.ceil(np.log10(data.abs().max())) #小数定标规范化 x* = x/10^k
