# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 09:01:23 2020

@author: Usuario
"""
import signals as dt
import matplotlib.pyplot as plt
from scipy.fftpack  import fft
import numpy as np
from scipy import signal
#from matplotlib import style


#Graficas de las funciones
x1=dt.airflow_100Hz
x2=dt.airflow_calibrated_100Hz
x3=dt.ecg_100Hz

def plot(signal,title):
        plt.plot(signal);plt.title(title)
        plt.xlabel("Time"); plt.ylabel("Magnitude")
        plt.grid("on")
        plt.show()
        
plot(x1,"Airflow")
plot(x2,"Airflow Calibrated")
plot(x3,"Ecg")
#Transformada de Fourier


tf1=fft(x1)
tf2=fft(x2)
tf3=fft(x3)
def plotf(signal,title):
    plt.stem(signal);plt.title(title)
    plt.xlabel("Frecuency"); plt.ylabel("Time")
    plt.grid("on")
    plt.xlim(0,len(signal)/2)
    plt.show()
    

plotf(tf1,"Transformada Airflow")
plotf(tf2,"Transformada Airflow Calibrated")
plotf(tf3,"Transformada Ecg")

#Normalizacion
norm_signal=np.zeros(len(x2))
for i,num in enumerate(x2):
    norm_signal[i]=float(x2[i]/max(x2))

plot(norm_signal,"Señal Normalizada")


#Filtros FIIR
highpas_coef=signal.firwin(21,2,nyq=100,pass_zero=False,window='bartlett')
signal_output=signal.convolve(norm_signal,highpas_coef,mode='same')
lowpass_coef=signal.firwin(21,30,nyq=100, window='bartlett')
output=signal.convolve(signal_output,lowpass_coef, mode='same')
plot(output,"Señal Filtrada Ventana Bartlett")


highpas_coef=signal.firwin(21,2,nyq=100,pass_zero=False,window='blackman')
signal_output=signal.convolve(norm_signal,highpas_coef,mode='same')
lowpass_coef=signal.firwin(21,40,nyq=100, window='blackman')
output=signal.convolve(signal_output,lowpass_coef, mode='same')
plot(output,"Señal Filtrada Ventana Blackman")

#Filtros IIR

sos = signal.cheby1(2, 1,2, 'hp', fs=100,analog=False, output='sos')
filtered1 = signal.sosfilt(sos, norm_signal)
sos2 = signal.cheby1(2, 1,5, 'lp', fs=100,analog=False, output='sos')
filtered2 = signal.sosfilt(sos2, filtered1)
plot(filtered2,"Filtro IIR Chebyshef")


butter = signal.butter(3, 2, 'hp', fs=100,analog=False, output='sos')
filtered3 = signal.sosfilt(butter, norm_signal)
butter2 = signal.butter(3, 5, 'lp', fs=100,analog=False, output='sos')
filtered4 = signal.sosfilt(butter2, filtered3)
plot(filtered4,"Filtro IIR Butterworth")


plt.subplot(2,1,1)
plt.plot(norm_signal)
plt.subplot(2,1,2)
plt.plot(filtered4)









