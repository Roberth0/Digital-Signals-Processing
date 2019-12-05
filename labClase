# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:34:17 2019

@author: Itami
"""
import numpy as np
import pylab as plt
import pandas as pd
from scipy import signal
from scipy.ndimage import gaussian_filter
from pykalman import KalmanFilter
import math
from scipy.fftpack import fft, fftfreq, ifft

from matplotlib import pyplot as plt
from matplotlib import style


datos=pd.ExcelFile('muestras.xlsx')
df=datos.parse("Hoja1")

senalCorazon=[]
for i in range(0,1400):
    valor=df.iloc[i,5]
    senalCorazon.append(valor)

print(senalCorazon)

def calc_dft(sig_src_arr):
    sig_dest_imx_arr = [None]*int((len(sig_src_arr)/2))
    sig_dest_rex_arr = [None]*int((len(sig_src_arr)/2))
    sig_dest_mag_arr = [None]*int((len(sig_src_arr)/2))
    
    for j in range(int(len(sig_src_arr)/2)):
        sig_dest_rex_arr[j] =0
        sig_dest_imx_arr[j] =0

    for k in range(int(len(sig_src_arr)/2)):
        for i in range(len(sig_src_arr)):
            sig_dest_rex_arr[k] = sig_dest_rex_arr[k] + sig_src_arr[i]*math.cos(2*math.pi*k*i/len(sig_src_arr))
            sig_dest_imx_arr[k] = sig_dest_imx_arr[k] - sig_src_arr[i]*math.sin(2*math.pi*k*i/len(sig_src_arr))

    for x in range(int(len(sig_src_arr)/2)):
        sig_dest_mag_arr[x] = math.sqrt(math.pow(sig_dest_rex_arr[x],2)+math.pow(sig_dest_imx_arr[x],2))
        
    

    style.use('ggplot')
    f,plt_arr = plt.subplots(4, sharex=True)
    f.suptitle("Discrete Fourier Transform (DFT)")

    plt_arr[0].plot(sig_src_arr, color='red')
    plt_arr[0].set_title("Input Signal",color='red')
    
    plt_arr[1].plot(sig_dest_rex_arr, color='green')
    plt_arr[1].set_title("Frequency Domain(Real part)",color='green')

    plt_arr[2].plot(sig_dest_imx_arr, color='green')
    plt_arr[2].set_title("Frequency Domain(Imaginary part)",color='green')

    plt_arr[3].plot(sig_dest_mag_arr, color='magenta')
    plt_arr[3].set_title("Frequency Domain (Magnitude))",color='magenta')
   #
    

    plt.show()
    
calc_dft(senalCorazon)

def calc_dft2(sig_src_arr):
    sig_dest_imx_arr = [None]*int((len(sig_src_arr)/2))
    sig_dest_rex_arr = [None]*int((len(sig_src_arr)/2))
    sig_dest_mag_arr = [None]*int((len(sig_src_arr)/2))
    
    for j in range(int(len(sig_src_arr)/2)):
        sig_dest_rex_arr[j] =0
        sig_dest_imx_arr[j] =0

    for k in range(int(len(sig_src_arr)/2)):
        for i in range(len(sig_src_arr)):
            sig_dest_rex_arr[k] = sig_dest_rex_arr[k] + sig_src_arr[i]*math.cos(2*math.pi*k*i/len(sig_src_arr))
            sig_dest_imx_arr[k] = sig_dest_imx_arr[k] - sig_src_arr[i]*math.sin(2*math.pi*k*i/len(sig_src_arr))

    for x in range(int(len(sig_src_arr)/2)):
        sig_dest_mag_arr[x] = math.sqrt(math.pow(sig_dest_rex_arr[x],2)+math.pow(sig_dest_imx_arr[x],2))
    
    plt.xlim(0,900)
    plt.stem(sig_dest_mag_arr)
    

    plt.show()


calc_dft2(senalCorazon)


########################Filtro Senal################
#

def snr(suavizado):
    ruido=np.array(senalCorazon)-np.array(suavizado)  
    ruido2=np.array(senalCorazon)-np.array(suavizado)
    plt.plot(ruido,'c')
    plt.xlabel('Tiempo')
    plt.ylabel('Magnitud')
    plt.title('Ruido Filtro')
    plt.show()
    return ruido2
    
    


#################################Savitzky Golay##################################
savis_smooth=signal.savgol_filter(senalCorazon,9,3) ### senal de entrada/ tamano de wi/ exponente
signal.savgol_coeffs(11,3)
plt.plot(savis_smooth,color='m')
plt.xlabel("Tiempo")
plt.ylabel("Magnitud")
plt.title("Filtro Savitzky Golay")
plt.grid()
#plt.plot(senalCorazon,color='red',label='original samples')
plt.show()
snr(savis_smooth)
calc_dft2(snr(savis_smooth))

