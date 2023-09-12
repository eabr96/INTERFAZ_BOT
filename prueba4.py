# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 16:17:31 2023

@author: ebolanos
"""
import pandas as pd

def validacin_plan_trabajo():
    
    # Cargar los DataFrames desde archivos Excel
    df_base = pd.read_excel('Validacion_plan_trabajo.xlsx')
    df_bot = pd.read_excel('Datos_entrada.xlsx')
    
    # Obtener la columna 'PLAN_TRABAJO' de df_bot, se obtienen los datos en ella
    plan_trabajo_bot = df_bot['PLAN_TRABAJO']
    print(f"{plan_trabajo_bot}")
    
    # Iterar sobre los datos de 'PLAN_TRABAJO' en df_bot
    for dato_plan_trabajo in plan_trabajo_bot: 
        print(f"dato_plan_trabajo bot es:'{dato_plan_trabajo}'")
        
        # Filtrar df_base para obtener las filas con el mismo 'PLAN_TRABAJO' que el dato actual de df_bot
        a = df_base.loc[df_base['PLAN_TRABAJO'] == dato_plan_trabajo]
        
        # Verificar si el dato de 'PLAN_TRABAJO' existe en df_base
        if not a.empty:
            print(f"--------------------Dato '{dato_plan_trabajo}' encontrado en df_base.--------------------")
            
            # Obtener las columnas de a y almacenarlas en una lista
            columnas_a_validar = a.columns.tolist()
    
            # Iterar sobre las columnas a validar
            for columna in columnas_a_validar:
                if columna in df_bot.columns:
                    print(f"La columna {columna} existe en df_bot.")
                    
                    # Comparar el dato actual de df_bot con el valor correspondiente en df_base
                    if df_bot[columna][df_bot['PLAN_TRABAJO'] == dato_plan_trabajo].values[0] == a[columna].values[0]:
                        print(f"El valor en la columna {columna} es válido en df_bot según df_base.")
                    else:
                        print(f"El valor en la columna {columna} no es válido en df_bot según df_base.")
                    
                else:
                    print(f"La columna {columna} no existe en df_bot.")
        else:
            print(f"Dato '{dato_plan_trabajo}' no encontrado en df_base.")



validacin_plan_trabajo()
