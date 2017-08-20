# -*- coding:utf-8 -*-
"""
Brief Desc: 测试心率信号显示
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Date: 2017-08-20 22:38:02. Created By paddyguan. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import matplotlib.pyplot as plt
import numpy as np

with open('./heart_rate_data.txt', 'r') as f:
    heart_rate_data = [int(i.strip()) for i in f.readlines()]

plt.figure()
plt.plot(heart_rate_data[0:100])
plt.show()



