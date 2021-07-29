#!/usr/bin/env python
# coding: utf-8

# In[2]:


# SECCIÓN 1. Datos, Notas del autor y Bibliografía. (Recomendado leer antes de correr por primera vez el programa.)

# DATOS.

# Autor: Uriel Benítez Ordaz.
# Título: Ingeniero Petrolero.
# Correo electrónico: u.r12@hotmail.com
# Perfil de linked In: www.linkedin.com/in/uriel-benitez-ordaz-92aa371a9 (Copiar en la barra de direcciones de tu computador)
# Fecha de publicación: 25 / 05 / 2021

# NOTAS.

# Nota 1

# Este trabajo fue desarrollado usando Jupyter Notebook dentro el entorno de trabajo Anaconda navigator.

# Nota 2

# Durante el desarrollo de este programa, fueron necesitadas librerías externas a las ya implementadas en Python nativo,
# por lo que es posible que se presenten errores de ejecución si en tu computadora no tienes instalada alguna de estas al 
# momento de correr el programa.

# Hasta el momento, en las pruebas que se realizaron en diferentes computadoras, solo la librería llamada OpenCV causo problemas 
# de ejecución al no venir instalada por default en Python nativo.

# Este problema se soluciona al instalar dicha librería en tu computadora, para ello, basta con escribir el siguiente comando:
# pip install opencv-python en la consola de tu computadora abriéndola como administrador, esto en caso de estar ejecutando
# Python desde tu consola, en caso de estar ocupando Jupyter Notebook lo deberías hacer en CMD.exe Prompt desde el entorno de
# trabajo de Anaconda Navigator.

# Nota 3

# Para el correcto funcionamiento del software es necesario que ubique la carpeta TENSION Y ANGULO DE CONTACTO en la misma
# dirección en donde guardo los archivos de instalación de Anaconda Navigator

# Nota 4

# Este trabajo es aún un proyecto en desarrollo, lo que quiere decir que se seguirá trabajando en él para implementarle
# mejoras, mejoras en la interfaz gráfica, mejoras en el funcionamiento interno, mejoras en la lectura y escrituras de archivos,
# y mucho más, pero al ser un proyecto en desarrollo se debe de entender que pueden presentarse algunos problemas de código 
# durante la ejecución del mismo, sin embargo, estos problemas no deberían de ser frecuentes o incluso no deberían de 
# presentarse si se sigue el flujo de trabajo explicado en el manual del software.

# Mencionado lo anterior se debe de aclarar que esta versión publica número 1 del software ya es una versión totalmente estable 
# y funcional.

# Nota 5

# Este trabajo fue creado bajo la filosofía de software libre, por lo que en concreto puedes, (1) ejecutar el programa, 
# (2) estudiar y modificar el código fuente del programa, (3) redistribuir copias exactas y (4) distribuir versiones 
# modificadas.

# En caso de distribuir versiones modificadas, se pide amablemente se comparta el código fuente con el autor, esto para evaluar  
# su implementación a la versión original y de esta manera todos los implicados se vean beneficiados.

# Nota 6

# Espero profundamente que este trabajo sea de utilidad para todo aquel que necesite un método sencillo y confiable para
# calcular la tensión interfacial, tensión superficial y ángulo de contacto de una muestra de fluido.

# Quedo total y completamente al tanto a través de mi contacto de cualquier duda, sugerencia y crítica hacia este trabajo.

# BIBLIOGRAFÍA

# Método

# D. Misak, M. "Equations for Determining 1/H Versus S Values for Interfacial Tension Calculations by the Pendent Drop Method.
# " Halliburton Services, Duncan, Oklahoma.

# Imagenes

# TensionEjemplo1: D. Misak, M. "Equations for Determining 1/H Versus S Values for Interfacial Tension Calculations by the Pendent Drop Method."  (p.8) Halliburton Services, Duncan, Oklahoma.
# TensionEjemplo2: https://www.researchgate.net/figure/Figura-31-Angulos-de-contacto-A-y-C-y-gotas-colgantes-B-y-D-usados-para-calcular_fig1_283908842
# TensionEjemplo3: https://www.researchgate.net/figure/Figura-31-Angulos-de-contacto-A-y-C-y-gotas-colgantes-B-y-D-usados-para-calcular_fig1_283908842

# AnguloEjemplo1: https://www.researchgate.net/figure/Figura-63-Esquema-del-angulo-de-contacto-El-angulo-de-contacto-es-un-parametro-que_fig4_334448714
# AnguloEjemplo2: https://www.researchgate.net/figure/Figura-31-Angulos-de-contacto-A-y-C-y-gotas-colgantes-B-y-D-usados-para-calcular_fig1_283908842  
# AnguloEjemplo3: https://www.researchgate.net/figure/Figura-31-Angulos-de-contacto-A-y-C-y-gotas-colgantes-B-y-D-usados-para-calcular_fig1_283908842


# SECCIÓN 2. Importamos librerias necesarias. -------------------------------------------------------

import tkinter
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import pyplot as plt
import numpy as np
from skimage import io
import cv2
from matplotlib.widgets import Cursor
import pandas as pd
import math
from sympy import *
import matplotlib.patches as patches

# SECCIÓN 3. Funciones de los avisos de error -------------------------------------------------------

#Función de aviso de introducción de texto.

def textoIntroducido():
    messagebox.showwarning('Advertencia', 'Dato introducido de tipo texto o Dato omitido.\nSe recomienda verificar los datos introducidos.')

# Función de aviso de dato omitido.

def datoOmitido():
    messagebox.showwarning('Advertencia', 'Dato omitido.\nSe recomienda verificar los datos introducidos.')

# Función de aviso de que dSPx es mayor que dEPx.

def dSPxMayorQdEPx():
    messagebox.showwarning('Advertencia', 'El Ds en Px es mayor que el De en px.\n\nEscenario imposible del experimento, se recomienda verificar la coherencia de ambos')

# Función de aviso de que S esta fuera del límite inferior permitido.

def SInvalida():
    messagebox.showwarning('Advertencia', 'El valor de S esta fuera del límite inferior permitido.\n\nSe recomienda verificar la coherencia del Ds y De')

# Función de apoyo para la TIF en caso de error en la ejecución.

def TIFError():
        tIF = 'Error :('
        return VarAuxTIF.set(tIF)

# Función de apoyo en caso de error en la medición de De.

def DeError():
    vDe = 'Error :('
    return varAuxDe.set(vDe)

# Función de apoyo en caso de error en la medición de Ds.

def DsError():
    vDs = 'Error :('
    return varAuxDs.set(vDs)

# Función de apoyo en caso de error en la medición de Dt.

def DtError():
    vDt = 'Error :('
    return varAuxDt.set(vDt)

# Función de error en el caso de botón de color presionado cuando no hay una imagen.

def errorNoImagen():
    messagebox.showwarning('Advertencia', 'No puede realizar esta acción sin antes abrir una imagen.')

# Función de error en el caso de que el usuario quiera dibujar sobrepuesta dos veces una misma línea.
    
def errorLineaSobrePuesta():
    messagebox.showwarning('Advertencia', 'No puede sobreponer líneas. Si quiere sobrescribir un diámetro asegúrese de que el anterior sea borrado.')
    
# Función de error en el caso de que el usuario quiera dibujar sobrepuesta dos veces una misma línea.
    
def errorLineaSobrePuestaA():
    messagebox.showwarning('Advertencia', 'No puede sobreponer puntos. Si quiere sobrescribir un punto asegurese de que el anterior sea borrado.')

# Funcion de error en caso de que el usuario quiera dibujar dos veces seguidas la fecha.

def errorLineaSobrePuestaA():
    messagebox.showwarning('Advertencia', 'No puede sobreponer puntos. Si quiere sobrescribir un punto asegurese de que el anterior sea borrado.')
    
# Funcion de error en caso de que el usuario precione dos veces seguidas el boton de borrar.

def errorTextoSobrePuestaA():
    messagebox.showwarning('Advertencia', 'No puede sobreponer texto. Si quiere sobrescribir un texto asegúrese de que el anterior sea borrado.')

# Función de error en caso de que el usuario presione dos veces seguidas el botón de borrar.

def errorDobleBorrar():
    messagebox.showwarning('Advertencia', 'No puede borrar una línea que no ha sido dibujada.')

# Función de error en caso de que el usuario presione dos veces seguidas el botón de borrar.

def errorDobleBorrarA():
    messagebox.showwarning('Advertencia', 'No puede borrar un punto que no ha sido dibujado.')

# Función en caso de que el usuario presione el botón de borrar y no haya nada que borrar.

def errorBorrarVacio():
    messagebox.showwarning('Advertencia', 'No puede borrar un dato si no lo ha aceptado antes.')
    
# Función de error en el caso de que el usuario quiera aceptar un análisis sin haber terminado de medir la imagen.

def errorAnalisisIncompleto():
    messagebox.showwarning('Advertencia', 'No puede aceptar un análisis si aún no ha terminado de medir la imagen, o no están dibujadas todas las líneas de medida.')

# Función de error en el caso de que el usuario quiera aceptar un análisis sin haber terminado de medir la imagen.

def errorAnalisisIncompletoA():
    messagebox.showwarning('Advertencia', 'No puede aceptar un análisis si aún no ha terminado de dibujar los puntos superior e inferior sobre la imagen.')
    
# Función de error en el caso de que el usuario quiera aceptar un análisis sin haber terminado de medir la imagen.

def errorAnalisisIncompletoRA():
    messagebox.showwarning('Advertencia', 'No puede aceptar un análisis si aún no ha terminado de dibujar el ángulo izquierdo y derecho sobre la imagen.')

# Función de error en caso de que el usuario quiera aceptar un análisis sin antes haber borrado el anterior análisis.

def errorDobleAnalisis():
    messagebox.showwarning('Advertencia', 'No puede aceptar un análisis si no ha borrado el análisis anterior.')
    
# Función de error en caso de que el usuario quiera limpiar un análisis que no ha sido aceptado.

def errorLimpiarAnalisisInexistente():
    messagebox.showwarning('Advertencia', 'No puede limpiar un análisis si antes no ha aceptado uno.')

# Función de error en caso de que el usuario quiera rotar la imagen sin antes limpiar el análisis actual.

def errorRotarConAnalisis():
    messagebox.showwarning('Advertencia', 'No puede rotar una imagen si no ha limpiado el análisis actual.')
    
# Función de error en caso de que el usuario quiera medir la imagen sin limpiar el análisis actual.

def errorMedirBorrarConAnalisis():
    messagebox.showwarning('Advertencia', 'No puede realizar esta acción si no ha limpiado el análisis actual.')

# Función de error en caso de que el usuario quiera guardar una lectura y el archivo .csv esté abierto

def errorArchivoCSVAbiertoT():
    messagebox.showwarning('Advertencia', 'No puede realizar esta acción mientras que el archivo TensionOutPut.csv esté abierto.')

# Función de error en caso de que el usuario quiera guardar una lectura y en archivo .csv esté abierto

def errorArchivoCSVAbiertoA():
    messagebox.showwarning('Advertencia', 'No puede realizar esta acción mientras que el archivo AnguloOutPut.csv esté abierto.')

# Función de advertencia si realmente quiere limpiar todas las lecturas del archivo .csv de tensión

def advertenciaLimpiarCSVT():
    return(messagebox.askyesno('Advertencia', 'Esta acción limpiara todas las lecturas del archivo TensionOutPut.csv. ¿Seguro que quiere continuar?'))
  
# Función de advertencia si realmente quiere limpiar todos las lecturas del archivo .csv de ángulo.

def advertenciaLimpiarCSVA():
    return(messagebox.askyesno('Advertencia', 'Esta acción limpiara todas las lecturas del archivo AnguloOutPut.csv. ¿Seguro que quiere continuar?'))

#SECCIÓN 4. Funciones de los botones TIF tab. ------------------------------------------------------

# Función del botón Calcular TIF.

dTPx = None
dTCm = None
dEPx = None
dSPx = None
dWater = None
dOil = None
tIFmin = None
tIFmax = None
tIFM = None
tIFerror = None
tIFAlen = None

def calcularTIF():
    
    while True:
        
        global dTPx
        global dTCm
        global dEPx
        global dSPx
        global dWater
        global dOil
        
        dTPx = entrydTPx.get() 
        dTCm = entrydTCm.get()
        dEPx = entrydEPx.get()
        dSPx = entrydSPx.get()
        dWater = entrydWater.get()
        dOil = entrydOil.get()

        try:
            
            dTPx = abs(int(dTPx))
            dTCm = abs(float(dTCm))
            dEPx = abs(int(dEPx))
            dSPx = abs(int(dSPx))
            dWater = abs(float(dWater))
            dOil = abs(float(dOil))

        except ValueError:
            TIFError()
            textoIntroducido()
            break

        if dSPx <= dEPx:
            
            tIFR = []
            
            dTPxR = [dTPx - 2, dTPx - 1, dTPx, dTPx + 1, dTPx + 2]
            dEPxR = [dEPx - 2, dEPx - 1, dEPx, dEPx + 1, dEPx + 2]
            dSPxR = [dSPx - 2, dSPx - 1, dSPx, dSPx + 1, dSPx + 2]
            
            for i in dTPxR: 
            
                fConver = dTCm / i
                dECm = dEPx * fConver
                sP = dSPx / dEPx 
                g = 980
                dD = abs(dWater - dOil)

                if sP < 0.3:
                    SInvalida()
                    TIFError()
                    break

                elif sP >= 0.3 and sP <= 0.4:
                    iH = (0.34074 / sP ** (2.52303)) + (123.9495 * sP ** (5)) - (72.82991 * sP ** (4)) + (0.0132 * sP ** (3)) - (3.3821 * sP ** (2)) + (5.52969 * sP) - (1.0726)

                elif sP > 0.4 and sP <= 0.46:
                    iH = (0.3272 / sP ** (2.56651)) - (0.97553 * sP ** (2)) + (0.84059 * sP) - (0.18069)

                elif sP > 0.46 and sP <= 0.59:
                    iH = (0.31968 / sP ** (2.59725)) - (0.46898 * sP ** (2)) + (0.50059 * sP) - (0.13261)

                elif sP > 0.59 and sP <= 0.68: 
                    iH = (0.31522 / sP ** (2.62435)) - (0.11714 * sP ** (2)) + (0.15756 * sP) - (0.05285)

                elif sP > 0.68 and sP <= 0.9:
                    iH = (0.31345 / sP ** (2.64267)) - (0.09155 * sP ** (2)) + (0.14701 * sP) - (0.05877)

                else:
                    iH = (0.30715 / sP ** (2.84636)) - (0.69116 * sP ** (3)) + (1.08315 * sP ** (2)) - (0.18341 * sP) - (0.2097)
                
                tIF = round(((dD) * (g) * (dECm ** 2)) * (iH), 3)
                tIFR.append(tIF)
        
            for i in dEPxR: 
            
                fConver = dTCm / dTPx
                dECm = i * fConver
                sP = dSPx / dEPx 
                g = 980
                dD = abs(dWater - dOil) 

                if sP < 0.3:
                    SInvalida()
                    TIFError()
                    break
                
                elif sP >= 0.3 and sP <= 0.4:
                    sP = dSPx / i
                    iH = (0.34074 / sP ** (2.52303)) + (123.9495 * sP ** (5)) - (72.82991 * sP ** (4)) + (0.0132 * sP ** (3)) - (3.3821 * sP ** (2)) + (5.52969 * sP) - (1.0726)

                elif sP > 0.4 and sP <= 0.46:
                    sP = dSPx / i
                    iH = (0.3272 / sP ** (2.56651)) - (0.97553 * sP ** (2)) + (0.84059 * sP) - (0.18069)

                elif sP > 0.46 and sP <= 0.59:
                    sP = dSPx / i
                    iH = (0.31968 / sP ** (2.59725)) - (0.46898 * sP ** (2)) + (0.50059 * sP) - (0.13261)

                elif sP > 0.59 and sP <= 0.68:
                    sP = dSPx / i
                    iH = (0.31522 / sP ** (2.62435)) - (0.11714 * sP ** (2)) + (0.15756 * sP) - (0.05285)

                elif sP > 0.68 and sP <= 0.9:
                    sP = dSPx / i
                    iH = (0.31345 / sP ** (2.64267)) - (0.09155 * sP ** (2)) + (0.14701 * sP) - (0.05877)

                else:
                    sP = dSPx / i
                    iH = (0.30715 / sP ** (2.84636)) - (0.69116 * sP ** (3)) + (1.08315 * sP ** (2)) - (0.18341 * sP) - (0.2097)

                tIF = round(((dD) * (g) * (dECm ** 2)) * (iH), 3)
                tIFR.append(tIF)
        
            for i in dSPxR:

                fConver = dTCm / dTPx
                dECm = dEPx * fConver
                sP = dSPx / dEPx
                g = 980
                dD = abs(dWater - dOil)

                if sP < 0.3:
                    SInvalida()
                    TIFError()
                    break

                elif sP >= 0.3 and sP <= 0.4:
                    sP = i / dEPx
                    iH = (0.34074 / sP ** (2.52303)) + (123.9495 * sP ** (5)) - (72.82991 * sP ** (4)) + (0.0132 * sP ** (3)) - (3.3821 * sP ** (2)) + (5.52969 * sP) - (1.0726)

                elif sP > 0.4 and sP <= 0.46:
                    sP = i / dEPx
                    iH = (0.3272 / sP ** (2.56651)) - (0.97553 * sP ** (2)) + (0.84059 * sP) - (0.18069)

                elif sP > 0.46 and sP <= 0.59:
                    sP = i / dEPx
                    iH = (0.31968 / sP ** (2.59725)) - (0.46898 * sP ** (2)) + (0.50059 * sP) - (0.13261)

                elif sP > 0.59 and sP <= 0.68:
                    sP = i / dEPx
                    iH = (0.31522 / sP ** (2.62435)) - (0.11714 * sP ** (2)) + (0.15756 * sP) - (0.05285)

                elif sP > 0.68 and sP <= 0.9:
                    sP = i / dEPx
                    iH = (0.31345 / sP ** (2.64267)) - (0.09155 * sP ** (2)) + (0.14701 * sP) - (0.05877)

                else:
                    sP = i / dEPx
                    iH = (0.30715 / sP ** (2.84636)) - (0.69116 * sP ** (3)) + (1.08315 * sP ** (2)) - (0.18341 * sP) - (0.2097)

                tIF = round(((dD) * (g) * (dECm ** 2)) * (iH), 4)
                tIFR.append(tIF)
            
            tIFA = np.array(tIFR)
            global tIFAlen
            tIFAlen = len(tIFA)
            global tIFmin
            tIFmin = tIFA.min()
            global tIFmax
            tIFmax = tIFA.max()
            global tIFM
            tIFM = round(tIFA.mean(), 4)
            global tIFerror
            tIFerror = round(((tIFM - tIFmin) + abs(tIFM - tIFmax)) / 2, 4)
            return VarAuxTIF.set(tIFM)

        else:
            dSPxMayorQdEPx()
            TIFError()
            break

            
# Función del botón Generar Archivo .csv.

def generarArchivo():
    
    SiNoT = advertenciaLimpiarCSVT()
    
    if SiNoT == True:
        
        columnas = pd.DataFrame(columns = ['Nombre de la muestra', 'Angulo de rote (grados)', 'De (Px)', 'Ds (Px)', 'Dt (Px)', 'Dt (Cm)', 'dWater (gr/cm3)', 'dOil (gr/cm3)', 'TIF (din/cm2)', 'Numero de Corridas', 'TIF Minima', 'TIF Maxima', 'Error'])

        try:
            columnas.to_csv('TensionOutPut.csv', index = False, mode = 'w' )

        except PermissionError:
            errorArchivoCSVAbiertoT()
    else:
        
        pass
    
# Función del botón Limpiar Resumen TIF.
    
def limpiarResumenTIF():
    
    EntryNombreMuestraRTIF11.delete(0, 'end')
    EntryAnguloMuestraRTIF12.delete(0, 'end')
    EntryDeRTIF13.delete(0, 'end')
    EntryDsRTIF14.delete(0, 'end')
    EntryDtRTIF15.delete(0, 'end')
    EntryDtcmRTIF16.delete(0, 'end')
    EntryDwRTIF17.delete(0, 'end')
    EntryDoRTIF18.delete(0, 'end')
    EntrytifRTIF19.delete(0, 'end')
    EntryNCRTIF110.delete(0, 'end')
    EntrytifmRTIF111.delete(0, 'end')
    EntrytifMRTIF112.delete(0, 'end')
    EntrytifERTIF113.delete(0, 'end')
    
    EntryNombreMuestraRTIF21.delete(0, 'end')
    EntryAnguloMuestraRTIF22.delete(0, 'end')
    EntryDeRTIF23.delete(0, 'end')
    EntryDsRTIF24.delete(0, 'end')
    EntryDtRTIF25.delete(0, 'end')
    EntryDtcmRTIF26.delete(0, 'end')
    EntryDwRTIF27.delete(0, 'end')
    EntryDoRTIF28.delete(0, 'end')
    EntrytifRTIF29.delete(0, 'end')
    EntryNCRTIF210.delete(0, 'end')
    EntrytifmRTIF211.delete(0, 'end')
    EntrytifMRTIF212.delete(0, 'end')
    EntrytifERTIF213.delete(0, 'end')
    
    EntryNombreMuestraRTIF31.delete(0, 'end')
    EntryAnguloMuestraRTIF32.delete(0, 'end')
    EntryDeRTIF33.delete(0, 'end')
    EntryDsRTIF34.delete(0, 'end')
    EntryDtRTIF35.delete(0, 'end')
    EntryDtcmRTIF36.delete(0, 'end')
    EntryDwRTIF37.delete(0, 'end')
    EntryDoRTIF38.delete(0, 'end')
    EntrytifRTIF39.delete(0, 'end')
    EntryNCRTIF310.delete(0, 'end')
    EntrytifmRTIF311.delete(0, 'end')
    EntrytifMRTIF312.delete(0, 'end')
    EntrytifERTIF313.delete(0, 'end')
    
    EntryNombreMuestraRTIF41.delete(0, 'end')
    EntryAnguloMuestraRTIF42.delete(0, 'end')
    EntryDeRTIF43.delete(0, 'end')
    EntryDsRTIF44.delete(0, 'end')
    EntryDtRTIF45.delete(0, 'end')
    EntryDtcmRTIF46.delete(0, 'end')
    EntryDwRTIF47.delete(0, 'end')
    EntryDoRTIF48.delete(0, 'end')
    EntrytifRTIF49.delete(0, 'end')
    EntryNCRTIF410.delete(0, 'end')
    EntrytifmRTIF411.delete(0, 'end')
    EntrytifMRTIF412.delete(0, 'end')
    EntrytifERTIF413.delete(0, 'end')
    
    EntryNombreMuestraRTIF51.delete(0, 'end')
    EntryAnguloMuestraRTIF52.delete(0, 'end')
    EntryDeRTIF53.delete(0, 'end')
    EntryDsRTIF54.delete(0, 'end')
    EntryDtRTIF55.delete(0, 'end')
    EntryDtcmRTIF56.delete(0, 'end')
    EntryDwRTIF57.delete(0, 'end')
    EntryDoRTIF58.delete(0, 'end')
    EntrytifRTIF59.delete(0, 'end')
    EntryNCRTIF510.delete(0, 'end')
    EntrytifmRTIF511.delete(0, 'end')
    EntrytifMRTIF512.delete(0, 'end')
    EntrytifERTIF513.delete(0, 'end')
    
    EntryNombreMuestraRTIF61.delete(0, 'end')
    EntryAnguloMuestraRTIF62.delete(0, 'end')
    EntryDeRTIF63.delete(0, 'end')
    EntryDsRTIF64.delete(0, 'end')
    EntryDtRTIF65.delete(0, 'end')
    EntryDtcmRTIF66.delete(0, 'end')
    EntryDwRTIF67.delete(0, 'end')
    EntryDoRTIF68.delete(0, 'end')
    EntrytifRTIF69.delete(0, 'end')
    EntryNCRTIF610.delete(0, 'end')
    EntrytifmRTIF611.delete(0, 'end')
    EntrytifMRTIF612.delete(0, 'end')
    EntrytifERTIF613.delete(0, 'end')
    
    EntryNombreMuestraRTIF71.delete(0, 'end')
    EntryAnguloMuestraRTIF72.delete(0, 'end')
    EntryDeRTIF73.delete(0, 'end')
    EntryDsRTIF74.delete(0, 'end')
    EntryDtRTIF75.delete(0, 'end')
    EntryDtcmRTIF76.delete(0, 'end')
    EntryDwRTIF77.delete(0, 'end')
    EntryDoRTIF78.delete(0, 'end')
    EntrytifRTIF79.delete(0, 'end')
    EntryNCRTIF710.delete(0, 'end')
    EntrytifmRTIF711.delete(0, 'end')
    EntrytifMRTIF712.delete(0, 'end')
    EntrytifERTIF713.delete(0, 'end')
    
    EntryNombreMuestraRTIF81.delete(0, 'end')
    EntryAnguloMuestraRTIF82.delete(0, 'end')
    EntryDeRTIF83.delete(0, 'end')
    EntryDsRTIF84.delete(0, 'end')
    EntryDtRTIF85.delete(0, 'end')
    EntryDtcmRTIF86.delete(0, 'end')
    EntryDwRTIF87.delete(0, 'end')
    EntryDoRTIF88.delete(0, 'end')
    EntrytifRTIF89.delete(0, 'end')
    EntryNCRTIF810.delete(0, 'end')
    EntrytifmRTIF811.delete(0, 'end')
    EntrytifMRTIF812.delete(0, 'end')
    EntrytifERTIF813.delete(0, 'end')
    
    EntryNombreMuestraRTIF91.delete(0, 'end')
    EntryAnguloMuestraRTIF92.delete(0, 'end')
    EntryDeRTIF93.delete(0, 'end')
    EntryDsRTIF94.delete(0, 'end')
    EntryDtRTIF95.delete(0, 'end')
    EntryDtcmRTIF96.delete(0, 'end')
    EntryDwRTIF97.delete(0, 'end')
    EntryDoRTIF98.delete(0, 'end')
    EntrytifRTIF99.delete(0, 'end')
    EntryNCRTIF910.delete(0, 'end')
    EntrytifmRTIF911.delete(0, 'end')
    EntrytifMRTIF912.delete(0, 'end')
    EntrytifERTIF913.delete(0, 'end')
    
    EntryNombreMuestraRTIF101.delete(0, 'end')
    EntryAnguloMuestraRTIF102.delete(0, 'end')
    EntryDeRTIF103.delete(0, 'end')
    EntryDsRTIF104.delete(0, 'end')
    EntryDtRTIF105.delete(0, 'end')
    EntryDtcmRTIF106.delete(0, 'end')
    EntryDwRTIF107.delete(0, 'end')
    EntryDoRTIF108.delete(0, 'end')
    EntrytifRTIF109.delete(0, 'end')
    EntryNCRTIF1010.delete(0, 'end')
    EntrytifmRTIF1011.delete(0, 'end')
    EntrytifMRTIF1012.delete(0, 'end')
    EntrytifERTIF1013.delete(0, 'end')
    

