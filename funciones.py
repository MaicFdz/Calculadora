


import os
from os import listdir
from Modulos import Mod_cargaDeConfiguraciones

def suma(Master, valor1, valor2):
 valor1=int(valor1)
 valor2=int(valor2)
 return(Master.funcionesC.calculaSuma(valor1, valor2))

def resta(Master, valor1, valor2):
 valor1=int(valor1)
 valor2=int(valor2)
 return(Master.funcionesC.calculaResta(valor1, valor2))
