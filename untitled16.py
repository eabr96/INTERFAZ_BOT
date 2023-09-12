# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:50:38 2023

@author: ebolanos
"""

import pandas as pd
import json

# Cargar el archivo JSON
try:
    with open("correspondencia.json", encoding='utf-8') as file:
        correspondencia = json.load(file)
except FileNotFoundError:
    correspondencia = {}

df_excel = pd.read_excel('Datos_entrada.xlsx')

def validar_correspondencia(df_excel, columna1, columna2, estructura_correspondencia):
    for index, row in df_excel.iterrows():
        valor_columna1 = str(row[columna1])
        valor_columna2 = str(row[columna2])
        
        # Comprobar si existe la correspondencia en el diccionario JSON
        if estructura_correspondencia in correspondencia and valor_columna1 in correspondencia[estructura_correspondencia]:
            if valor_columna2 == correspondencia[estructura_correspondencia][valor_columna1]:
                print(f"Fila {index}: Existe correspondencia")
            else:
                print(f"Fila {index}: No coincide con la correspondencia. Variable1: {valor_columna1}, Variable2: {valor_columna2}")
        else:
            print(f"Fila {index}: No existe correspondencia. Variable1: {valor_columna1}, Variable2: {valor_columna2}")

# Prueba con tus claves reales del diccionario JSON
validar_correspondencia(df_excel, "NOMBRE_CLASIFICACION", "CLASIFICACION", 'datos_clasificaciones')
validar_correspondencia(df_excel, "NOMBRE_PLANIFICADOR", "PLANIFICADOR", 'datos_planificadores')

# Puedes realizar correcciones si es necesario aquí