# Función del botón Ingresar lectura.

def ingresarLectura():
    
    while True:
    
        fila = pd.DataFrame( columns = [ID2, anguloImagen, dEPx, dSPx, dTPx, dTCm, dWater, dOil, tIFM, tIFAlen, tIFmin, tIFmax, tIFerror])
        
        try:
            fila.to_csv('TensionOutPut.csv', index = False, mode = 'a')
            
        except PermissionError:
            errorArchivoCSVAbiertoT()
            break

        if len(EntryNombreMuestraRTIF11.get()) == 0:
            return varAuxNombreMuestra11.set(ID2), varAuxAnguloTIFMuestra12.set(anguloImagen), varAuxDeR13.set(dEPx), varAuxDsR14.set(dSPx), varAuxDtR15.set(dTPx), varAuxDtCm16.set(dTCm), varAuxdW17.set(dWater), varAuxdO18.set(dOil), varAuxTIFR19.set(tIFM), varAuxNC110.set(tIFAlen), varAuxTIFmin111.set(tIFmin), varAuxTIFmax112.set(tIFmax), varAuxTIFerror113.set(tIFerror)

        elif len(EntryNombreMuestraRTIF21.get()) == 0:
            return varAuxNombreMuestra21.set(ID2), varAuxAnguloTIFMuestra22.set(anguloImagen), varAuxDeR23.set(dEPx), varAuxDsR24.set(dSPx), varAuxDtR25.set(dTPx), varAuxDtCm26.set(dTCm), varAuxdW27.set(dWater), varAuxdO28.set(dOil), varAuxTIFR29.set(tIFM), varAuxNC210.set(tIFAlen), varAuxTIFmin211.set(tIFmin), varAuxTIFmax212.set(tIFmax), varAuxTIFerror213.set(tIFerror)

        elif len(EntryNombreMuestraRTIF31.get()) == 0:
            return varAuxNombreMuestra31.set(ID2), varAuxAnguloTIFMuestra32.set(anguloImagen), varAuxDeR33.set(dEPx), varAuxDsR34.set(dSPx), varAuxDtR35.set(dTPx), varAuxDtCm36.set(dTCm), varAuxdW37.set(dWater), varAuxdO38.set(dOil), varAuxTIFR39.set(tIFM), varAuxNC310.set(tIFAlen), varAuxTIFmin311.set(tIFmin), varAuxTIFmax312.set(tIFmax), varAuxTIFerror313.set(tIFerror)

        elif len(EntryNombreMuestraRTIF41.get()) == 0:
            return varAuxNombreMuestra41.set(ID2), varAuxAnguloTIFMuestra42.set(anguloImagen), varAuxDeR43.set(dEPx), varAuxDsR44.set(dSPx), varAuxDtR45.set(dTPx), varAuxDtCm46.set(dTCm), varAuxdW47.set(dWater), varAuxdO48.set(dOil), varAuxTIFR49.set(tIFM), varAuxNC410.set(tIFAlen), varAuxTIFmin411.set(tIFmin), varAuxTIFmax412.set(tIFmax), varAuxTIFerror413.set(tIFerror)

        elif len(EntryNombreMuestraRTIF51.get()) == 0:
            return varAuxNombreMuestra51.set(ID2), varAuxAnguloTIFMuestra52.set(anguloImagen), varAuxDeR53.set(dEPx), varAuxDsR54.set(dSPx), varAuxDtR55.set(dTPx), varAuxDtCm56.set(dTCm), varAuxdW57.set(dWater), varAuxdO58.set(dOil), varAuxTIFR59.set(tIFM), varAuxNC510.set(tIFAlen), varAuxTIFmin511.set(tIFmin), varAuxTIFmax512.set(tIFmax), varAuxTIFerror513.set(tIFerror)

        elif len(EntryNombreMuestraRTIF61.get()) == 0:
            return varAuxNombreMuestra61.set(ID2), varAuxAnguloTIFMuestra62.set(anguloImagen), varAuxDeR63.set(dEPx), varAuxDsR64.set(dSPx), varAuxDtR65.set(dTPx), varAuxDtCm66.set(dTCm), varAuxdW67.set(dWater), varAuxdO68.set(dOil), varAuxTIFR69.set(tIFM), varAuxNC610.set(tIFAlen), varAuxTIFmin611.set(tIFmin), varAuxTIFmax612.set(tIFmax), varAuxTIFerror613.set(tIFerror)

        elif len(EntryNombreMuestraRTIF71.get()) == 0:
            return varAuxNombreMuestra71.set(ID2), varAuxAnguloTIFMuestra72.set(anguloImagen), varAuxDeR73.set(dEPx), varAuxDsR74.set(dSPx), varAuxDtR75.set(dTPx), varAuxDtCm76.set(dTCm), varAuxdW77.set(dWater), varAuxdO78.set(dOil), varAuxTIFR79.set(tIFM), varAuxNC710.set(tIFAlen), varAuxTIFmin711.set(tIFmin), varAuxTIFmax712.set(tIFmax), varAuxTIFerror713.set(tIFerror)

        elif len(EntryNombreMuestraRTIF81.get()) == 0:
            return varAuxNombreMuestra81.set(ID2), varAuxAnguloTIFMuestra82.set(anguloImagen), varAuxDeR83.set(dEPx), varAuxDsR84.set(dSPx), varAuxDtR85.set(dTPx), varAuxDtCm86.set(dTCm), varAuxdW87.set(dWater), varAuxdO88.set(dOil), varAuxTIFR89.set(tIFM), varAuxNC810.set(tIFAlen), varAuxTIFmin811.set(tIFmin), varAuxTIFmax812.set(tIFmax), varAuxTIFerror813.set(tIFerror)

        elif len(EntryNombreMuestraRTIF91.get()) == 0:
            return varAuxNombreMuestra91.set(ID2), varAuxAnguloTIFMuestra92.set(anguloImagen), varAuxDeR93.set(dEPx), varAuxDsR94.set(dSPx), varAuxDtR95.set(dTPx), varAuxDtCm96.set(dTCm), varAuxdW97.set(dWater), varAuxdO98.set(dOil), varAuxTIFR99.set(tIFM), varAuxNC910.set(tIFAlen), varAuxTIFmin911.set(tIFmin), varAuxTIFmax912.set(tIFmax), varAuxTIFerror913.set(tIFerror)

        elif len(EntryNombreMuestraRTIF101.get()) == 0:
            return varAuxNombreMuestra101.set(ID2), varAuxAnguloTIFMuestra102.set(anguloImagen), varAuxDeR103.set(dEPx), varAuxDsR104.set(dSPx), varAuxDtR105.set(dTPx), varAuxDtCm106.set(dTCm), varAuxdW107.set(dWater), varAuxdO108.set(dOil), varAuxTIFR109.set(tIFM), varAuxNC1010.set(tIFAlen), varAuxTIFmin1011.set(tIFmin), varAuxTIFmax1012.set(tIFmax), varAuxTIFerror1013.set(tIFerror)

        break
        
        
# Función del botón Abrir Imagen:

global imagen
imagen = None
global imagen3
imagen3 = None
global imagen5
imagen5 = None

