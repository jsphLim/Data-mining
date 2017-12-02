import matplotlib.pyplot as plt

labels = 'Frogs','Hogs','Dogs','Logs'
sizes = [15,30,45,10] #各自占的比例

colors = ['yellowgreen','gold','lightskyblue','lightcoral'] #颜色设置
explode = (0,0.1,0,0) #突出显示部分的设置

plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.lf%%',shadow=True,startangle=90)
plt.axis('equal') #显示为圆 避免压缩
plt.show()
