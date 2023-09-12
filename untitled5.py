# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:40:55 2023

@author: ebolanos
"""

import pandas as pd

df_excel = pd.read_excel('Datos_entrada.xlsx')

def validar_formato_fechas(columnas_fecha):
    if df_excel is None:
        print("No se ha cargado ningún archivo Excel.")
        return
    
    formato_deseado = "%d/%m/%Y %H:%M:%S"
    
    for columna in columnas_fecha:
        if columna not in df_excel.columns:
            print(f"La columna {columna} no existe en el DataFrame.")
            continue
            
        formato_correcto = True
        errores_formato = []
        valores_vacios_o_nan = []

        for index, fecha_str in enumerate(df_excel[columna]):
            if pd.isna(fecha_str) or fecha_str == "":
                # Comprobar si el valor es NaN o está vacío
                valores_vacios_o_nan.append(index + 1)
                
                continue

            try:
                fecha = pd.to_datetime(fecha_str, format=formato_deseado)
            except ValueError:
                formato_correcto = False
                errores_formato.append(index + 1)
        
        if formato_correcto or valores_vacios_o_nan:
            print(f"El formato en la columna {columna} es correcto en todas las filas.")
            print(f"La columna {columna} tiene campos vacíos en las filas {', '.join(map(str, valores_vacios_o_nan))}.")
       
       
        else:
            print(f"El formato en la columna {columna} es incorrecto en las filas {', '.join(map(str, errores_formato))}.")

        

try:
    columnas_fecha = ["INICIO_PREVISTO", "FIN_PREVISTO"]  # Columnas que deseas validar
    validar_formato_fechas(columnas_fecha)

except Exception as e:
    print(f"Error en validación de formato fecha: {str(e)}")