def abrirImagen(): 
     
    RutaImagen = filedialog.askopenfilename(title = 'Abrir Imagen', initialdir = 'C:/', filetypes = (('Archivos png' , '*.png'), ('Archivos jpg','*.jpg'), ('Archivos bmp', '*.bmp'), ('Imagenes jpeg', '*.jpeg'), ('Todos los Archivos', '*.*')))
    
    if len(RutaImagen) > 0:
        
        toolbar.update()
        global alto
        global ancho
        global ID2
        global anguloImagen
        global dEPx
        global dSPx
        global dTPx
        global dTCm
        global dWater
        global dOil
        global tIFM
        global tIFAlen
        global tIFmin
        global tIFmax
        global tIFerror
        global LIDeL
        global LSDeL 
        global LIGL
        global LIDsL
        global LSDsL
        global LIDtL 
        global LSDtL
        global flagAnalisis

        ID2 = None
        anguloImagen = None
        dEPx = None
        dSPx = None
        dTPx = None
        dTCm = None
        dWater = None
        dOil = None
        tIFM = None
        tIFAlen = None
        tIFmin = None
        tIFmax = None
        tIFerror = None
        LIDeL = None
        LSDeL = None
        LIGL = None
        LIDsL = None
        LSDsL = None
        LIDtL = None
        LSDtL = None
        flagAnalisis = True
        alto = None 
        ancho = None 

        limpiar()
        ax.clear()
        ax.set_xlabel('Pixeles', size = 10)
        ax.set_ylabel('Pixeles', size = 10)
        
        global imagen
        imagen = io.imread(RutaImagen, as_gray = True)
        global imagen3
        imagen3 = io.imread(RutaImagen)
        global imagen5
        imagen5 = cv2.imread(RutaImagen)
        alto = imagen.shape[0]
        ancho = imagen.shape[1]
        global imagen6
        imagen5b = cv2.cvtColor(imagen5, cv2.COLOR_BGR2RGB)
        imagen5Gris = cv2.cvtColor(imagen5b, cv2.COLOR_RGB2GRAY)
        _, binaria = cv2.threshold(imagen5Gris, 225, 255, cv2.THRESH_BINARY_INV) 
        contornos, _ = cv2.findContours(binaria, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        tama = (imagen5.shape[0], imagen5.shape[1])
        imagenBlanca = np.ones(tama)
        imagen6 = cv2.drawContours(imagenBlanca, contornos, -1, (0, 0, 0), 0)
        ax.imshow(imagen, cmap = 'gray')
        canvas.draw()
    
    else:
        pass
    

# Función del Botón Limpiar Pantalla.

def limpiar():
    
    EntryNombreMuestra.delete(0, 'end')
    entrydTPx.delete(0, 'end')
    entrydTCm.delete(0, 'end')
    entrydEPx.delete(0, 'end')
    entrydSPx.delete(0, 'end')
    entrydWater.delete(0, 'end')
    entrydOil.delete(0, 'end')
    labelResulTIF.delete(0, 'end')
    entryRotarImagen.delete(0, 'end')
    entryLIDe.delete(0, 'end')
    entryLSDe.delete(0, 'end')
    entryLIGota.delete(0, 'end')
    entryLIDs.delete(0, 'end')
    entryLSDs.delete(0, 'end')
    entryLIDt.delete(0, 'end')
    entryLSDt.delete(0, 'end')
    
    global ID2
    global anguloImagen
    global dEPx
    global dSPx
    global dTPx
    global dTCm
    global dWater
    global dOil
    global tIFM
    global tIFAlen
    global tIFmin
    global tIFmax
    global tIFerror

    ID2 = None
    anguloImagen = None
    dEPx = None
    dSPx = None
    dTPx = None
    dTCm = None
    dWater = None
    dOil = None
    tIFM = None
    tIFAlen = None
    tIFmin = None
    tIFmax = None
    tIFerror = None
    

# Función dibujar De 

def dibujarDe():
    
    if type(imagen) != type(None):
        
        if flagAnalisis == True:
            
            global LIDeL
            global LSDeL

            if type (LIDeL) and type(LSDeL) == type(None):

                while True:

                    global LIDeV
                    global LSDeV

                    LIDeV = entryLIDe.get() 
                    LSDeV = entryLSDe.get()

                    try:
                        
                        LIDeV = abs(int(LIDeV))
                        LSDeV = abs(int(LSDeV))

                    except ValueError:
                            textoIntroducido()
                            DeError()
                            break

                    LIDeL = ax.axvline(LIDeV, color = 'red', linestyle = '--', linewidth = 1)
                    LSDeL = ax.axvline(LSDeV, label = 'De', color = 'red', linestyle = '--', linewidth = 1)
                    ax.legend()
                    global vDe
                    vDe = abs(LSDeV - LIDeV)
                    canvas.draw()
                    return varAuxDe.set(vDe)
                
            else:
                errorLineaSobrePuesta()
                
        else:
            errorMedirBorrarConAnalisis()
            
    else:
        errorNoImagen()
        

# Función limpiar De 

def limpiarDe():
    
    if type(imagen) != type(None):
        
        if flagAnalisis == True:
        
            global LIDeL
            global LSDeL

            if type(LIDeL) and type (LSDeL) != type (None):

                LIDeL.remove()
                LSDeL.remove()
                LIDeL = None
                LSDeL = None
                ax.legend('')
                canvas.draw()

            else:
                errorDobleBorrar()
                
        else:
            errorMedirBorrarConAnalisis()
        
    else:
        errorNoImagen()
        
    
# Función dibujar Límite Inferior de la Gota 
    
def dibujarLIGota():
    
    if type(imagen) != type(None):
        
        if flagAnalisis == True:
        
            global  LIGL 

            if type (LIGL) == type(None):

                while True:

                    global LIGV 
                    global PDs

                    LIGV = entryLIGota.get()

                    try:

                        LIGV = abs(int(entryLIGota.get()))

                    except ValueError:
                            textoIntroducido()
                            break

                    pDe = LIDeV + (vDe / 2)
                    LDe = [pDe, pDe]
                    LDe2 = [LIGV, LIGV - vDe]
                    LDs = [0, ancho - 1]
                    LDs2 = [LIGV - vDe, LIGV - vDe]
                    LIGL = ax.axhline(LIGV, color = 'olive', linestyle = '--', label = 'L.I Gota', linewidth = 1)
                    PDs = ax.axhline(LIGV - vDe, color = 'purple', linestyle = '--', label = 'P Ds', linewidth = 1)
                    ax.legend()
                    canvas.draw()
                    break
                    
            else:
                errorLineaSobrePuesta()
        
        else:           
            errorMedirBorrarConAnalisis()
            
    else:
        errorNoImagen()
        

# Función borrar Límite Inferior de la Gota 

def limpiarLIGota():
    
    if type(imagen) != type(None):
        
        if flagAnalisis == True:
        
            global LIGL

            if type(LIGL) != type (None):

                LIGL.remove()
                PDs.remove()
                LIGL = None
                ax.legend()
                canvas.draw()

            else:
                 errorDobleBorrar()
                    
        else:                  
            errorMedirBorrarConAnalisis()
            
    else:       
        errorNoImagen()
        

# Función dibujar Ds 

def dibujarDs():
    
    if type(imagen) != type(None):
        
        if flagAnalisis == True:
        
            global LIDsL
            global LSDsL

            if type (LIDsL) and type(LSDsL) == type(None):

                while True:

                    global LIDsV
                    global LSDsV

                    LIDsV = entryLIDs.get() 
                    LSDsV = entryLSDs.get()

                    try:

                        LIDsV = abs(int(LIDsV))
                        LSDsV = abs(int(LSDsV))

                    except ValueError:
                            textoIntroducido()
                            DsError()
                            break

                    LIDsL = ax.axvline(LIDsV, color = 'blue', linestyle = '--', linewidth = 1)
                    LSDsL = ax.axvline(LSDsV, color = 'blue', linestyle = '--', linewidth = 1, label = 'Ds')
                    ax.legend()
                    global vDs
                    vDs = abs(LSDsV - LIDsV)
                    canvas.draw()
                    return varAuxDs.set(vDs)

            else:
                errorLineaSobrePuesta()
                
        else:            
            errorMedirBorrarConAnalisis()
    
    else:        
        errorNoImagen()
        

# Función limpiar Ds 

def limpiarDs():
    
    if type(imagen) != type(None):
        
        if flagAnalisis == True:
        
            global LIDsL
            global LSDsL

            if type(LIDsL) and type (LSDsL) != type (None):

                LIDsL.remove()
                LSDsL.remove()
                LIDsL = None
                LSDsL = None
                ax.legend()
                canvas.draw()

            else:
                 errorDobleBorrar()
        
        else:            
            errorMedirBorrarConAnalisis()

    else:        
        errorNoImagen()
        

# función dibujar Dt

def dibujarDt():
    
    if type(imagen) != type(None):
        
        if flagAnalisis == True:
        
            global LIDtL
            global LSDtL

            if type (LIDtL) and type(LSDtL) == type(None):

                while True:

                    global LIDtV
                    global LSDtV

                    LIDtV = entryLIDt.get() 
                    LSDtV = entryLSDt.get()

                    try:

                        LIDtV = abs(int(LIDtV))
                        LSDtV = abs(int(LSDtV))

                    except ValueError:
                            textoIntroducido()
                            DtError()
                            break

                    LIDtL = ax.axvline(LIDtV, color = 'magenta', linestyle = '--', linewidth = 1 )
                    LSDtL = ax.axvline(LSDtV, color = 'magenta', linestyle = '--', linewidth = 1, label = 'Dt')
                    ax.legend()
                    global vDt
                    vDt = abs(LSDtV - LIDtV)
                    canvas.draw()
                    return varAuxDt.set(vDt)

            else:
                errorLineaSobrePuesta()
                
        else:            
            errorMedirBorrarConAnalisis()
        
    else:        
        errorNoImagen()
        

# función limpiar Dt

def limpiarDt():
    
    if type(imagen) != type(None):
        
        if flagAnalisis == True:
        
            global LIDtL
            global LSDtL

            if type(LIDtL) and type (LSDtL) != type (None):

                LIDtL.remove()
                LSDtL.remove()
                LIDtL = None
                LSDtL = None
                ax.legend()      
                canvas.draw()

            else:
                 errorDobleBorrar()
                    
        else:            
            errorMedirBorrarConAnalisis()
                
    else:      
        errorNoImagen()


# Función imagen para guardar
    
def imagenParaGuardar():
    
    if type(imagen) != type(None):
        
        global flagAnalisis
        
        if flagAnalisis == True:
            if type(LIDeL) and type(LSDeL) != type(None):
                if type(LIGL) != type(None):
                    if type(LIDsL) and type(LSDsL) != type(None):
                        if type(LIDtL) and type(LSDtL) != type(None):

                            global LIDeLC
                            global LSDeLC
                            global LIDsLC
                            global LSDsLC
                            global LIDtLC
                            global LSDtLC

                            limpiarDt()
                            limpiarDs()
                            limpiarLIGota()
                            limpiarDe()

                            x = [int(entryLIDe.get()), int(entryLIDe.get())]
                            y = [int(entryLIGota.get()) - vDe, int(entryLIGota.get())]
                            LIDeLC = ax.vlines(x[0], ymin = y[0], ymax = y[1], color = 'red', linestyle = '--', linewidth = 1)

                            x2 = [int(entryLSDe.get()), int(entryLSDe.get())]
                            y2 = [int(entryLIGota.get()) - vDe,  int(entryLIGota.get()) ]
                            LSDeLC = ax.vlines(x2[0], ymin = y2[0], ymax = y2[1], color = 'red', linestyle = '--', linewidth = 1, label = 'De = {} px'.format(vDe))

                            x3 = [int(entryLIDs.get()), int(entryLIDs.get())]
                            y3 = [int(entryLIGota.get()) - vDe, int(entryLIGota.get())]
                            LIDsLC = ax.vlines(x3[0], ymin = y3[0], ymax = y3[1], color = 'blue', linestyle = '--', linewidth = 1)

                            x4 = [int(entryLSDs.get()), int(entryLSDs.get())]
                            y4 = [int(entryLIGota.get()) - vDe, int(entryLIGota.get())]
                            LSDsLC = ax.vlines(x4[0], ymin = y4[0], ymax = y4[1], color = 'blue', linestyle = '--', linewidth = 1, label = 'Ds = {} px'.format(vDs))

                            x5 = [int(entryLIDt.get()), int(entryLIDt.get())]
                            y5 = [0,  int(entryLIGota.get())- vDe]
                            LIDtLC = ax.vlines(x5[0], ymin = y5[0], ymax = y5[1], color = 'magenta', linestyle = '--', linewidth = 1)

                            x6 = [int(entryLSDt.get()), int(entryLSDt.get())]
                            y6 = [0, int(entryLIGota.get()) - vDe]
                            LSDtLC = ax.vlines(x6[0], ymin = y6[0], ymax = y6[1], color = 'magenta', linestyle = '--', linewidth = 1, label = 'Dt = {} px'.format(vDt) )            
                            ax.legend()
                            canvas.draw()
                            #global flagAnalisis
                            flagAnalisis = False
                            

                        else:
                            errorAnalisisIncompleto()
                    else:
                        errorAnalisisIncompleto()
                else:
                    errorAnalisisIncompleto()
            else:
                errorAnalisisIncompleto() 
        else:
            errorDobleAnalisis()
    else:
        errorNoImagen()
        

# Función limpiar imagen    

def limpiarImagen():
    
    if type(imagen) != type(None):
        
        global flagAnalisis
        
        if flagAnalisis == False:
            
            LIDeLC.remove()
            LSDeLC.remove()
            LIDsLC.remove()
            LSDsLC.remove()
            LIDtLC.remove()
            LSDtLC.remove()
            ax.legend('')       
            canvas.draw()
            flagAnalisis = True
            
        else:
            errorLimpiarAnalisisInexistente()
            
    else:
        errorNoImagen()
        

# Función rotar imagen

anguloImagen = None

def rotarImagen():
    
    if type(imagen) != type(None):
        
        global LIDeL
        global LSDeL 
        global LIGL
        global LIDsL
        global LSDsL
        global LIDtL 
        global LSDtL
        global anguloImagen
        
        IDeL = None
        LSDeL = None
        LIGL = None
        LIDsL = None
        LSDsL = None
        LIDtL = None
        LSDtL = None
        
        if flagAnalisis == True:
            
            while True:

                anguloImagen = entryRotarImagen.get() 

                try:

                    anguloImagen = int(anguloImagen)

                except ValueError:
                        textoIntroducido()
                        if len(anguloImagen) == 0:
                            anguloImagen = None
                        else:
                            pass
                        break

                global imagen2
                global imagen4
                global imagen7

                ax.clear()
                ax.set_xlabel('Pixeles', size = 10)
                ax.set_ylabel('Pixeles', size = 10)
                ax.set_title(ID2)
                M = cv2.getRotationMatrix2D((ancho // 2, alto // 2), anguloImagen, 1)
                imagen2 = cv2.warpAffine(imagen, M, (ancho, alto))
                imagen4 = cv2.warpAffine(imagen3, M, (ancho, alto))
                imagen7 = cv2.warpAffine(imagen6, M, (ancho, alto))

                if flag == None:
                    ax.imshow(imagen2, cmap = 'gray')

                elif flag == 1:
                    ax.imshow(imagen2, cmap = 'gray')

                elif flag == 2:
                    ax.imshow(imagen4)

                elif flag == 3:
                    ax.imshow(imagen7, cmap = 'gray')

                canvas.draw()
                break
                
        else:      
            errorRotarConAnalisis()
        
    else: 
        errorNoImagen()
        
        
global flag
flag = None 

# Función visualizar imagen a color

def visualizarImagenColor():
    
    if type(imagen) != type(None):
    
        global flag
        flag = 2

        if len(entryRotarImagen.get()) == 0:
            ax.imshow(imagen3)

        elif len(entryRotarImagen.get()) != 0:
            ax.imshow(imagen4)

        canvas.draw()
        
    else:
        
        errorNoImagen()
        

# Función visualizar imagen a escala de grises    

def visualizarImagenBYN():
    
    if type(imagen) != type(None):
        
        global flag
        flag = 1

        if len(entryRotarImagen.get()) == 0:
            ax.imshow(imagen, cmap = 'gray')

        elif len(entryRotarImagen.get()) != 0:
            ax.imshow(imagen2, cmap = 'gray')

        canvas.draw()
    
    else:
        
        errorNoImagen()
        

# Función visualizar borde

def visualizarBorde():
    
    if type(imagen) != type(None):
        
        global flag
        flag = 3
        
        if len(entryRotarImagen.get()) == 0:
            ax.imshow(imagen6, cmap = 'gray') 

        elif len(entryRotarImagen.get()) != 0:
            ax.imshow(imagen7, cmap = 'gray')

        canvas.draw()
    
    else:
        
        errorNoImagen()
        
        
# Función aceptar nombre Tensión.

ID2 = None

def aceptarNombre():
        
        global ID2
        ID2 = EntryNombreMuestra.get()
        
        if len (ID2) != 0:
            ax.set_title(ID2)
            canvas.draw()
            
        else:
            ax.set_title(ID2)
            canvas.draw()
            ID2 = None
            

# SECCIÓN 5. Funciones de los botones Ángulo tab. ------------------------------------------------
 
# Función del botón Abrir Imagen 2

global imAgen
imAgen = None
global imAgen3
imAgen3 = None
global imAgen5
imAgen5 = None

def abrirImagen2(): 
    
    RutaImagen2 = filedialog.askopenfilename(title = 'Abrir Imagen', initialdir = 'C:/', filetypes = (('Archivos png' , '*.png'), ('Archivos jpg','*.jpg'), ('Archivos bmp', '*.bmp'), ('Imagenes jpeg', '*.jpeg'), ('Todos los Archivos', '*.*')))
    
    if len(RutaImagen2) > 0:
        
        toolbar2.update()
        
        global alto2
        global ancho2
    
        global IDA
        global anguloImagen2
        global fechaAV
        global fechaAT
        global horaAV
        global horaAT
        global anguloI
        global anguloD
        global PSAILH
        global PSAILV
        global PSAIC
        global PIAILH
        global PIAILV
        global PIAIC
        global flagAnalisisAI
        global PSADLH
        global PSADLV
        global PSADC
        global PIADLH
        global PIADLV
        global PIADC
        global flagAnalisisAD
        global flagAnalisisRA
        global rectApliAI
        global rectApliAD

        IDA = None
        anguloImagen2 = None
        fechaAV = None
        fechaAT = None
        horaAV = None
        horaAT = None
        anguloI = None
        anguloD = None
        PSAILH = None
        PSAILV = None
        PSAIC = None
        PIAILH = None
        PIAILV = None
        PIAIC = None
        flagAnalisisAI = True
        PSADLH = None
        PSADLV = None
        PSADC = None
        PIADLH = None
        PIADLV = None
        PIADC = None
        flagAnalisisAD = True
        flagAnalisisRA = True
        rectApliAI = None 
        rectApliAD = None 

        limpiarA()
        ax2.clear() 
        ax2.set_xlabel('Pixeles', size = 10)
        ax2.set_ylabel('Pixeles', size = 10)
        
        global imAgen
        imAgen = io.imread(RutaImagen2, as_gray = True)
        global imAgen3
        imAgen3 = io.imread(RutaImagen2)
        global imAgen5
        imAgen5 = cv2.imread(RutaImagen2)
        alto2 = imAgen.shape[0]
        ancho2 = imAgen.shape[1]
        global imAgen6
        imAgen5b = cv2.cvtColor(imAgen5, cv2.COLOR_BGR2RGB)
        imAgen5Gris = cv2.cvtColor(imAgen5b, cv2.COLOR_RGB2GRAY)
        _, binaria2 = cv2.threshold(imAgen5Gris, 225, 255, cv2.THRESH_BINARY_INV) 
        contornos2, _ = cv2.findContours(binaria2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        tama2 = (imAgen5.shape[0], imAgen5.shape[1])
        imagenBlanca2 = np.ones(tama2)
        imAgen6 = cv2.drawContours(imagenBlanca2, contornos2, -1, (0, 0, 0), 0)
        ax2.imshow(imAgen, cmap = 'gray')
        canvas2.draw()
        
    else:
        pass
    

# Función generar archivo

def generarArchivoA():
    
    SiNoA = advertenciaLimpiarCSVA()
    
    if SiNoA == True:
        
        columnasA = pd.DataFrame(columns = ['Nombre de la muestra', 'Angulo de rote (grados)', 'Fecha de toma de foto (dd/mm/aaaa)', 'Hora de toma de foto (hrs:min:seg)', 'Angulo Izquierdo (grados)', 'Angulo Derecho (grados)'])
        
        try:
            
            columnasA.to_csv('AnguloOutPut.csv', index = False, mode = 'w')   

        except PermissionError:
            errorArchivoCSVAbiertoA()
    else:
        
        pass
    
    
# Función limpiar resumen ángulo
    
def limpiarResumenA():
    
    EntryNombreMuestraRA11.delete(0, 'end')
    EntryAnguloMuestraRA12.delete(0, 'end')
    EntryFechaTomaRA13.delete(0, 'end')
    EntryHoraTomaRA14.delete(0, 'end')
    EntryAnguloIRA15.delete(0, 'end')
    EntryAnguloDRA16.delete(0, 'end')
    
    EntryNombreMuestraRA21.delete(0, 'end')
    EntryAnguloMuestraRA22.delete(0, 'end')
    EntryFechaTomaRA23.delete(0, 'end')
    EntryHoraTomaRA24.delete(0, 'end')
    EntryAnguloIRA25.delete(0, 'end')
    EntryAnguloDRA26.delete(0, 'end')
    
    EntryNombreMuestraRA31.delete(0, 'end')
    EntryAnguloMuestraRA32.delete(0, 'end')
    EntryFechaTomaRA33.delete(0, 'end')
    EntryHoraTomaRA34.delete(0, 'end')
    EntryAnguloIRA35.delete(0, 'end')
    EntryAnguloDRA36.delete(0, 'end')
    
    EntryNombreMuestraRA41.delete(0, 'end')
    EntryAnguloMuestraRA42.delete(0, 'end')
    EntryFechaTomaRA43.delete(0, 'end')
    EntryHoraTomaRA44.delete(0, 'end')
    EntryAnguloIRA45.delete(0, 'end')
    EntryAnguloDRA46.delete(0, 'end')
    
    EntryNombreMuestraRA51.delete(0, 'end')
    EntryAnguloMuestraRA52.delete(0, 'end')
    EntryFechaTomaRA53.delete(0, 'end')
    EntryHoraTomaRA54.delete(0, 'end')
    EntryAnguloIRA55.delete(0, 'end')
    EntryAnguloDRA56.delete(0, 'end')
    
    EntryNombreMuestraRA61.delete(0, 'end')
    EntryAnguloMuestraRA62.delete(0, 'end')
    EntryFechaTomaRA63.delete(0, 'end')
    EntryHoraTomaRA64.delete(0, 'end')
    EntryAnguloIRA65.delete(0, 'end')
    EntryAnguloDRA66.delete(0, 'end')
    
    EntryNombreMuestraRA71.delete(0, 'end')
    EntryAnguloMuestraRA72.delete(0, 'end')
    EntryFechaTomaRA73.delete(0, 'end')
    EntryHoraTomaRA74.delete(0, 'end')
    EntryAnguloIRA75.delete(0, 'end')
    EntryAnguloDRA76.delete(0, 'end')
    
    EntryNombreMuestraRA81.delete(0, 'end')
    EntryAnguloMuestraRA82.delete(0, 'end')
    EntryFechaTomaRA83.delete(0, 'end')
    EntryHoraTomaRA84.delete(0, 'end')
    EntryAnguloIRA85.delete(0, 'end')
    EntryAnguloDRA86.delete(0, 'end')
    
    EntryNombreMuestraRA91.delete(0, 'end')
    EntryAnguloMuestraRA92.delete(0, 'end')
    EntryFechaTomaRA93.delete(0, 'end')
    EntryHoraTomaRA94.delete(0, 'end')
    EntryAnguloIRA95.delete(0, 'end')
    EntryAnguloDRA96.delete(0, 'end')
    
    EntryNombreMuestraRA101.delete(0, 'end')
    EntryAnguloMuestraRA102.delete(0, 'end')
    EntryFechaTomaRA103.delete(0, 'end')
    EntryHoraTomaRA104.delete(0, 'end')
    EntryAnguloIRA105.delete(0, 'end')
    EntryAnguloDRA106.delete(0, 'end')
    
    
# Función del botón Ingresar lectura.
    
def ingresarLecturaA():
    
    while True:
        
        filaA = pd.DataFrame(columns = [IDA, anguloImagen2, fechaAV, horaAV, anguloI, anguloD])
            
        try:
            filaA.to_csv('AnguloOutPut.csv', index = False, mode = 'a')
                
        except PermissionError:
            errorArchivoCSVAbiertoA()
            break

        if len(EntryNombreMuestraRA11.get()) == 0:
            return varAuxNombreMuestraRA11.set(IDA), varAuxAnguloMuestraRA12.set(anguloImagen2), varAuxFechaTomaRA13.set(fechaAV), varAuxHoraTomaRA14.set(horaAV), varAuxAnguloIRA15.set(anguloI), varAuxAnguloDRA16.set(anguloD)
                
        elif len(EntryNombreMuestraRA21.get()) == 0:
            return varAuxNombreMuestraRA21.set(IDA), varAuxAnguloMuestraRA22.set(anguloImagen2), varAuxFechaTomaRA23.set(fechaAV), varAuxHoraTomaRA24.set(horaAV), varAuxAnguloIRA25.set(anguloI), varAuxAnguloDRA26.set(anguloD)

        elif len(EntryNombreMuestraRA31.get()) == 0:
            return varAuxNombreMuestraRA31.set(IDA), varAuxAnguloMuestraRA32.set(anguloImagen2), varAuxFechaTomaRA33.set(fechaAV), varAuxHoraTomaRA34.set(horaAV), varAuxAnguloIRA35.set(anguloI), varAuxAnguloDRA36.set(anguloD)

        elif len(EntryNombreMuestraRA41.get()) == 0:
            return varAuxNombreMuestraRA41.set(IDA), varAuxAnguloMuestraRA42.set(anguloImagen2), varAuxFechaTomaRA43.set(fechaAV), varAuxHoraTomaRA44.set(horaAV), varAuxAnguloIRA45.set(anguloI), varAuxAnguloDRA46.set(anguloD)

        elif len(EntryNombreMuestraRA51.get()) == 0:
            return varAuxNombreMuestraRA51.set(IDA), varAuxAnguloMuestraRA52.set(anguloImagen2), varAuxFechaTomaRA53.set(fechaAV), varAuxHoraTomaRA54.set(horaAV), varAuxAnguloIRA55.set(anguloI), varAuxAnguloDRA56.set(anguloD)

        elif len(EntryNombreMuestraRA61.get()) == 0:
            return varAuxNombreMuestraRA61.set(IDA), varAuxAnguloMuestraRA62.set(anguloImagen2), varAuxFechaTomaRA63.set(fechaAV), varAuxHoraTomaRA64.set(horaAV), varAuxAnguloIRA65.set(anguloI), varAuxAnguloDRA66.set(anguloD)

        elif len(EntryNombreMuestraRA71.get()) == 0:
            return varAuxNombreMuestraRA71.set(IDA), varAuxAnguloMuestraRA72.set(anguloImagen2), varAuxFechaTomaRA73.set(fechaAV), varAuxHoraTomaRA74.set(horaAV), varAuxAnguloIRA75.set(anguloI), varAuxAnguloDRA76.set(anguloD)

        elif len(EntryNombreMuestraRA81.get()) == 0:
            return varAuxNombreMuestraRA81.set(IDA), varAuxAnguloMuestraRA82.set(anguloImagen2), varAuxFechaTomaRA83.set(fechaAV), varAuxHoraTomaRA84.set(horaAV), varAuxAnguloIRA85.set(anguloI), varAuxAnguloDRA86.set(anguloD)

        elif len(EntryNombreMuestraRA91.get()) == 0:
            return varAuxNombreMuestraRA91.set(IDA), varAuxAnguloMuestraRA92.set(anguloImagen2), varAuxFechaTomaRA93.set(fechaAV), varAuxHoraTomaRA94.set(horaAV), varAuxAnguloIRA95.set(anguloI), varAuxAnguloDRA96.set(anguloD)

        elif len(EntryNombreMuestraRA101.get()) == 0:
            return varAuxNombreMuestraRA101.set(IDA), varAuxAnguloMuestraRA102.set(anguloImagen2), varAuxFechaTomaRA103.set(fechaAV), varAuxHoraTomaRA104.set(horaAV), varAuxAnguloIRA105.set(anguloI), varAuxAnguloDRA106.set(anguloD)

        break
        
        
global flAg
flAg = None

# Función visualizar imagen a color

def visualizarImagenColor2():
    
    if type(imAgen) != type(None):
    
        global flAg
        flAg = 2

        if len(entryRotarImagen2.get()) == 0:
            ax2.imshow(imAgen3)

        elif len(entryRotarImagen2.get()) != 0:
            ax2.imshow(imAgen4)

        canvas2.draw()
        
    else:
        errorNoImagen()
        

# Función visualizar imagen a escala de grises    

def visualizarImagenBYN2():
    
    if type(imAgen) != type(None):
        
        global flAg
        flAg = 1

        if len(entryRotarImagen2.get()) == 0:
            ax2.imshow(imAgen, cmap = 'gray')

        elif len(entryRotarImagen2.get()) != 0:
            ax2.imshow(imAgen2, cmap = 'gray')

        canvas2.draw()
    
    else:
        errorNoImagen()
        

# Función visualizar borde

def visualizarBorde2():
    
    if type(imAgen) != type(None):
        
        global flAg
        flAg = 3

        if len(entryRotarImagen2.get()) == 0:
            ax2.imshow(imAgen6, cmap = 'gray') 

        elif len(entryRotarImagen2.get()) != 0:
            ax2.imshow(imAgen7, cmap = 'gray')

        canvas2.draw()
    
    else:
        errorNoImagen()
        

# Función rotar imagen    

anguloImagen2 = None

def rotarImagen2():
    
    if type(imAgen) != type(None):
        
        global anguloImagen2
        
        if type(rectApliAI) != type(None):
            limpiarProbarAnalisisAI()
            
        else:
        
            if type(PSAIC) != type(None):
                limpiarPSAI()
            else:
                pass

            if type(PIAIC) != type(None):
                limpiarPIAI()
            else:
                pass
            
        if type(rectApliAD) != type(None):
            limpiarProbarAnalisisAD()
            
        else:
        
            if type(PSADC) != type(None):
                limpiarPSAD()
            else:
                pass

            if type(PIADC) != type(None):
                limpiarPIAD()
            else:
                pass
        
        if flagAnalisisRA == True:
        
            while True:

                anguloImagen2 = entryRotarImagen2.get()

                try:

                    anguloImagen2 = int(anguloImagen2)

                except ValueError:
                        textoIntroducido()
                        if len(anguloImagen2) == 0:
                            anguloImagen2 = None
                        else:
                            pass
                        break

                global imAgen2
                global imAgen4
                global imAgen7

                ax2.clear()
                ax2.set_xlabel('Pixeles', size = 10)
                ax2.set_ylabel('Pixeles', size = 10)
                M2 = cv2.getRotationMatrix2D((ancho2 // 2, alto2 // 2), anguloImagen2, 1)
                imAgen2 = cv2.warpAffine(imAgen, M2, (ancho2, alto2))
                imAgen4 = cv2.warpAffine(imAgen3, M2, (ancho2, alto2))
                imAgen7 = cv2.warpAffine(imAgen6, M2, (ancho2, alto2))

                if flAg == None:
                    ax2.imshow(imAgen2, cmap = 'gray')

                elif flAg == 1:
                    ax2.imshow(imAgen2, cmap = 'gray')

                elif flAg == 2:
                    ax2.imshow(imAgen4)

                elif flAg == 3:
                    ax2.imshow(imAgen7, cmap = 'gray')

                canvas2.draw()
                break
        else:
            errorRotarConAnalisis()
    else:
        errorNoImagen()
        

# Función dibujar punto superior ángulo Izquierdo        
        
def dibujarPSAI():
    
    if type(imAgen) != type(None):
        
        if flagAnalisisRA == True:
        
            global PSAILH
            global PSAILV
            global PSAIC

            if type(PSAILH) and type(PSAILV) == type(None):
                if type(PSAIC) == type(None):

                    while True:

                        global PSAIXV
                        global PSAIYV
                        PSAIXV = entryPSAIX.get() 
                        PSAIYV = entryPSAIY.get()

                        try:

                            PSAIXV = abs(float(PSAIXV))
                            PSAIYV = abs(float(PSAIYV))

                        except ValueError:
                            textoIntroducido()
                            break

                        PSAILH = ax2.axhline(PSAIYV, color = 'red', linestyle = '--', linewidth = 1)
                        PSAILV = ax2.axvline(PSAIXV, color = 'red', linestyle = '--', linewidth = 1)
                        PSAIC = ax2.plot(float(PSAIXV), float(PSAIYV), marker = '+', color = 'cyan', scalex = False, scaley = False)
                        canvas2.draw()
                        break
                        
            else:
                errorLineaSobrePuestaA()
                
        else:          
             errorMedirBorrarConAnalisis() 
                
    else:        
        errorNoImagen()
        

# Función limpiar PSAI

def limpiarPSAI():
    
    if type(imAgen) != type(None):
        
        if flagAnalisisRA == True:
        
            global PSAILH
            global PSAILV
            global PSAIC

            if type(PSAILH) and type(PSAILV) != type(None):
                if type(PSAIC) != type(None):

                    PSAILH.remove()
                    PSAILV.remove()
                    PSAIC[0].remove()
                    PSAILH = None
                    PSAILV = None
                    PSAIC = None
                    canvas2.draw()
                    
            else:
                errorDobleBorrarA()
                
        else:          
            errorMedirBorrarConAnalisis()
            
    else:       
        errorNoImagen()
        
        
# Función dibujar punto inferiror ángulo Izquierdo  

anguloI = None

def dibujarPIAI():
    
    if type(imAgen) != type(None):
        
        if flagAnalisisRA == True:
        
            global PIAILH
            global PIAILV
            global PIAIC 

            if type(PIAILH) and type(PIAILV) == type(None):
                if type(PIAIC) == type(None):

                    while True:

                        global PIAIXV 
                        global PIAIYV
                        global anguloI
                        global mAI

                        PIAIXV = entryPIAIX.get() 
                        PIAIYV = entryPIAIY.get()

                        try:
                            PIAIXV = abs(float(PIAIXV))
                            PIAIYV = abs(float(PIAIYV))

                        except ValueError:
                            textoIntroducido()
                            break

                        mAI = (PIAIYV - PSAIYV) / (PIAIXV - PSAIXV)
                        anguloI = abs(round(math.degrees(math.atan(mAI)), 2))
                        PIAILH = ax2.axhline(PIAIYV, color = 'red', linestyle = '--', linewidth = 1)
                        PIAILV = ax2.axvline(PIAIXV, color = 'red', linestyle = '--', linewidth = 1)
                        PIAIC = ax2.plot(float(PIAIXV), float(PIAIYV), marker = '+', color = 'cyan', scalex = False, scaley = False)
                        canvas2.draw()
                        break
                        
            else:
                errorLineaSobrePuestaA()
                
        else:
             errorMedirBorrarConAnalisis()
      
    else:
        errorNoImagen()
        

# Función limpiar PIAI

def limpiarPIAI():
    
    if type(imAgen) != type(None):
        
        if flagAnalisisRA == True:
        
            global PIAILH
            global PIAILV
            global PIAIC

            if type(PIAILH) and type(PIAILV) != type(None):
                if type(PIAIC) != type(None):

                    PIAILH.remove()
                    PIAILV.remove()
                    PIAIC[0].remove()
                    PIAILH = None
                    PIAILV = None
                    PIAIC = None
                    canvas2.draw()
                    
            else:
                errorDobleBorrarA()
                
        else:
            errorMedirBorrarConAnalisis()
            
    else:
        errorNoImagen()
        

# Función probar ánalisis ángulo izquierdo

def probarAnalisisAI():
        
    if type(imAgen) != type(None):
        
        if flagAnalisisRA == True:
        
            global flagAnalisisAI

            if flagAnalisisAI == True:

                if type(PSAILH) and type(PSAILV) != type(None):
                    if type(PSAIC) != None:
                        if type(PIAILH) and type(PIAILV) != type (None):
                            if type(PIAIC) != type(None):

                                limpiarPIAI()
                                limpiarPSAI()

                                global LDAI
                                global PSAIC2
                                global PIAIC2 
                                global rectApliAI
                                global AIE

                                rectAI = patches.Rectangle((PSAIXV, PSAIYV), PIAIXV - PSAIXV, PIAIYV - PSAIYV, linewidth = 1, edgecolor = 'red', linestyle = '--', fill = False)
                                rectApliAI = ax2.add_patch(rectAI)
                                LDAI = ax2.plot([PSAIXV, PIAIXV], [PSAIYV, PIAIYV], scalex = False, scaley = False, color = 'cyan', linestyle = '--', linewidth = 1)
                                PSAIC2 = ax2.plot(float(PSAIXV), float(PSAIYV), scalex = False, scaley = False, marker = '+', color = 'cyan')
                                PIAIC2 = ax2.plot(float(PIAIXV), float(PIAIYV), marker = '+', color = 'cyan', scalex = False, scaley = False)
                                AIE = ax2.text((ancho2 * 0.10), (alto2 * 0.20), '{}'.format(anguloI), fontsize = 15, fontfamily = 'Calibri', color = 'white', backgroundcolor = 'red', fontweight = 'bold')
                                canvas2.draw()
                                flagAnalisisAI = False

                            else:
                                errorAnalisisIncompletoA()
                        else:
                            errorAnalisisIncompletoA()
                    else:
                        errorAnalisisIncompletoA()
                else:
                    errorAnalisisIncompletoA()

            else:
                errorDobleAnalisis()
                
        else:
            errorMedirBorrarConAnalisis()
            
    else:       
        errorNoImagen()
        

# Función limpiar ánalisis ángulo izquierdo

def limpiarProbarAnalisisAI():
    
    if type(imAgen) != type(None):
        
        if flagAnalisisRA == True:
        
            global flagAnalisisAI
            global rectApliAI

            if flagAnalisisAI == False:

                rectApliAI.remove()
                PSAIC2[0].remove() 
                PIAIC2[0].remove()
                LDAI[0].remove()
                AIE.remove()
                canvas2.draw()
                rectApliAI = None
                flagAnalisisAI = True

            else:
                errorLimpiarAnalisisInexistente()
                
        else:
            errorMedirBorrarConAnalisis()
            
    else:
        errorNoImagen()
        
        
# Función dibujar punto superior ángulo Derecho        
        
def dibujarPSAD():
    
    if type(imAgen) != type(None):
        
        if flagAnalisisRA == True:
        
            global PSADLH
            global PSADLV
            global PSADC

            if type(PSADLH) and type(PSADLV) == type(None):
                if type(PSADC) == type(None):

                    while True:

                        global PSADXV
                        global PSADYV

                        PSADXV = entryPSADX.get() 
                        PSADYV = entryPSADY.get()

                        try:

                            PSADXV = abs(float(PSADXV))
                            PSADYV = abs(float(PSADYV))

                        except ValueError:
                            textoIntroducido()
                            break

                        PSADLH = ax2.axhline(PSADYV, color = 'red', linestyle = '--', linewidth = 1)
                        PSADLV = ax2.axvline(PSADXV, color = 'red', linestyle = '--', linewidth = 1)
                        PSADC = ax2.plot(float(PSADXV), float(PSADYV), marker = '+', color = 'cyan', scalex = False, scaley = False)
                        canvas2.draw()
                        break
                        
            else:
                errorLineaSobrePuestaA()
                
        else:
            errorMedirBorrarConAnalisis()
            
    else:        
        errorNoImagen()
        

# Función limpiar PSAD
        
def limpiarPSAD():
    
    if type(imAgen) != type(None):
        
        if flagAnalisisRA == True:
        
            global PSADLH
            global PSADLV
            global PSADC

            if type(PSADLH) and type(PSADLV) != type(None):
                if type(PSADC) != type(None):

                    PSADLH.remove()
                    PSADLV.remove()
                    PSADC[0].remove()
                    PSADLH = None
                    PSADLV = None
                    PSADC = None
                    canvas2.draw()
                    
            else:
                errorDobleBorrarA()
                
        else:
            errorMedirBorrarConAnalisis()
    
    else:
        errorNoImagen()

anguloD = None


# Función dibujar punto inferiror ángulo derecho.

def dibujarPIAD():
    
    if type(imAgen) != type(None):
        
        if flagAnalisisRA == True:
        
            global PIADLH
            global PIADLV
            global PIADC

            if type(PIADLH) and type(PIADLV) == type(None):
                if type(PIADC) == type(None):

                    while True:

                        global PIADXV 
                        global PIADYV 
                        global anguloD
                        global mAD

                        PIADXV = entryPIADX.get() 
                        PIADYV = entryPIADY.get()

                        try:
                            PIADXV = abs(float(PIADXV))
                            PIADYV = abs(float(PIADYV))

                        except ValueError:
                            textoIntroducido()
                            break

                        mAD = (PIADYV - PSADYV) / (PIADXV - PSADXV)
                        anguloD = abs(round(math.degrees(math.atan(mAD)), 2))
                        PIADLH = ax2.axhline(PIADYV, color = 'red', linestyle = '--', linewidth = 1)
                        PIADLV = ax2.axvline(PIADXV, color = 'red', linestyle = '--', linewidth = 1)
                        PIADC = ax2.plot(float(PIADXV), float(PIADYV), marker = '+', color = 'cyan', scalex = False, scaley = False)
                        canvas2.draw()
                        break

            else:
                errorLineaSobrePuestaA()
                
        else:
            errorMedirBorrarConAnalisis()
            
    else:
        
        errorNoImagen()
        

# Función limpiar PIAD
        
def limpiarPIAD():
    
    if type(imAgen) != type(None):
        
        if flagAnalisisRA == True:
        
            global PIADLH
            global PIADLV
            global PIADC

            if type(PIADLH) and type(PIADLV) != type(None):
                if type(PIADC) != type(None):

                    PIADLH.remove()
                    PIADLV.remove()
                    PIADC[0].remove()
                    PIADLH = None
                    PIADLV = None
                    PIADC = None
                    canvas2.draw()
                    
            else:
                errorDobleBorrarA()
                
        else:
            errorMedirBorrarConAnalisis()
            
    else:
        errorNoImagen()
        
        
# Función probar ánalisis ángulo derecho.

def probarAnalisisAD():
        
    if type(imAgen) != type(None):
        
        if flagAnalisisRA == True:
        
            global flagAnalisisAD

            if flagAnalisisAD == True:

                if type(PSADLH) and type(PSADLV) != type(None):
                    if type(PSADC) != None:
                        if type(PIADLH) and type(PIADLV) != type (None):
                            if type(PIADC) != type(None):

                                limpiarPIAD()
                                limpiarPSAD()

                                global LDAD
                                global PSADC2
                                global PIADC2 
                                global rectApliAD
                                global ADE

                                rectAD = patches.Rectangle((PSADXV, PSADYV), PIADXV - PSADXV, PIADYV - PSADYV, linewidth = 1, edgecolor = 'red', linestyle = '--', fill = False)
                                rectApliAD = ax2.add_patch(rectAD)
                                LDAD = ax2.plot([PSADXV, PIADXV], [PSADYV, PIADYV], scalex = False, scaley = False, color = 'cyan', linestyle = '--', linewidth = 1, label = 'Ang.Dere. = {}'.format(anguloD))
                                PSADC2 = ax2.plot(float(PSADXV), float(PSADYV), scalex = False, scaley = False, marker = '+', color = 'cyan')
                                PIADC2 = ax2.plot(float(PIADXV), float(PIADYV), marker = '+', color = 'cyan', scalex = False, scaley = False)
                                ADE = ax2.text((ancho2 * 0.83), (alto2 * 0.20), '{}'.format(anguloD), fontsize = 15, fontfamily = 'Calibri', color = 'white', backgroundcolor = 'red', fontweight = 'bold')
                                canvas2.draw()
                                flagAnalisisAD = False

                            else:
                                errorAnalisisIncompletoA()
                        else:
                            errorAnalisisIncompletoA()
                    else:
                        errorAnalisisIncompletoA()
                else:
                    errorAnalisisIncompletoA()                  
            else:
                errorDobleAnalisis()
                
        else:
            errorMedirBorrarConAnalisis()
    
    else:
        errorNoImagen()
        
        
# Función limpiar ánalisis ángulo derecho

def limpiarProbarAnalisisAD():
    
    if type(imAgen) != type(None):
        
        if flagAnalisisRA == True:
        
            global flagAnalisisAD
            global rectApliAD

            if flagAnalisisAD == False:

                rectApliAD.remove()
                PSADC2[0].remove() 
                PIADC2[0].remove()
                LDAD[0].remove()
                ADE.remove()
                rectApliAD = None
                canvas2.draw()
                flagAnalisisAD = True 

            else:
                errorLimpiarAnalisisInexistente()
                
        else:
            errorMedirBorrarConAnalisis()
            
    else:
        
        errorNoImagen()
        
        
# Función reporte ángulo
        
def RA():
    
    if type(imAgen) != type(None):
        
        global flagAnalisisRA
        
        if flagAnalisisRA == True:
            
            if flagAnalisisAI == False:
                if flagAnalisisAD == False:
                
                    while True:

                        global AIER
                        global ADER
                        global AIRL
                        global ADRL
                        global YPIL
                        global arcApliAI
                        global arcApliAD

                        xS = symbols('x')
                        yS = symbols('y')

                        YPSV = entryYPSV.get() 
                        YPIV = entryYPIV.get()

                        try:
                            YPSV = abs(int(YPSV))
                            YPIV = abs(int(YPIV))

                        except ValueError:
                            textoIntroducido()
                            break

                        limpiarProbarAnalisisAI()
                        limpiarProbarAnalisisAD()

                        SSEPSAI = solve([mAI * (xS - PSAIXV) + PSAIYV - yS, int(entryYPSV.get()) - yS], [xS, yS])
                        SSEPIAI = solve([mAI * (xS - PSAIXV) + PSAIYV - yS, int(entryYPIV.get()) - yS], [xS, yS])
                        PSAIR = [int(SSEPSAI[xS]), int(entryYPSV.get())]
                        PIAIR = [int(SSEPIAI[xS]), int(entryYPIV.get())]
                        AIRL = ax2.plot([PSAIR[0], PIAIR[0]], [PSAIR[1], PIAIR[1]], color = 'red', linestyle = '--', linewidth = 1)
                        YPIL = ax2.axhline(int(entryYPIV.get()), color = 'red', linestyle = '--', linewidth = 1)
                        AIER = ax2.text((ancho2 * 0.10), (alto2 * 0.20), '{}'.format(anguloI), fontsize = 15, fontfamily = 'Calibri', color = 'white', backgroundcolor = 'red', fontweight = 'bold')

                        SSEPSAD = solve([mAD * (xS - PSADXV) + PSADYV - yS, int(entryYPSV.get()) - yS], [xS, yS])
                        SSEPIAD = solve([mAD * (xS - PSADXV) + PSADYV - yS, int(entryYPIV.get()) - yS], [xS, yS])
                        PSADR = [int(SSEPSAD[xS]), int(entryYPSV.get())]
                        PIADR = [int(SSEPIAD[xS]), int(entryYPIV.get())]
                        ADRL = ax2.plot([PSADR[0], PIADR[0]], [PSADR[1], PIADR[1]], color = 'red', linestyle = '--', linewidth = 1)
                        ADER = ax2.text((ancho2 * 0.83), (alto2 * 0.20), '{}'.format(anguloD), fontsize = 15, fontfamily = 'Calibri', color = 'white', backgroundcolor = 'red', fontweight = 'bold')
                        canvas2.draw()
                        flagAnalisisRA = False
                        break
                else:
                    errorAnalisisIncompletoRA()
            else:
                errorAnalisisIncompletoRA()
        else:
            errorDobleAnalisis()  
    else:        
        errorNoImagen()
        
        
# Función limpiar reporte ángulo.

def limpiarRA():
    
    if type(imAgen) != type(None):
        
        global flagAnalisisRA
        
        if  flagAnalisisRA == False:
        
            AIER.remove()
            ADER.remove()
            AIRL[0].remove()
            ADRL[0].remove()
            YPIL.remove()
            flagAnalisisRA = True
            canvas2.draw()
            
        else:
            errorLimpiarAnalisisInexistente()
    
    else: 
        errorNoImagen()
        
        
# Función aceptar nombre ángulo
    
IDA = None

def aceptarNombreA():
    
    if type(imAgen) != type(None):
        
        global IDA
        IDA = EntryNombreMuestraA.get()
        
        if len(IDA) != 0:
            ax2.set_title(IDA)
            canvas2.draw()
            
        else:
            ax2.set_title(IDA)
            canvas2.draw()
            IDA = None
            
    else:       
        errorNoImagen()
        
        
# Función aceptar fecha ángulo.
        
fechaAV = None
        
def aceptarFechaA():
    
    if type(imAgen) != type(None):
        
        global fechaAV
        global fechaAT
        
        if type (fechaAT) == type(None):
        
            fechaAV = EntryFechaMuestraA.get()

            if len(fechaAV) == 0:
                datoOmitido()
                fechaAV = None

            else:
                fechaAT = ax2.text((ancho2 / 2) - (ancho2 * 0.10), (alto2 * 0.15), '{}'.format(fechaAV), fontsize = 15, fontfamily = 'Calibri', color = 'white', backgroundcolor = 'red', fontweight = 'bold')
                canvas2.draw()
        else:
             errorTextoSobrePuestaA()

    else:       
        errorNoImagen()
        
# Función borrar fecha ángulo

def borrarFechaA():
    
    if type(imAgen) != type(None):
        
        global fechaAV
        global fechaAT
        
        if type(fechaAT) != type(None):
            
            fechaAT.remove()
            fechaAT = None
            fechaAV = None
            canvas2.draw()
        
        else:
            errorBorrarVacio() 
    else:   
        errorNoImagen()
        
        
# Función aceptar hora ángulo
        
horaAV = None

def aceptarHoraA():
    
    if type(imAgen) != type(None):
        
        global horaAV
        global horaAT
        
        if type (horaAT) == type(None):
        
            horaAV = EntryHoraMuestraA.get()
            
            if len(horaAV) == 0:
                datoOmitido()
                horaAV = None
                
            else:
                horaAT = ax2.text((ancho2 / 2) - (ancho2 * 0.075), (alto2 * 0.31), '{}'.format(horaAV), fontsize = 15, fontfamily = 'Calibri', color = 'white', backgroundcolor = 'red', fontweight = 'bold')
                canvas2.draw()
        else:
            errorTextoSobrePuestaA()
    
    else:
        errorNoImagen()


# Función borrar hora ángulo

def borrarHoraA():
    
    if type(imAgen) != type(None):
        
        global horaAV
        global horaAT
        
        if type(horaAT) != type(None):
            
            horaAT.remove()
            horaAT = None
            horaAV = None
            canvas2.draw()
        
        else:
            errorBorrarVacio() 
    else:   
        errorNoImagen()
        
        
# Función limpiar resumen ángulo
        
def limpiarA():
    
    EntryNombreMuestraA.delete(0, 'end') #
    entryRotarImagen2.delete(0, 'end')
    entryPSAIX.delete(0, 'end')
    entryPSAIY.delete(0, 'end')
    entryPIAIX.delete(0, 'end')
    entryPIAIY.delete(0, 'end')
    entryPSADX.delete(0, 'end')
    entryPSADY.delete(0, 'end')
    entryPIADX.delete(0, 'end')
    entryPIADY.delete(0, 'end')
    entryYPSV.delete(0, 'end')
    entryYPIV.delete(0, 'end')
    EntryFechaMuestraA.delete(0, 'end')
    EntryHoraMuestraA.delete(0, 'end')
    
    global IDA
    global anguloImagen2
    global fechaAV
    global horaAV
    global anguloI
    global anguloD
    
    IDA = None
    anguloImagen2 = None
    fechaAV = None
    horaAV = None
    anguloI = None
    anguloD = None


# SECCIÓN 6. Código de la Interfaz Gráfica ---------------------------------------------------

# sección de la interfaz gráfica en común 

# ventana

root = tkinter.Tk()
root.title('TENSIÓN Y ÁNGULO DE CONTACTO')
root.iconbitmap('gotaicono.ico')

# panel para las tabs 

panel = ttk.Notebook(root)
panel.pack(fill = 'both', expand = 'yes' )

# tabs

p1 = ttk.Frame(master = panel)
panel.add(p1, text = 'Tensión')
p1.config()

p1.rowconfigure(0, weight = 1)
p1.rowconfigure(1, weight = 1)
p1.rowconfigure(2, weight = 1)
p1.rowconfigure(3, weight = 1)
p1.rowconfigure(4, weight = 1)
p1.rowconfigure(5, weight = 1)
p1.rowconfigure(6, weight = 1)
p1.rowconfigure(7, weight = 1)
p1.rowconfigure(8, weight = 0)

p1.columnconfigure(0, weight = 1)
p1.columnconfigure(1, weight = 1)
p1.columnconfigure(2, weight = 1)
p1.columnconfigure(3, weight = 1)
p1.columnconfigure(4, weight = 1)
p1.columnconfigure(5, weight = 1)

p2 = ttk.Frame(master = panel)
panel.add(p2, text = 'Ángulo')

p2.rowconfigure(0, weight = 1)
p2.rowconfigure(1, weight = 1)
p2.rowconfigure(2, weight = 1)
p2.rowconfigure(3, weight = 1)
p2.rowconfigure(4, weight = 1)
p2.rowconfigure(5, weight = 1)
p2.rowconfigure(6, weight = 0)

p2.columnconfigure(0, weight = 1)
p2.columnconfigure(1, weight = 1)
p2.columnconfigure(2, weight = 1)
p2.columnconfigure(3, weight = 1)
p2.columnconfigure(4, weight = 1)
p2.columnconfigure(5, weight = 1)

p3 = ttk.Frame(master = panel)
panel.add(p3, text = 'Resumen') 

p3.rowconfigure(0, weight = 1)
p3.rowconfigure(1, weight = 1)
p3.rowconfigure(2, weight = 1)
p3.rowconfigure(3, weight = 1)
p3.rowconfigure(4, weight = 1)

p3.columnconfigure(0, weight = 1)
p3.columnconfigure(1, weight = 1)
p3.columnconfigure(2, weight = 1)
p3.columnconfigure(3, weight = 1)
p3.columnconfigure(4, weight = 1)
p3.columnconfigure(5, weight = 1)


# Imágenes de los botones 

palomita = Image.open('palomita.jpg') 
palomita = palomita.resize((20, 20))
palomita = ImageTk.PhotoImage(palomita)

bote = Image.open('bote.jpg') 
bote = bote.resize((20, 20)) 
bote = ImageTk.PhotoImage(bote)

gotaBorde = Image.open('gotaborde.jpg') 
gotaBorde = gotaBorde.resize((20, 20)) 
gotaBorde = ImageTk.PhotoImage(gotaBorde)

gotaNegra = Image.open('gotanegra.jpg') 
gotaNegra = gotaNegra.resize((20, 20)) 
gotaNegra = ImageTk.PhotoImage(gotaNegra)

gotaColor = Image.open('gotacolor.jpg') 
gotaColor = gotaColor.resize((20, 20)) 
gotaColor = ImageTk.PhotoImage(gotaColor)

# Variable de conexión entre el resultado de la función que calcula la TIF, De, Ds y Dt en y el Entry que mostrara esos resultados.

VarAuxTIF = tkinter.StringVar()
varAuxDe = tkinter.StringVar()
varAuxDs = tkinter.StringVar()
varAuxDt = tkinter.StringVar()

# Resumen TIF

varAuxNombreMuestra11 = tkinter.StringVar() # para el reporte
varAuxAnguloTIFMuestra12 = tkinter.StringVar() # para el reporte
varAuxDeR13 = tkinter.StringVar() # para el reporte
varAuxDsR14 = tkinter.StringVar() # para el reporte 
varAuxDtR15 = tkinter.StringVar() # para el reporte
varAuxDtCm16 = tkinter.StringVar() # para el reporte 
varAuxdW17 = tkinter.StringVar() # para el reporte 
varAuxdO18 = tkinter.StringVar() # para el reporte 
varAuxTIFR19 = tkinter.StringVar() # para el reporte
varAuxNC110 = tkinter.StringVar() # para el reporte
varAuxTIFmin111 = tkinter.StringVar() # para el reporte
varAuxTIFmax112 = tkinter.StringVar() # para el reporte
varAuxTIFerror113 = tkinter.StringVar() # para el reporte

varAuxNombreMuestra21 = tkinter.StringVar() # para el reporte
varAuxAnguloTIFMuestra22 = tkinter.StringVar() # para el reporte
varAuxDeR23 = tkinter.StringVar() # para el reporte
varAuxDsR24 = tkinter.StringVar() # para el reporte 
varAuxDtR25 = tkinter.StringVar() # para el reporte
varAuxDtCm26 = tkinter.StringVar() # para el reporte 
varAuxdW27 = tkinter.StringVar() # para el reporte 
varAuxdO28 = tkinter.StringVar() # para el reporte 
varAuxTIFR29 = tkinter.StringVar() # para el reporte
varAuxNC210 = tkinter.StringVar() # para el reporte
varAuxTIFmin211 = tkinter.StringVar() # para el reporte
varAuxTIFmax212 = tkinter.StringVar() # para el reporte
varAuxTIFerror213 = tkinter.StringVar() # para el reporte

varAuxNombreMuestra31 = tkinter.StringVar() # para el reporte
varAuxAnguloTIFMuestra32 = tkinter.StringVar() # para el reporte
varAuxDeR33 = tkinter.StringVar() # para el reporte
varAuxDsR34 = tkinter.StringVar() # para el reporte 
varAuxDtR35 = tkinter.StringVar() # para el reporte
varAuxDtCm36 = tkinter.StringVar() # para el reporte 
varAuxdW37 = tkinter.StringVar() # para el reporte 
varAuxdO38 = tkinter.StringVar() # para el reporte 
varAuxTIFR39 = tkinter.StringVar() # para el reporte
varAuxNC310 = tkinter.StringVar() # para el reporte
varAuxTIFmin311 = tkinter.StringVar() # para el reporte
varAuxTIFmax312 = tkinter.StringVar() # para el reporte
varAuxTIFerror313 = tkinter.StringVar() # para el reporte

varAuxNombreMuestra41 = tkinter.StringVar() # para el reporte
varAuxAnguloTIFMuestra42 = tkinter.StringVar() # para el reporte
varAuxDeR43 = tkinter.StringVar() # para el reporte
varAuxDsR44 = tkinter.StringVar() # para el reporte 
varAuxDtR45 = tkinter.StringVar() # para el reporte
varAuxDtCm46 = tkinter.StringVar() # para el reporte 
varAuxdW47 = tkinter.StringVar() # para el reporte 
varAuxdO48 = tkinter.StringVar() # para el reporte 
varAuxTIFR49 = tkinter.StringVar() # para el reporte
varAuxNC410 = tkinter.StringVar() # para el reporte
varAuxTIFmin411 = tkinter.StringVar() # para el reporte
varAuxTIFmax412 = tkinter.StringVar() # para el reporte
varAuxTIFerror413 = tkinter.StringVar() # para el reporte

varAuxNombreMuestra51 = tkinter.StringVar() # para el reporte
varAuxAnguloTIFMuestra52 = tkinter.StringVar() # para el reporte
varAuxDeR53 = tkinter.StringVar() # para el reporte
varAuxDsR54 = tkinter.StringVar() # para el reporte 
varAuxDtR55 = tkinter.StringVar() # para el reporte
varAuxDtCm56 = tkinter.StringVar() # para el reporte 
varAuxdW57 = tkinter.StringVar() # para el reporte 
varAuxdO58 = tkinter.StringVar() # para el reporte 
varAuxTIFR59 = tkinter.StringVar() # para el reporte
varAuxNC510 = tkinter.StringVar() # para el reporte
varAuxTIFmin511 = tkinter.StringVar() # para el reporte
varAuxTIFmax512 = tkinter.StringVar() # para el reporte
varAuxTIFerror513 = tkinter.StringVar() # para el reporte

varAuxNombreMuestra61 = tkinter.StringVar() # para el reporte
varAuxAnguloTIFMuestra62 = tkinter.StringVar() # para el reporte
varAuxDeR63 = tkinter.StringVar() # para el reporte
varAuxDsR64 = tkinter.StringVar() # para el reporte 
varAuxDtR65 = tkinter.StringVar() # para el reporte
varAuxDtCm66 = tkinter.StringVar() # para el reporte 
varAuxdW67 = tkinter.StringVar() # para el reporte 
varAuxdO68 = tkinter.StringVar() # para el reporte 
varAuxTIFR69 = tkinter.StringVar() # para el reporte
varAuxNC610 = tkinter.StringVar() # para el reporte
varAuxTIFmin611 = tkinter.StringVar() # para el reporte
varAuxTIFmax612 = tkinter.StringVar() # para el reporte
varAuxTIFerror613 = tkinter.StringVar() # para el reporte

varAuxNombreMuestra71 = tkinter.StringVar() # para el reporte
varAuxAnguloTIFMuestra72 = tkinter.StringVar() # para el reporte
varAuxDeR73 = tkinter.StringVar() # para el reporte
varAuxDsR74 = tkinter.StringVar() # para el reporte 
varAuxDtR75 = tkinter.StringVar() # para el reporte
varAuxDtCm76 = tkinter.StringVar() # para el reporte 
varAuxdW77 = tkinter.StringVar() # para el reporte 
varAuxdO78 = tkinter.StringVar() # para el reporte 
varAuxTIFR79 = tkinter.StringVar() # para el reporte
varAuxNC710 = tkinter.StringVar() # para el reporte
varAuxTIFmin711 = tkinter.StringVar() # para el reporte
varAuxTIFmax712 = tkinter.StringVar() # para el reporte
varAuxTIFerror713 = tkinter.StringVar() # para el reporte

varAuxNombreMuestra81 = tkinter.StringVar() # para el reporte
varAuxAnguloTIFMuestra82 = tkinter.StringVar() # para el reporte
varAuxDeR83 = tkinter.StringVar() # para el reporte
varAuxDsR84 = tkinter.StringVar() # para el reporte 
varAuxDtR85 = tkinter.StringVar() # para el reporte
varAuxDtCm86 = tkinter.StringVar() # para el reporte 
varAuxdW87 = tkinter.StringVar() # para el reporte 
varAuxdO88 = tkinter.StringVar() # para el reporte 
varAuxTIFR89 = tkinter.StringVar() # para el reporte
varAuxNC810 = tkinter.StringVar() # para el reporte
varAuxTIFmin811 = tkinter.StringVar() # para el reporte
varAuxTIFmax812 = tkinter.StringVar() # para el reporte
varAuxTIFerror813 = tkinter.StringVar() # para el reporte

varAuxNombreMuestra91 = tkinter.StringVar() # para el reporte
varAuxAnguloTIFMuestra92 = tkinter.StringVar() # para el reporte
varAuxDeR93 = tkinter.StringVar() # para el reporte
varAuxDsR94 = tkinter.StringVar() # para el reporte 
varAuxDtR95 = tkinter.StringVar() # para el reporte
varAuxDtCm96 = tkinter.StringVar() # para el reporte 
varAuxdW97 = tkinter.StringVar() # para el reporte 
varAuxdO98 = tkinter.StringVar() # para el reporte 
varAuxTIFR99 = tkinter.StringVar() # para el reporte
varAuxNC910 = tkinter.StringVar() # para el reporte
varAuxTIFmin911 = tkinter.StringVar() # para el reporte
varAuxTIFmax912 = tkinter.StringVar() # para el reporte
varAuxTIFerror913 = tkinter.StringVar() # para el reporte

varAuxNombreMuestra101 = tkinter.StringVar() # para el reporte
varAuxAnguloTIFMuestra102 = tkinter.StringVar() # para el reporte
varAuxDeR103 = tkinter.StringVar() # para el reporte
varAuxDsR104 = tkinter.StringVar() # para el reporte 
varAuxDtR105 = tkinter.StringVar() # para el reporte
varAuxDtCm106 = tkinter.StringVar() # para el reporte 
varAuxdW107 = tkinter.StringVar() # para el reporte 
varAuxdO108 = tkinter.StringVar() # para el reporte 
varAuxTIFR109 = tkinter.StringVar() # para el reporte
varAuxNC1010 = tkinter.StringVar() # para el reporte
varAuxTIFmin1011 = tkinter.StringVar() # para el reporte
varAuxTIFmax1012 = tkinter.StringVar() # para el reporte
varAuxTIFerror1013 = tkinter.StringVar() # para el reporte

# Resumen Angulo

varAuxNombreMuestraRA11 = tkinter.StringVar() # para reporte
varAuxAnguloMuestraRA12 = tkinter.StringVar() # para reporte
varAuxFechaTomaRA13 = tkinter.StringVar() # para reporte
varAuxHoraTomaRA14 = tkinter.StringVar() # para reporte
varAuxAnguloIRA15 = tkinter.StringVar() # para reporte
varAuxAnguloDRA16 = tkinter.StringVar() # para reporte

varAuxNombreMuestraRA21 = tkinter.StringVar() # para reporte
varAuxAnguloMuestraRA22 = tkinter.StringVar() # para reporte
varAuxFechaTomaRA23 = tkinter.StringVar() # para reporte
varAuxHoraTomaRA24 = tkinter.StringVar() # para reporte
varAuxAnguloIRA25 = tkinter.StringVar() # para reporte
varAuxAnguloDRA26 = tkinter.StringVar() # para reporte

varAuxNombreMuestraRA31 = tkinter.StringVar() # para reporte
varAuxAnguloMuestraRA32 = tkinter.StringVar() # para reporte
varAuxFechaTomaRA33 = tkinter.StringVar() # para reporte
varAuxHoraTomaRA34 = tkinter.StringVar() # para reporte
varAuxAnguloIRA35 = tkinter.StringVar() # para reporte
varAuxAnguloDRA36 = tkinter.StringVar() # para reporte

varAuxNombreMuestraRA41 = tkinter.StringVar() # para reporte
varAuxAnguloMuestraRA42 = tkinter.StringVar() # para reporte
varAuxFechaTomaRA43 = tkinter.StringVar() # para reporte
varAuxHoraTomaRA44 = tkinter.StringVar() # para reporte
varAuxAnguloIRA45 = tkinter.StringVar() # para reporte
varAuxAnguloDRA46 = tkinter.StringVar() # para reporte

varAuxNombreMuestraRA51 = tkinter.StringVar() # para reporte
varAuxAnguloMuestraRA52 = tkinter.StringVar() # para reporte
varAuxFechaTomaRA53 = tkinter.StringVar() # para reporte
varAuxHoraTomaRA54 = tkinter.StringVar() # para reporte
varAuxAnguloIRA55 = tkinter.StringVar() # para reporte
varAuxAnguloDRA56 = tkinter.StringVar() # para reporte

varAuxNombreMuestraRA61 = tkinter.StringVar() # para reporte
varAuxAnguloMuestraRA62 = tkinter.StringVar() # para reporte
varAuxFechaTomaRA63 = tkinter.StringVar() # para reporte
varAuxHoraTomaRA64 = tkinter.StringVar() # para reporte
varAuxAnguloIRA65 = tkinter.StringVar() # para reporte
varAuxAnguloDRA66 = tkinter.StringVar() # para reporte

varAuxNombreMuestraRA71 = tkinter.StringVar() # para reporte
varAuxAnguloMuestraRA72 = tkinter.StringVar() # para reporte
varAuxFechaTomaRA73 = tkinter.StringVar() # para reporte
varAuxHoraTomaRA74 = tkinter.StringVar() # para reporte
varAuxAnguloIRA75 = tkinter.StringVar() # para reporte
varAuxAnguloDRA76 = tkinter.StringVar() # para reporte

varAuxNombreMuestraRA81 = tkinter.StringVar() # para reporte
varAuxAnguloMuestraRA82 = tkinter.StringVar() # para reporte
varAuxFechaTomaRA83 = tkinter.StringVar() # para reporte
varAuxHoraTomaRA84 = tkinter.StringVar() # para reporte
varAuxAnguloIRA85 = tkinter.StringVar() # para reporte
varAuxAnguloDRA86 = tkinter.StringVar() # para reporte

varAuxNombreMuestraRA91 = tkinter.StringVar() # para reporte
varAuxAnguloMuestraRA92 = tkinter.StringVar() # para reporte
varAuxFechaTomaRA93 = tkinter.StringVar() # para reporte
varAuxHoraTomaRA94 = tkinter.StringVar() # para reporte
varAuxAnguloIRA95 = tkinter.StringVar() # para reporte
varAuxAnguloDRA96 = tkinter.StringVar() # para reporte

varAuxNombreMuestraRA101 = tkinter.StringVar() # para reporte
varAuxAnguloMuestraRA102 = tkinter.StringVar() # para reporte
varAuxFechaTomaRA103 = tkinter.StringVar() # para reporte
varAuxHoraTomaRA104 = tkinter.StringVar() # para reporte
varAuxAnguloIRA105 = tkinter.StringVar() # para reporte
varAuxAnguloDRA106 = tkinter.StringVar() # para reporte

# sección de la interfaz gráfica que pertenece a la TIF tab

# Imagen de la gota roja.

imagenGota = tkinter.PhotoImage(file = 'gotaroja.png')
labelImage = tkinter.Label(master = p1, image = imagenGota)
labelImage.grid(row = 0, column = 2, sticky = 'E', ipady = 15) 

# Label  Titulo

labelTitulo = tkinter.Label(master = p1, text = 'T.I.F / T.S.F con el método de la Gota pendiente', font = ('Calibri light', 13, 'bold'))
labelTitulo.grid(row = 0, column = 3, sticky = 'W', ipady = 15)

# Figura y Canvas en la interfaz

fig = plt.Figure(figsize = (5, 4), dpi = 100) 
ax = fig.subplots()
ax.set_xlabel('Pixeles', size = 10)
ax.set_ylabel('Pixeles', size = 10)
canvas = FigureCanvasTkAgg(fig, master = p1)
canvas.draw()                                 
canvas.get_tk_widget().grid(row = 1, column = 2, rowspan =  7, columnspan = 2, sticky = 'NSEW', padx = 30, pady = 5)
cursor = Cursor(ax, useblit = True, color = 'r', lw = 0.5)

# Frame Toolbar

FrameTBarTIF = tkinter.Frame(master = p1) 
FrameTBarTIF.config(borderwidth = 1, relief = "solid") 
FrameTBarTIF.grid(row = 8, column = 1, columnspan = 4, sticky = 'NSEW', padx = 10, pady = 5)

toolbar = NavigationToolbar2Tk(canvas, FrameTBarTIF) 
toolbar.update()

# Frame Colores 

FrameColores = tkinter.Frame(master = p1)
FrameColores.config(bg = 'seashell2', borderwidth = 1, relief = "solid")
FrameColores.grid(row = 1, column = 1, sticky = 'NSEW', padx = 10, pady = 5)

FrameColores.rowconfigure(0, weight = 1)
FrameColores.rowconfigure(1, weight = 1)

FrameColores.columnconfigure(0, weight = 1)
FrameColores.columnconfigure(1, weight = 1)
FrameColores.columnconfigure(2, weight = 1)
FrameColores.columnconfigure(3, weight = 1)

labelGota = tkinter.Label(master = FrameColores, text = 'Gota', font = ('Calibri', 9, 'bold', 'italic'), bg = 'seashell2')
labelGota.grid(row = 0, column = 0, sticky = 'W')

labelColor = tkinter.Label(master = FrameColores, text = 'Colores', font = ('Calibri', 11, 'bold', 'italic'), bg = 'seashell2' )
labelColor.grid(row = 1, column = 0, sticky = 'NSEW', padx = 2, pady = 5) 

buttonVisualizarImagenColor = tkinter.Button(master = FrameColores, image = gotaColor, command = visualizarImagenColor, borderwidth = 1, relief = 'solid', cursor = 'hand2')
buttonVisualizarImagenColor.grid(row = 1, column = 1, sticky = 'NSEW', padx = 2, pady = 5, ipady = 5)

buttonVisualizarImagenBYN= tkinter.Button(master = FrameColores, image = gotaNegra, command = visualizarImagenBYN, borderwidth = 1, relief = 'solid', cursor = 'hand2')
buttonVisualizarImagenBYN.grid(row = 1, column = 2, sticky = 'NSEW', padx = 2, pady = 5, ipady = 5)

buttonVisualizarBordes = tkinter.Button(master = FrameColores, image = gotaBorde, command = visualizarBorde, borderwidth = 1, relief = 'solid', cursor = 'hand2' ) 
buttonVisualizarBordes.grid(row = 1, column = 3, sticky = 'NSEW', padx = 2, pady = 5, ipady = 5)

# Frame Rotar Imagen 

FrameRotarImagen = tkinter.Frame(master = p1)
FrameRotarImagen.config(bg = 'seashell2', borderwidth = 1, relief = "solid")
FrameRotarImagen.grid(row = 2, column = 1, sticky = 'NSEW', padx = 10, pady = 5)

FrameRotarImagen.rowconfigure(0, weight = 1)
FrameRotarImagen.rowconfigure(1, weight = 1)
FrameRotarImagen.rowconfigure(2, weight = 1)

FrameRotarImagen.columnconfigure(0, weight = 1)
FrameRotarImagen.columnconfigure(1, weight = 1)
FrameRotarImagen.columnconfigure(2, weight = 1)

labelRotarImagen = tkinter.Label(master = FrameRotarImagen, bg = 'seashell2', text = 'Rotar', font = ('Calibri', 9, 'bold', 'italic'))
labelRotarImagen.grid(row = 0, column = 0, sticky = 'W')

labelGradosImagen = tkinter.Label(master = FrameRotarImagen, bg = 'seashell2', text = 'Grados', font = ('Calibri', 11, 'bold', 'italic'))
labelGradosImagen.grid(row = 1, column = 0, sticky = 'NSEW', ipadx = 15)

entryRotarImagen = tkinter.Entry(master = FrameRotarImagen, width = 5)
entryRotarImagen.grid(row = 1, column = 1, sticky = 'NSEW', padx = 2, pady = 2)

buttonRotarImagen = tkinter.Button(master = FrameRotarImagen, image = palomita, command = rotarImagen, borderwidth = 1, relief = 'solid', cursor = 'hand2' )
buttonRotarImagen.grid(row = 1, column = 2, sticky = 'NSEW', padx = 2, pady = 2)

# Frame De 

FrameDe = tkinter.Frame(master = p1)
FrameDe.config(bg = 'seashell2', borderwidth = 1, relief = "solid")
FrameDe.grid(row = 3, column = 1, sticky = 'NSEW', padx = 10, pady = 5)

FrameDe.rowconfigure(0, weight = 1)
FrameDe.rowconfigure(1, weight = 1)
FrameDe.rowconfigure(2, weight = 1)
FrameDe.rowconfigure(3, weight = 1)

FrameDe.columnconfigure(0, weight = 1)
FrameDe.columnconfigure(1, weight = 1)
FrameDe.columnconfigure(2, weight = 1)

labelDe = tkinter.Label(master = FrameDe, bg = 'seashell2', text = 'De', font = ('Calibri', 9, 'bold', 'italic'))
labelDe.grid(row = 0, column = 0, sticky = 'W')

labelDeCX = tkinter.Label(master = FrameDe, bg = 'seashell2', text = 'X (Px)', font = ('Calibri', 9, 'bold', 'italic'))
labelDeCX.grid(row = 1, column = 1, sticky = 'N', pady = 5)

labelLIDe = tkinter.Label(master = FrameDe, text = 'L. Inferior', font = ('Calibri', 11, 'bold', 'italic'), bg = 'seashell2')
labelLIDe.grid(row = 2, column = 0, sticky = 'NSEW')

labelLSDe = tkinter.Label(master = FrameDe, text = 'L. Superior', font = ('Calibri', 11, 'bold', 'italic'), bg = 'seashell2')
labelLSDe.grid(row = 3, column = 0, sticky = 'NSEW')

entryLIDe = tkinter.Entry(master = FrameDe, width = 5)
entryLIDe.grid(row = 2, column = 1, sticky = 'NSEW', padx = 2, pady = 2)

entryLSDe = tkinter.Entry(master = FrameDe, width = 5)
entryLSDe.grid(row = 3, column = 1, sticky = 'NSEW', padx = 2, pady = 2)

buttonDibujarDe = tkinter.Button(master = FrameDe, image = palomita, command = dibujarDe, borderwidth = 1, relief = "solid", cursor = 'hand2')
buttonDibujarDe.grid(row = 2, column = 2, sticky = 'NSEW', padx = 2, pady = 2)

buttonLimpiarDe = tkinter.Button(master = FrameDe, image = bote, command = limpiarDe, borderwidth = 1, relief = "solid", cursor = 'hand2')
buttonLimpiarDe.grid(row = 3, column = 2, sticky = 'NSEW', padx = 2, pady = 2)

# Frame L.I Gota 

FrameLIGota = tkinter.Frame(master = p1)
FrameLIGota.config(bg = 'seashell2', borderwidth = 1, relief = "solid")
FrameLIGota.grid(row = 4, column = 1, sticky = 'NSEW', padx = 10, pady = 5)

FrameLIGota.rowconfigure(0, weight = 1)
FrameLIGota.rowconfigure(1, weight = 1)
FrameLIGota.rowconfigure(2, weight = 1)
FrameLIGota.rowconfigure(3, weight = 1)

FrameLIGota.columnconfigure(0, weight = 1)
FrameLIGota.columnconfigure(1, weight = 1)
FrameLIGota.columnconfigure(2, weight = 1)


labelGotaF = tkinter.Label(master = FrameLIGota, text = 'Gota', font = ('Calibri', 9, 'bold', 'italic'), bg = 'seashell2')
labelGotaF.grid(row = 0, column = 0, sticky = 'W')

labelLICY = tkinter.Label(master = FrameLIGota, text = 'Y (Px)', font = ('Calibri', 9, 'bold', 'italic'), bg = 'seashell2')
labelLICY.grid(row = 1, column = 1, sticky = 'N')

labelLIGota = tkinter.Label(master = FrameLIGota, text = 'L. Inferior', font = ('Calibri', 11, 'bold', 'italic'), bg = 'seashell2')
labelLIGota.grid(row = 2, column = 0, sticky = 'NSEW')

entryLIGota = tkinter.Entry(master = FrameLIGota, width = 5)
entryLIGota.grid(row = 2, column = 1, sticky = 'NSEW', padx = 2, pady = 2)

buttonDibujarLIGota = tkinter.Button(master = FrameLIGota, image = palomita, command = dibujarLIGota, borderwidth = 1, relief = "solid", cursor = 'hand2')
buttonDibujarLIGota.grid(row = 2, column = 2, sticky = 'NSEW', padx = 2, pady = 2)

buttonLimpiarLIGota = tkinter.Button(master = FrameLIGota, image = bote, command = limpiarLIGota, borderwidth = 1, relief = "solid", cursor = 'hand2')
buttonLimpiarLIGota.grid(row = 3, column = 2, sticky = 'NSEW', padx = 2, pady = 2)

# Frame Ds 

FrameDs = tkinter.Frame(master = p1)
FrameDs.config(bg = 'seashell2', borderwidth = 1, relief = "solid")
FrameDs.grid(row = 5, column = 1, sticky = 'NSEW', padx = 10, pady = 5)

FrameDs.rowconfigure(0, weight = 1)
FrameDs.rowconfigure(1, weight = 1)
FrameDs.rowconfigure(2, weight = 1)
FrameDs.rowconfigure(3, weight = 1)

FrameDs.columnconfigure(0, weight = 1)
FrameDs.columnconfigure(1, weight = 1)
FrameDs.columnconfigure(2, weight = 1)

labelDs = tkinter.Label(master = FrameDs, bg = 'seashell2', text = 'Ds', font = ('Calibri', 9, 'bold', 'italic'))
labelDs.grid(row = 0, column = 0, sticky = 'W')

labelDsCX = tkinter.Label(master = FrameDs, bg = 'seashell2', text = 'X (Px)', font = ('Calibri', 9, 'bold', 'italic'))
labelDsCX.grid(row = 1, column = 1, sticky = 'N')

labelLIDs = tkinter.Label(master = FrameDs, text = 'L. Inferior', font = ('Calibri', 11, 'bold', 'italic'), bg = 'seashell2')
labelLIDs.grid(row = 2, column = 0, sticky = 'NSEW')

labelLSDs = tkinter.Label(master = FrameDs, text = 'L. Superior', font = ('Calibri', 11, 'bold', 'italic'), bg = 'seashell2')
labelLSDs.grid(row = 3, column = 0, sticky = 'NSEW')

entryLIDs = tkinter.Entry(master = FrameDs, width = 5)
entryLIDs.grid(row = 2, column = 1, sticky = 'NSEW', padx = 2, pady = 2)

entryLSDs = tkinter.Entry(master = FrameDs, width = 5)
entryLSDs.grid(row = 3, column = 1, sticky = 'NSEW', padx = 2, pady = 2)

buttonDibujarDs = tkinter.Button(master = FrameDs, image = palomita, command = dibujarDs,  borderwidth = 1, relief = "solid", cursor = 'hand2')
buttonDibujarDs.grid(row = 2, column = 2, sticky = 'NSEW', padx = 2, pady = 2)

buttonLimpiarDs = tkinter.Button(master = FrameDs, image = bote, command = limpiarDs, borderwidth = 1, relief = "solid", cursor = 'hand2')
buttonLimpiarDs.grid(row = 3, column = 2, sticky = 'NSEW', padx = 2, pady = 2)

# Frame Dt 

FrameDt = tkinter.Frame(master = p1)
FrameDt.config(bg = 'seashell2', borderwidth = 1, relief = "solid")
FrameDt.grid(row = 6, column = 1, sticky = 'NSEW', padx = 10, pady = 5)

FrameDt.rowconfigure(0, weight = 1)
FrameDt.rowconfigure(1, weight = 1)
FrameDt.rowconfigure(2, weight = 1)
FrameDt.rowconfigure(3, weight = 1)

FrameDt.columnconfigure(0, weight = 1)
FrameDt.columnconfigure(1, weight = 1)
FrameDt.columnconfigure(2, weight = 1)

labelDt = tkinter.Label(master = FrameDt, bg = 'seashell2', text = 'Dt', font = ('Calibri', 9, 'bold', 'italic'))
labelDt.grid(row = 0, column = 0, sticky = 'W')

labelDtCX = tkinter.Label(master = FrameDt, bg = 'seashell2', text = 'X (Px)', font = ('Calibri', 9, 'bold', 'italic'))
labelDtCX.grid(row = 1, column = 1, sticky = 'N')

labelLIDt = tkinter.Label(master = FrameDt, text = 'L. Inferior', font = ('Calibri', 11, 'bold', 'italic'), bg = 'seashell2')
labelLIDt.grid(row = 2, column = 0, sticky = 'NSEW')

labelLSDt = tkinter.Label(master = FrameDt, text = 'L. Superior', font = ('Calibri', 11, 'bold', 'italic'), bg = 'seashell2')
labelLSDt.grid(row = 3, column = 0, sticky = 'NSEW')

entryLIDt = tkinter.Entry(master = FrameDt, width = 5)
entryLIDt.grid(row = 2, column = 1, sticky = 'NSEW', padx = 2, pady = 2)

entryLSDt = tkinter.Entry(master = FrameDt, width = 5)
entryLSDt.grid(row = 3, column = 1, sticky = 'NSEW', padx = 2, pady = 2)

buttonDibujarDt = tkinter.Button(master = FrameDt, image = palomita, command = dibujarDt, borderwidth = 1, relief = "solid", cursor = 'hand2')
buttonDibujarDt.grid(row = 2, column = 2, sticky = 'NSEW', padx = 2, pady = 2)

buttonLimpiarDt = tkinter.Button(master = FrameDt, image = bote, command = limpiarDt, borderwidth = 1, relief = "solid", cursor = 'hand2')
buttonLimpiarDt.grid(row = 3, column = 2, sticky = 'NSEW', padx = 2, pady = 2)

# Frame Análisis

FrameAnalisis = tkinter.Frame(master = p1)
FrameAnalisis.config(bg = 'seashell2', borderwidth = 1, relief = "solid")
FrameAnalisis.grid(row = 7, column = 1, sticky = 'NSEW', padx = 10, pady = 5) 

FrameAnalisis.rowconfigure(0, weight = 1)
FrameAnalisis.rowconfigure(1, weight = 1)

FrameAnalisis.columnconfigure(0, weight = 1)

buttonLimpiarImagen = tkinter.Button(master = FrameAnalisis, text = "Limpiar Análisis", font = ('Calibri', 10, 'bold', 'italic'), command = limpiarImagen, borderwidth = 1, relief = "solid", cursor = 'hand2')
buttonLimpiarImagen.grid(row = 1, column = 0,  sticky = 'NSEW', padx = 5, pady = 3 )

buttonAceptarAnalisis = tkinter.Button(master = FrameAnalisis, text = "Aceptar Análisis", font = ('Calibri', 10, 'bold', 'italic'), command = imagenParaGuardar, borderwidth = 1, relief = "solid", cursor = 'hand2')
buttonAceptarAnalisis.grid(row = 0, column = 0,  sticky = 'NSEW', padx = 5, pady = 3 )

# Frame Nombre de la Muestra

FrameNombreMuestra = tkinter.Frame(master = p1)
FrameNombreMuestra.config(bg = 'seashell2', borderwidth = 1, relief = "solid")
FrameNombreMuestra.grid(row = 2, column = 4, sticky = 'NSEW', padx = 10, pady = 5)

FrameNombreMuestra.rowconfigure(0, weight = 1)
FrameNombreMuestra.rowconfigure(1, weight = 1)

FrameNombreMuestra.columnconfigure(0, weight = 1 )
FrameNombreMuestra.columnconfigure(1, weight = 1 )
FrameNombreMuestra.columnconfigure(2, weight = 1 )
FrameNombreMuestra.columnconfigure(3, weight = 1 )

labelNombreMuestra = tkinter.Label(master = FrameNombreMuestra, text = 'ID de la muestra', font = ('Calibri', 12, 'bold', 'italic'  ), bg = 'seashell2'  )
labelNombreMuestra.grid(row = 0, column = 1, sticky = 'NSEW', pady = 5 )

EntryNombreMuestra = tkinter.Entry(master = FrameNombreMuestra, width = 5)
EntryNombreMuestra.grid(row = 1, column = 1, sticky = 'NSEW', padx = 5, pady = 5 )

buttonAceptarNombre = tkinter.Button(master = FrameNombreMuestra, command = aceptarNombre, image = palomita, borderwidth = 1, relief = "solid", cursor = 'hand2')
buttonAceptarNombre.grid(row = 1, column = 2, sticky = 'NSEW', padx = 5, pady = 5)

# Frame Datos 

FrameDatos = tkinter.Frame(master = p1)
FrameDatos.config(bg = 'seashell2', borderwidth = 1, relief = "solid")
FrameDatos.grid(row = 3, column = 4, rowspan = 3, sticky = 'NSEW', padx = 10, pady = 5)

FrameDatos.rowconfigure(0, weight = 1)
FrameDatos.rowconfigure(1, weight = 1)
FrameDatos.rowconfigure(2, weight = 1)
FrameDatos.rowconfigure(3, weight = 1)
FrameDatos.rowconfigure(4, weight = 1)
FrameDatos.rowconfigure(5, weight = 1)
FrameDatos.rowconfigure(6, weight = 1)
FrameDatos.rowconfigure(7, weight = 1)

FrameDatos.columnconfigure(0, weight = 1)
FrameDatos.columnconfigure(1, weight = 1)
FrameDatos.columnconfigure(2, weight = 1)
FrameDatos.columnconfigure(3, weight = 1)


labelDatos = tkinter.Label(master = FrameDatos, text = 'Datos', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelDatos.grid(row = 0, column = 0, columnspan = 2, sticky = 'NW')

labeldTPx = tkinter.Label(master = FrameDatos, text = 'Dt en Px', font = ('Calibri', 12, 'bold', 'italic'  ), bg = 'seashell2')
labeldTPx.grid(row = 1, column = 1, sticky = 'NSEW', padx = 5, pady = 6)

entrydTPx = tkinter.Entry(master = FrameDatos, textvariable = varAuxDt, width = 5)
entrydTPx.grid(row = 1, column = 2, sticky = 'NSEW', padx = 5, pady = 6)

labeldTCm = tkinter.Label(master = FrameDatos, text = 'Dt en Cm', font = ('Calibri', 12, 'bold', 'italic' ), bg = 'seashell2')
labeldTCm.grid(row = 2, column = 1, sticky = 'NSEW', padx = 5, pady = 6)

entrydTCm = tkinter.Entry(master = FrameDatos, width = 5)
entrydTCm.grid(row = 2, column = 2, sticky = 'NSEW', padx = 5, pady = 6)

labeldEPx = tkinter.Label(master = FrameDatos, text = 'De en Px', font = ('Calibri', 12, 'bold', 'italic'), bg = 'seashell2')
labeldEPx.grid(row = 3, column = 1, sticky = 'NSEW', padx = 5, pady = 6)

entrydEPx = tkinter.Entry(master = FrameDatos, textvariable = varAuxDe, width = 5) 
entrydEPx.grid(row = 3, column = 2, sticky = 'NSEW', padx = 5, pady = 6)

labeldSPx = tkinter.Label(master = FrameDatos, text = 'Ds en Px', font = ('Calibri', 12, 'bold', 'italic'), bg = 'seashell2')
labeldSPx.grid(row = 4, column = 1, sticky = 'NSEW', padx = 5, pady = 6)

entrydSPx = tkinter.Entry(master = FrameDatos, textvariable = varAuxDs, width = 5)
entrydSPx.grid(row = 4, column = 2, sticky = 'NSEW', padx = 5, pady = 6)

labeldWater = tkinter.Label(master = FrameDatos, text = 'dW en gr/cm\u00B3', font = ('calibri', 12, 'bold', 'italic'), bg = 'seashell2')
labeldWater.grid(row = 5, column = 1, sticky = 'NSEW', padx = 5, pady = 6)

entrydWater = tkinter.Entry(master = FrameDatos, width = 5)
entrydWater.grid(row = 5, column = 2, sticky = 'NSEW', padx = 5, pady = 6)

labeldOil = tkinter.Label(master = FrameDatos, text = 'dO en gr/cm\u00B3', font = ('Calibri', 12, 'bold', 'italic'), bg = 'seashell2')
labeldOil.grid(row = 6, column = 1, sticky = 'NSEW', padx = 5, pady = 6)

entrydOil = tkinter.Entry(master = FrameDatos, width = 5)
entrydOil.grid(row = 6, column = 2, sticky = 'NSEW', padx = 5, pady = 6)

labelPalabraTIF = tkinter.Label(master = FrameDatos, text = 'Tensión en din/cm\u00B2', font = ('Calibri', 12, 'bold', 'italic'), bg = 'seashell2')
labelPalabraTIF.grid(row = 7, column = 1, sticky = 'NSEW', padx = 5, pady = 25)

labelResulTIF = tkinter.Entry(master = FrameDatos, textvariable = VarAuxTIF, font = ('Calibri', 12, 'bold', 'italic'), width = 8, justify = 'center')
labelResulTIF.grid(row = 7, column = 2, sticky = 'NSEW', padx = 5, pady = 25)

# Frame Botones Derecha 

FrameBotonesDerecha = tkinter.Frame(master = p1)
FrameBotonesDerecha.config(bg = 'seashell2', borderwidth = 1, relief = "solid")
FrameBotonesDerecha.grid(row = 6, column = 4, rowspan = 2, sticky = 'NSEW', padx = 10, pady = 5)

FrameBotonesDerecha.rowconfigure(0, weight = 1)
FrameBotonesDerecha.rowconfigure(1, weight = 1)
FrameBotonesDerecha.rowconfigure(2, weight = 1)
FrameBotonesDerecha.rowconfigure(3, weight = 1)
FrameBotonesDerecha.rowconfigure(4, weight = 1)
FrameBotonesDerecha.rowconfigure(5, weight = 1)

FrameBotonesDerecha.columnconfigure(0, weight = 1)

labelPHT = tkinter.Label(master = FrameBotonesDerecha, text = 'Panel de Herramientas', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2'  )
labelPHT.grid(row = 0, column = 0, sticky = 'NSEW')

botonAbrirImagen = tkinter.Button(master = FrameBotonesDerecha, text = 'Abrir Imagen', font = ('Calibri', 10, 'bold', 'italic'), command = abrirImagen , cursor = 'hand2', relief = "solid", borderwidth = 1)
botonAbrirImagen.grid(row = 1, column = 0, sticky = 'NSEW', padx = 5, pady = 2)

botonCalcular = tkinter.Button(master = FrameBotonesDerecha, text = 'Calcular Tensión', font = ('Calibri', 10, 'bold', 'italic'), command = calcularTIF, cursor = 'hand2', relief = "solid", borderwidth = 1)
botonCalcular.grid(row = 2, column = 0, sticky = 'NSEW', padx = 5, pady = 2)

botonArchivoNuevo = tkinter.Button(master = FrameBotonesDerecha, text = 'Archivo Nuevo', font = ('Calibri', 10, 'bold', 'italic'), command = generarArchivo, cursor = 'hand2', relief = "solid", borderwidth = 1)
botonArchivoNuevo.grid(row = 3, column = 0, sticky = 'NSEW', padx = 5, pady = 2)

botonIngresarLectura = tkinter.Button(master = FrameBotonesDerecha, text = 'Anexar Lectura', font = ('Calibri', 10, 'bold', 'italic'), command = ingresarLectura, cursor = 'hand2', relief = "solid", borderwidth = 1)
botonIngresarLectura.grid(row = 4, column = 0, sticky = 'NSEW', padx = 5, pady = 2)

botonLimpiarPantalla = tkinter.Button(master = FrameBotonesDerecha, text = 'Limpiar Pantalla', font = ('Calibri', 10, 'bold', 'italic'), command = limpiar, cursor = 'hand2', relief = "solid", borderwidth = 1)
botonLimpiarPantalla.grid(row = 5, column = 0, sticky = 'NSEW', padx = 5, pady = 2)


# sección de la interfaz gráfica que pertenece a la Ángulo tab 

# figura y Canvas en la interfaz

fig2 = plt.Figure(figsize=(5, 4), dpi = 100) 
ax2 = fig2.subplots()
ax2.set_xlabel('Pixeles', size = 10)
ax2.set_ylabel('Pixeles', size = 10)
ax2.autoscale_view(tight = False, scalex = False, scaley = False)
canvas2 = FigureCanvasTkAgg(fig2, master = p2)                                 
canvas2.get_tk_widget().grid(row = 1, column = 2, rowspan =  5, columnspan = 2, sticky = 'NSEW', padx = 30, pady = 10)
canvas2.draw()
cursor2 = Cursor(ax2, useblit = True, color = 'r', lw = 0.5)

# barra de herramientas 

# Frame Toolbar

FrameTBarA = tkinter.Frame(master = p2) 
FrameTBarA.config(borderwidth = 1, relief = "solid") 
FrameTBarA.grid(row = 6, column = 1, columnspan = 4, sticky = 'NSEW', padx = 10, pady = 5)

toolbar2 = NavigationToolbar2Tk(canvas2, FrameTBarA) 
toolbar2.update()

# Imagen de la gota roja.

labelImageA = tkinter.Label(master = p2, image = imagenGota)
labelImageA.grid(row = 0 , column = 2, sticky = 'E', ipady = 15)

# Label  Titulo

labelTituloA = tkinter.Label(master = p2, text = 'Ángulo con el método de la Gota pendiente', font = ('Calibri light', 13, 'bold'))
labelTituloA.grid(row = 0 , column = 3, sticky = 'W', ipady = 15)

# Frame Colores 

FrameColores2 = tkinter.Frame(master = p2)
FrameColores2.config(bg = 'seashell2', borderwidth = 1, relief = "solid") 
FrameColores2.grid(row = 1, column = 1, sticky = 'NSEW', padx = 10, pady = 10) 

FrameColores2.rowconfigure(0, weight = 1)
FrameColores2.rowconfigure(1, weight = 1)

FrameColores2.columnconfigure(0, weight = 1)
FrameColores2.columnconfigure(1, weight = 1)
FrameColores2.columnconfigure(2, weight = 1)
FrameColores2.columnconfigure(3, weight = 1)

labelGota2 = tkinter.Label(master = FrameColores2, text = 'Gota', font = ('Calibri', 9, 'bold', 'italic'), bg = 'seashell2' )
labelGota2.grid(row = 0, column = 0, sticky = 'W') 

labelColor2 = tkinter.Label(master = FrameColores2, text = 'Colores', font = ('Calibri', 11, 'bold', 'italic'), bg = 'seashell2' )
labelColor2.grid(row = 1, column = 0, sticky = 'NSEW', padx = 2, pady = 5, ipady = 3) 

buttonVisualizarImagenColor2 = tkinter.Button(master = FrameColores2, image = gotaColor, command = visualizarImagenColor2, borderwidth = 1, relief = 'solid', cursor = 'hand2')
buttonVisualizarImagenColor2.grid(row = 1, column = 1, sticky = 'NSEW', padx = 2, pady = 5, ipady = 5)

buttonVisualizarImagenBYN2 = tkinter.Button(master = FrameColores2, image = gotaNegra, command = visualizarImagenBYN2, borderwidth = 1, relief = 'solid', cursor = 'hand2')
buttonVisualizarImagenBYN2.grid(row = 1, column = 2, sticky = 'NSEW', padx = 2, pady = 5, ipady = 5)

buttonVisualizarBordes2 = tkinter.Button(master = FrameColores2, image = gotaBorde, command = visualizarBorde2, borderwidth = 1, relief = 'solid', cursor = 'hand2' ) 
buttonVisualizarBordes2.grid(row = 1, column = 3, sticky = 'NSEW', padx = 2, pady = 5, ipady = 5)

# Frame Rotar Imagen 

FrameRotarImagen2 = tkinter.Frame(master = p2)
FrameRotarImagen2.config(bg = 'seashell2', borderwidth = 1, relief = "solid")
FrameRotarImagen2.grid(row = 2, column = 1, sticky = 'NSEW', padx = 10, pady = 10)

FrameRotarImagen2.rowconfigure(0, weight = 1)
FrameRotarImagen2.rowconfigure(1, weight = 1)

FrameRotarImagen2.columnconfigure(0, weight = 1)
FrameRotarImagen2.columnconfigure(1, weight = 1)
FrameRotarImagen2.columnconfigure(2, weight = 1)

labelRotarImagen2 = tkinter.Label(master = FrameRotarImagen2, bg = 'seashell2', text = 'Rotar', font = ('Calibri', 9, 'bold', 'italic'))
labelRotarImagen2.grid(row = 0, column = 0, sticky = 'W')

labelGradosImagen2 = tkinter.Label(master = FrameRotarImagen2, bg = 'seashell2', text = 'Grados', font = ('Calibri', 11, 'bold', 'italic'))
labelGradosImagen2.grid(row = 1, column = 0, sticky = 'NSEW')

entryRotarImagen2 = tkinter.Entry(master = FrameRotarImagen2, width = 5)
entryRotarImagen2.grid(row = 1, column = 1, sticky = 'NSEW', padx = 2, pady = 5)

buttonRotarImagen2 = tkinter.Button(master = FrameRotarImagen2, image = palomita, command = rotarImagen2, borderwidth = 1, relief = 'solid', cursor = 'hand2' )
buttonRotarImagen2.grid(row = 1, column = 2, sticky = 'NSEW', padx = 2, pady = 5)

# Frame ángulo Izquierdo 

FrameAI = tkinter.Frame(master = p2) 
FrameAI.config(bg = 'seashell2', borderwidth = 1, relief = "solid")
FrameAI.grid(row = 3, column = 1, sticky = 'NSEW', padx = 10, pady = 10)

FrameAI.rowconfigure(0, weight = 1)
FrameAI.rowconfigure(1, weight = 1)
FrameAI.rowconfigure(2, weight = 1)
FrameAI.rowconfigure(3, weight = 1)
FrameAI.rowconfigure(4, weight = 1)

FrameAI.columnconfigure(0, weight = 1)
FrameAI.columnconfigure(1, weight = 1)
FrameAI.columnconfigure(2, weight = 1)
FrameAI.columnconfigure(3, weight = 1)
FrameAI.columnconfigure(4, weight = 1)


labelAI = tkinter.Label(master = FrameAI, text = 'Áng. Izq.', font = ('Calibri', 9, 'bold', 'italic'), bg = 'seashell2')
labelAI.grid(row = 0, column = 0, sticky = 'W')

labelPSAI = tkinter.Label(master = FrameAI, text = 'P.S', font = ('Calibri', 11, 'bold', 'italic'), bg = 'seashell2')
labelPSAI.grid(row = 2, column = 0, sticky = 'NSEW')

labelPIAI = tkinter.Label(master = FrameAI, text = 'P.I', font = ('Calibri', 11, 'bold', 'italic'), bg = 'seashell2')
labelPIAI.grid(row = 3, column = 0, sticky = 'NSEW')

labelXCAI = tkinter.Label(master = FrameAI, text = 'X (Px)', font = ('Calibri', 9, 'bold', 'italic'), bg = 'seashell2')
labelXCAI.grid(row = 1, column = 1, sticky = 'NSEW', pady = 5)

labelYCAI = tkinter.Label(master = FrameAI, text = 'Y (Px)', font = ('Calibri', 9, 'bold', 'italic'), bg = 'seashell2')
labelYCAI.grid(row = 1, column = 2, sticky = 'NSEW', pady = 5 )

labelPAAI = tkinter.Label(master = FrameAI, text = 'Probar Análisis', font = ('Calibri', 9, 'bold', 'italic'), bg = 'seashell2')
labelPAAI.grid(row = 4, column = 1, columnspan = 2, sticky = 'NSEW', pady = 5)

entryPSAIX = tkinter.Entry(master = FrameAI, width = 5)
entryPSAIX.grid(row = 2, column = 1, sticky = 'NSEW', padx = 2, pady = 2)

entryPSAIY = tkinter.Entry(master = FrameAI, width = 5)
entryPSAIY.grid(row = 2, column = 2, sticky = 'NSEW', padx = 2, pady = 2)

entryPIAIX = tkinter.Entry(master = FrameAI, width = 5)
entryPIAIX.grid(row = 3, column = 1, sticky = 'NSEW', padx = 2, pady = 2) 

entryPIAIY = tkinter.Entry(master = FrameAI, width = 5)
entryPIAIY.grid(row = 3, column = 2, sticky = 'NSEW', padx = 2, pady = 2)

buttonDibujarPSAI = tkinter.Button(master = FrameAI, command = dibujarPSAI, image = palomita, borderwidth = 1, relief = 'solid', cursor = 'hand2' )
buttonDibujarPSAI.grid(row = 2, column = 3, sticky = 'NSEW', padx = 2, pady = 2)

buttonDibujarPIAI = tkinter.Button(master = FrameAI, command = dibujarPIAI, image = palomita, borderwidth = 1, relief = 'solid', cursor = 'hand2' )
buttonDibujarPIAI.grid(row = 3, column = 3, sticky = 'NSEW', padx = 2, pady = 2 )

buttonBorrarPSAI = tkinter.Button(master = FrameAI, image = bote, command = limpiarPSAI, borderwidth = 1, relief = 'solid', cursor = 'hand2' )
buttonBorrarPSAI.grid(row = 2, column = 4, sticky = 'NSEW', padx = 2, pady = 2)

buttonBorrarPIAI = tkinter.Button(master = FrameAI, image = bote, command = limpiarPIAI, borderwidth = 1, relief = 'solid', cursor = 'hand2')
buttonBorrarPIAI.grid(row = 3, column = 4, sticky = 'NSEW', padx = 2, pady = 2)

buttonProbarAAI = tkinter.Button(master = FrameAI, image = palomita, command = probarAnalisisAI, borderwidth = 1, relief = 'solid', cursor = 'hand2' )
buttonProbarAAI.grid(row = 4, column = 3, sticky = 'NSEW', padx = 2, pady = 5)

buttonBorrarAAI = tkinter.Button(master = FrameAI, image = bote, command = limpiarProbarAnalisisAI, borderwidth = 1, relief = 'solid', cursor = 'hand2' )
buttonBorrarAAI.grid(row = 4, column = 4, sticky = 'NSEW', padx = 2, pady = 5)

# Frame Ángulo Derecho 

FrameAD = tkinter.Frame(master = p2) 
FrameAD.config(bg = 'seashell2', borderwidth = 1, relief = "solid")
FrameAD.grid(row = 4, column = 1, sticky = 'NSEW', padx = 10, pady = 10) 

FrameAD.rowconfigure(0, weight = 1)
FrameAD.rowconfigure(1, weight = 1)
FrameAD.rowconfigure(2, weight = 1)
FrameAD.rowconfigure(3, weight = 1)
FrameAD.rowconfigure(4, weight = 1)

FrameAD.columnconfigure(0, weight = 1)
FrameAD.columnconfigure(1, weight = 1)
FrameAD.columnconfigure(2, weight = 1)
FrameAD.columnconfigure(3, weight = 1)
FrameAD.columnconfigure(4, weight = 1)

labelAD = tkinter.Label(master = FrameAD, text = 'Áng. Dere.', font = ('Calibri', 9, 'bold', 'italic'), bg = 'seashell2')
labelAD.grid(row = 0, column = 0, sticky = 'W')

labelPSAD = tkinter.Label(master = FrameAD, text = 'P.S', font = ('Calibri', 11, 'bold', 'italic'), bg = 'seashell2')
labelPSAD.grid(row = 2, column = 0, sticky = 'NSEW')

labelPIAD = tkinter.Label(master = FrameAD, text = 'P.I', font = ('Calibri', 11, 'bold', 'italic'), bg = 'seashell2')
labelPIAD.grid(row = 3, column = 0, sticky = 'NSEW')

labelXCAD = tkinter.Label(master = FrameAD, text = 'X (Px)', font = ('Calibri', 9, 'bold', 'italic'), bg = 'seashell2')
labelXCAD.grid(row = 1, column = 1, sticky = 'NSEW', pady = 5) 

labelYCAD = tkinter.Label(master = FrameAD, text = 'Y (Px)', font = ('Calibri', 9, 'bold', 'italic'), bg = 'seashell2')
labelYCAD.grid(row = 1, column = 2, sticky = 'NSEW', pady = 5 ) 

labelPAAD = tkinter.Label(master = FrameAD, text = 'Probar Análisis', font = ('Calibri', 9, 'bold', 'italic'), bg = 'seashell2')
labelPAAD.grid(row = 4, column = 1, columnspan = 2, sticky = 'NSEW', pady = 5)

entryPSADX = tkinter.Entry(master = FrameAD, width = 5)
entryPSADX.grid(row = 2, column = 1, sticky = 'NSEW', padx = 2, pady = 2)

entryPSADY = tkinter.Entry(master = FrameAD, width = 5)
entryPSADY.grid(row = 2, column = 2, sticky = 'NSEW', padx = 2, pady = 2)

entryPIADX = tkinter.Entry(master = FrameAD, width = 5)
entryPIADX.grid(row = 3, column = 1, sticky = 'NSEW', padx = 2, pady = 2)

entryPIADY = tkinter.Entry(master = FrameAD, width = 5)
entryPIADY.grid(row = 3, column = 2, sticky = 'NSEW', padx = 2, pady = 2)

buttonDibujarPSAD = tkinter.Button(master = FrameAD, command = dibujarPSAD, image = palomita, borderwidth = 1, relief = 'solid', cursor = 'hand2' )
buttonDibujarPSAD.grid(row = 2, column = 3, sticky = 'NSEW', padx = 2, pady = 2)

buttonDibujarPIAD = tkinter.Button(master = FrameAD, command = dibujarPIAD, image = palomita, borderwidth = 1, relief = 'solid', cursor = 'hand2' )
buttonDibujarPIAD.grid(row = 3, column = 3, sticky = 'NSEW', padx = 2, pady = 2 )

buttonBorrarPSAD = tkinter.Button(master = FrameAD, image = bote, command = limpiarPSAD, borderwidth = 1, relief = 'solid', cursor = 'hand2' )
buttonBorrarPSAD.grid(row = 2, column = 4, sticky = 'NSEW', padx = 2, pady = 2)

buttonBorrarPIAD = tkinter.Button(master = FrameAD, image = bote, command = limpiarPIAD, borderwidth = 1, relief = 'solid', cursor = 'hand2' )
buttonBorrarPIAD.grid(row = 3, column = 4, sticky = 'NSEW', padx = 2, pady = 2)

buttonProbarAAD = tkinter.Button(master = FrameAD, image = palomita, command = probarAnalisisAD, borderwidth = 1, relief = 'solid', cursor = 'hand2' )
buttonProbarAAD.grid(row = 4, column = 3, sticky = 'NSEW', padx = 2, pady = 5) 

buttonBorrarAAD = tkinter.Button(master = FrameAD, image = bote, command = limpiarProbarAnalisisAD, borderwidth = 1, relief = 'solid', cursor = 'hand2' )
buttonBorrarAAD.grid(row = 4, column = 4, sticky = 'NSEW', padx = 2, pady = 5) 

# Frame Reporte Ángulo

FrameRA = tkinter.Frame(master = p2) 
FrameRA.config(bg = 'seashell2', borderwidth = 1, relief = "solid")
FrameRA.grid(row = 5, column = 1, sticky = 'NSEW', padx = 10, pady = 10)

FrameRA.rowconfigure(0, weight = 1)
FrameRA.rowconfigure(1, weight = 1)
FrameRA.rowconfigure(2, weight = 1)
FrameRA.rowconfigure(3, weight = 1)

FrameRA.columnconfigure(0, weight = 1)
FrameRA.columnconfigure(1, weight = 1)
FrameRA.columnconfigure(2, weight = 1)

labelRA = tkinter.Label(master = FrameRA, text = 'Reporte', font = ('Calibri', 9, 'bold', 'italic'), bg = 'seashell2')
labelRA.grid(row = 0, column = 0, sticky = 'W')

labelPS = tkinter.Label(master = FrameRA, text = 'P.S', font = ('Calibri', 11, 'bold', 'italic'), bg = 'seashell2')
labelPS.grid(row = 2, column = 0, sticky = 'NSEW')

labelPI = tkinter.Label(master = FrameRA, text = 'P.I', font = ('Calibri', 11, 'bold', 'italic'), bg = 'seashell2')
labelPI.grid(row = 3, column = 0, sticky = 'NSEW')

labelYP = tkinter.Label(master = FrameRA, text = 'Y (Px)', font = ('Calibri', 9, 'bold', 'italic'), bg = 'seashell2')
labelYP.grid(row = 1, column = 1, sticky = 'NSEW', pady = 5)

entryYPSV = tkinter.Entry(master = FrameRA, width = 5)
entryYPSV.grid(row = 2, column = 1, sticky = 'NSEW', padx = 2, pady = 2)

entryYPIV = tkinter.Entry(master = FrameRA, width = 5)
entryYPIV.grid(row = 3, column = 1, sticky = 'NSEW', padx = 2, pady = 2)

buttonDibujarRA = tkinter.Button(master = FrameRA, command = RA, text = 'Aceptar Análisis' , borderwidth = 1, relief = 'solid', cursor = 'hand2', font = ('Calibri', 10, 'bold', 'italic'))
buttonDibujarRA.grid(row = 2, column = 2, sticky = 'NSEW', padx = 2, pady = 2) 

buttonLimpiarRA = tkinter.Button(master = FrameRA, command = limpiarRA, text = 'Limpiar Análisis', borderwidth = 1, relief = 'solid', cursor = 'hand2', font = ('Calibri', 10, 'bold', 'italic'))
buttonLimpiarRA.grid(row = 3, column = 2, sticky = 'NSEW', padx = 2, pady = 2) 

# Frame Nombre de la Muestra 

FrameNombreMuestraA = tkinter.Frame(master = p2)
FrameNombreMuestraA.config(bg = 'seashell2', borderwidth = 1, relief = "solid")
FrameNombreMuestraA.grid(row = 2, column = 4, sticky = 'NSEW', padx = 10, pady = 10)

FrameNombreMuestraA.rowconfigure(0, weight = 1)
FrameNombreMuestraA.rowconfigure(1, weight = 1)

FrameNombreMuestraA.columnconfigure(0, weight = 1 )
FrameNombreMuestraA.columnconfigure(1, weight = 1 )
FrameNombreMuestraA.columnconfigure(2, weight = 1 )
FrameNombreMuestraA.columnconfigure(3, weight = 1 )
FrameNombreMuestraA.columnconfigure(4, weight = 1 )

labelNombreMuestraA = tkinter.Label(master = FrameNombreMuestraA, text = 'ID de la muestra', font = ('Calibri', 12, 'bold', 'italic'  ), bg = 'seashell2')
labelNombreMuestraA.grid(row = 0, column = 1, sticky = 'NSEW', pady = 2 )

EntryNombreMuestraA = tkinter.Entry(master = FrameNombreMuestraA)
EntryNombreMuestraA.grid(row = 1, column = 1, sticky = 'NSEW', padx = 2, pady = 5 )

buttonAceptarNombreA = tkinter.Button(master = FrameNombreMuestraA, command = aceptarNombreA, image = palomita, borderwidth = 1, relief = "solid", cursor = 'hand2')
buttonAceptarNombreA.grid(row = 1, column = 2, sticky = 'NSEW', padx = 2, pady = 5)

# Frame Fecha y Hora de la muestra

FrameFHMuestraA = tkinter.Frame(master = p2)
FrameFHMuestraA.config(bg = 'seashell2', borderwidth = 1, relief = "solid")
FrameFHMuestraA.grid(row = 3, column = 4, sticky = 'NSEW', padx = 10, pady = 10)

FrameFHMuestraA.rowconfigure(0, weight = 1)
FrameFHMuestraA.rowconfigure(1, weight = 1)
FrameFHMuestraA.rowconfigure(2, weight = 1)
FrameFHMuestraA.rowconfigure(3, weight = 1)
FrameFHMuestraA.rowconfigure(4, weight = 1)
FrameFHMuestraA.rowconfigure(5, weight = 1)

FrameFHMuestraA.columnconfigure(0, weight = 1 )
FrameFHMuestraA.columnconfigure(1, weight = 1 )
FrameFHMuestraA.columnconfigure(2, weight = 1 )
FrameFHMuestraA.columnconfigure(3, weight = 1 )
FrameFHMuestraA.columnconfigure(4, weight = 1 )

labelFechaMuestraA = tkinter.Label(master = FrameFHMuestraA, text = 'Fecha de la toma ', font = ('Calibri', 12, 'bold', 'italic'  ), bg = 'seashell2'  )
labelFechaMuestraA.grid(row = 2, column = 1, sticky = 'NSEW', pady = 2)

labelFormatoFechaA = tkinter.Label(master = FrameFHMuestraA, text = 'DD/MM/AAAA', font = ('Calibri', 8, 'bold', 'italic'  ), bg = 'seashell2'  )
labelFormatoFechaA.grid(row = 3, column = 1, sticky = 'NSEW')

EntryFechaMuestraA = tkinter.Entry(master = FrameFHMuestraA, width = 5)
EntryFechaMuestraA.grid(row = 4, column = 1, sticky = 'NSEW', padx = 2, pady = 2)

buttonAceptarFechaA = tkinter.Button(master = FrameFHMuestraA, command = aceptarFechaA, image = palomita, borderwidth = 1, relief = "solid", cursor = 'hand2')
buttonAceptarFechaA.grid(row = 4, column = 2, sticky = 'NSEW', padx = 2, pady = 2)

buttonBorrarFechaA = tkinter.Button(master = FrameFHMuestraA, command = borrarFechaA, image = bote, borderwidth = 1, relief = 'solid', cursor = 'hand2' )
buttonBorrarFechaA.grid(row = 4, column = 3, sticky = 'NSEW', padx = 2, pady = 2)

labelHoraMuestraA = tkinter.Label(master = FrameFHMuestraA, text = 'Hora de la toma ', font = ('Calibri', 12, 'bold', 'italic'  ), bg = 'seashell2'  )
labelHoraMuestraA.grid(row = 5, column = 1, sticky = 'NSEW', pady = 2)

labelFormatoHoraA = tkinter.Label(master = FrameFHMuestraA, text = 'HH:MM:SS', font = ('Calibri', 8, 'bold', 'italic'  ), bg = 'seashell2'  )
labelFormatoHoraA.grid(row = 6, column = 1, sticky = 'NSEW')

EntryHoraMuestraA = tkinter.Entry(master = FrameFHMuestraA, width = 5)
EntryHoraMuestraA.grid(row = 7, column = 1, sticky = 'NSEW', padx = 2, pady = 5)

buttonAceptarHoraA = tkinter.Button(master = FrameFHMuestraA, image = palomita, command = aceptarHoraA, borderwidth = 1, relief = "solid", cursor = 'hand2')
buttonAceptarHoraA.grid(row = 7, column = 2, sticky = 'NSEW', padx = 2, pady = 5)

buttonBorrarHoraA = tkinter.Button(master = FrameFHMuestraA, image = bote, command = borrarHoraA, borderwidth = 1, relief = 'solid', cursor = 'hand2' )
buttonBorrarHoraA.grid(row = 7, column = 3, sticky = 'NSEW', padx = 2, pady = 5)

# Frame Botones Derecha 

FrameBotonesDerecha2 = tkinter.Frame(master = p2) 
FrameBotonesDerecha2.config(bg = 'seashell2', borderwidth = 1, relief = "solid")
FrameBotonesDerecha2.grid(row = 4, column = 4, sticky = 'NSEW', padx = 10, pady = 10)

FrameBotonesDerecha2.rowconfigure(0, weight = 1)
FrameBotonesDerecha2.rowconfigure(1, weight = 1)
FrameBotonesDerecha2.rowconfigure(2, weight = 1)
FrameBotonesDerecha2.rowconfigure(3, weight = 1)
FrameBotonesDerecha2.rowconfigure(4, weight = 1)
FrameBotonesDerecha2.columnconfigure(0, weight = 1)

labelPHA = tkinter.Label(master = FrameBotonesDerecha2, text = 'Panel de Herramientas', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelPHA.grid(row = 0, column = 0, sticky = 'NSEW', pady = 2)

botonAbrirImagen2 = tkinter.Button(master = FrameBotonesDerecha2, text = 'Abrir Imagen', font = ('Calibri', 10, 'bold', 'italic'), command = abrirImagen2, cursor = 'hand2', relief = "solid", borderwidth = 1)
botonAbrirImagen2.grid(row = 1, column = 0,  sticky = 'NSEW', padx = 5, pady = 3)

botonArchivoNuevoA = tkinter.Button(master = FrameBotonesDerecha2, text = 'Archivo Nuevo', command = generarArchivoA, font = ('Calibri', 10, 'bold', 'italic'), cursor = 'hand2', relief = "solid", borderwidth = 1)
botonArchivoNuevoA.grid(row = 2, column = 0,  sticky = 'NSEW', padx = 5, pady = 3)

botonIngresarLecturaA = tkinter.Button(master = FrameBotonesDerecha2, text = 'Anexar Lectura', command = ingresarLecturaA, font = ('Calibri', 10, 'bold', 'italic'), cursor = 'hand2', relief = "solid", borderwidth = 1)
botonIngresarLecturaA.grid(row = 3, column = 0,  sticky = 'NSEW', padx = 5, pady = 3)

botonLimpiarPantallaA = tkinter.Button(master = FrameBotonesDerecha2, text = 'Limpiar Pantalla', command = limpiarA, font = ('Calibri', 10, 'bold', 'italic'), cursor = 'hand2', relief = "solid", borderwidth = 1)
botonLimpiarPantallaA.grid(row = 4, column = 0,  sticky = 'NSEW', padx = 5, pady = 3)


# sección de la interfaz gráfica que pertenece a la resumen tab 

# Resumen TIF

# Label  Titulo

labelTitulo = tkinter.Label(master = p3, text = 'Resumen del análisis de la Tensión', font = ('Calibri light', 13, 'bold'))
labelTitulo.grid(row = 0, column = 3, sticky = 'W', ipady = 15)

# Imagen de la gota roja.

labelImage = tkinter.Label(master = p3, image = imagenGota)
labelImage.grid(row = 0, column = 1, columnspan = 2, sticky = 'E', ipady = 15) 

# Frame Resumen TIF

FrameResumenTIF = tkinter.Frame(master = p3)
FrameResumenTIF.config(bg = 'seashell2', borderwidth = 1, relief = "solid")
FrameResumenTIF.grid(row = 1, column = 1, columnspan = 4, sticky = 'NSEW')

FrameResumenTIF.rowconfigure(0, weight = 1)
FrameResumenTIF.rowconfigure(1, weight = 1)
FrameResumenTIF.rowconfigure(2, weight = 1)
FrameResumenTIF.rowconfigure(3, weight = 1)
FrameResumenTIF.rowconfigure(4, weight = 1)
FrameResumenTIF.rowconfigure(5, weight = 1)
FrameResumenTIF.rowconfigure(6, weight = 1)
FrameResumenTIF.rowconfigure(7, weight = 1)
FrameResumenTIF.rowconfigure(8, weight = 1)
FrameResumenTIF.rowconfigure(9, weight = 1)
FrameResumenTIF.rowconfigure(10, weight = 1)
FrameResumenTIF.rowconfigure(11, weight = 1)

FrameResumenTIF.columnconfigure(0, weight = 1)
FrameResumenTIF.columnconfigure(1, weight = 1)
FrameResumenTIF.columnconfigure(2, weight = 1)
FrameResumenTIF.columnconfigure(3, weight = 1)
FrameResumenTIF.columnconfigure(4, weight = 1)
FrameResumenTIF.columnconfigure(5, weight = 1)
FrameResumenTIF.columnconfigure(6, weight = 1)
FrameResumenTIF.columnconfigure(7, weight = 1)
FrameResumenTIF.columnconfigure(8, weight = 1)
FrameResumenTIF.columnconfigure(9, weight = 1)
FrameResumenTIF.columnconfigure(10, weight = 1)
FrameResumenTIF.columnconfigure(11, weight = 1)
FrameResumenTIF.columnconfigure(12, weight = 1)
FrameResumenTIF.columnconfigure(13, weight = 1)
FrameResumenTIF.columnconfigure(14, weight = 1)

labelNombreMuestraRTIF = tkinter.Label(master = FrameResumenTIF, text = 'ID de la muestra', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelNombreMuestraRTIF.grid(row = 0, column = 1, sticky = 'NSEW', pady = 10)

labelAnguloMuestraRTIF = tkinter.Label(master = FrameResumenTIF, text = 'Ángulo (°)', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelAnguloMuestraRTIF.grid(row = 0, column = 2, sticky = 'NSEW', pady = 10)

labelDeRTIF = tkinter.Label(master = FrameResumenTIF, text = 'De (Px)', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelDeRTIF.grid(row = 0, column = 3, sticky = 'NSEW', pady = 10)

labelDsRTIF = tkinter.Label(master = FrameResumenTIF, text = 'Ds (Px)', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelDsRTIF.grid(row = 0, column = 4, sticky = 'NSEW', pady = 10)

labelDtRTIF = tkinter.Label(master = FrameResumenTIF, text = 'Dt (Px)', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelDtRTIF.grid(row = 0, column = 5, sticky = 'NSEW', pady = 10)

labelDtcmRTIF = tkinter.Label(master = FrameResumenTIF, text = 'Dt (Cm)', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelDtcmRTIF.grid(row = 0, column = 6, sticky = 'NSEW', pady = 10)

labelDwRTIF = tkinter.Label(master = FrameResumenTIF, text = 'Dw (gr/cm\u00B3)', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelDwRTIF.grid(row = 0, column = 7, sticky = 'NSEW', pady = 10)

labelDoRTIF = tkinter.Label(master = FrameResumenTIF, text = 'Do (gr/cm\u00B3)', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelDoRTIF.grid(row = 0, column = 8, sticky = 'NSEW', pady = 10)

labeltifRTIF = tkinter.Label(master = FrameResumenTIF, text = 'Tensión (Din/cm\u00B2)', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labeltifRTIF.grid(row = 0, column = 9, sticky = 'NSEW', pady = 10)

labelNCRTIF = tkinter.Label(master = FrameResumenTIF, text = 'N.Corridas', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelNCRTIF.grid(row = 0, column = 10, sticky = 'NSEW', pady = 10)

labeltifmRTIF = tkinter.Label(master = FrameResumenTIF, text = 'Ten. Mínima', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labeltifmRTIF.grid(row = 0, column = 11, sticky = 'NSEW', pady = 10)

labeltifMRTIF = tkinter.Label(master = FrameResumenTIF, text = 'Ten. Máxima', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labeltifMRTIF.grid(row = 0, column = 12, sticky = 'NSEW', pady = 10)

labelErrorRTIF = tkinter.Label(master = FrameResumenTIF, text = 'Error (±)', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelErrorRTIF.grid(row = 0, column = 13, sticky = 'NSEW', pady = 10)

labelNumero1R = tkinter.Label(master = FrameResumenTIF, text = '1', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelNumero1R.grid(row = 1, column = 0, sticky = 'NSEW', pady = 2)

labelNumero2R = tkinter.Label(master = FrameResumenTIF, text = '2', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelNumero2R.grid(row = 2, column = 0, sticky = 'NSEW', pady = 2)

labelNumero3R = tkinter.Label(master = FrameResumenTIF, text = '3', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelNumero3R.grid(row = 3, column = 0, sticky = 'NSEW', pady = 2)

labelNumero4R = tkinter.Label(master = FrameResumenTIF, text = '4', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelNumero4R.grid(row = 4, column = 0, sticky = 'NSEW', pady = 2)

labelNumero5R = tkinter.Label(master = FrameResumenTIF, text = '5', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelNumero5R.grid(row = 5, column = 0, sticky = 'NSEW', pady = 2)

labelNumero6R = tkinter.Label(master = FrameResumenTIF, text = '6', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelNumero6R.grid(row = 6, column = 0, sticky = 'NSEW', pady = 2 )

labelNumero7R = tkinter.Label(master = FrameResumenTIF, text = '7', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelNumero7R.grid(row = 7, column = 0, sticky = 'NSEW', pady = 2)

labelNumero8R = tkinter.Label(master = FrameResumenTIF, text = '8', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelNumero8R.grid(row = 8, column = 0, sticky = 'NSEW', pady = 2)

labelNumero9R = tkinter.Label(master = FrameResumenTIF, text = '9', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelNumero9R.grid(row = 9, column = 0, sticky = 'NSEW', pady = 2)

labelNumero10R = tkinter.Label(master = FrameResumenTIF, text = '10', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelNumero10R.grid(row = 10, column = 0, sticky = 'NSEW', pady = 2)


EntryNombreMuestraRTIF11 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxNombreMuestra11, width = 20, borderwidth = 1, relief = "flat")
EntryNombreMuestraRTIF11.grid(row = 1, column = 1, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloMuestraRTIF12 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxAnguloTIFMuestra12, width = 10, borderwidth = 1, relief = "flat")
EntryAnguloMuestraRTIF12.grid(row = 1, column = 2, sticky = 'NSEW', padx = 1, pady = 1)

EntryDeRTIF13 = tkinter.Entry(master = FrameResumenTIF, width = 10, justify = 'center', textvariable = varAuxDeR13, borderwidth = 1, relief = "flat")
EntryDeRTIF13.grid(row = 1, column = 3, sticky = 'NSEW', padx = 1, pady = 1)

EntryDsRTIF14 = tkinter.Entry(master = FrameResumenTIF, width = 10, justify = 'center', textvariable = varAuxDsR14, borderwidth = 1, relief = "flat")
EntryDsRTIF14.grid(row = 1, column = 4, sticky = 'NSEW', padx = 1, pady = 1)

EntryDtRTIF15 = tkinter.Entry(master = FrameResumenTIF, width = 10, justify = 'center', textvariable = varAuxDtR15, borderwidth = 1, relief = "flat")
EntryDtRTIF15.grid(row = 1, column = 5, sticky = 'NSEW', padx = 1, pady = 1)

EntryDtcmRTIF16 = tkinter.Entry(master = FrameResumenTIF, width = 10, justify = 'center', textvariable = varAuxDtCm16, borderwidth = 1, relief = "flat")
EntryDtcmRTIF16.grid(row = 1, column = 6, sticky = 'NSEW', padx = 1, pady = 1)

EntryDwRTIF17 = tkinter.Entry(master = FrameResumenTIF, width = 12, justify = 'center', textvariable = varAuxdW17, borderwidth = 1, relief = "flat")
EntryDwRTIF17.grid(row = 1, column = 7, sticky = 'NSEW', padx = 1, pady = 1)

EntryDoRTIF18 = tkinter.Entry(master = FrameResumenTIF, width = 12, justify = 'center', textvariable = varAuxdO18, borderwidth = 1, relief = "flat")
EntryDoRTIF18.grid(row = 1, column = 8, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifRTIF19 = tkinter.Entry(master = FrameResumenTIF, width = 12, justify = 'center', textvariable = varAuxTIFR19, borderwidth = 1, relief = "flat")
EntrytifRTIF19.grid(row = 1, column = 9, sticky = 'NSEW', padx = 1, pady = 1)

EntryNCRTIF110 = tkinter.Entry(master = FrameResumenTIF, width = 12, justify = 'center', textvariable = varAuxNC110, borderwidth = 1, relief = "flat")
EntryNCRTIF110.grid(row = 1, column = 10, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifmRTIF111 = tkinter.Entry(master = FrameResumenTIF, width = 12, justify = 'center', textvariable = varAuxTIFmin111, borderwidth = 1, relief = "flat")
EntrytifmRTIF111.grid(row = 1, column = 11, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifMRTIF112 = tkinter.Entry(master = FrameResumenTIF, width = 12, justify = 'center', textvariable = varAuxTIFmax112, borderwidth = 1, relief = "flat")
EntrytifMRTIF112.grid(row = 1, column = 12, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifERTIF113 = tkinter.Entry(master = FrameResumenTIF, width = 12, justify = 'center', textvariable = varAuxTIFerror113, borderwidth = 1, relief = "flat")
EntrytifERTIF113.grid(row = 1, column = 13, sticky = 'NSEW', padx = 1, pady = 1)


EntryNombreMuestraRTIF21 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxNombreMuestra21, width = 20, borderwidth = 1, relief = "flat")
EntryNombreMuestraRTIF21.grid(row = 2, column = 1, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloMuestraRTIF22 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxAnguloTIFMuestra22, width = 10, borderwidth = 1, relief = "flat")
EntryAnguloMuestraRTIF22.grid(row = 2, column = 2, sticky = 'NSEW', padx = 1, pady = 1)

EntryDeRTIF23 = tkinter.Entry(master = FrameResumenTIF, width = 10, justify = 'center', textvariable = varAuxDeR23, borderwidth = 1, relief = "flat")
EntryDeRTIF23.grid(row = 2, column = 3, sticky = 'NSEW', padx = 1, pady = 1)

EntryDsRTIF24 = tkinter.Entry(master = FrameResumenTIF, width = 10, justify = 'center', textvariable = varAuxDsR24, borderwidth = 1, relief = "flat")
EntryDsRTIF24.grid(row = 2, column = 4, sticky = 'NSEW', padx = 1, pady = 1)

EntryDtRTIF25 = tkinter.Entry(master = FrameResumenTIF, width = 10, justify = 'center', textvariable = varAuxDtR25, borderwidth = 1, relief = "flat")
EntryDtRTIF25.grid(row = 2, column = 5, sticky = 'NSEW', padx = 1, pady = 1)

EntryDtcmRTIF26 = tkinter.Entry(master = FrameResumenTIF, width = 10, justify = 'center', textvariable = varAuxDtCm26, borderwidth = 1, relief = "flat")
EntryDtcmRTIF26.grid(row = 2, column = 6, sticky = 'NSEW', padx = 1, pady = 1)

EntryDwRTIF27 = tkinter.Entry(master = FrameResumenTIF, width = 12, justify = 'center', textvariable = varAuxdW27, borderwidth = 1, relief = "flat")
EntryDwRTIF27.grid(row = 2, column = 7, sticky = 'NSEW', padx = 1, pady = 1)

EntryDoRTIF28 = tkinter.Entry(master = FrameResumenTIF, width = 12, justify = 'center', textvariable = varAuxdO28, borderwidth = 1, relief = "flat")
EntryDoRTIF28.grid(row = 2, column = 8, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifRTIF29 = tkinter.Entry(master = FrameResumenTIF, width = 12, justify = 'center', textvariable = varAuxTIFR29, borderwidth = 1, relief = "flat")
EntrytifRTIF29.grid(row = 2, column = 9, sticky = 'NSEW', padx = 1, pady = 1)

EntryNCRTIF210 = tkinter.Entry(master = FrameResumenTIF, width = 12, justify = 'center', textvariable = varAuxNC210, borderwidth = 1, relief = "flat")
EntryNCRTIF210.grid(row = 2, column = 10, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifmRTIF211 = tkinter.Entry(master = FrameResumenTIF, width = 12, justify = 'center', textvariable = varAuxTIFmin211, borderwidth = 1, relief = "flat")
EntrytifmRTIF211.grid(row = 2, column = 11, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifMRTIF212 = tkinter.Entry(master = FrameResumenTIF, width = 12, justify = 'center', textvariable = varAuxTIFmax212, borderwidth = 1, relief = "flat")
EntrytifMRTIF212.grid(row = 2, column = 12, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifERTIF213 = tkinter.Entry(master = FrameResumenTIF, width = 12, justify = 'center', textvariable = varAuxTIFerror213, borderwidth = 1, relief = "flat")
EntrytifERTIF213.grid(row = 2, column = 13, sticky = 'NSEW', padx = 1, pady = 1)


EntryNombreMuestraRTIF31 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxNombreMuestra31, width = 20, borderwidth = 1, relief = "flat")
EntryNombreMuestraRTIF31.grid(row = 3, column = 1, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloMuestraRTIF32 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxAnguloTIFMuestra32, width = 10, borderwidth = 1, relief = "flat")
EntryAnguloMuestraRTIF32.grid(row = 3, column = 2, sticky = 'NSEW', padx = 1, pady = 1)

EntryDeRTIF33 = tkinter.Entry(master = FrameResumenTIF, width = 10, justify = 'center', textvariable = varAuxDeR33, borderwidth = 1, relief = "flat")
EntryDeRTIF33.grid(row = 3, column = 3, sticky = 'NSEW', padx = 1, pady = 1)

EntryDsRTIF34 = tkinter.Entry(master = FrameResumenTIF, width = 10, justify = 'center', textvariable = varAuxDsR34, borderwidth = 1, relief = "flat")
EntryDsRTIF34.grid(row = 3, column = 4, sticky = 'NSEW', padx = 1, pady = 1)

EntryDtRTIF35 = tkinter.Entry(master = FrameResumenTIF, width = 10, justify = 'center', textvariable = varAuxDtR35, borderwidth = 1, relief = "flat")
EntryDtRTIF35.grid(row = 3, column = 5, sticky = 'NSEW', padx = 1, pady = 1)

EntryDtcmRTIF36 = tkinter.Entry(master = FrameResumenTIF, width = 10, justify = 'center', textvariable = varAuxDtCm36, borderwidth = 1, relief = "flat")
EntryDtcmRTIF36.grid(row = 3, column = 6, sticky = 'NSEW', padx = 1, pady = 1)

EntryDwRTIF37 = tkinter.Entry(master = FrameResumenTIF, width = 12, justify = 'center', textvariable = varAuxdW37, borderwidth = 1, relief = "flat")
EntryDwRTIF37.grid(row = 3, column = 7, sticky = 'NSEW', padx = 1, pady = 1)

EntryDoRTIF38 = tkinter.Entry(master = FrameResumenTIF, width = 12, justify = 'center', textvariable = varAuxdO38, borderwidth = 1, relief = "flat")
EntryDoRTIF38.grid(row = 3, column = 8, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifRTIF39 = tkinter.Entry(master = FrameResumenTIF, width = 12, justify = 'center', textvariable = varAuxTIFR39, borderwidth = 1, relief = "flat")
EntrytifRTIF39.grid(row = 3, column = 9, sticky = 'NSEW', padx = 1, pady = 1)

EntryNCRTIF310 = tkinter.Entry(master = FrameResumenTIF, width = 12, justify = 'center', textvariable = varAuxNC310, borderwidth = 1, relief = "flat")
EntryNCRTIF310.grid(row = 3, column = 10, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifmRTIF311 = tkinter.Entry(master = FrameResumenTIF, width = 12, justify = 'center', textvariable = varAuxTIFmin311, borderwidth = 1, relief = "flat")
EntrytifmRTIF311.grid(row = 3, column = 11, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifMRTIF312 = tkinter.Entry(master = FrameResumenTIF, width = 12, justify = 'center', textvariable = varAuxTIFmax312, borderwidth = 1, relief = "flat")
EntrytifMRTIF312.grid(row = 3, column = 12, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifERTIF313 = tkinter.Entry(master = FrameResumenTIF, width = 12, justify = 'center', textvariable = varAuxTIFerror313, borderwidth = 1, relief = "flat")
EntrytifERTIF313.grid(row = 3, column = 13, sticky = 'NSEW', padx = 1, pady = 1)



EntryNombreMuestraRTIF41 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxNombreMuestra41, width = 20, borderwidth = 1, relief = "flat")
EntryNombreMuestraRTIF41.grid(row = 4, column = 1, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloMuestraRTIF42 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxAnguloTIFMuestra42, width = 10, borderwidth = 1, relief = "flat")
EntryAnguloMuestraRTIF42.grid(row = 4, column = 2, sticky = 'NSEW', padx = 1, pady = 1)

EntryDeRTIF43 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDeR43, width = 10, borderwidth = 1, relief = "flat")
EntryDeRTIF43.grid(row = 4, column = 3, sticky = 'NSEW', padx = 1, pady = 1)

EntryDsRTIF44 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDsR44, width = 10, borderwidth = 1, relief = "flat")
EntryDsRTIF44.grid(row = 4, column = 4, sticky = 'NSEW', padx = 1, pady = 1)

EntryDtRTIF45 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDtR45, width = 10, borderwidth = 1, relief = "flat")
EntryDtRTIF45.grid(row = 4, column = 5, sticky = 'NSEW', padx = 1, pady = 1)

EntryDtcmRTIF46 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDtCm46, width = 10, borderwidth = 1, relief = "flat")
EntryDtcmRTIF46.grid(row = 4, column = 6, sticky = 'NSEW', padx = 1, pady = 1)

EntryDwRTIF47 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxdW47, width = 12, borderwidth = 1, relief = "flat")
EntryDwRTIF47.grid(row = 4, column = 7, sticky = 'NSEW', padx = 1, pady = 1)

EntryDoRTIF48 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxdO48, width = 12, borderwidth = 1, relief = "flat")
EntryDoRTIF48.grid(row = 4, column = 8, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifRTIF49 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFR49, width = 12, borderwidth = 1, relief = "flat")
EntrytifRTIF49.grid(row = 4, column = 9, sticky = 'NSEW', padx = 1, pady = 1)

EntryNCRTIF410 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxNC410, width = 12, borderwidth = 1, relief = "flat")
EntryNCRTIF410.grid(row = 4, column = 10, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifmRTIF411 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFmin411, width = 12, borderwidth = 1, relief = "flat")
EntrytifmRTIF411.grid(row = 4, column = 11, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifMRTIF412 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFmax412, width = 12, borderwidth = 1, relief = "flat")
EntrytifMRTIF412.grid(row = 4, column = 12, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifERTIF413 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFerror413, width = 12, borderwidth = 1, relief = "flat")
EntrytifERTIF413.grid(row = 4, column = 13, sticky = 'NSEW', padx = 1, pady = 1)


EntryNombreMuestraRTIF51 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxNombreMuestra51, width = 20, borderwidth = 1, relief = "flat")
EntryNombreMuestraRTIF51.grid(row = 5, column = 1, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloMuestraRTIF52 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxAnguloTIFMuestra52, width = 10, borderwidth = 1, relief = "flat")
EntryAnguloMuestraRTIF52.grid(row = 5, column = 2, sticky = 'NSEW', padx = 1, pady = 1)

EntryDeRTIF53 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDeR53, width = 10, borderwidth = 1, relief = "flat")
EntryDeRTIF53.grid(row = 5, column = 3, sticky = 'NSEW', padx = 1, pady = 1)

EntryDsRTIF54 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDsR54, width = 10, borderwidth = 1, relief = "flat")
EntryDsRTIF54.grid(row = 5, column = 4, sticky = 'NSEW', padx = 1, pady = 1)

EntryDtRTIF55 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDtR55, width = 10, borderwidth = 1, relief = "flat")
EntryDtRTIF55.grid(row = 5, column = 5, sticky = 'NSEW', padx = 1, pady = 1)

EntryDtcmRTIF56 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDtCm56, width = 10, borderwidth = 1, relief = "flat")
EntryDtcmRTIF56.grid(row = 5, column = 6, sticky = 'NSEW', padx = 1, pady = 1)

EntryDwRTIF57 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxdW57, width = 12, borderwidth = 1, relief = "flat")
EntryDwRTIF57.grid(row = 5, column = 7, sticky = 'NSEW', padx = 1, pady = 1)

EntryDoRTIF58 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxdO58, width = 12, borderwidth = 1, relief = "flat")
EntryDoRTIF58.grid(row = 5, column = 8, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifRTIF59 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFR59, width = 12, borderwidth = 1, relief = "flat")
EntrytifRTIF59.grid(row = 5, column = 9, sticky = 'NSEW', padx = 1, pady = 1)

EntryNCRTIF510 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxNC510, width = 12, borderwidth = 1, relief = "flat")
EntryNCRTIF510.grid(row = 5, column = 10, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifmRTIF511 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFmin511, width = 12, borderwidth = 1, relief = "flat")
EntrytifmRTIF511.grid(row = 5, column = 11, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifMRTIF512 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFmax512, width = 12, borderwidth = 1, relief = "flat")
EntrytifMRTIF512.grid(row = 5, column = 12, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifERTIF513 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFerror513, width = 12, borderwidth = 1, relief = "flat")
EntrytifERTIF513.grid(row = 5, column = 13, sticky = 'NSEW', padx = 1, pady = 1)



EntryNombreMuestraRTIF61 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxNombreMuestra61, width = 20, borderwidth = 1, relief = "flat")
EntryNombreMuestraRTIF61.grid(row = 6, column = 1, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloMuestraRTIF62 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxAnguloTIFMuestra62, width = 10, borderwidth = 1, relief = "flat")
EntryAnguloMuestraRTIF62.grid(row = 6, column = 2, sticky = 'NSEW', padx = 1, pady = 1)

EntryDeRTIF63 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDeR63, width = 10, borderwidth = 1, relief = "flat")
EntryDeRTIF63.grid(row = 6, column = 3, sticky = 'NSEW', padx = 1, pady = 1)

EntryDsRTIF64 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDsR64, width = 10, borderwidth = 1, relief = "flat")
EntryDsRTIF64.grid(row = 6, column = 4, sticky = 'NSEW', padx = 1, pady = 1)

EntryDtRTIF65 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDtR65, width = 10, borderwidth = 1, relief = "flat")
EntryDtRTIF65.grid(row = 6, column = 5, sticky = 'NSEW', padx = 1, pady = 1)

EntryDtcmRTIF66 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDtCm66, width = 10, borderwidth = 1, relief = "flat")
EntryDtcmRTIF66.grid(row = 6, column = 6, sticky = 'NSEW', padx = 1, pady = 1)

EntryDwRTIF67 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxdW67, width = 12, borderwidth = 1, relief = "flat")
EntryDwRTIF67.grid(row = 6, column = 7, sticky = 'NSEW', padx = 1, pady = 1)

EntryDoRTIF68 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxdO68, width = 12, borderwidth = 1, relief = "flat")
EntryDoRTIF68.grid(row = 6, column = 8, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifRTIF69 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFR69, width = 12, borderwidth = 1, relief = "flat")
EntrytifRTIF69.grid(row = 6, column = 9, sticky = 'NSEW', padx = 1, pady = 1)

EntryNCRTIF610 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxNC610, width = 12, borderwidth = 1, relief = "flat")
EntryNCRTIF610.grid(row = 6, column = 10, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifmRTIF611 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFmin611, width = 12, borderwidth = 1, relief = "flat")
EntrytifmRTIF611.grid(row = 6, column = 11, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifMRTIF612 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFmax612, width = 12, borderwidth = 1, relief = "flat")
EntrytifMRTIF612.grid(row = 6, column = 12, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifERTIF613 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFerror613, width = 12, borderwidth = 1, relief = "flat")
EntrytifERTIF613.grid(row = 6, column = 13, sticky = 'NSEW', padx = 1, pady = 1)


EntryNombreMuestraRTIF71 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxNombreMuestra71, width = 20, borderwidth = 1, relief = "flat")
EntryNombreMuestraRTIF71.grid(row = 7, column = 1, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloMuestraRTIF72 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxAnguloTIFMuestra72, width = 10, borderwidth = 1, relief = "flat")
EntryAnguloMuestraRTIF72.grid(row = 7, column = 2, sticky = 'NSEW', padx = 1, pady = 1)

EntryDeRTIF73 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDeR73, width = 10, borderwidth = 1, relief = "flat")
EntryDeRTIF73.grid(row = 7, column = 3, sticky = 'NSEW', padx = 1, pady = 1)

EntryDsRTIF74 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDsR74, width = 10, borderwidth = 1, relief = "flat")
EntryDsRTIF74.grid(row = 7, column = 4, sticky = 'NSEW', padx = 1, pady = 1)

EntryDtRTIF75 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDtR75, width = 10, borderwidth = 1, relief = "flat")
EntryDtRTIF75.grid(row = 7, column = 5, sticky = 'NSEW', padx = 1, pady = 1)

EntryDtcmRTIF76 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDtCm76, width = 10, borderwidth = 1, relief = "flat")
EntryDtcmRTIF76.grid(row = 7, column = 6, sticky = 'NSEW', padx = 1, pady = 1)

EntryDwRTIF77 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxdW77, width = 12, borderwidth = 1, relief = "flat")
EntryDwRTIF77.grid(row = 7, column = 7, sticky = 'NSEW', padx = 1, pady = 1)

EntryDoRTIF78 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxdO78, width = 12, borderwidth = 1, relief = "flat")
EntryDoRTIF78.grid(row = 7, column = 8, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifRTIF79 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFR79, width = 12, borderwidth = 1, relief = "flat")
EntrytifRTIF79.grid(row = 7, column = 9, sticky = 'NSEW', padx = 1, pady = 1)

EntryNCRTIF710 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxNC710, width = 12, borderwidth = 1, relief = "flat")
EntryNCRTIF710.grid(row = 7, column = 10, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifmRTIF711 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFmin711, width = 12, borderwidth = 1, relief = "flat")
EntrytifmRTIF711.grid(row = 7, column = 11, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifMRTIF712 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFmax712, width = 12, borderwidth = 1, relief = "flat")
EntrytifMRTIF712.grid(row = 7, column = 12, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifERTIF713 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFerror713, width = 12, borderwidth = 1, relief = "flat")
EntrytifERTIF713.grid(row = 7, column = 13, sticky = 'NSEW', padx = 1, pady = 1)



EntryNombreMuestraRTIF81 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxNombreMuestra81, width = 20, borderwidth = 1, relief = "flat")
EntryNombreMuestraRTIF81.grid(row = 8, column = 1, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloMuestraRTIF82 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxAnguloTIFMuestra82, width = 10, borderwidth = 1, relief = "flat")
EntryAnguloMuestraRTIF82.grid(row = 8, column = 2, sticky = 'NSEW', padx = 1, pady = 1)

EntryDeRTIF83 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDeR83, width = 10, borderwidth = 1, relief = "flat")
EntryDeRTIF83.grid(row = 8, column = 3, sticky = 'NSEW', padx = 1, pady = 1)

EntryDsRTIF84 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDsR84, width = 10, borderwidth = 1, relief = "flat")
EntryDsRTIF84.grid(row = 8, column = 4, sticky = 'NSEW', padx = 1, pady = 1)

EntryDtRTIF85 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDtR85, width = 10, borderwidth = 1, relief = "flat")
EntryDtRTIF85.grid(row = 8, column = 5, sticky = 'NSEW', padx = 1, pady = 1)

EntryDtcmRTIF86 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDtCm86, width = 10, borderwidth = 1, relief = "flat")
EntryDtcmRTIF86.grid(row = 8, column = 6, sticky = 'NSEW', padx = 1, pady = 1)

EntryDwRTIF87 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxdW87, width = 12, borderwidth = 1, relief = "flat")
EntryDwRTIF87.grid(row = 8, column = 7, sticky = 'NSEW', padx = 1, pady = 1)

EntryDoRTIF88 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxdO88, width = 12, borderwidth = 1, relief = "flat")
EntryDoRTIF88.grid(row = 8, column = 8, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifRTIF89 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFR89, width = 12, borderwidth = 1, relief = "flat")
EntrytifRTIF89.grid(row = 8, column = 9, sticky = 'NSEW', padx = 1, pady = 1)

EntryNCRTIF810 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxNC810, width = 12, borderwidth = 1, relief = "flat")
EntryNCRTIF810.grid(row = 8, column = 10, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifmRTIF811 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFmin811, width = 12, borderwidth = 1, relief = "flat")
EntrytifmRTIF811.grid(row = 8, column = 11, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifMRTIF812 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFmax812, width = 12, borderwidth = 1, relief = "flat")
EntrytifMRTIF812.grid(row = 8, column = 12, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifERTIF813 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFerror813, width = 12, borderwidth = 1, relief = "flat")
EntrytifERTIF813.grid(row = 8, column = 13, sticky = 'NSEW', padx = 1, pady = 1)


EntryNombreMuestraRTIF91 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxNombreMuestra91, width = 20, borderwidth = 1, relief = "flat")
EntryNombreMuestraRTIF91.grid(row = 9, column = 1, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloMuestraRTIF92 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxAnguloTIFMuestra92, width = 10, borderwidth = 1, relief = "flat")
EntryAnguloMuestraRTIF92.grid(row = 9, column = 2, sticky = 'NSEW', padx = 1, pady = 1)

