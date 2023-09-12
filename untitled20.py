# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 14:38:49 2023

@author: ebolanos
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

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

def cargar_archivo():
    global df_excel
    file_path = filedialog.askopenfilename(filetypes=[("Archivos de Excel", "*.xlsx")])
    if file_path:
        try:
            df_excel = pd.read_excel(file_path)
            columnas_fecha = ["INICIO_PREVISTO", "FIN_PREVISTO", "INICIO_PROGRAMADO", "FIN_PROGRAMADO"]
            validar_agenda(columnas_fecha)
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar el archivo: {str(e)}")

def validar_y_mostrar():
    if "df_excel" not in globals():
        messagebox.showerror("Error", "No se ha cargado ningún archivo Excel.")
        return
    
    columnas_fecha = ["INICIO_PREVISTO", "FIN_PREVISTO", "INICIO_PROGRAMADO", "FIN_PROGRAMADO"]
    resultados = validar_formato_fechas(columnas_fecha)
    
    for columna_inicio, columna_fin in zip(columnas_fecha[::2], columnas_fecha[1::2]):
        if resultados.get(columna_inicio, False) and resultados.get(columna_fin, False):
            fechas_inicio = pd.to_datetime(df_excel[columna_inicio], format='%d/%m/%Y %H:%M:%S')
            fechas_fin = pd.to_datetime(df_excel[columna_fin], format='%d/%m/%Y %H:%M:%S')
            
            agendadas_correctamente = all(fecha_fin > fecha_inicio for fecha_inicio, fecha_fin in zip(fechas_inicio, fechas_fin))
            
            if agendadas_correctamente:
                messagebox.showinfo("Resultado", f"Las fechas en las columnas {columna_inicio} y {columna_fin} están agendadas correctamente.")
            else:
                messagebox.showwarning("Resultado", f"Las fechas en las columnas {columna_inicio} y {columna_fin} no están agendadas correctamente, revisar y corregir.")

# Crear la ventana principal
root = tk.Tk()
root.title("Validación de Fechas")

# Botones
load_button = tk.Button(root, text="Cargar Archivo Excel", command=cargar_archivo)
validate_button = tk.Button(root, text="Validar y Mostrar Resultados", command=validar_y_mostrar)

load_button.pack(pady=10)
validate_button.pack(pady=10)

root.mainloop()
