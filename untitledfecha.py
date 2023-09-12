# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 09:37:26 2023

@author: ebolanos
"""

import pandas as pd

df_excel = pd.read_excel('Datos_entrada.xlsx')

import pandas as pd

def validar_fecha1(df, columna_fecha_inicial, columna_fecha_final, columna_id):
    formato_personalizado = "%d/%m/%Y %H:%M:%S"  # Formato día/mes/año

    try:
        for index, row in df.iterrows():
            fecha_inicial = row[columna_fecha_inicial]
            fecha_final = row[columna_fecha_final]

            

            try:
                # Convierte las fechas al formato deseado "día/mes/año"
                fecha_inicial = pd.to_datetime(fecha_inicial, format=formato_personalizado)
                fecha_final = pd.to_datetime(fecha_final, format=formato_personalizado)
                
                # Verifica si alguno de los campos de fecha está vacío (NaN)
                if (fecha_inicial == ''or 'nan') or (fecha_final == ''or 'nan') :
                    print(f"Advertencia, en OT {row[columna_id]}: Uno o ambos campos de fecha '{columna_fecha_inicial}' y '{columna_fecha_final}' están vacíos.")
                    continue  # Salta esta iteración y pasa a la siguiente fila

                # Verifica si la fecha final es mayor que la fecha inicial
                if fecha_final <= fecha_inicial:
                    print(f"Error de agendamiento en OT {row[columna_id]}: La fecha '{columna_fecha_final}' no es mayor que la '{columna_fecha_inicial}'. ")
                else:
                    print(f"En OT {row[columna_id]}: fecha '{columna_fecha_inicial}' y '{columna_fecha_final}' agendadas correctamente.")
                    
            except Exception as e:
                # Imprime el error junto con la columna_id para una mejor identificación
                print(f"Error en fila {index + 1} (ID: {row[columna_id]}): {e}")

    except Exception as e:
        print(f"Error al validar fechas: {e}")


# Suponiendo que tienes un DataFrame llamado df_excel y columnas de fecha llamadas
# 'fecha_inicial' y 'fecha_final' que deseas convertir a datetime
# validar_fecha(df_excel, 'INICIO_PREVISTO', 'FIN_PREVISTO', 'ID')

#%%FUNCION FORMATO FECHA

def validar_fecha(df, columna_fecha_inicial, columna_fecha_final, columna_id):
    formato_personalizado = "%d/%m/%Y %H:%M"  # Formato día/mes/año

    try:
        for index, row in df.iterrows():
            fecha_inicial = row[columna_fecha_inicial]
            fecha_final = row[columna_fecha_final]
            
            print(f"'{fecha_inicial}' y '{fecha_final}'")

            if pd.isna(fecha_inicial) or pd.isna(fecha_final) or fecha_inicial == '' or fecha_final == '' or pd.isnull(fecha_inicial) or pd.isnull(fecha_final):
                print(f"En OT {row[columna_id]}: Alguno de los campos en '{columna_fecha_inicial}' y '{columna_fecha_final}' está vacío, NaN o NaT, verificar. REVISAR.")
                continue  # Salta esta iteración y pasa a la siguiente fila
                            

            try:
                # Convierte las fechas al formato deseado "día/mes/año"
                fecha_inicial = pd.to_datetime(fecha_inicial, format=formato_personalizado)
                fecha_final = pd.to_datetime(fecha_final, format=formato_personalizado)

                if pd.notna(fecha_inicial) and pd.notna(fecha_final):  # Verifica que la conversión se haya realizado correctamente
                    print(f"En OT {row[columna_id]}: fecha '{columna_fecha_inicial}' y '{columna_fecha_final}' en formato correctamente.")
                
                # Verifica si la fecha final es mayor que la fecha inicial
                if fecha_final <= fecha_inicial:
                    print(f"Error de agendamiento en OT {row[columna_id]}: La fecha '{columna_fecha_final}' no es mayor que la '{columna_fecha_inicial}'. ")
                    
            except Exception as e:
                # Imprime el error junto con la columna_id para una mejor identificación
                print(f"Error en fila {index + 1} (ID: {row[columna_id]}): {e}")

    except Exception as e:
        print(f"Error al validar fechas: {e}")


        
        
validar_fecha(df_excel, 'INICIO_PREVISTO', 'FIN_PREVISTO', 'ID')
        