EntryDeRTIF93 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDeR93, width = 10, borderwidth = 1, relief = "flat")
EntryDeRTIF93.grid(row = 9, column = 3, sticky = 'NSEW', padx = 1, pady = 1)

EntryDsRTIF94 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDsR94, width = 10, borderwidth = 1, relief = "flat")
EntryDsRTIF94.grid(row = 9, column = 4, sticky = 'NSEW', padx = 1, pady = 1)

EntryDtRTIF95 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDtR95, width = 10, borderwidth = 1, relief = "flat")
EntryDtRTIF95.grid(row = 9, column = 5, sticky = 'NSEW', padx = 1, pady = 1)

EntryDtcmRTIF96 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDtCm96, width = 10, borderwidth = 1, relief = "flat")
EntryDtcmRTIF96.grid(row = 9, column = 6, sticky = 'NSEW', padx = 1, pady = 1)

EntryDwRTIF97 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxdW97, width = 12, borderwidth = 1, relief = "flat")
EntryDwRTIF97.grid(row = 9, column = 7, sticky = 'NSEW', padx = 1, pady = 1)

EntryDoRTIF98 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxdO98, width = 12, borderwidth = 1, relief = "flat")
EntryDoRTIF98.grid(row = 9, column = 8, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifRTIF99 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFR99, width = 12, borderwidth = 1, relief = "flat")
EntrytifRTIF99.grid(row = 9, column = 9, sticky = 'NSEW', padx = 1, pady = 1)

