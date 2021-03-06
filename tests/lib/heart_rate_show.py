# -*- coding:utf-8 -*-
"""
Brief Desc: 测试心率信号显示
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Date: 2017-08-20 22:38:02. Created By paddyguan. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# 采样频率
Fs = 25.0
Ts = 1.0/Fs

# 读取信号
with open('./heart_rate_data.txt', 'r') as f:
    heart_rate_data = [int(i.strip()) for i in f.readlines()]

heart_rate_data = heart_rate_data[0:500]
heart_rate_data = np.asarray(heart_rate_data)
fft_data = np.fft.fft(heart_rate_data)
plt.figure()
plt.subplot(221)
plt.title('origin_data')
plt.plot(heart_rate_data)
plt.subplot(222)
plt.title('fft_data')
fft_data = np.abs(fft_data[0:len(fft_data)/2])
#x_data = np.asarray([i*0.05 for i in range(len(fft_data))])
x_data = np.arange(0, len(fft_data)*Ts, Ts)
plt.plot(x_data, fft_data)
filtered_data = signal.medfilt(heart_rate_data, 3)
#b,a = signal.butter(10, 0.15, 'low')
#filtered_data = signal.filtfilt(b, a, heart_rate_data)
plt.subplot(223)
plt.title('meddle_filtered_data')
plt.plot(filtered_data)
filtered_fft_data = np.fft.fft(filtered_data)
plt.subplot(224)
plt.title('fft_data')
filtered_fft_data = np.abs(filtered_fft_data[0:len(filtered_fft_data)/2])
xx_data = np.arange(0, len(filtered_fft_data)*Ts, Ts)
plt.plot(xx_data, filtered_fft_data)
# plt.show()
print len(filtered_fft_data)
a = max(filtered_fft_data[30:len(filtered_fft_data)/2])

for i, j in enumerate(filtered_fft_data):
    if j == a:
        print i
        break


print a
