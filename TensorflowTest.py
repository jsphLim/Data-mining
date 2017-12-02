# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tensorflow as tf
import numpy as np

#creat data

x_data=np.random.rand(100).astype(np.float32)
y_data=x_data*0.1+0.3

###creat tensorflow structure start###
#tf.Variable来创建描述y 的参数，可以把y_data=x_data*0.1+0.3想象成y=Weights*x+biases然后就是神经网络学者把Weights变成0.1，把biases变成0.3

Weights=tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases=tf.Variable(tf.zeros([1]))
y=Weights*x_data+biases

#计算误差并使用optimizer更新

loss=tf.reduce_mean(tf.square(y-y_data))
optimizer=tf.train.GradientDescentOptimizer(0.5)

#0.5指的是机器学习的学习效率

train=optimizer.minimize(loss)

#在使用神经网络结构之前必须初始话所有之前定义的Variable
#init=tf.initialize_all_variables()

init=tf.global_variables_initializer()

#接着创建会话Session并执行init初始化，run每次的training数据
###creat tensorflow structure start###
#激活部分sess像是指针run激活

sess=tf.Session()
sess.run(init)#Very important
for step in range(201):
    sess.run(train)
    if step%20==0:
        print(step,sess.run(Weights),sess.run(biases))

#设置步长为20，tensor张量数据流。