EntryNCRTIF910 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxNC910, width = 12, borderwidth = 1, relief = "flat")
EntryNCRTIF910.grid(row = 9, column = 10, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifmRTIF911 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFmin911, width = 12, borderwidth = 1, relief = "flat")
EntrytifmRTIF911.grid(row = 9, column = 11, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifMRTIF912 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFmax912, width = 12, borderwidth = 1, relief = "flat")
EntrytifMRTIF912.grid(row = 9, column = 12, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifERTIF913 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFerror913, width = 12, borderwidth = 1, relief = "flat")
EntrytifERTIF913.grid(row = 9, column = 13, sticky = 'NSEW', padx = 1, pady = 1)



EntryNombreMuestraRTIF101 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxNombreMuestra101, width = 20, borderwidth = 1, relief = "flat")
EntryNombreMuestraRTIF101.grid(row = 10, column = 1, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloMuestraRTIF102 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxAnguloTIFMuestra102, width = 10, borderwidth = 1, relief = "flat")
EntryAnguloMuestraRTIF102.grid(row = 10, column = 2, sticky = 'NSEW', padx = 1, pady = 1)

EntryDeRTIF103 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDeR103, width = 10, borderwidth = 1, relief = "flat")
EntryDeRTIF103.grid(row = 10, column = 3, sticky = 'NSEW', padx = 1, pady = 1)

