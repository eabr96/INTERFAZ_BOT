# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 16:34:06 2023

@author: ebolanos
"""

import pandas as pd

df_excel = pd.read_excel('Datos_entrada.xlsx')

def validar_formato_fechas(columnas_fecha):
    if df_excel is None:
        print("No se ha cargado ningún archivo Excel.")
        return False  # Retorna False si no se ha cargado ningún archivo
    
    formato_deseado = "%d/%m/%Y %H:%M:%S"
    
    formatos_correctos = {}  # Un diccionario para almacenar los resultados por columna
    
    for columna in columnas_fecha:
        if columna not in df_excel.columns:
            print(f"La columna {columna} no existe en el DataFrame.")
            formatos_correctos[columna] = False
            continue
            
        formato_correcto = True
        errores = []
        
        for index, fecha_str in enumerate(df_excel[columna]):
            if pd.isna(fecha_str) or fecha_str.isspace():
                continue  # Ignorar celdas vacías o con espacios en blanco
            
            try:
                # Intenta convertir la fecha en el formato deseado, si falla, marca un error.
                fecha = pd.to_datetime(fecha_str, format=formato_deseado)
            except ValueError:
                formato_correcto = False
                errores.append(index + 1)
        
        formatos_correctos[columna] = formato_correcto
        
        if formato_correcto:
            print(f"El formato en la columna {columna} es correcto en todas las filas, incluso con celdas vacías o espacios en blanco.")

        else:
            print(f"El formato en la columna {columna} es incorrecto en las filas {', '.join(map(str, errores))}.")
    
    return formatos_correctos  # Retorna el diccionario de resultados

def validar_agenda(columnas_fecha):
    resultados = validar_formato_fechas(columnas_fecha)
    
    for columna_inicio, columna_fin in zip(columnas_fecha[::2], columnas_fecha[1::2]):
        if resultados.get(columna_inicio, False) and resultados.get(columna_fin, False):
            fechas_inicio = pd.to_datetime(df_excel[columna_inicio], format='%d/%m/%Y %H:%M:%S')
            fechas_fin = pd.to_datetime(df_excel[columna_fin], format='%d/%m/%Y %H:%M:%S')
            
            agendadas_correctamente = all(fecha_fin > fecha_inicio for fecha_inicio, fecha_fin in zip(fechas_inicio, fechas_fin))
            
            if agendadas_correctamente:
                print(f"Las fechas en las columnas {columna_inicio} y {columna_fin} están agendadas correctamente.")
            else:
                print(f"Las fechas en las columnas {columna_inicio} y {columna_fin} no están agendadas correctamente, revisar y corregir.")

try:
    columnas_fecha = ["INICIO_PREVISTO", "FIN_PREVISTO", "INICIO_PROGRAMADO", "FIN_PROGRAMADO"]  # Columnas que deseas validar y comparar
    validar_agenda(columnas_fecha)
    
except Exception as e:
    print(f"Error en validación de agenda: {str(e)}")

#%%% comparar 



df_excel = pd.read_excel('Datos_entrada.xlsx')

def validar_fecha(df, columna_fecha_inicial, columna_fecha_final):
    
    try:
        df[columna_fecha_inicial] = pd.to_datetime(df_excel[columna_fecha_inicial], errors='coerce')
        df[columna_fecha_final] = pd.to_datetime(df_excel[columna_fecha_final], errors='coerce')
        print(f"Fechas en las columnas '{columna_fecha_inicial}' y '{columna_fecha_final}' fueron convertidas exitosamente.")
    except Exception as e:
        print(f"Error al validar fechas: {e}")
        print(f"No se pudieron convertir las fechas en las columnas '{columna_fecha_inicial}' y '{columna_fecha_final}'.")

# Supongamos que tienes un DataFrame llamado df_excel y columnas de fecha llamadas
# 'fecha_inicial' y 'fecha_final' que deseas convertir a datetime
validar_fecha(df_excel, 'fecha_inicial', 'fecha_final')

