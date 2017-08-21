# -*- coding:utf-8 -*-
"""
Brief Desc: 心率数据处理
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Date: 2017-08-20 22:36:20. Created By paddyguan. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from scipy import signal
import numpy as np

def filter_date(origin_data):
    '''滤波'''
    tmp_data = np.asarray(origin_data)
    filter_date = signal.medfilt(tmp_data, 3)  # 滤波
    fft_data = np.fft.fft(filter_date)  # fft
    fft_data = fft_data[0:len(fft_data)/2]
    heart_rate = compute_heart_rate(fft_data)
    return {'filter_date': filter_date, 'heart_rate': heart_rate,}


def compute_heart_rate(fft_data):
    '''计算心率'''
    return 0