EntryDsRTIF104 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDsR104, width = 10, borderwidth = 1, relief = "flat")
EntryDsRTIF104.grid(row = 10, column = 4, sticky = 'NSEW', padx = 1, pady = 1)

EntryDtRTIF105 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxDtR105, width = 10, borderwidth = 1, relief = "flat")
EntryDtRTIF105.grid(row = 10, column = 5, sticky = 'NSEW', padx = 1, pady = 1)

EntryDtcmRTIF106 = tkinter.Entry(master = FrameResumenTIF,justify = 'center', textvariable = varAuxDtCm106, width = 10, borderwidth = 1, relief = "flat")
EntryDtcmRTIF106.grid(row = 10, column = 6, sticky = 'NSEW', padx = 1, pady = 1)

EntryDwRTIF107 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxdW107, width = 12, borderwidth = 1, relief = "flat")
EntryDwRTIF107.grid(row = 10, column = 7, sticky = 'NSEW', padx = 1, pady = 1)

EntryDoRTIF108 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxdO108, width = 12, borderwidth = 1, relief = "flat")
EntryDoRTIF108.grid(row = 10, column = 8, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifRTIF109 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFR109, width = 12, borderwidth = 1, relief = "flat")
EntrytifRTIF109.grid(row = 10, column = 9, sticky = 'NSEW', padx = 1, pady = 1)

