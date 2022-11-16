from tkinter import ttk
from tkinter import *
from Desktop_Alert import Alert
import sys

class notify_window:
    def __init__(self,Windowprincipal):
        self.window = Windowprincipal
        self.window.title("Desktop_Alert")
        frameAlerta=LabelFrame(self.window, text = 'Define tu alerta')
        #columspan son columnas que quiero que tenga vacias
        #pady indica que quiero pixeles en el row vacios
        frameAlerta.grid(row=0,column = 0, columnspan = 1,pady=20)

        LabelAlerta=Label(frameAlerta, text = 'Ingresa el texto de tu alerta').grid(row= 1,column = 0)
        self.textAlerta=Entry(frameAlerta)
        self.textAlerta.focus()
        self.textAlerta.grid(row=2,column = 0)
        
        Labeltiempo=Label(frameAlerta, text = 'Notificación de la Alerta en minutos').grid(row= 3,column = 0,columnspan = 2)
        self.tiempoAlerta=Entry(frameAlerta)
        self.tiempoAlerta.grid(row=4,column = 0)
        
        Labelfrecuencia=Label(frameAlerta, text = 'Frecuencia de la notificación').grid(row= 5,column = 0)
        self.frecAlerta=Entry(frameAlerta)
        self.frecAlerta.grid(row=6,column = 0)

        ttk.Button(frameAlerta, text='Registrar',command=self.set_Alerta).grid(row=10,column=0, columnspan = 2,pady=10)#,pady = 10,sticky=W+E)
        ttk.Button(frameAlerta, text='Salir',command=Windowprincipal.destroy).grid(row=10,column=1, columnspan = 2,pady=10)
        self.Labelnotify=Label(text='',fg='red')
        self.Labelnotify.grid(row=11,column = 0,columnspan=2,sticky=W+E)
        
    def blank_validation(self):
        return len(self.textAlerta.get()) !=0 and len(self.tiempoAlerta.get()) !=0 and len(self.frecAlerta.get()) !=0

    def set_Alerta(self):
        def_Alert=Alert()
        if self.blank_validation():
            tiempoAlerta=int(self.tiempoAlerta.get())*60
            frecAlerta=int(self.frecAlerta.get())
            #self.Labelnotify['text']='Alerta establecida para notificarte en {} segudos'.format(self.tiempoAlerta.get())
            Nueva_Alerta = def_Alert.Alerta(self.textAlerta.get(),tiempoAlerta,frecAlerta) 
            self.textAlerta.delete(0,END)
            self.tiempoAlerta.delete(0,END)
            self.frecAlerta.delete(0,END)
            
        else:
            self.Labelnotify['text']=('No puedes dejar espacions en blanco')

    
if __name__==('__main__'):
    
    Windowprincipal = Tk()
    apllication=notify_window(Windowprincipal)
    Windowprincipal.mainloop()
