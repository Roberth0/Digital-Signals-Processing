# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:11:35 2019

@author: Itami


"""
import numpy as np
import math
import matplotlib.pyplot as plt
import pylab as pl
from IPython import display
import time as ttime
import random
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import pearsonr as pr

z1=2+1j*3
z2=5-1j*5
z3=4+1j*2

suma=z1+z2
mul=z1*z2
div=z1/z2

print(z1+z2)
print(z1*z2)
print(z1/z2)

####Grafica Suma
plt.plot(np.real(suma),np.imag(suma),'ro')
plt.axis('square')
plt.axis([0, 10, -5, 10])
plt.grid(True)
plt.xlabel('Real axis'), plt.ylabel('Imaginary axis')
plt.show()

#Grafica Multiplicacion
plt.plot(np.real(mul),np.imag(mul),'ro')
plt.axis('square')
plt.axis([0, 30, 0, 30])
plt.grid(True)
plt.xlabel('Real axis'), plt.ylabel('Imaginary axis')
plt.show()

#Grafica Division
plt.plot(np.real(div),np.imag(div),'ro')
plt.axis('square')
plt.axis([-1, 1, -1, 1])
plt.grid(True)
plt.xlabel('Real axis'), plt.ylabel('Imaginary axis')
plt.show()

####Grafica e^(x1(t))
srate = 500; # sampling rate in Hz
t  = np.arange(0.,.25,1./srate)
freq=25
freq1=75/2
phas=0
phas1=np.pi

x1=2*np.cos(2*np.pi * freq * t + phas)
csw = np.exp(x1)

plt.plot(t,csw,'r',label=('2cos(50pit)'))
plt.legend(loc='best')
plt.xlabel('Tiempo')
plt.ylabel('Magnitud')
plt.grid(True)
plt.show()


#Grafica e^(x2(t))
t1  = np.arange(0.,0.25,1./srate)
x2=2*np.cos(2*np.pi * freq1 * t1 + phas1)
e2=np.exp(x2)


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(t1,e2)
ax.set_xlabel('Time (s)'), ax.set_ylabel('Real part'), ax.set_zlabel('Imag part')
ax.set_title('Sinusoide en 3D')
plt.show()


#Producto punto entre x1(t) y x2(t)
dp = np.dot(x1,x2);
print(dp)
#Producto punto entre x1(t) y una senal Gaussiana
srate = 1000;
time  = np.arange(-1.,1.,1./srate)
sinew  = 2*np.cos(2*np.pi * freq * time + phas)
gauss  = np.exp( (-time**2) / .1);
signal = np.multiply(sinew,gauss)

# sine wave frequencies
sinefrex = np.arange(0,25.,.5);

# plot signal
plt.plot(time,signal)
plt.xlabel('Time (sec.)'), plt.ylabel('Amplitude (a.u.)')
plt.title('Signal')
plt.show()



# initialize dot products vector
dps = np.zeros(len(sinefrex));

# loop over sine waves
for fi in range(1,len(dps)):
    
    # create sine wave
    sinew = np.sin( 2*np.pi*sinefrex[fi]*time)
    
    # compute dot product
    dps[fi] = np.dot( sinew,signal ) / len(time)


# and plot
plt.stem(sinefrex,dps)
plt.xlabel('Frequency (Hz)'), plt.ylabel('Producto Punto')
plt.title('Producto punto de las señales')
plt.show()