EntryNCRTIF1010 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxNC1010, width = 12, borderwidth = 1, relief = "flat")
EntryNCRTIF1010.grid(row = 10, column = 10, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifmRTIF1011 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFmin1011, width = 12, borderwidth = 1, relief = "flat")
EntrytifmRTIF1011.grid(row = 10, column = 11, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifMRTIF1012 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFmax1012, width = 12, borderwidth = 1, relief = "flat")
EntrytifMRTIF1012.grid(row = 10, column = 12, sticky = 'NSEW', padx = 1, pady = 1)

EntrytifERTIF1013 = tkinter.Entry(master = FrameResumenTIF, justify = 'center', textvariable = varAuxTIFerror1013, width = 12, borderwidth = 1, relief = "flat")
EntrytifERTIF1013.grid(row = 10, column = 13, sticky = 'NSEW', padx = 1, pady = 1)

buttonBorrarRTIF = tkinter.Button(master = FrameResumenTIF, text = 'Limpiar Resumen', command = limpiarResumenTIF, borderwidth = 1, relief = 'solid', cursor = 'hand2', font = ('Calibri', 10, 'bold', 'italic' ))
buttonBorrarRTIF.grid(row = 11, column = 13, sticky = 'NSEW', padx = 3, pady = 5 )

