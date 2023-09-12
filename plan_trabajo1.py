# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 08:48:35 2023

@author: ebolanos
"""

import pandas as pd
import tkinter as tk

# Leer los DataFrames desde los archivos Excel
df_base = pd.read_excel('Validacion_plan_trabajo.xlsx')
df_bot = pd.read_excel('Datos_entrada.xlsx')


# Definir las funciones de validación y mostrar mensajes
def validacion_plan_trabajo(columa_id):

    plan_trabajo_bot = df_bot['PLAN_TRABAJO'] #infromacion columna plan de trabajo 
    print (plan_trabajo_bot)

    for dato_plan_trabajo in plan_trabajo_bot: 

        a = df_base.loc[df_base['PLAN_TRABAJO'] == dato_plan_trabajo] #informacion de plan_trabajo de df_base
        print(a)

        if not a.empty:
            print(f"---------------Dato '{dato_plan_trabajo}' encontrado en df_base.---------------")

            columnas_a_validar = a.columns.tolist() #columnas del df_base 
            x= print(f"{columnas_a_validar} de df_base")

            for columna in columnas_a_validar: #recorrer columna de df_base
                print (f" '{columna}' en {columnas_a_validar} de df_base ")
                       
                if columna in df_bot.columns: #si columna de df_base esta en df_bot,object????????????????????????????????????
                    print(f" '{columna}' en  '{df_bot.columns}' ")
                    
                    if df_bot[columna][df_bot['PLAN_TRABAJO'] == dato_plan_trabajo].values[0] == a[columna].values[0]:
                        print(f"El valor en la columna {columna} es válido para ID: {df_bot['ID'].values[0]} en df_bot según df_base .")

                    elif pd.isna(df_bot[columna][df_bot['PLAN_TRABAJO'] == dato_plan_trabajo].values[0]) and pd.isna(a[columna].values[0]):
                        print(f"El valor en la columna {columna} está vacío y es válido para ID: {df_bot['ID'].values[0]} en df_bot según df_base.")
                        
                    elif pd.isna(df_bot[columna][df_bot['PLAN_TRABAJO'] == dato_plan_trabajo].values[0]):
                        print(f"El valor en la columna {columna} está vacío en para ID: {df_bot['ID'].values[0]} de df_bot")

                    else: 
                        print(f"El valor en la columna {columna} no es válido ID: {df_bot['ID'].values[0]} en df_bot según df_base.")
                else:
                    print(f"La columna {columna} ID: {df_bot['ID'].values[0]} no existe en df_bot.")
        else:
            print(f"Dato '{dato_plan_trabajo}' no encontrado en df_base.")

# Llamada a la función
validacion_plan_trabajo("ID")
