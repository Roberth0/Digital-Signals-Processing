[5:23 PM, 11/11/2019] Juan: # -- coding: utf-8 --
"""
Created on Mon Nov 11 14:17:47 2019

@author: ROMERO-VILATUÑA
"""

""""
Generar la señal x(t)=  2cos(60*pi*t)
""""
import numpy as np
import pylab as plt


#SEÑAL x(t)=2cos(60*pi*f)

muestras= np.arange(0,1,1/300)
muestras
#parámetros
amplitud=2
f=30
fase=0
tmin=-0.5
tmax=0.5

#generar señal
x1= amplitud*np.cos(2*np.pi*f*muestras)
plt.title("EJERCICIO 1")

plt.xlabel("Tiempo")
#titulo eje y
plt.ylabel("Corriente")
#titulo de la grafica
plt.grid()
print
#graficar la señal
plt.plot(x1, label='x1(t)=2cos(60pit)',color='red')
plt.legend(loc='best')

T=1/(6*f)
#tiempos de la grafica 
nmin=np.ceil(tmin/T)
nmax=np.floor(tmax/T)

#muestras de la señal
n=np.arange(nmin,nmax)
#sacar la seña de muestreo
x1=2*np.cos(2*np.pi*n*T*f)

plt.title("MUESTREO EJERCICIO 1 (6B)")
plt.plot(n*T,x1)
plt.plot(n*T,x1,'y.')


################################EJERCICIO 2###################################

muestras= np.arange(0,0.3,1/360)
muestras
#parámetros
a2=2
f2=30

tmin=-0.5
tmax=0.5

#generar señal
x1= a2*np.cos(2*np.pi*f2*muestras)
plt.title("EJERCICIO 2")

plt.xlabel("Tiempo")
#titulo eje y
plt.ylabel("Corriente")
#titulo de la grafica
plt.grid()
print
#graficar la señal
#plt.plot(x1, label='x1(t)=2cos(60pit)',color='red')
#plt.legend(loc='best')

#####

a3=2
f3=40
x2= a3*np.cos(2*np.pi*f3*muestras)

xt=x1+x2
plt.plot(xt, label='x1(t)=2cos(60pit)',color='red')
plt.legend(loc='best')

#####
a4=2
f4=45
x4= a4*np.cos(2*np.pi*f4*muestras)

xt1=xt+x4
plt.plot(xt1, label='x1(t)=2cos(60pit)+2cos(80pit)+2cos(90pit)',color='green')
#plt.legend(loc='best')


###### muestreo de la señal##########

T=1/(2*f)
am=2
fr=360
tmin=-0.5
tmax=0.5


#tiempos de la grafica 
nmin=np.ceil(tmin/T)
nmax=np.floor(tmax/T)

#muestras de la señal
n=np.arange(nmin,nmax)
#sacar la seña de muestreo
x1=am*np.cos((2*np.pi*30)*n*T)+am*np.cos((2*np.pi*40)*n*T)+am*np.cos((2*np.pi*45)*n*T)

plt.title("MUESTREO EJERCICIO 2)")
plt.plot(n*T,x1)
plt.plot(n*T,x1,'y.')

################## EJERCICIO 3#######################


muestras= np.arange(0,0.3,1/360)
muestras
#parámetros
a2=2
f2=300



#generar señal
x1= a2*np.cos(2*np.pi*f2*muestras)
plt.title("EJERCICIO 3")

plt.xlabel("Tiempo")
#titulo eje y
plt.ylabel("Corriente")
#titulo de la grafica
plt.grid()
print
#graficar la señal
#plt.plot(x1, label='x1(t)=2cos(60pit)',color='red')
#plt.legend(loc='best')

#####

a3=2
f3=400
x2= a3*np.cos(2*np.pi*f3*muestras)

xt=x1+x2
#plt.plot(xt, label='x1(t)=2cos(60pit)',color='red')
#plt.legend(loc='best')

#####
a4=2
f4=450
x4= a4*np.cos(2*np.pi*f4*muestras)

xt1=xt+x4
plt.plot(xt1, label='x1(t)=2cos(600pit)+2cos(800pit)+2cos(900pit)',color='yellow')
plt.legend(loc='best')

############## MUESTREO DE LA SEÑAL #################



T=1/(2*f)
am=2
fr=3600
tmin=-0.5
tmax=0.5


#tiempos de la grafica 
nmin=np.ceil(tmin/T)
nmax=np.floor(tmax/T)

#muestras de la señal
n=np.arange(nmin,nmax)
#sacar la seña de muestreo
x1=am*np.cos((2*np.pi*300)*n*T)+am*np.cos((2*np.pi*400)*n*T)+am*np.cos((2*np.pi*450)*n*T)

plt.title("MUESTREO EJERCICIO (3)")
plt.plot(n*T,x1)
plt.plot(n*T,x1,'m*')
