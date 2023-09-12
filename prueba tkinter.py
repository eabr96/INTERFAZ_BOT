# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 10:04:08 2023

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

    plan_trabajo_bot = df_bot['PLAN_TRABAJO']

    for dato_plan_trabajo in plan_trabajo_bot: 
        
        
        a = df_base.loc[df_base['PLAN_TRABAJO'] == dato_plan_trabajo]

        if not a.empty:
            mensajes.append(f"---------------Dato '{dato_plan_trabajo}' encontrado en df_base.---------------")

            columnas_a_validar = a.columns.tolist()

            for columna in columnas_a_validar:
                if columna in df_bot.columns:
                    if df_bot[columna][df_bot['PLAN_TRABAJO'] == dato_plan_trabajo].values[0] == a[columna].values[0]:
                        mensajes.append(f"El valor en la columna {columna} es válido en df_bot según df_base.")

                    elif pd.isna(df_bot[columna][df_bot['PLAN_TRABAJO'] == dato_plan_trabajo].values[0]) and pd.isna(a[columna].values[0]):
                        mensajes.append(f"El valor en la columna {columna} está vacío y es válido en df_bot según df_base.")
                        
                    elif pd.isna(df_bot[columna][df_bot['PLAN_TRABAJO'] == dato_plan_trabajo].values[0]):
                        mensajes.append(f"El valor en la columna {columna} está vacío y es válido para df_bot")

                    else:
                        mensajes.append(f"El valor en la columna {columna} no es válido en df_bot según df_base.")
                else:
                    mensajes.append(f"La columna {columna} no existe en df_bot.")
        else:
            mensajes.append(f"Dato '{dato_plan_trabajo}' no encontrado en df_base.")
    
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