# resumen Ángulo

# Label  Titulo

labelTituloRA = tkinter.Label(master = p3, text = 'Resumen del análisis del Ángulo', font = ('Calibri light', 13, 'bold'))
labelTituloRA.grid(row = 2, column = 3, sticky = 'W', ipady = 15)

# Imagen de la gota roja.

labelImageRA = tkinter.Label(master = p3, image = imagenGota)
labelImageRA.grid(row = 2, column = 1, columnspan = 2, sticky = 'E', ipady = 15) 

# Frame Resumen Ángulo

FrameResumenAngulo = tkinter.Frame(master = p3)
FrameResumenAngulo.config(bg = 'seashell2', borderwidth = 1, relief = "solid")
FrameResumenAngulo.grid(row = 3, column = 1, columnspan = 3, sticky = 'NSEW' )

FrameResumenAngulo.rowconfigure(0, weight = 1)
FrameResumenAngulo.rowconfigure(1, weight = 1)
FrameResumenAngulo.rowconfigure(2, weight = 1)
FrameResumenAngulo.rowconfigure(3, weight = 1)
FrameResumenAngulo.rowconfigure(4, weight = 1)
FrameResumenAngulo.rowconfigure(5, weight = 1)
FrameResumenAngulo.rowconfigure(6, weight = 1)
FrameResumenAngulo.rowconfigure(7, weight = 1)
FrameResumenAngulo.rowconfigure(8, weight = 1)
FrameResumenAngulo.rowconfigure(9, weight = 1)
FrameResumenAngulo.rowconfigure(10, weight = 1)
FrameResumenAngulo.rowconfigure(11, weight = 1)

FrameResumenAngulo.columnconfigure(0, weight = 1)
FrameResumenAngulo.columnconfigure(1, weight = 1)
FrameResumenAngulo.columnconfigure(2, weight = 1)
FrameResumenAngulo.columnconfigure(3, weight = 1)
FrameResumenAngulo.columnconfigure(4, weight = 1)
FrameResumenAngulo.columnconfigure(5, weight = 1)
FrameResumenAngulo.columnconfigure(6, weight = 1)
FrameResumenAngulo.columnconfigure(7, weight = 1)

labelNombreMuestraRA = tkinter.Label(master = FrameResumenAngulo, text = 'ID de la muestra', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelNombreMuestraRA.grid(row = 0, column = 1, sticky = 'NSEW', pady = 10)

labelAnguloMuestraRA = tkinter.Label(master = FrameResumenAngulo, text = 'Ángulo de rote (°)', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelAnguloMuestraRA.grid(row = 0, column = 2, sticky = 'NSEW', pady = 10)

labelFechaTomaRA = tkinter.Label(master = FrameResumenAngulo, text = 'Fecha de la toma', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelFechaTomaRA.grid(row = 0, column = 3, sticky = 'NSEW', pady = 10)

labelHoraTomaRA = tkinter.Label(master = FrameResumenAngulo, text = 'Hora de la toma', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelHoraTomaRA.grid(row = 0, column = 4, sticky = 'NSEW', pady = 10)

labelAnguloIRA = tkinter.Label(master = FrameResumenAngulo, text = 'Ángulo Izquierdo (°)', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelAnguloIRA.grid(row = 0, column = 5, sticky = 'NSEW', pady = 10)

labelAnguloDRA = tkinter.Label(master = FrameResumenAngulo, text = 'Ángulo Derecho (°)', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelAnguloDRA.grid(row = 0, column = 6, sticky = 'NSEW', pady = 10)


labelNumero1R = tkinter.Label(master = FrameResumenAngulo, text = '1', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelNumero1R.grid(row = 1, column = 0, sticky = 'NSEW', pady = 2)

labelNumero2R = tkinter.Label(master = FrameResumenAngulo, text = '2', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelNumero2R.grid(row = 2, column = 0, sticky = 'NSEW', pady = 2)

labelNumero3R = tkinter.Label(master = FrameResumenAngulo, text = '3', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelNumero3R.grid(row = 3, column = 0, sticky = 'NSEW', pady = 2)

labelNumero4R = tkinter.Label(master = FrameResumenAngulo, text = '4', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelNumero4R.grid(row = 4, column = 0, sticky = 'NSEW', pady = 2)

labelNumero5R = tkinter.Label(master = FrameResumenAngulo, text = '5', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelNumero5R.grid(row = 5, column = 0, sticky = 'NSEW', pady = 2)

labelNumero6R = tkinter.Label(master = FrameResumenAngulo, text = '6', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelNumero6R.grid(row = 6, column = 0, sticky = 'NSEW', pady = 2)

labelNumero7R = tkinter.Label(master = FrameResumenAngulo, text = '7', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelNumero7R.grid(row = 7, column = 0, sticky = 'NSEW', pady = 2)

labelNumero8R = tkinter.Label(master = FrameResumenAngulo, text = '8', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelNumero8R.grid(row = 8, column = 0, sticky = 'NSEW', pady = 2)

labelNumero9R = tkinter.Label(master = FrameResumenAngulo, text = '9', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelNumero9R.grid(row = 9, column = 0, sticky = 'NSEW', pady = 2)

labelNumero10R = tkinter.Label(master = FrameResumenAngulo, text = '10', font = ('Calibri', 10, 'bold', 'italic'  ), bg = 'seashell2')
labelNumero10R.grid(row = 10, column = 0, sticky = 'NSEW', pady = 2)


EntryNombreMuestraRA11 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxNombreMuestraRA11, width = 20, borderwidth = 1, relief = "flat")
EntryNombreMuestraRA11.grid(row = 1, column = 1, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloMuestraRA12 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloMuestraRA12, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloMuestraRA12.grid(row = 1, column = 2, sticky = 'NSEW', padx = 1, pady = 1)

EntryFechaTomaRA13 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxFechaTomaRA13, width = 20, borderwidth = 1, relief = "flat")
EntryFechaTomaRA13.grid(row = 1, column = 3, sticky = 'NSEW', padx = 1, pady = 1)

EntryHoraTomaRA14 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxHoraTomaRA14, width = 20, borderwidth = 1, relief = "flat")
EntryHoraTomaRA14.grid(row = 1, column = 4, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloIRA15 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloIRA15, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloIRA15.grid(row = 1, column = 5, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloDRA16 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloDRA16, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloDRA16.grid(row = 1, column = 6, sticky = 'NSEW', padx = 1, pady = 1)


EntryNombreMuestraRA21 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxNombreMuestraRA21, width = 20, borderwidth = 1, relief = "flat")
EntryNombreMuestraRA21.grid(row = 2, column = 1, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloMuestraRA22 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloMuestraRA22, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloMuestraRA22.grid(row = 2, column = 2, sticky = 'NSEW', padx = 1, pady = 1)

EntryFechaTomaRA23 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxFechaTomaRA23, width = 20, borderwidth = 1, relief = "flat")
EntryFechaTomaRA23.grid(row = 2, column = 3, sticky = 'NSEW', padx = 1, pady = 1)

EntryHoraTomaRA24 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxHoraTomaRA24, width = 20, borderwidth = 1, relief = "flat")
EntryHoraTomaRA24.grid(row = 2, column = 4, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloIRA25 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloIRA25, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloIRA25.grid(row = 2, column = 5, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloDRA26 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloDRA26, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloDRA26.grid(row = 2, column = 6, sticky = 'NSEW', padx = 1, pady = 1)


EntryNombreMuestraRA31 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxNombreMuestraRA31, width = 20, borderwidth = 1, relief = "flat")
EntryNombreMuestraRA31.grid(row = 3, column = 1, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloMuestraRA32 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloMuestraRA32, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloMuestraRA32.grid(row = 3, column = 2, sticky = 'NSEW', padx = 1, pady = 1)

EntryFechaTomaRA33 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxFechaTomaRA33, width = 20, borderwidth = 1, relief = "flat")
EntryFechaTomaRA33.grid(row = 3, column = 3, sticky = 'NSEW', padx = 1, pady = 1)

EntryHoraTomaRA34 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxHoraTomaRA34, width = 20, borderwidth = 1, relief = "flat")
EntryHoraTomaRA34.grid(row = 3, column = 4, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloIRA35 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloIRA35, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloIRA35.grid(row = 3, column = 5, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloDRA36 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloDRA36, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloDRA36.grid(row = 3, column = 6, sticky = 'NSEW', padx = 1, pady = 1)



EntryNombreMuestraRA41 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxNombreMuestraRA41, width = 20, borderwidth = 1, relief = "flat")
EntryNombreMuestraRA41.grid(row = 4, column = 1, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloMuestraRA42 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloMuestraRA42, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloMuestraRA42.grid(row = 4, column = 2, sticky = 'NSEW', padx = 1, pady = 1)

EntryFechaTomaRA43 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxFechaTomaRA43, width = 20, borderwidth = 1, relief = "flat")
EntryFechaTomaRA43.grid(row = 4, column = 3, sticky = 'NSEW', padx = 1, pady = 1)

EntryHoraTomaRA44 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxHoraTomaRA44, width = 20, borderwidth = 1, relief = "flat")
EntryHoraTomaRA44.grid(row = 4, column = 4, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloIRA45 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloIRA45, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloIRA45.grid(row = 4, column = 5, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloDRA46 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloDRA46, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloDRA46.grid(row = 4, column = 6, sticky = 'NSEW', padx = 1, pady = 1)



EntryNombreMuestraRA51 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxNombreMuestraRA51, width = 20, borderwidth = 1, relief = "flat")
EntryNombreMuestraRA51.grid(row = 5, column = 1, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloMuestraRA52 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloMuestraRA52, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloMuestraRA52.grid(row = 5, column = 2, sticky = 'NSEW', padx = 1, pady = 1)

EntryFechaTomaRA53 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxFechaTomaRA53, width = 20, borderwidth = 1, relief = "flat")
EntryFechaTomaRA53.grid(row = 5, column = 3, sticky = 'NSEW', padx = 1, pady = 1)

EntryHoraTomaRA54 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxHoraTomaRA54, width = 20, borderwidth = 1, relief = "flat")
EntryHoraTomaRA54.grid(row = 5, column = 4, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloIRA55 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloIRA55, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloIRA55.grid(row = 5, column = 5, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloDRA56 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloDRA56, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloDRA56.grid(row = 5, column = 6, sticky = 'NSEW', padx = 1, pady = 1)



EntryNombreMuestraRA61 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxNombreMuestraRA61, width = 20, borderwidth = 1, relief = "flat")
EntryNombreMuestraRA61.grid(row = 6, column = 1, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloMuestraRA62 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloMuestraRA62, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloMuestraRA62.grid(row = 6, column = 2, sticky = 'NSEW', padx = 1, pady = 1)

EntryFechaTomaRA63 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxFechaTomaRA63, width = 20, borderwidth = 1, relief = "flat")
EntryFechaTomaRA63.grid(row = 6, column = 3, sticky = 'NSEW', padx = 1, pady = 1)

EntryHoraTomaRA64 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxHoraTomaRA64, width = 20, borderwidth = 1, relief = "flat")
EntryHoraTomaRA64.grid(row = 6, column = 4, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloIRA65 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloIRA65, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloIRA65.grid(row = 6, column = 5, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloDRA66 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloDRA66, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloDRA66.grid(row = 6, column = 6, sticky = 'NSEW', padx = 1, pady = 1)


EntryNombreMuestraRA71 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxNombreMuestraRA71, width = 20, borderwidth = 1, relief = "flat")
EntryNombreMuestraRA71.grid(row = 7, column = 1, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloMuestraRA72 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloMuestraRA72, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloMuestraRA72.grid(row = 7, column = 2, sticky = 'NSEW', padx = 1, pady = 1)

EntryFechaTomaRA73 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxFechaTomaRA73, width = 20, borderwidth = 1, relief = "flat")
EntryFechaTomaRA73.grid(row = 7, column = 3, sticky = 'NSEW', padx = 1, pady = 1)

EntryHoraTomaRA74 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxHoraTomaRA74, width = 20, borderwidth = 1, relief = "flat")
EntryHoraTomaRA74.grid(row = 7, column = 4, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloIRA75 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloIRA75, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloIRA75.grid(row = 7, column = 5, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloDRA76 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloDRA76, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloDRA76.grid(row = 7, column = 6, sticky = 'NSEW', padx = 1, pady = 1)



EntryNombreMuestraRA81 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxNombreMuestraRA81, width = 20, borderwidth = 1, relief = "flat")
EntryNombreMuestraRA81.grid(row = 8, column = 1, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloMuestraRA82 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloMuestraRA82, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloMuestraRA82.grid(row = 8, column = 2, sticky = 'NSEW', padx = 1, pady = 1)

EntryFechaTomaRA83 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxFechaTomaRA83, width = 20, borderwidth = 1, relief = "flat")
EntryFechaTomaRA83.grid(row = 8, column = 3, sticky = 'NSEW', padx = 1, pady = 1)

EntryHoraTomaRA84 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxHoraTomaRA84, width = 20, borderwidth = 1, relief = "flat")
EntryHoraTomaRA84.grid(row = 8, column = 4, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloIRA85 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloIRA85, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloIRA85.grid(row = 8, column = 5, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloDRA86 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloDRA86, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloDRA86.grid(row = 8, column = 6, sticky = 'NSEW', padx = 1, pady = 1)



EntryNombreMuestraRA91 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxNombreMuestraRA91, width = 20, borderwidth = 1, relief = "flat")
EntryNombreMuestraRA91.grid(row = 9, column = 1, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloMuestraRA92 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloMuestraRA92, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloMuestraRA92.grid(row = 9, column = 2, sticky = 'NSEW', padx = 1, pady = 1)

EntryFechaTomaRA93 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxFechaTomaRA93, width = 20, borderwidth = 1, relief = "flat")
EntryFechaTomaRA93.grid(row = 9, column = 3, sticky = 'NSEW', padx = 1, pady = 1)

EntryHoraTomaRA94 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxHoraTomaRA94, width = 20, borderwidth = 1, relief = "flat")
EntryHoraTomaRA94.grid(row = 9, column = 4, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloIRA95 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloIRA95, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloIRA95.grid(row = 9, column = 5, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloDRA96 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloDRA96, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloDRA96.grid(row = 9, column = 6, sticky = 'NSEW', padx = 1, pady = 1)


EntryNombreMuestraRA101 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxNombreMuestraRA101, width = 20, borderwidth = 1, relief = "flat")
EntryNombreMuestraRA101.grid(row = 10, column = 1, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloMuestraRA102 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloMuestraRA102, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloMuestraRA102.grid(row = 10, column = 2, sticky = 'NSEW', padx = 1, pady = 1)

EntryFechaTomaRA103 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxFechaTomaRA103, width = 20, borderwidth = 1, relief = "flat")
EntryFechaTomaRA103.grid(row = 10, column = 3, sticky = 'NSEW', padx = 1, pady = 1)

EntryHoraTomaRA104 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxHoraTomaRA104, width = 20, borderwidth = 1, relief = "flat")
EntryHoraTomaRA104.grid(row = 10, column = 4, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloIRA105 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloIRA105, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloIRA105.grid(row = 10, column = 5, sticky = 'NSEW', padx = 1, pady = 1)

EntryAnguloDRA106 = tkinter.Entry(master = FrameResumenAngulo, justify = 'center', textvariable = varAuxAnguloDRA106, width = 20, borderwidth = 1, relief = "flat")
EntryAnguloDRA106.grid(row = 10, column = 6, sticky = 'NSEW', padx = 1, pady = 1)

buttonBorrarRA = tkinter.Button(master = FrameResumenAngulo, text = 'Limpiar Resumen', command = limpiarResumenA, borderwidth = 1, relief = 'solid', cursor = 'hand2', font = ('Calibri', 10, 'bold', 'italic' ))
buttonBorrarRA.grid(row = 11, column = 6, sticky = 'NSEW', padx = 3, pady = 5)

root.mainloop()


# In[ ]:




