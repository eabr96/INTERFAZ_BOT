# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 10:53:14 2023

@author: ebolanos
"""

#chrystiam
#%% Importar librerías
import pandas as pd
import json


#%% crear json
try:
    with open("validacion.json", encoding='utf-8') as file:
        validacion = json.load(file)
except FileNotFoundError:
    pass

df_excel = pd.read_excel('Datos_entrada.xlsx')

#%% crear funciones


import pandas as pd

def validacion_datos(df_excel, validacion):
    mensaje = ""

    # Convertir todas las columnas del DataFrame a formato de cadena (str)
    df_excel = df_excel.astype(str)

    for col, valores_validos in validacion.items():
        if col not in df_excel:
            mensaje += f"Advertencia: La columna '{col}' definida en el JSON no está presente en el archivo Excel y no será validada.\n"
            continue

        column_data = df_excel[col]

        for index, valor in column_data.items():
            if valor.strip() == "" or valor.strip() == "nan":
                mensaje += f"Advertencia: El valor en columna '{col}' en la fila {index} está vacío.\n"
                continue  # Valor vacío, pasa a la siguiente iteración

            if valor not in valores_validos:
                mensaje += f"Error: Valor '{valor}' en columna '{col}' en la fila {index} no es válido según el JSON.\n"

    if "Error" not in mensaje:
        mensaje += "Todos los datos son válidos según el JSON."
    else:
        mensaje += "Se encontraron algunos errores de validación o datos que debes verificar."

    return mensaje



#%% Prueba
# Llama a la función validacion_datos
resultado = validacion_datos(df_excel, validacion)

# Imprime el resultado
print(resultado)














#df_excel[["NOMBRE_PLANIFICADOR", "PLANIFICADOR"]]
#df_excel.loc[1,'PLANIFICADOR']==correspondencia[estructura_correspondencia][valor_columna1]
