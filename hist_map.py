import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(1000) #1000个服从正态分布的随机数
plt.hist(x,10) #分成十组绘制直方图
plt.show()
