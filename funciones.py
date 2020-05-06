


import os
from os import listdir
from Modulos import Mod_cargaDeConfiguraciones

def suma(Master, valor1, valor2):
 valor1=int(valor1)
 valor2=int(valor2)
 return(Master.funcionesC.suma(valor1, valor2))

def resta(Master, valor1, valor2):
 valor1=int(valor1)
 valor2=int(valor2)
 return(Master.funcionesC.resta(valor1, valor2))

def multiplicacion(Master, valor1, valor2):
 valor1=int(valor1)
 valor2=int(valor2)
 return(Master.funcionesC.multiplicacion(valor1, valor2))

def division(Master, valor1, valor2):
 valor1=int(valor1)
 valor2=int(valor2)
 return(Master.funcionesC.division(valor1, valor2))
