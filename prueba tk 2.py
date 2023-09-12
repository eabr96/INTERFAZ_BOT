# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 15:34:08 2023

@author: ebolanos
"""

import pandas as pd
import tkinter as tk

# Leer los DataFrames desde los archivos Excel
df_base = pd.read_excel('Validacion_plan_trabajo.xlsx')
df_bot = pd.read_excel('Datos_entrada.xlsx')

# Definir las funciones de validación y mostrar mensajes
def validacion_plan_trabajo():
    mensajes = []  # Lista para almacenar los mensajes
    comparaciones_exitosas = 0  # Contador de comparaciones exitosas

    # Definir columnas_a_validar como una lista vacía por defecto
    columnas_a_validar = []

    

    for index, row in df_bot.iterrows():
        if pd.isna(row['OT']) and not pd.isna(df_base.at[index, 'OT']):
            mensajes.append(f"La fila {index} en df_bot tiene 'OT' vacío, pero en df_base contiene información.")

    plan_trabajo_bot = df_bot['PLAN_TRABAJO']

    for dato_plan_trabajo in plan_trabajo_bot: 
        a = df_base.loc[df_base['PLAN_TRABAJO'][0] == dato_plan_trabajo]

        if not a.empty:
            mensajes.append(f"---------------Dato '{dato_plan_trabajo}' encontrado en df_base.---------------")

            columnas_a_validar = a.columns.tolist()

            for columna in columnas_a_validar:
                if columna in df_bot.columns:
                    if pd.notna(df_bot['OT'][df_bot['PLAN_TRABAJO'] == dato_plan_trabajo].values[0]):
                        if df_bot[columna][df_bot['PLAN_TRABAJO'] == dato_plan_trabajo].values[0] == a[columna].values[0]:
                            comparaciones_exitosas += 1
                        else:
                            mensajes.append(f"El valor en la columna {columna} no es válido en df_bot según df_base.")
                    else:
                        mensajes.append(f"El campo 'OT' está vacío, se considera válido para la columna {columna}.")
                else:
                    mensajes.append(f"La columna {columna} no existe en df_bot.")
        else:
            mensajes.append(f"Dato '{dato_plan_trabajo}' no encontrado en df_base.")


    if comparaciones_exitosas == len(columnas_a_validar):
        mensajes.append("Todas las comparaciones fueron exitosas.")
    else:
        mensajes.append(f"No todas las comparaciones fueron exitosas. Se realizaron {comparaciones_exitosas} comparaciones exitosas.")

    return mensajes

def mostrar_mensajes():
    mensajes = validacion_plan_trabajo()
    for mensaje in mensajes:
        etiqueta = tk.Label(ventana, text=mensaje)
        etiqueta.pack()

# Crear ventana de tkinter
ventana = tk.Tk()

# Botón para iniciar la validación
boton_validar = tk.Button(ventana, text="Validar", command=mostrar_mensajes)
boton_validar.pack()

ventana.mainloop()
