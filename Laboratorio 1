# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 08:18:20 2019

@author: Itami
"""
import numpy as np
import pylab as plt
########Laboratorio 1 ###############
#x(t)=4cos(t)
plt.figure()
muestras=np.arange(0,10,1/60)
amplitud1=4
frecuencia=1/(2*np.pi)
x1=amplitud1*np.cos(2*np.pi*frecuencia*muestras)
plt.plot(x1,label='x(t)=4cos(t)',color='g')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Ejercicio 1")
plt.legend(loc='best')
plt.grid()
plt.show()
plt.figure(1)

#x(t)=4cos(6t)
plt.figure()
amplitud2=4
frecuencia2=3/(np.pi)
x2=amplitud2*np.cos(2*np.pi*frecuencia2*muestras)
plt.plot(x2,label='x(t)=4cos(6t)',color='red')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Ejercicio 2")
plt.legend(loc='best')
plt.grid()
plt.show()
plt.figure(2)

#x(t)=4cos(6t+pi)
plt.figure()
amplitud3=4
frecuencia3=3/np.pi
fase1=np.pi
x3=amplitud3*np.cos(2*np.pi*frecuencia3*muestras+fase1)
plt.plot(x3,label='x(t)=4cos(6t+pi)',color='purple')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Ejercicio 3")
plt.legend(loc='best')
plt.grid()
plt.show()
plt.figure(3)

#x(t)=4cos(6t+pi)+3sin(5t+2pi/3)

amplitud4=4
frecuencia4=6/(2*np.pi)
fase4=np.pi
x4=amplitud4*np.cos(2*np.pi*frecuencia4*muestras+fase4)

amplitud5=3
frecuencia5=5/(2*np.pi)
fase5=2*np.pi/3
x5=amplitud5*np.sin(2*np.pi*frecuencia5*muestras+fase5)

#Grafica Ejercicio 4
xt=x4+x5
plt.figure()
plt.plot(xt,label='x(t)=4cos(6t+pi)+3sin(5t+2pi/3)',color='yellow')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Ejercicio 4")
plt.legend(loc='best')
plt.grid()
plt.show()
plt.figure(4)
###################Senales Discretas#################
#x[n]=2sin(n)
plt.figure()
frecuencia6=1/(2*np.pi)
amplitud6=2
n=np.linspace(0,20.0*np.pi*frecuencia6,100)
x7=amplitud6*np.sin(n)
plt.stem(n,x7,'c',use_line_collection=True,label='x[n]=2sin(n)')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Ejercicio 5")
plt.legend(loc='best')
plt.grid()
plt.show()
plt.figure(5)

#x[n]=2sin(4n+pi)
plt.figure()
frecuencia7=4/(2*np.pi)
amplitud7=2
fase6=np.pi
x8=amplitud7*np.sin(n+fase6)
plt.stem(n,x8,'m',use_line_collection=True,label='x[n]=2sin(4n+pi)')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Ejercicio 6")
plt.legend(loc='best')
plt.grid()
plt.show()
plt.figure(6)


#########Enunciado A2################
print('###########################################')
print('               Enunciado A2 y A3        ')

plt.subplot(2,1,1)
amplitud3=4
frecuencia3=3/np.pi
fase1=np.pi
x3=amplitud3*np.cos(2*np.pi*frecuencia3*muestras+fase1)
plt.plot(x3,label='x(t)=4cos(6t+pi)',color='purple')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Frecuencia Original")
plt.legend(loc='best')
plt.grid()
plt.show()

plt.subplot(2,1,2)
amplitud3=4
frecuencia3=8/np.pi
fase1=np.pi
x3=amplitud3*np.cos(2*np.pi*frecuencia3*muestras+fase1)
plt.plot(x3,label='x(t)=4cos(6t+pi)',color='purple')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Frecuencia Aumentada")
plt.legend(loc='best')
plt.grid()
plt.show()

################Enunciado B2##################
print('###########################################')
print('                   Enunciado B2         ')
plt.subplot(2,1,1)
frecuencia6=1/(2*np.pi)
amplitud6=2
n=np.linspace(0,20.0*np.pi*frecuencia6,100)
x7=amplitud6*np.sin(n)
plt.stem(n,x7,'c',use_line_collection=True,label='x[n]=2sin(n)')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Fase 0")
plt.legend(loc='best')
plt.grid()
plt.show()


plt.subplot(2,1,2)
frecuencia6=1/(2*np.pi)
amplitud6=2
fase7=2*np.pi
n=np.linspace(0,20.0*np.pi*frecuencia6,100)
x7=amplitud6*np.sin(n+fase7)
plt.stem(n,x7,'c',use_line_collection=True,label='x[n]=2sin(n+2pi)')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Fase 2pi")
plt.legend(loc='best')
plt.grid()
plt.show()
########################Enunciado B3########################
print('###############################################')
print('                 Enunciado B3            ')
plt.subplot(5,1,1)
frecuencia6=4
amplitud6=2
n=np.linspace(0,1.0*np.pi*frecuencia6,100)
x8=amplitud6*np.sin(n)
plt.stem(n,x8,'b',use_line_collection=True,label='x[n]=2sin(8*pi*n)')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Frecuencia Menor a 5")
plt.legend(loc='best')
plt.grid()
plt.show()

plt.subplot(5,1,2)
frecuencia8=3
n2=np.linspace(0,1.0*np.pi*frecuencia8,100)
x9=amplitud6*np.sin(n2)
plt.stem(n2,x8,'b',use_line_collection=True,label='x[n]=2sin(8*pi*n)')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Frecuencia Menor a 5")
plt.legend(loc='best')
plt.grid()
plt.show()

plt.subplot(5,1,3)
frecuencia9=5
n3=np.linspace(0,1.0*np.pi*frecuencia9,100)
x10=amplitud6*np.sin(n3)
plt.stem(n3,x10,'b',use_line_collection=True,label='x[n]=2sin(8*pi*n)')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Frecuencia Igual a 5")
plt.legend(loc='best')
plt.grid()
plt.show()

plt.subplot(5,1,4)
frecuencia10=7
n4=np.linspace(0,1.0*np.pi*frecuencia10,100)
x11=amplitud6*np.sin(n4)
plt.stem(n4,x11,'b',use_line_collection=True,label='x[n]=2sin(8*pi*n)')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Frecuencia Mayor a 5")
plt.legend(loc='best')
plt.grid()
plt.show()

plt.subplot(5,1,5)
frecuencia11=9
n5=np.linspace(0,1.0*np.pi*frecuencia11,100)
x12=amplitud6*np.sin(n5)
plt.stem(n5,x12,'b',use_line_collection=True,label='x[n]=2sin(8*pi*n)')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Frecuencia Mayor a 5")
plt.legend(loc='best')
plt.grid()
plt.show()
