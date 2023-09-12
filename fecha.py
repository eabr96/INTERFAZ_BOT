# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 13:47:44 2023

@author: ebolanos
"""
import pandas as pd
from datetime import datetime 


df_excel = pd.read_excel('Datos_entrada.xlsx')

def validar_formato_fechas(df_excel, columna_fecha_inicial, columna_fecha_final, columna_id):
    formato_personalizado = "%d/%m/%Y %H:%M:%S %p"  # Formato día/mes/año
    mensajes = []  # Lista para almacenar los mensajes
    agendamientos_correctos = True  # Variable de bandera

    try:
        for index, row in df_excel.iterrows():
            fecha_inicial = row[columna_fecha_inicial]
            fecha_final = row[columna_fecha_final]

            try:
                if pd.isna(fecha_inicial) or pd.isna(fecha_final) or fecha_inicial == '' or fecha_final == '' or pd.isnull(fecha_inicial) or pd.isnull(fecha_final):
                    mensajes.append(f"En OT {row[columna_id]}: existen campos vacios para validar fecha")
                    print(f"En OT {row[columna_id]}: Alguno de los campos en '{columna_fecha_inicial}' y '{columna_fecha_final}' está vacío, NaN o NaT, verificar. REVISAR.")
                    agendamientos_correctos = False  # Cambiar bandera si hay error
                else: 
                            
                    fecha_inicial_dt =datetime.strptime((fecha_inicial), format = formato_personalizado)
                    fecha_final_dt = datetime.strptime((fecha_final), format = formato_personalizado)

                    if fecha_final_dt > fecha_inicial_dt:
                        mensajes.append(f"Agendamiento correcto en OT {row[columna_id]}: La fecha final  es mayor que la fecha inicial.")
                        #print(f"Agendamiento correcto en OT {row[columna_id]}: La fecha final  es mayor que la fecha inicial.")
                    else:
                        mensajes.append(f"En OT {row[columna_id]}: no cumple con la comparación de fechas, revisar.")
                        print(f"En OT {row[columna_id]}: no cumple con la comparación de fechas, revisar.")
                        agendamientos_correctos = False


            except Exception as e:
                mensajes.append(f"Error en el ciclo  (ID: {row[columna_id]}): {e}")
                agendamientos_correctos = False  # Cambiar bandera si hay error

            if not agendamientos_correctos:  # Si hubo algún error, marcarlo como incorrecto en el resumen final
                mensajes.append(f"Hubo errores en ID: {row[columna_id]} .")
                print(f"Hubo errores en ID: {row[columna_id]} .")

    except Exception as e:
        mensajes.append(f"Error al validar fechas: {e}")

    return agendamientos_correctos, mensajes

# Llamada a la función
agendamientos_correctos1, mensajes1 = validar_formato_fechas(df_excel,"INICIO_PREVISTO", "FIN_PREVISTO", "ID")
agendamientos_correctos2, mensajes2 = validar_formato_fechas(df_excel,"INICIO_PROGRAMADO", "FIN_PROGRAMADO", "ID")


for mensaje in mensajes1:
    print(mensaje)


for mensaje in mensajes2:
    print(mensaje)

