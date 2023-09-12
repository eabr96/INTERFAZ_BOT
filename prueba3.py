# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 17:24:02 2023

@author: ebolanos
"""

import pandas as pd

# Cargar los DataFrames desde archivos Excel
df_base = pd.read_excel('Validacion_plan_trabajo.xlsx')
df_bot = pd.read_excel('Datos_entrada.xlsx')

# Obtener la columna 'PLAN_TRABAJO' de df_bot
plan_trabajo_bot = df_bot['PLAN_TRABAJO']

# Iterar sobre los datos de 'PLAN_TRABAJO' en df_bot
for dato_plan_trabajo in plan_trabajo_bot: 
    print(f"Dato PLAN_TRABAJO bot es: '{dato_plan_trabajo}'")
    
    # Filtrar df_base para obtener las filas con el mismo 'PLAN_TRABAJO' que el dato actual de df_bot
    a = df_base.loc[df_base['PLAN_TRABAJO'] == dato_plan_trabajo]
    
    # Verificar si el dato de 'PLAN_TRABAJO' existe en df_base
    if not a.empty:
        print(f"Dato '{dato_plan_trabajo}' encontrado en df_base.")
        
        # Iterar sobre las columnas a validar
        for columna in df_bot.columns:
            if columna in df_base.columns:
                print(f"La columna {columna} existe en df_base y df_bot.")
                
                # Comparar los datos uno por uno en cada campo de cada columna
                for indice, valor_bot in enumerate(df_bot[columna]):
                    valor_base = a[columna].values[indice]
                    
                    if valor_bot == valor_base:
                        print(f"Dato en la columna {columna} para el dato '{dato_plan_trabajo}' es igual.")
                    else:
                        print(f"Dato en la columna {columna} para el dato '{dato_plan_trabajo}' es diferente.")
            else:
                print(f"La columna {columna} no existe en df_base.")
    else:
        print(f"Dato '{dato_plan_trabajo}' no encontrado en df_base.")
