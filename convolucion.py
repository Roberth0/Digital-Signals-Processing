# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 15:23:46 2019

@author: Itami
"""
######################5.1 Signal to Convolve######################
from matplotlib import pyplot as plt

import signals as sg
from matplotlib import style


style.use('ggplot')
f, plt_arr =plt.subplots(2,sharex=True)
f.suptitle("Input signal and impulse response")
plt_arr[0].plot(sg.airflow_calibrated_100Hz)
plt_arr[0].set_title('Airflow')
plt_arr[1].plot(sg.Impulse_response)
plt_arr[1].set_title('Impulse')
plt.show()

###########################5.2 Convolution#############################
import mysignals as sigs
from matplotlib import pyplot as plt
from matplotlib import style
from scipy import signal

output_signal = signal.convolve(sg.airflow_calibrated_100Hz,sg.Impulse_response, mode='same')

style.use('ggplot')

f,plt_arr = plt.subplots(3,sharex=True)
f.suptitle("Convolution")
plt_arr[0].plot(sg.airflow_calibrated_100Hz, color ='cyan')
plt_arr[0].set_title("Input  Signal")
plt_arr[1].plot(sigs.Impulse_response, color ='blue')
plt_arr[1].set_title("Impulse Response")
plt_arr[2].plot(output_signal, color ='magenta')
plt_arr[2].set_title("Output Signal")

plt.show()

##############################5.3 Deconvolution#############################
from scipy import signal
import numpy as np


sig = sg.ecg_100Hz
filter = sg.Impulse_response

conv_result = signal.convolve(sig,filter)
deconv_result = signal.deconvolve(conv_result,filter)



print("Convolution result :")
print(conv_result)
print("Deconvolution result : ")
print(deconv_result)

f,plt_arr = plt.subplots(2,sharex=True)
f.suptitle("Convolution")
plt_arr[0].plot(conv_result, color ='cyan')
plt_arr[0].set_title("Input Signal")
plt_arr[1].plot(deconv_result, color ='blue')
plt_arr[1].set_title("Impulse Response")

plt.show()





#########################5.4 Correlation #############################
from scipy import signal
from matplotlib import pyplot as plt




corr_output_signal = signal.correlate(sg.airflow_calibrated_100Hz, sg.Impulse_response,mode ='same')
conv_output_signal = signal.convolve(sg.airflow_calibrated_100Hz, sg.Impulse_response,mode ='same')







f,plt_arr = plt.subplots(2,sharex=True)
f.suptitle("Graficas")
plt_arr[0].plot(corr_output_signal, color ='cyan')
plt_arr[0].set_title("Correlación")
plt_arr[1].plot(conv_output_signal, color ='blue')
plt_arr[1].set_title("Convolución")

plt.show()


##################5.6 Running Sum ##########################
from matplotlib import pyplot as plt
from matplotlib import style
import mysignals as sigs
import numpy as np


output_signal = np.cumsum(sg.airflow_calibrated_100Hz)

#style.use('ggplot')
style.use('dark_background')

f,plt_arr = plt.subplots(2,sharex=True)
f.suptitle("Running Sum")

plt_arr[0].plot(sg.airflow_calibrated_100Hz,color='yellow')
plt_arr[0].set_title("Input Signal")

plt_arr[1].plot(output_signal,color ='magenta')
plt_arr[1].set_title("Output Signal")

plt.show()

##############################CODE#############################################################
from matplotlib import pyplot as plt
from matplotlib import style
import mysignals as sigs



def calc_running_sum(sig_src_arr,sig_dest_arr):
    for x in range(len(sig_dest_arr)):
        sig_dest_arr[x] = 0

    for x in range(len(sig_src_arr)):
        sig_dest_arr[x] =  sig_dest_arr[x-1]+sig_src_arr[x]

        

    style.use('ggplot')
    #style.use('dark_background')

    f,plt_arr = plt.subplots(2,sharex=True)
    f.suptitle("Running Sum")

    plt_arr[0].plot(sig_src_arr,color='red')
    plt_arr[0].set_title("Input Signal")

    plt_arr[1].plot(output_signal,color ='magenta')
    plt_arr[1].set_title("Output Signal")

    plt.show()

output_signal =[None]*320
calc_running_sum(sg.ecg_100Hz,output_signal)


###########################5.7 First Difference ##############################################
from matplotlib import pyplot as plt
from matplotlib import style
import mysignals as sigs
import numpy as np


output_signal = np.diff(sg.airflow_calibrated_100Hz)

style.use('ggplot')
#style.use('dark_background')

f,plt_arr = plt.subplots(2,sharex=True)
f.suptitle("First Difference")

plt_arr[0].plot(sg.airflow_calibrated_100Hz,color='red')
plt_arr[0].set_title("Input Signal")

plt_arr[1].plot(output_signal,color ='magenta')
plt_arr[1].set_title("Output Signal")

plt.show()

###################################################CODE##############################################################

from matplotlib import pyplot as plt
from matplotlib import style
import mysignals as sigs


def calc_first_difference(sig_src_arr,sig_dest_arr):
    for x in range(len(sig_dest_arr)):
        sig_dest_arr[x] =0

    for x in range(len(sig_src_arr)):
        sig_dest_arr[x] = sig_src_arr[x] - sig_src_arr[x-1]
        

    style.use('ggplot')
    #style.use('dark_background')

    f,plt_arr = plt.subplots(2,sharex=True)
    f.suptitle("First Difference")

    plt_arr[0].plot(sig_src_arr,color='red')
    plt_arr[0].set_title("Input Signal")

    plt_arr[1].plot(sig_dest_arr,color ='magenta')
    plt_arr[1].set_title("Output Signal")

    plt.show()


output_signal =[None]*320
calc_first_difference(sigs.InputSignal_1kHz_15kHz,output_signal)



