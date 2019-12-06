# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 18:45:22 2019

@author: Itami
"""


import tkinter as tk
import numpy as np
import matplotlib 
matplotlib.use("TKAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg




tmin=0
tmax=0


def correct(inp):
    if inp.isdigit():
        return True
    elif inp == '':
        return True
    else :
        return False


def lcm3(nums):
    nums.sort()
    worst=nums[0]*nums[1]*nums[2]
    for x in range (nums[2],worst + 1,nums[2]):
        if x % nums[0] == 0 and x % nums[1] == 0:
            return x

def gcd(x, y):
    return x if not y else gcd(y, x % y)
 
def lcm2(x, y):
    return x * y / gcd(x, y)
    
def frecuencia():   
     nums=[int(freq.get()),int(freq2.get()),int(freq3.get())]
     num2=nums
     
     return num2


from tkinter import messagebox

def test():
    messagebox.Dialog("Ingrese un numero")

def clear():
    
    amp.set('')
    amp2.set('')
    amp3.set('')
      
    freq.set('')
    freq2.set('')
    freq3.set('')
      
    phase1.set('')
    phase2.set('')
    phase3.set('')

def prueba():
#    a=float(amp.get())
#    a2=float(amp2.get())
#    a3=float(amp3.get())
#    
#    f=float(freq.get())
#    f2=float(freq2.get())
#    f3=float(freq3.get())
#    
#    p=float(phase1.get())
#    p2=float(phase2.get())
#    p3=float(phase3.get())
    
    
    textSenal.set(amp.get()+'cos('+freq.get()+'pit+'+phase1.get()+')+'+amp2.get()+'cos('+freq2.get()+'pit+'+phase2.get()+')+'+amp3.get()+'cos('+freq3.get()+'pit+'+phase3.get()+')')
        
    temp=0                    
#    if (and == "") and ( and =="") == True :
#        fm=float(freq3.get())
#        temp=4
#        print(temp)
#    elif amp.get() and amp3.get() =="":
#        fm=int(freq2.get())
#        temp=5
#    elif amp2.get() and amp3.get() =="":
#        fm=int(freq.get())
#        temp=6
    if amp2.get()=="":
        x=int(freq.get())
        y=int(freq3.get())
        fm=lcm2(x,y)
        temp=2
    elif amp3.get()=="":
        fm=lcm2(int(freq.get()),int(freq2.get()))
        temp=3
    elif amp.get()=="":
        fm=lcm2(int(freq2.get()),int(freq3.get()))
        temp=1
    else:
        fm=lcm3(frecuencia())
        temp=7
                        
               
    if fm <= 10:
        tmax=5
    elif fm <=500:
        tmax=0.05
    else:
        tmax=0.005
    
    time=np.linspace(tmin,tmax,400)
    
    T=1/(2*fm)
    nmin=np.ceil(tmin/T)
    nmax=np.floor(tmax/T)
    n=np.arange(nmin,nmax)

    if temp==1:
        x2=float(amp2.get())*np.cos(2*np.pi*float(freq2.get())*time+float(phase2.get()))
        x3=float(amp3.get())*np.cos(2*np.pi*float(freq3.get())*time+float(phase3.get()))
        xt=x2+x3   
        x22=float(amp2.get())*np.cos(2*np.pi*float(freq2.get())*n*T+float(phase2.get()))
        x33=float(amp3.get())*np.cos(2*np.pi*float(freq3.get())*n*T+float(phase3.get()))
        xt2=x22+x33
        f=Figure(figsize=(4,3),dpi=100)
        g=Figure(figsize=(4,3),dpi=100)
        img=f.add_subplot(111) ##Una figura
        #i=interact(newTime,x=5)
        img.plot(time,xt)

    
        img2=g.add_subplot(111)
        img2.plot(n*T,xt2,'r.')
        canvas=FigureCanvasTkAgg(f,frame)# Figura se inserta dentro de la interfaz
        canvas.draw()
        canvas.get_tk_widget().place(x=150,y=400)
            
        canvas=FigureCanvasTkAgg(g,frame)# Figura se inserta dentro de la interfaz
        canvas.draw()
        canvas.get_tk_widget().place(x=600,y=400)
        clear()      
    elif temp==2:
        x1=float(amp.get())*np.cos(2*np.pi*float(freq.get())*time+float(phase1.get()))
        x3=float(amp3.get())*np.cos(2*np.pi*float(freq3.get())*time+float(phase3.get()))
        xt=x1+x3   
        x11=float(amp.get())*np.cos(2*np.pi*float(freq.get())*n*T+float(phase1.get()))
        x33=float(amp3.get())*np.cos(2*np.pi*float(freq3.get())*n*T+float(phase3.get()))
        xt2=x11+x33
        f=Figure(figsize=(4,3),dpi=100)
        g=Figure(figsize=(4,3),dpi=100)
        img=f.add_subplot(111) ##Una figura
        #i=interact(newTime,x=5)
        img.plot(time,xt)
             
             
        img2=g.add_subplot(111)
        img2.plot(n*T,xt2,'r.')
        canvas=FigureCanvasTkAgg(f,frame)# Figura se inserta dentro de la interfaz
        canvas.draw()
        canvas.get_tk_widget().place(x=150,y=400)
    
        canvas=FigureCanvasTkAgg(g,frame)# Figura se inserta dentro de la interfaz
        canvas.draw()
        canvas.get_tk_widget().place(x=600,y=400)
        clear()
             
    elif temp==3:
          
        x1=float(amp.get())*np.cos(2*np.pi*float(freq.get())*time+float(phase1.get()))
        x2=float(amp2.get())*np.cos(2*np.pi*float(freq2.get())*time+float(phase2.get()))
        xt=x1+x2
        x11=float(amp.get())*np.cos(2*np.pi*float(freq.get())*n*T+float(phase1.get()))
        x22=float(amp2.get())*np.cos(2*np.pi*float(freq2.get())*n*T+float(phase2.get()))
        xt2=x11+x22
        f=Figure(figsize=(4,3),dpi=100)
        g=Figure(figsize=(4,3),dpi=100)
        img=f.add_subplot(111) ##Una figura
        #i=interact(newTime,x=5)
        img.plot(time,xt)

        img2=g.add_subplot(111)
        img2.plot(n*T,xt2,'r.')
        canvas=FigureCanvasTkAgg(f,frame)# Figura se inserta dentro de la interfaz
        canvas.draw()
        canvas.get_tk_widget().place(x=150,y=400)
        
        canvas=FigureCanvasTkAgg(g,frame)# Figura se inserta dentro de la interfaz
        canvas.draw()
        canvas.get_tk_widget().place(x=600,y=400)
        clear()
    elif temp==4:             
        x3=float(amp3.get())*np.cos(2*np.pi*float(freq3.get())*time+float(phase3.get()))                
        xt=x3
        x33=float(amp3.get())*np.cos(2*np.pi*float(freq3.get())*n*T+float(phase3.get()))                
        xt2=x33                                                                
        f=Figure(figsize=(4,3),dpi=100)
        g=Figure(figsize=(4,3),dpi=100)
        img=f.add_subplot(111) ##Una figura
        #i=interact(newTime,x=5)
        img.plot(time,xt)                                                
        img2=g.add_subplot(111)
        img2.plot(n*T,xt2,'r.')                                                             
        canvas=FigureCanvasTkAgg(f,frame)# Figura se inserta dentro de la interfaz
        canvas.draw()
        canvas.get_tk_widget().place(x=150,y=400)
        canvas=FigureCanvasTkAgg(g,frame)# Figura se inserta dentro de la interfaz
        canvas.draw()
        canvas.get_tk_widget().place(x=600,y=400)                                                                
        clear()
    elif temp==5:
                    
        x3=float(amp2.get())*np.cos(2*np.pi*float(freq2.get())*time+float(phase2.get()))                
        xt=x3
        x33=float(amp2.get())*np.cos(2*np.pi*float(freq2.get())*n*T+float(phase2.get()))                
        xt2=x33                                                                
        f=Figure(figsize=(4,3),dpi=100)
        g=Figure(figsize=(4,3),dpi=100)
        img=f.add_subplot(111) ##Una figura
        #i=interact(newTime,x=5)
        img.plot(time,xt)                                                
        img2=g.add_subplot(111)
        img2.plot(n*T,xt2,'r.')                                                             
        canvas=FigureCanvasTkAgg(f,frame)# Figura se inserta dentro de la interfaz
        canvas.draw()
        canvas.get_tk_widget().place(x=150,y=400)
        canvas=FigureCanvasTkAgg(g,frame)# Figura se inserta dentro de la interfaz
        canvas.draw()
        canvas.get_tk_widget().place(x=600,y=400)                                                                
        clear()
    elif temp==6: 
        x3=float(amp.get())*np.cos(2*np.pi*float(freq.get())*time+float(phase1.get()))                
        xt=x3
        x33=float(amp.get())*np.cos(2*np.pi*float(freq.get())*n*T+float(phase1.get()))                
        xt2=x33                                                                
        f=Figure(figsize=(4,3),dpi=100)
        g=Figure(figsize=(4,3),dpi=100)
        img=f.add_subplot(111) ##Una figura
        #i=interact(newTime,x=5)
        img.plot(time,xt)                                                
        img2=g.add_subplot(111)
        img2.plot(n*T,xt2,'r.')                                                             
        canvas=FigureCanvasTkAgg(f,frame)# Figura se inserta dentro de la interfaz
        canvas.draw()
        canvas.get_tk_widget().place(x=150,y=400)
        canvas=FigureCanvasTkAgg(g,frame)# Figura se inserta dentro de la interfaz
        canvas.draw()
        canvas.get_tk_widget().place(x=600,y=400)                                                                
        clear()
    else:
                
        x1=float(amp.get())*np.cos(2*np.pi*float(freq.get())*time+float(phase1.get()))
        x2=float(amp2.get())*np.cos(2*np.pi*float(freq2.get())*time+float(phase2.get()))
        x3=float(amp3.get())*np.cos(2*np.pi*float(freq3.get())*time+float(phase3.get()))                
        xt=x1+x2+x3   
        x11=float(amp.get())*np.cos(2*np.pi*float(freq.get())*n*T+float(phase1.get()))
        x22=float(amp2.get())*np.cos(2*np.pi*float(freq2.get())*n*T+float(phase2.get()))
        x33=float(amp3.get())*np.cos(2*np.pi*float(freq3.get())*n*T+float(phase3.get()))                
        xt2=x11+x22+x33                                                                
        f=Figure(figsize=(4,3),dpi=100)
        g=Figure(figsize=(4,3),dpi=100)
        img=f.add_subplot(111) ##Una figura
        #i=interact(newTime,x=5)
        img.plot(time,xt)                                                
        img2=g.add_subplot(111)
        img2.plot(n*T,xt2,'r.')                                                             
        canvas=FigureCanvasTkAgg(f,frame)# Figura se inserta dentro de la interfaz
        canvas.draw()
        canvas.get_tk_widget().place(x=150,y=400)
                
        canvas=FigureCanvasTkAgg(g,frame)# Figura se inserta dentro de la interfaz
        canvas.draw()
        canvas.get_tk_widget().place(x=600,y=400)                                                                
        clear()
        
                
root=tk.Tk()

reg= root.register(correct)
root.title('Proyecto PDS')

amp=tk.StringVar()
amp2=tk.StringVar()
amp3=tk.StringVar()

freq=tk.StringVar()
freq2=tk.StringVar()
freq3=tk.StringVar()

phase1=tk.StringVar()
phase2=tk.StringVar()
phase3=tk.StringVar()

textSenal=tk.StringVar()

frame=tk.Frame(root,width=1080,height=720)
#frame.config(bg='lightblue')
frame.config(cursor="arrow")
frame.pack()

label1=tk.Label(frame,text='Universidad Técnica del Norte',fg='red',font=('Impact',16))
label1.place(x=425,y=50)


label2=tk.Label(frame,text='Fica-Citel',font=('Copperplate Gothic Bold',12))
label2.config(justify='center')

label2.place(x=515,y=80)


label3=tk.Label(frame,text='Amplitud',font=('Times New Roman',12))
label3.place(x=100,y=150)

text1=tk.Entry(frame,textvariable=amp )
text1.place(x=200,y=150)
text1.config(validate="key",validatecommand=(reg,"%P"))


label4=tk.Label(frame,text='Frecuencia',font=('Times New Roman',12))
label4.place(x=100,y=180)

text2=tk.Entry(frame,textvariable=freq)
text2.place(x=200,y=180)
text2.config(validate="key",validatecommand=(reg,"%P"))

label5=tk.Label(frame,text='Fase',font=('Times New Roman',12))
label5.place(x=100,y=210)

text3=tk.Entry(frame,textvariable=phase1)
text3.place(x=200,y=210)
text3.config(validate="key",validatecommand=(reg,"%P"))

label6=tk.Label(frame,text='Amplitud 2',font=('Times New Roman',12))
label6.place(x=400,y=150)
text4=tk.Entry(frame,textvariable=amp2)
text4.place(x=500,y=150)
text4.config(validate="key",validatecommand=(reg,"%P"))

label7=tk.Label(frame,text='Frecuencia 2',font=('Times New Roman',12))
label7.place(x=400,y=180)
text5=tk.Entry(frame,textvariable=freq2)
text5.place(x=500,y=180)
text5.config(validate="key",validatecommand=(reg,"%P"))

label8=tk.Label(frame,text='Fase 2',font=('Times New Roman',12))
label8.place(x=400,y=210)
text6=tk.Entry(frame,textvariable=phase2)
text6.place(x=500,y=210)
text6.config(validate="key",validatecommand=(reg,"%P"))


label9=tk.Label(frame,text='Amplitud 3',font=('Times New Roman',12))
label9.place(x=700,y=150)
text7=tk.Entry(frame,textvariable=amp3)
text7.place(x=800,y=150)
text7.config(validate="key",validatecommand=(reg,"%P"))

label10=tk.Label(frame,text='Frecuencia 3',font=('Times New Roman',12))
label10.place(x=700,y=180)
text8=tk.Entry(frame,textvariable=freq3)
text8.place(x=800,y=180)
text8.config(validate="key",validatecommand=(reg,"%P"))

label11=tk.Label(frame,text='Fase 3',font=('Times New Roman',12))
label11.place(x=700,y=210)
text9=tk.Entry(frame,textvariable=phase3)
text9.place(x=800,y=210)
text9.config(validate="key",validatecommand=(reg,"%P"))

label12=tk.Label(frame,text='Señal Generada:',font=('Rockwell',12))
label12.place(x=325,y=280)

label13=tk.Label(frame,text='Señal Original',font=('Rockwell',12))
label13.place(x=250,y=350)

label14=tk.Label(frame,text='Señal Muestreada',font=('Rockwell',12))
label14.place(x=700,y=350)

btnMuestrear=tk.Button(frame, text='Muestrear',command=prueba,font=('Rockwell',12))
btnMuestrear.place(x=900,y=278)

Senal=tk.Label(frame,textvariable=textSenal)
Senal.place(x=500,y=280)



root.mainloop()
