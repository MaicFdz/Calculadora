

import tkinter as tk
from tkinter import Tk, ttk, font, PhotoImage, Label, StringVar, Button, Menu, Entry
from tkinter import END

#-------------------------------------------------------------------------------
def cargarWidgetsIniciales(self_Ventana, self_ventanita):

 def suma():
  if self_Ventana.Master.valorPrevio == 'vacio':
   self_Ventana.Master.valorPrevio=self_ventanita.entrada.get()  
  self_Ventana.Master.operacionSeleccionada='suma'
  self_ventanita.cajaEntrada.delete(0, END)

 def resta():
  if self_Ventana.Master.valorPrevio == 'vacio':
   self_Ventana.Master.valorPrevio=self_ventanita.entrada.get()  
  self_Ventana.Master.operacionSeleccionada='resta'
  self_ventanita.cajaEntrada.delete(0, END)

 def resolver():

  if self_Ventana.Master.operacionSeleccionada=='suma':
   retorno=self_Ventana.Master.valorPrevio=self_Ventana.Master.funciones.suma(self_Ventana.Master, self_Ventana.Master.valorPrevio, self_ventanita.entrada.get())

  elif self_Ventana.Master.operacionSeleccionada=='resta':
   retorno=self_Ventana.Master.valorPrevio=self_Ventana.Master.funciones.resta(self_Ventana.Master, self_Ventana.Master.valorPrevio, self_ventanita.entrada.get())

  self_ventanita.cajaEntrada.delete(0, END)
  self_ventanita.cajaEntrada.insert(0, retorno)

 def sinFuncion():
  pass

 def boton0():
  self_ventanita.cajaEntrada.insert(END, '0')

 def boton1():
  self_ventanita.cajaEntrada.insert(END, '1')

 def boton2():
  self_ventanita.cajaEntrada.insert(END, '2')

 def boton3():
  self_ventanita.cajaEntrada.insert(END, '3')

 def boton4():
  self_ventanita.cajaEntrada.insert(END, '4')

 def boton5():
  self_ventanita.cajaEntrada.insert(END, '5')

 def boton6():
  self_ventanita.cajaEntrada.insert(END, '6')

 def boton7():
  self_ventanita.cajaEntrada.insert(END, '7')

 def boton8():
  self_ventanita.cajaEntrada.insert(END, '8')

 def boton9():
  self_ventanita.cajaEntrada.insert(END, '9')

#----------------------------------------------------------------------

 self_ventanita.barramenu=Menu(self_ventanita)
 self_ventanita['menu'] = self_ventanita.barramenu

 self_ventanita.verMenu=Menu(self_ventanita.barramenu, tearoff=0)
# self_ventanita.bibliotecaMenu.add_command(label="Cambiar", command=cambiarLibro, accelerator='Ctrl+A')
 self_ventanita.edicionMenu=Menu(self_ventanita.barramenu, tearoff=0)
# self_ventanita.consolaMenu.add_command(label='Interrumpir ejecucion', command=interrumpirI, accelerator='Ctrl+C')
# self_ventanita.consolaMenu.add_command(label='Limpiar', command=limpiarConsola, accelerator='Ctrl+L')
# self_ventanita.ejemploMenu=Menu(self_ventanita.barramenu, tearoff=0) 
# self_ventanita.ejemploMenu.add_command(label='Reproducir', command=reproducir, accelerator='Ctrl+R')
# self_ventanita.ejemploMenu.add_command(label='Editar', command=editar, accelerator='Ctrl+E')
# self_ventanita.ejemploMenu.add_command(label='Guardar consejo', command=guardarConsejo, accelerator='Ctrl+G')
 self_ventanita.ayudaMenu=Menu(self_ventanita.barramenu, tearoff=0)
# self_ventanita.ayudaMenu.add_command(label="Sobre Memo")

 self_ventanita.barramenu.add_cascade(menu=self_ventanita.verMenu, label='Ver')
 self_ventanita.barramenu.add_cascade(menu=self_ventanita.edicionMenu, label='Edición')
 self_ventanita.barramenu.add_cascade(menu=self_ventanita.ayudaMenu, label='Ayuda')

#-------------------------------------------------------------------------------

 self_ventanita.entrada=StringVar()
 self_ventanita.cajaEntrada=Entry(self_ventanita, textvariable=self_ventanita.entrada)
 self_ventanita.cajaEntrada.place(x=11, y=10)

