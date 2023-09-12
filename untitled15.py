# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:39:51 2023

@author: ebolanos
"""
#chrystiam
#%% Importar librerías
import pandas as pd
import json


#%% crear json
try:
    with open("correspondencia.json", encoding='utf-8') as file:
        correspondencia = json.load(file)
        
except FileNotFoundError:
    correspondencia = {}


df_excel = pd.read_excel('Datos_entrada.xlsx')

#%% crear funciones
def validar_correspondencia(df_excel, columna1, columna2, estructura_correspondencia):
    
    # df_excel = pd.read_excel('Datos_entrada.xlsx')
    # columna1= "NOMBRE_CLASIFICACION"
    # columna2= "CLASIFICACION"
    # estructura_correspondencia= 'datos_clasificaciones'
    
    
    for index, row in df_excel.iterrows():
        valor_columna1 = str(row[columna1])
        valor_columna2 = str(row[columna2])
        
        if correspondencia[estructura_correspondencia][valor_columna1]==valor_columna2:
            print(correspondencia[estructura_correspondencia][valor_columna1])
        # if valor_columna1 in estructura_correspondencia and valor_columna2 == estructura_correspondencia.get(valor_columna1):
            print(f"-Fila {index}: Existe correspondencia entre Variable1: {valor_columna1}, Variable2: {valor_columna2} -")
      
        else:
            print(f"-Fila {index}: No existe correspondencia. Variable1: {valor_columna1}, Variable2: {valor_columna2}-")


#%% Prueba

validar_correspondencia(df_excel, "NOMBRE_CLASIFICACION", "CLASIFICACION", 'datos_clasificaciones')

validar_correspondencia(df_excel, "NOMBRE_PLANIFICADOR", "PLANIFICADOR", 'datos_planificadores')















#df_excel[["NOMBRE_PLANIFICADOR", "PLANIFICADOR"]]
#df_excel.loc[1,'PLANIFICADOR']==correspondencia[estructura_correspondencia][valor_columna1]
