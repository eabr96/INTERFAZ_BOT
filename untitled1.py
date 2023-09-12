# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:42:25 2023

@author: ebolanos
"""

import pandas as pd
import json


from datetime import datetime
import re
from datetime import datetime as dt  # Renombrar el módulo import tkinter as tk
from tkinter import filedialog
import os
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np





df_excel = pd.read_excel('Datos_entrada.xlsx')



def compara_fechas(fecha_inicial,fecha_final):
    fecha_inicial_dt=pd.to_datetime(fecha_inicial, format=formato_deseado)
    fecha_final_dt=pd.to_datetime(fecha_final, format=formato_deseado)
    
    variable_retorno=None
    
    if fecha_final>fecha_inicial:
        variable_retorno=True
    else:
        variable_retorno=False
    
    return(variable_retorno)


# def validar_formato_fechas(columnas_fecha):
#     if df_excel is None:
#         print("No se ha cargado ningún archivo Excel.")
#         return
    
#     formato_deseado = "%d/%m/%Y %H:%M:%S"
    
#     for columna in columnas_fecha:
#         if columna not in df_excel.columns:
#             print(f"La columna {columna} no existe en el DataFrame.")
#             continue
            
#         formato_correcto = True
#         errores = []
        
#         for index, fecha_str in enumerate(df_excel[columna]):
#             try:
#                 # Intenta convertir la fecha en el formato deseado, si falla, marca un error.
#                 fecha1 = pd.to_datetime(fecha_str, format=formato_deseado)
                
                
#             except ValueError:
#                 formato_correcto = False
#                 errores.append(index + 1)
        
#         if formato_correcto:
#             print(f"El formato en la columna {columna} es correcto en todas las filas.")

#         else:
#             print(f"El formato en la columna {columna} es incorrecto en las filas {', '.join(map(str, errores))}.")
            
#     return fecha1

def validar_formato_fechas(columna_inicio, columna_final):
    if df_excel is None:
        print("No se ha cargado ningún archivo Excel.")
        return
    
    formato_deseado = "%d/%m/%Y %H:%M:%S"
    
    for columna in [columna_inicio, columna_final]:
        if columna not in df_excel.columns:
            print(f"La columna {columna} no existe en el DataFrame.")
            continue
            
        formato_correcto = True
        errores = []
        
        for index, fecha_str in enumerate(df_excel[columna]):
            try:
                # Intenta convertir la fecha en el formato deseado, si falla, marca un error.
                fecha = pd.to_datetime(fecha_str, format=formato_deseado)
            except ValueError:
                formato_correcto = False
                errores.append(index + 1)
        
        if formato_correcto:
            print(f"El formato en la columna {columna} es correcto en todas las filas.")
        else:
            print(f"El formato en la columna {columna} es incorrecto en las filas {', '.join(map(str, errores))}.")

try:
    #columna_inicio = "INICIO_PREVISTO"
    #columna_final = "FIN_PREVISTO"
    
    columna_inicio = "INICIO_PROGRAMADO"
    columna_final = "FIN_PROGRAMADO"
    
    validar_formato_fechas(columna_inicio, columna_final)
    
    

except Exception as e:
    print(f"Error en validación de formato fecha: {str(e)}")




# try:
#     columnas_fecha = ["INICIO_PREVISTO", "FIN_PREVISTO", "INICIO_PROGRAMADO", "FIN_PROGRAMADO"]  # Columnas que deseas validar
#     validar_formato_fechas(columnas_fecha)

# except Exception as e:
#     print(f"Error en validación de formato fecha: {str(e)}")
    
    

