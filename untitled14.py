# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 17:15:14 2023

@author: ebolanos
"""
import pandas as pd
import json

try:
    with open("correspondencia.json", encoding='utf-8') as file:
        correspondencia = json.load(file)
        
except FileNotFoundError:
    correspondencia = {}

df_excel = pd.read_excel('Datos_entrada.xlsx')

def validar_correspondencia(df_excel, columna1, columna2, estructura_correspondencia):
     
    for index, row in df_excel.iterrows(): 
        if row[columna1] in estructura_correspondencia and row[columna2] == estructura_correspondencia[row[columna1]]:
            print("Existe correspondencia")
        else:
            print("No existe correspondencia")



       

validar_correspondencia(df_excel,'OTs', "NOMBRE_CLASIFICACION", "CLASIFICACION", correspondencia.get("datos_clasificaciones", {}))
validar_correspondencia(df_excel, 'OTs', "NOMBRE_PLANIFICADOR", "PLANIFICADOR", correspondencia.get("datos_planificadores", {}))



