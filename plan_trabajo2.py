# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 10:23:11 2023

@author: ebolanos
"""

import pandas as pd
import tkinter as tk

# Leer la hoja 'Planes_Trabajo' del archivo Excel 'Datos_entrada.xlsx'
df_planes_trabajo = pd.read_excel('Datos_entrada.xlsx', sheet_name='Planes_Trabajo')

df_bot = pd.read_excel('Datos_entrada.xlsx')

# Definir las funciones de validación y mostrar mensajes
def validacion_plan_trabajo(columna_id):

    plan_trabajo_bot = df_bot['PLAN_TRABAJO'] # Información de la columna plan de trabajo 
    print(plan_trabajo_bot)

    for dato_plan_trabajo in plan_trabajo_bot: 

        a = df_planes_trabajo.loc[df_planes_trabajo['PLAN_TRABAJO'] == dato_plan_trabajo] # Informacion de plan_trabajo de df_bot
        print(a)

        if not a.empty:
            print(f"---------------Dato '{dato_plan_trabajo}' encontrado en Planes_Trabajo de df_bot.---------------")

            columnas_a_validar = a.columns.tolist() # Columnas de la hoja 'Planes_Trabajo'
            x = print(f"{columnas_a_validar} de Planes_Trabajo de df_bot")

            for columna in columnas_a_validar: # Recorrer columna de la hoja 'Planes_Trabajo'
                print(f"'{columna}' en {columnas_a_validar} de Planes_Trabajo de df_bot ")
                       
                if columna in df_bot.columns: # Si columna de df_bot está en df_bot
                    print(f"'{columna}' en  '{df_bot.columns}' ")
                    
                    if df_bot[columna][df_bot['PLAN_TRABAJO'] == dato_plan_trabajo].values[0] == a[columna].values[0]:
                        print(f"El valor en la columna {columna} es válido para ID: {df_bot[columna_id].values[0]} en df_bot según Planes_Trabajo de df_bot.")

                    elif pd.isna(df_bot[columna][df_bot['PLAN_TRABAJO'] == dato_plan_trabajo].values[0]) and pd.isna(a[columna].values[0]):
                        print(f"El valor en la columna {columna} está vacío y es válido para ID: {df_bot[columna_id].values[0]} en df_bot según Planes_Trabajo de df_bot.")
                        
                    elif pd.isna(df_bot[columna][df_bot['PLAN_TRABAJO'] == dato_plan_trabajo].values[0]):
                        print(f"El valor en la columna {columna} está vacío en para ID: {df_bot[columna_id].values[0]} de df_bot")

                    else: 
                        print(f"El valor en la columna {columna} no es válido ID: {df_bot[columna_id].values[0]} en df_bot según Planes_Trabajo de df_bot.")
                else:
                    print(f"La columna {columna} ID: {df_bot[columna_id].values[0]} no existe en df_bot.")
        else:
            print(f"Dato '{dato_plan_trabajo}' no encontrado en Planes_Trabajo de df_bot.")

# Llamada a la función
validacion_plan_trabajo(columna_id="ID")
