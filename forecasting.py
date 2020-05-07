# coding=utf-8
#####  拟合的代码，用于预测第八年数据
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 8, 1)
y = np.array([0.4381,0.6299,0.5048,0.7005,0.2631,0.5954,1.0453])#股票编号1的1-7年的每股收益(期末摊薄，元/股)
z1 = np.polyfit(x, y, 3)#用3次多项式拟合
p1 = np.poly1d(z1)
print(p1) #在屏幕上打印拟合多项式
yvals=p1(x)
plot1=plt.plot(x, y, '*',label='original values')
plot2=plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(loc=4)
plt.title('polyfitting')
plt.show()
