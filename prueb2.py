# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 09:13:03 2023

@author: ebolanos
"""
import pandas as pd


df_base = pd.read_excel('Validacion_plan_trabajo.xlsx')
df_bot = pd.read_excel('Datos_entrada.xlsx')


# Lista para almacenar los resultados
resultados = []
resultados1 =[]
SIN_UC=False
CON_UC=True
NADA=None

# Iterar a través del DataFrame de validación
for index, row in df_bot.iterrows():
    
    # Obtener la columna 'PLAN_TRABAJO' de df_bot, se obtienen los datos en ella OPCIONES
    plan_trabajo_bot = df_bot['PLAN_TRABAJO']
    print(f"{plan_trabajo_bot}")

    
    # Comprobar si el valor de 'PLAN_TRABAJO' está presente en el DataFrame base
    if plan_trabajo_bot in plan_trabajo_bot.values:
        print(f'OT: ID {row["ID"]} - Opcion de plan_trabajo en df_bot se encuentra en df_base')
       
        
        # Iterar sobre los datos de 'PLAN_TRABAJO' en df_bot
        for dato_plan_trabajo in plan_trabajo_bot: 
            print(f"dato_plan_trabajo bot es:'{dato_plan_trabajo}'")
            print(f"plan_trabajo_bot es:'{plan_trabajo_bot}'")
            # Filtrar df_base para obtener las filas con el mismo 'PLAN_TRABAJO' que el dato actual de df_bot
            a = df_base.loc[df_base['PLAN_TRABAJO'] == dato_plan_trabajo]
            
            # Verificar si el dato de 'PLAN_TRABAJO' existe en df_base
            if not a.empty:
                print(f"Dato '{dato_plan_trabajo}' encontrado en df_base.")
                
                # Obtener las columnas de a y almacenarlas en una lista
                columnas_a_validar = a.columns.tolist()
  
                # Iterar sobre las columnas a validar
                for columna in columnas_a_validar:
                    if columna in df_bot.columns:
                        print(f"La columna {columna} existe en df_bot.") #nombre de la columna 
                        
                        
                        
                    else:
                        print(f"La columna {columna} no existe en df_bot.")
            else:
                print(f"Dato '{dato_plan_trabajo}' no encontrado en df_base.")
              
    
            
    else:
        resultados.append(f'No Cumple' )

                          
# Imprimir los resultados
for resultado in resultados:
    
    print(resultado)





# # Comparar el dato actual de df_bot con el valor correspondiente en df_base
# if df_bot[columna][df_bot['PLAN_TRABAJO'] == dato_plan_trabajo].values[0] == a[columna].values[0]:
#     print(f"La columna {columna} es válida para el dato '{dato_plan_trabajo}'.")
    

# else:
#     print(f"La columna {columna} no es válida para el dato '{dato_plan_trabajo}'.")


