import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,1000)
y = np.sin(x)+1
z = np.cos(x**2) + 1

plt.figure(figsize=(8,4))
plt.plot(x,y,label = '$\sin x+1$',color = 'red',linewidth = 2) #绘图 设置标签，线条形状，颜色等
plt.plot(x,z,'b--',label='$\cos x^2+1$')
plt.xlabel('Time(s) ')
plt.ylabel('Volt')
plt.title('A Simple Example')
plt.ylim(0,2.2) #设置y轴范围
plt.legend()
plt.show()


#处理中文的显示
plt.rcParams['font.sans-serif'] = ['SimHei']
#处理负号的显示
plt.rcParams['axes.unicode_minus'] = False
