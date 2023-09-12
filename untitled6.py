# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:56:17 2023

@author: ebolanos
"""
import pandas as pd

df_excel = pd.read_excel('Datos_entrada.xlsx')

def validar_formato_fechas(columna_fechainicio, columna_fechafin):
    if df_excel is None:
        print("No se ha cargado ningún archivo Excel.")
        return
    
    formato_deseado = "%d/%m/%Y %H:%M:%S"
    
    # Verificar que ambas columnas existan en el DataFrame
    if columna_fechainicio not in df_excel.columns or columna_fechafin not in df_excel.columns:
        print("Al menos una de las columnas no existe en el DataFrame.")
        return

    formato_correcto = True
    errores_formato = []
    
    for index, fecha_inicio_str in enumerate(df_excel[columna_fechainicio]):
        fecha_fin_str = df_excel[columna_fechafin].iloc[index]

        try:
            # Intenta convertir las fechas en el formato deseado, si falla, marca un error de formato.
            fecha_inicio = pd.to_datetime(fecha_inicio_str, format=formato_deseado)
            fecha_fin = pd.to_datetime(fecha_fin_str, format=formato_deseado)
        except ValueError:
            formato_correcto = False
            errores_formato.append(index + 1)

        if fecha_inicio > fecha_fin:
            print(f"Error en la fila {index + 1}: La fecha en {columna_fechafin} es menor que la fecha en {columna_fechainicio}.")

    if formato_correcto:
        print(f"El formato en las columnas {columna_fechainicio} y {columna_fechafin} es correcto en todas las filas.")
    else:
        print(f"El formato en las columnas {columna_fechainicio} y {columna_fechafin} es incorrecto en las filas {', '.join(map(str, errores_formato))}.")

try:
    columna_fechainicio = "INICIO_PREVISTO"
    columna_fechafin = "FIN_PREVISTO"
    validar_formato_fechas(columna_fechainicio, columna_fechafin)

except Exception as e:
    print(f"Error en validación de formato fecha: {str(e)}")