#-------------------------------------------------------------------------------

 self_ventanita.boton7=Button(self_ventanita, text='7', command=boton7, foreground=self_Ventana.colorLetrasBoton, background=self_Ventana.colorFondoBoton, width=4, height=1)
 self_ventanita.boton7.pack()
 self_ventanita.boton7.place(x=11, y=133)

 self_ventanita.boton8=Button(self_ventanita, text='8', command=boton8, foreground=self_Ventana.colorLetrasBoton, background=self_Ventana.colorFondoBoton, width=4, height=1)
 self_ventanita.boton8.pack()
 self_ventanita.boton8.place(x=51, y=133)

 self_ventanita.boton9=Button(self_ventanita, text='9', command=boton9, foreground=self_Ventana.colorLetrasBoton, background=self_Ventana.colorFondoBoton, width=4, height=1)
 self_ventanita.boton9.pack()
 self_ventanita.boton9.place(x=91, y=133)

# self_ventanita.botonDividir=Button(self_ventanita, text='/', command=sinFuncion, foreground=self_Ventana.colorLetrasBoton, background=self_Ventana.colorFondoBoton, width=4, height=1)
# self_ventanita.botonDividir.pack()
# self_ventanita.botonDividir.place(x=131, y=133)

#-------------------------------------------------------------------------------

 self_ventanita.boton4=Button(self_ventanita, text='4', command=boton4, foreground=self_Ventana.colorLetrasBoton, background=self_Ventana.colorFondoBoton, width=4, height=1)
 self_ventanita.boton4.pack()
 self_ventanita.boton4.place(x=11, y=163)

 self_ventanita.boton5=Button(self_ventanita, text='5', command=boton5, foreground=self_Ventana.colorLetrasBoton, background=self_Ventana.colorFondoBoton, width=4, height=1)
 self_ventanita.boton5.pack()
 self_ventanita.boton5.place(x=51, y=163)

 self_ventanita.boton6=Button(self_ventanita, text='6', command=boton6, foreground=self_Ventana.colorLetrasBoton, background=self_Ventana.colorFondoBoton, width=4, height=1)
 self_ventanita.boton6.pack()
 self_ventanita.boton6.place(x=91, y=163)

# self_ventanita.botonMultiplicacion=Button(self_ventanita, text='*', command=sinFuncion, foreground=self_Ventana.colorLetrasBoton, background=self_Ventana.colorFondoBoton, width=4, height=1)
# self_ventanita.botonMultiplicacion.pack()
# self_ventanita.botonMultiplicacion.place(x=131, y=163)

#-------------------------------------------------------------------------------

 self_ventanita.boton1=Button(self_ventanita, text='1', command=boton1, foreground=self_Ventana.colorLetrasBoton, background=self_Ventana.colorFondoBoton, width=4, height=1)
 self_ventanita.boton1.pack()
 self_ventanita.boton1.place(x=11, y=193)

 self_ventanita.boton2=Button(self_ventanita, text='2', command=boton2, foreground=self_Ventana.colorLetrasBoton, background=self_Ventana.colorFondoBoton, width=4, height=1)
 self_ventanita.boton2.pack()
 self_ventanita.boton2.place(x=51, y=193)

 self_ventanita.boton3=Button(self_ventanita, text='3', command=boton3, foreground=self_Ventana.colorLetrasBoton, background=self_Ventana.colorFondoBoton, width=4, height=1)
 self_ventanita.boton3.pack()
 self_ventanita.boton3.place(x=91, y=193)

 self_ventanita.botonResta=Button(self_ventanita, text='-', command=resta, foreground=self_Ventana.colorLetrasBoton, background=self_Ventana.colorFondoBoton, width=4, height=1)
 self_ventanita.botonResta.pack()
 self_ventanita.botonResta.place(x=131, y=193)

 self_ventanita.botonResta=Button(self_ventanita, text='=', command=resolver, foreground=self_Ventana.colorLetrasBoton, background=self_Ventana.colorFondoBoton, width=4, height=1)
 self_ventanita.botonResta.pack()
 self_ventanita.botonResta.place(x=171, y=193)

#-------------------------------------------------------------------------------

 self_ventanita.boton0=Button(self_ventanita, text='0', command=boton0, foreground=self_Ventana.colorLetrasBoton, background=self_Ventana.colorFondoBoton, width=4, height=1)
 self_ventanita.boton0.pack()
 self_ventanita.boton0.place(x=11, y=223)

 self_ventanita.botonSuma=Button(self_ventanita, text='+', command=suma, foreground=self_Ventana.colorLetrasBoton, background=self_Ventana.colorFondoBoton, width=4, height=1)
 self_ventanita.botonSuma.pack()
 self_ventanita.botonSuma.place(x=131, y=223)

#-------------------------------------------------------------------------------
def reemplazarContenidoWidgets_deDivisa(self_Ventana):
 pass