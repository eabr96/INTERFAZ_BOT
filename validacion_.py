# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:09:53 2023

@author: ebolanos
"""



from datetime import datetime as dt
from datetime import datetime  
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import tkinter as tk
import numpy as np
import json
import re
import os



class ProcesadorDatos:
    def __init__(self):
        self.excel_file = None
        self.df_excel = None
        self.archivo = None
        self.validacion = None
        self.correspondencia = None
        self.validacion = {}
        self.correspondencia = {}
        
        

        try:
            with open("validacion.json", encoding='utf-8') as file:
                self.validacion = json.load(file)
        except FileNotFoundError:
            pass
            
        try:
            with open("correspondencia.json", encoding='utf-8') as file:
                self.correspondencia = json.load(file)
        except FileNotFoundError:
            pass 
    
            
    def seleccionar_archivo(self): #Selecciona archivo formato xlsx y tambein lo convierte en str
        archivo = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx")])
        mensaje = None
        
        if archivo:
            if archivo.lower().endswith('.xlsx'):
                self.excel_file = archivo
                self.df_excel = pd.read_excel(archivo, dtype=str)
                
                mensaje = f"Archivo seleccionado: {self.excel_file}\n"
            else:
                mensaje = "Formato incorrecto. Selecciona un archivo .xlsx"
        return mensaje, archivo, self.df_excel
    
        
    
    def eliminar_archivo(self): #Elimina el archivo seleccionado 
        
        if self.df_excel is not None:
            self.excel_file = None
            self.df_excel = None
        
           
        else:
            return "No se ha seleccionado ningún archivo"
          
        
        
    def cantidad_elementos_OTs(self, columna_a_contar): #cuenta el numero de campos en la columna #ordenes de trabajo o ID
        if columna_a_contar != 'ID':
            return f"Solo se permite contar la columa correspondiente al numero de ordenes de trabajo, corregir '{columna_a_contar}' ."
        
        mensaje= ""
        if self.df_excel is not None:
            
            try:
                if columna_a_contar in self.df_excel.columns:
                    # Utiliza len() para contar elementos únicos en la columna especificada
                    num_elementos = len(self.df_excel[columna_a_contar].unique())
                    mensaje += f"Número de OTs: {num_elementos}." #f"Número de elementos únicos en ordenes de trabajo '{columna_a_contar}': {num_elementos}"
                    print (f"Número de ordenes de trabajo: {num_elementos}")
                else:
                    mensaje += "No es posible contar la cantidad de OTs. Validar nombre de las columnas en el archivo seleccionado."
                    print(f"No es posible contar la cantidad de OTs. La columna '{columna_a_contar}' no existe en el DataFrame.")
                return mensaje
            except Exception as e:
                
                print (f"Error en la funcion cantidad_elementos_OTs: {str(e)}")    
        else:
            return "No se ha seleccionado ningún archivo"



    def resumen_archivo(self):
        resumen_texto = ""
        if self.df_excel is not None:
            try:
                num_filas, num_columnas = self.df_excel.shape
    
                primeras_filas_columnas = self.df_excel.iloc[:5, :5]
                resumen_texto += "\nInformación Primeras 5 filas y 4 columnas:\n"
                resumen_texto += str(primeras_filas_columnas)
    
                return resumen_texto, self.df_excel_str
            except Exception as e:
                return f"Error al generar el resumen: {str(e)}"
        else:
            return "No se ha seleccionado ningún archivo"
        


    def informacion_archivo(self):
        if self.df_excel is not None:
            #print("-")

            try:
                xls = pd.ExcelFile(self.excel_file)
                nombres_hojas = xls.sheet_names
                num_hojas = len(nombres_hojas)
                hojas_texto = ", ".join(nombres_hojas)
                mensaje = f"Numero de hojas: {num_hojas} hojas. Nombre/s: {hojas_texto}."
                return mensaje
            except Exception as e:
                return f"Error al leer el archivo Excel: {str(e)}"
        
        else:
            return "No se ha seleccionado ningún archivo"
        
    
    def ubicacion(self):
        if self.df_excel is not None:
            mensaje = ""
            try:
                mensaje += f"Ubicación del archivo: '{self.excel_file}'"
                return mensaje
            except Exception as e:
                return f"Error al leer el archivo Excel: {str(e)}"
        else:
            return "No se ha seleccionado ningún archivo"

        

        
    def validar_archivo_excel(self, hojas_correctas, numero_hojas): 
        if self.df_excel is not None:
            try:
                xls = pd.ExcelFile(self.excel_file)  # Elimina la lista 'hojas_correctas' aquí
                nombres_hojas = xls.sheet_names
    
                if len(nombres_hojas) == numero_hojas and set(nombres_hojas) == set(hojas_correctas):
                    mensaje = f"El archivo seleccionado tiene {numero_hojas} hojas con los nombres requeridos. VALIDO."
                    return mensaje
                else:
                    mensaje = "El archivo seleccionado no cumple con los requisitos de hojas."
                    return mensaje
    
            except Exception as e:
                return f"Error al leer el archivo Excel: {str(e)}"
        else:
            return "No se ha seleccionado ningún archivo"



   

    def validacion_datos(self): #NOOOOOOO ELIMINAR
        mensaje = ""
    
        for col, valores_validos in self.validacion.items():
            if col not in self.df_excel:
                mensaje += f"Advertencia: La columna '{col}' definida en el JSON no está presente en el archivo Excel y no será validada.\n"
                continue
    
            column_data = self.df_excel[col]
            
            
    
            for index, valor in column_data.items():
                if pd.isna(valor):
                    mensaje += f"VERIFICAR. En '{col}' en la fila {index} el campo está vacío." #f"VERIFICAR. En '{col}' en la fila {index} el campo está vacío.\n"
                    continue  # Valor vacío, pasa a la siguiente iteración
    
                if isinstance(valor, (int)):
                    # Si el valor es numérico, validamos como número
                    if valor not in valores_validos:
                        mensaje += f"Error: Valor numérico '{valor}' en columna '{col}' en la fila {index} no es válido según el JSON.\n"
                elif isinstance(valor, str):
                    # Si el valor es una cadena de texto, validamos como cadena
                    if valor not in valores_validos:
                        mensaje += f"Error: Valor de texto '{valor}' en columna '{col}' en la fila {index} no es válido según el JSON.\n"
                else:
                    mensaje += f"Advertencia: Valor de tipo no válido en columna '{col}' en la fila {index}.\n"
    
        if "Error" not in mensaje:
            mensaje += "Todos los datos son válidos.VALIDO."
        else:
            mensaje += "Se encontraron errores de validación."
    
        return mensaje
    
    
    
    
    def validacion_ID(self): #VALIDA SI LOS NUMEROS DE id ESTAN DENTRO DE LAS DEMAS HOJAS 
        valid = True
        mensaje = ""
        
        if self.df_excel is None:
            return "No se ha seleccionado ningún archivo"
        
        
        try:
            if not isinstance(self.excel_file, str) or not self.excel_file.lower().endswith('.xlsx'):
                return "El archivo seleccionado no es un archivo Excel válido"
            
            # Leer todas las hojas del archivo Excel
            xls = pd.ExcelFile(self.excel_file)
            nombres_hojas = xls.sheet_names
            
            # Obtener los números de la columna "ID" de la primera hoja
            try:
                ids_primera_hoja = set(self.df_excel['ID'])
            except KeyError:
                return "La columna 'ID' no está presente en la primera hoja."
            
            for nombre_hoja in nombres_hojas:
                if nombre_hoja in ["Tablas_Apoyo", "Planes_Trabajo"]:
                    continue  # Saltar estas hojas
                    
                # Leer los datos de la columna "ID" de la hoja actual
                df_hoja = pd.read_excel(self.excel_file, sheet_name=nombre_hoja)
                
                try:
                    ids_hoja_actual = set(df_hoja['ID'])
                except KeyError:
                    mensaje += f"Error: La columna 'ID' no está presente en la hoja '{nombre_hoja}'.\n"
                    valid = False
                    continue
                
                # Verificar que los números de la hoja actual estén en la primera hoja
                if not ids_hoja_actual.issubset(ids_primera_hoja):
                    mensaje += f"Error: Los números en la hoja '{nombre_hoja}' no son válidos según la primera hoja.\n"
                    valid = False
            
            if valid:
                mensaje += "Validación de IDs exitosa. Los números en las hojas coinciden con la primera hoja."
            return mensaje
        except Exception as e:
            return f"Error al realizar la validación de IDs: {str(e)}"
    
    



    def validacion_NUMEROS(self, hoja_base, nombre_columna, hojas_a_verificar, hojas_a_excluir):
        valid = True
        mensaje = ""
        
        if self.df_excel is None:
            return "No se ha seleccionado ningún archivo"
        
        try:
            if not isinstance(self.excel_file, str) or not self.excel_file.lower().endswith('.xlsx'):
                return "El archivo seleccionado no es un archivo Excel válido"
            
            # Leer la hoja base
            df_base = pd.read_excel(self.excel_file, sheet_name=hoja_base)
            
            try:
                numeros_tarea_base = set(df_base[nombre_columna])
            except KeyError:
                return f"La columna '{nombre_columna}' no está presente en la hoja base '{hoja_base}'."
            
            # Leer las hojas a verificar
            xls = pd.ExcelFile(self.excel_file)
            nombres_hojas = xls.sheet_names
            
            for nombre_hoja in nombres_hojas:
                if nombre_hoja in hojas_a_excluir:
                    continue  # Excluir hojas especificadas
                    
                if nombre_hoja not in hojas_a_verificar:
                    continue  # Saltar hojas que no están en la lista de verificación
                    
                # Leer los datos de la columna de tarea de la hoja actual
                df_hoja_actual = pd.read_excel(self.excel_file, sheet_name=nombre_hoja)
                
                try:
                    numeros_tarea_hoja_actual = set(df_hoja_actual[nombre_columna])
                except KeyError:
                    mensaje += f"Error: La columna '{nombre_columna}' no está presente en la hoja '{nombre_hoja}'.\n"
                    valid = False
                    continue
                
                # Verificar que los números de tarea de la hoja actual estén en la hoja base
                if not numeros_tarea_hoja_actual.issubset(numeros_tarea_base):
                    mensaje += f"Error: Los números de tarea en la hoja '{nombre_hoja}' no coinciden con la hoja base '{hoja_base}'.\n"
                    valid = False
            
            if valid:
                mensaje += f"Verificación de números de '{nombre_columna}' exitosa. VALIDO.\n" #f"Verificación de números de '{nombre_columna}' exitosa. Los números coinciden con la hoja base '{hoja_base}'. CORRECTO."
            
            return mensaje
        
        except Exception as e:
            return f"Error al realizar la verificación de números para '{nombre_columna}': {str(e)}\n"
        
        
        
        


    
      
        
        
    #NO BORRAR SIN VERIFICAR OT
    def campos_obligatorios(self, columnas_requeridas, columna_ot):
        if self.df_excel is not None:
            # Validar que las columnas requeridas existan en el archivo Excel
            for columna in columnas_requeridas:
                if columna not in self.df_excel.columns:
                    return f"La columna {columna} no existe en el archivo Excel."
    
            # Inicializar una variable para verificar si todas las columnas requeridas están diligenciadas
            todas_diligenciadas = True
    
            # Inicializar una lista para llevar un registro de columnas vacías y sus IDs de orden de trabajo
            columnas_vacias = []
    
            # Realizar la validación de espacios obligatorios
            for fila in self.df_excel.itertuples():
                valor_ot = getattr(fila, columna_ot)
    
                # Verificar si la columna OT está vacía
                if pd.isna(valor_ot) or str(valor_ot).strip() == '' or str(valor_ot) == 'nan':
                    id_ot = fila.ID  # Obtener el número de orden de trabajo de la columna ID
                    for columna in columnas_requeridas:
                        valor_columna = getattr(fila, columna)
                        if str(valor_columna).strip() == '' or str(valor_columna) == 'nan':
                            columnas_vacias.append((columna, id_ot))  # Agregar columna y número de orden de trabajo
    
                    # Si la OT está vacía pero todas las columnas requeridas están diligenciadas, marcarlo como correcto
                    if columnas_vacias:
                        todas_diligenciadas = False
    
            if todas_diligenciadas:
                return "Los espacios obligatorios están diligenciados. VALIDO."
            else:
                errores = {}
                for columna, id_ot in columnas_vacias:
                    if id_ot in errores:
                        errores[id_ot].append(columna)
                    else:
                        errores[id_ot] = [columna]
    
                mensaje_errores = "VERIFICAR. Si deseas crear OTs, ten en cuenta que los ccampos en DESCRIPCION, CLASIFICACION, UBICACION, TIPO_TRABAJO, PRIORIDAD, GROT, DURACION, deben estar diligenciados.\n"
                for id_ot, columnas in errores.items():
                    #mensaje_errores += f"Exiten campos vacios en las columnas requeridas."
                    print (f" exiten campos vacios en las columnas '{columnas_requeridas}' {' ,'.join(columnas)} de {id_ot}.")
                
                mensaje_errores += "Si necesitas crear una orden de trabajo, pero si deseas modificar, los campos pueden estar vacios."
    
                return mensaje_errores
        else:
            return "No se proporcionó un archivo Excel para validar."
        
        
        
        
    def validar_formato_fechas(self, columna_fecha_inicial, columna_fecha_final, columna_id):
        formato_personalizado = "%d/%m/%Y %H:%M"  # Formato día/mes/año
        mensajes = []  # Lista para almacenar los mensajes
        agendamientos_correctos = True  # Variable de bandera
    
        try:
            for index, row in self.df_excel.iterrows():
                fecha_inicial = row[columna_fecha_inicial]
                fecha_final = row[columna_fecha_final]
    
                if pd.isna(fecha_inicial) or pd.isna(fecha_final) or fecha_inicial == '' or fecha_final == '' or pd.isnull(fecha_inicial) or pd.isnull(fecha_final):
                    mensajes.append(f"En OT {row[columna_id]}: existen campos vacios para validar fecha")
                    print (f"En OT {row[columna_id]}: Alguno de los campos en '{columna_fecha_inicial}' y '{columna_fecha_final}' está vacío, NaN o NaT, verificar. REVISAR.")
                    agendamientos_correctos = False  # Cambiar bandera si hay error
                    continue  # Salta esta iteración y pasa a la siguiente fila
    
                if fecha_inicial is None or fecha_final is None:
                    mensajes.append(f"En OT {row[columna_id]}: Alguno de los campos en '{columna_fecha_inicial}' y '{columna_fecha_final}' es None, verificar. REVISAR.")
                    agendamientos_correctos = False  # Cambiar bandera si hay error
                    continue  # Salta esta iteración y pasa a la siguiente fila
    
                try:
                    fecha_inicial = datetime.strptime(fecha_inicial, formato_personalizado)
                    fecha_final = datetime.strptime(fecha_final, formato_personalizado)
    
                    if fecha_final <= fecha_inicial:
                        mensajes.append(f"Error de agendamiento en OT {row[columna_id]}: La fecha final no es mayor que la fecha inicial.")
                        agendamientos_correctos = False  # Cambiar bandera si hay error
                    else:
                        mensajes.append(f"Agendamiento correcto en OT {row[columna_id]}: La fecha final es mayor que la fecha inicial.")
    
                except Exception as e:
                    mensajes.append(f"Error en fila {index + 1} (ID: {row[columna_id]}): {e}")
                    agendamientos_correctos = False  # Cambiar bandera si hay error
    
        except Exception as e:
            mensajes.append(f"Error al validar fechas: {e}")
            agendamientos_correctos = False  # Cambiar bandera si hay error
    
        if agendamientos_correctos:
            mensajes = ["Todos los agendamientos son correctos."]
        else:
            mensajes.append("Hubo errores en algunos agendamientos.")
    
        return mensajes

        
        
        
    # def validar_formato_fechas(self, columna_fecha_inicial, columna_fecha_final, columna_id):
    #     formato_personalizado = "%d/%m/%Y %H:%M"  # Formato día/mes/año
    
    #     try:
    #         for index, row in self.df_excel.iterrows():
    #             fecha_inicial = row[columna_fecha_inicial]
    #             fecha_final = row[columna_fecha_final]
    
    #             if pd.isna(fecha_inicial) or pd.isna(fecha_final) or fecha_inicial == '' or fecha_final == '' or pd.isnull(fecha_inicial) or pd.isnull(fecha_final):
    #                 print(f"En OT {row[columna_id]}: Alguno de los campos en '{columna_fecha_inicial}' y '{columna_fecha_final}' está vacío, NaN o NaT, verificar. REVISAR.")
    #                 continue  # Salta esta iteración y pasa a la siguiente fila
    
    #             if fecha_inicial is None or fecha_final is None:
    #                 print(f"En OT {row[columna_id]}: Alguno de los campos en '{columna_fecha_inicial}' y '{columna_fecha_final}' es None, verificar. REVISAR.")
    #                 continue  # Salta esta iteración y pasa a la siguiente fila
    
    #             try:
    #                 # Convierte las cadenas de fecha y hora al formato deseado "día/mes/año"
    #                 fecha_inicial = datetime.strptime(fecha_inicial, formato_personalizado)
    #                 fecha_final = datetime.strptime(fecha_final, formato_personalizado)
                
    #                 # Ahora puedes trabajar con las fechas como objetos datetime
    #                 fecha_inicial_formateada = fecha_inicial.strftime("%d/%m/%Y %H:%M:%S")
    #                 fecha_final_formateada = fecha_final.strftime("%d/%m/%Y %H:%M:%S")
                
    #                 if fecha_inicial and fecha_final:
    #                     print(f"Fecha inicial formateada: {fecha_inicial_formateada}")
    #                     print(f"Fecha final formateada: {fecha_final_formateada}")
                
    #                     # Verifica si la fecha final es mayor que la fecha inicial
    #                     if fecha_final <= fecha_inicial:
    #                         print("Error de agendamiento: La fecha final no es mayor que la fecha inicial.")
    #                     else:
    #                         print("Agendamiento correcto: La fecha final es mayor que la fecha inicial.")
    #                 else:
    #                     print("Error: No se pudo convertir alguna(s) fecha(s).")

                                
    #             except Exception as e:
    #                 # Imprime el error junto con la columna_id para una mejor identificación
    #                 print(f"Error en fila {index + 1} (ID: {row[columna_id]}): {e}")

    #     except Exception as e:
    #         print(f"Error al validar fechas: {e}")


    


    
    
    
    def validar_correspondencia(self, columna1, columna2, estructura_correspondencia, columna_id):
        mensaje = ""  # Inicializa el mensaje
    
        for index, row in self.df_excel.iterrows():
            valor_columna1 = str(row[columna1])
            valor_columna2 = str(row[columna2])
    
            try:
                if self.correspondencia.get(estructura_correspondencia, {}).get(valor_columna1) == valor_columna2:
                    mensaje = f"Entre {columna1} y {columna2} existe correspondencia. VALIDO.\n"
                else:
                    mensaje += f"En OT {row[columna_id]}: No existe correspondencia. {valor_columna1} y {valor_columna2}\n"
            except KeyError:
                mensaje += f"Orden de Trabajo {row[columna_id]}: Error - Clave no encontrada en el diccionario\n"
            except Exception as e:
                mensaje += f"Orden de Trabajo {row[columna_id]}: Error - {str(e)}\n"
    
        return mensaje
    
    
    def validacion_plan_trabajo(self):
        mensajes = []  # Lista para almacenar los mensajes
    
        # Cargar los DataFrames desde archivos Excel
        df_base = pd.read_excel('Validacion_plan_trabajo.xlsx')
        df_bot = self.df_excel  # Utilizamos el DataFrame cargado previamente

        
        # Obtener la columna 'PLAN_TRABAJO' de df_bot, se obtienen los datos en ella
        plan_trabajo_bot = df_bot['PLAN_TRABAJO']
        #mensajes.append(f"{plan_trabajo_bot}")
        
        # Iterar sobre los datos de 'PLAN_TRABAJO' en df_bot
        for dato_plan_trabajo in plan_trabajo_bot: 
            #mensajes.append(f"dato_plan_trabajo bot es:'{dato_plan_trabajo}'")
            #mensajes.append(f"plan_trabajo_bot es:'{plan_trabajo_bot}'")
            
            # Filtrar df_base para obtener las filas con el mismo 'PLAN_TRABAJO' que el dato actual de df_bot
            a = df_base.loc[df_base['PLAN_TRABAJO'] == dato_plan_trabajo]
            
            # Verificar si el dato de 'PLAN_TRABAJO' existe en df_base
            if not a.empty:
                mensajes.append(f"---------------Dato '{dato_plan_trabajo}' encontrado en df_base.---------------")
                
                # Obtener las columnas de a y almacenarlas en una lista
                columnas_a_validar = a.columns.tolist()
        
                # Iterar sobre las columnas a validar
                for columna in columnas_a_validar:
                    if columna in df_bot.columns:
                        #mensajes.append(f"La columna {columna} existe en df_bot.")
                        
                        # Comparar el dato actual de df_bot con el valor correspondiente en df_base
                        if df_bot[columna][df_bot['PLAN_TRABAJO'] == dato_plan_trabajo].values[0] == a[columna].values[0]:
                            mensajes.append(f"El valor en la columna {columna} es válido en df_bot según df_base.")
                            
                        elif pd.isna(df_bot[columna][df_bot['PLAN_TRABAJO'] == dato_plan_trabajo].values[0]) and pd.isna(a[columna].values[0]):
                            mensajes.append(f"El valor en la columna {columna} está vacío y es válido en df_bot según df_base.")
                            
                        else:
                            mensajes.append(f"El valor en la columna {columna} no es válido en df_bot según df_base.")
                        
                    else:
                        mensajes.append(f"La columna {columna} no existe en df_bot.")
            else:
                mensajes.append(f"Dato '{dato_plan_trabajo}' no encontrado en df_base.")
        
        return mensajes


    
    
    
    
    

#ESTA FUNCION NO BORRARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR#ESTA FUNCION NO BORRARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR#ESTA FUNCION NO BORRARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR#ESTA FUNCION NO BORRARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR#ESTA FUNCION NO BORRARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR   
# def validar_formato_fechas(self, columnas_fecha): #ESTA FUNCION NO BORRARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
#     if self.df_excel is None:
#         return "No se ha cargado ningún archivo Excel"

#     formato_deseado = "%d/%m/%Y %H:%M:%S"
#     mensajes = ""

#     for columna in columnas_fecha:
#         if columna not in self.df_excel.columns:
#             continue  # Ignorar columnas que no existen en el DataFrame

#         formato_correcto = True
#         errores = []

#         for index, fecha_str in enumerate(self.df_excel[columna]):
#             try:
#                 # Intenta convertir la fecha en el formato deseado, si falla, marca un error.
#                 fecha = pd.to_datetime(fecha_str, format=formato_deseado)
                
#             except ValueError:
#                 formato_correcto = False
#                 errores.append(str(index + 1))  # Convierte el número de fila a cadena

#         if formato_correcto:
#             mensajes += f"El formato de fecha en {columna} es correcto en todas las filas.\n"
            
            
            
            
            
#         else:
#             # Asegúrate de que errores sea una lista antes de intentar unirlo
#             if errores:
#                 mensajes += f"El formato de fecha en {columna} es incorrecto en las filas: {', '.join(errores)}\n"
#             else:
#                 mensajes += f"El formato de fecha en {columna} es incorrecto en algunas filas.\n"

#     return mensajes




#TAMPOCOOOOOOOOOOOOOOOOOO
# def validar_formato_fechas(self, columnas_fecha):
#     if self.df_excel is None:
#         return "No se ha cargado ningún archivo Excel."
    
#     mensajes_formato=""

#     formato_deseado = "%d/%m/%Y %H:%M:%S"

#     formatos_correctos = {}

#     for columna in columnas_fecha:
#         if columna not in self.df_excel.columns:
#             formatos_correctos[columna] = False
#             continue

#         formato_correcto = True
#         errores = []

#         for index, fecha_str in enumerate(self.df_excel[columna]):
#             if pd.isna(fecha_str) or fecha_str.isspace():
#                 continue

#             try:
#                 fecha = pd.to_datetime(fecha_str, format=formato_deseado)
#             except ValueError:
#                 formato_correcto = False
#                 errores.append(index + 1)

#         formatos_correctos[columna] = formato_correcto

#         if formato_correcto:
#             print(f"El formato en la columna {columna} es correcto en todas las filas, incluso con celdas vacías o espacios en blanco.")
#             mensajes_formato+= f"El formato en la columna {columna} es correcto en todas las filas, incluso con celdas vacías o espacios en blanco."
#         else:
#             print(f"El formato en la columna {columna} es incorrecto en las filas {', '.join(map(str, errores))}.")
#             mensajes_formato+= f"El formato en la columna {columna} es incorrecto en las filas {', '.join(map(str, errores))}."
            
#     return formatos_correctos, mensajes_formato


# def validar_agenda(self, columnas_fecha):
#     resultados = self.validar_formato_fechas(columnas_fecha)
    
#     mensajes=""

#     for columna_inicio, columna_fin in zip(columnas_fecha[::2], columnas_fecha[1::2]):
#         if resultados.get(columna_inicio, False) and resultados.get(columna_fin, False):
#             fechas_inicio = pd.to_datetime(self.df_excel[columna_inicio], format='%d/%m/%Y %H:%M:%S')
#             fechas_fin = pd.to_datetime(self.df_excel[columna_fin], format='%d/%m/%Y %H:%M:%S')

#             agendadas_correctamente = all(fecha_fin > fecha_inicio for fecha_inicio, fecha_fin in zip(fechas_inicio, fechas_fin))

#             if agendadas_correctamente:
#                 print(f"Las fechas en las columnas {columna_inicio} y {columna_fin} están agendadas correctamente.")
#                 mensajes+= f"Las fechas en las columnas {columna_inicio} y {columna_fin} están agendadas correctamente."
#             else:
#                 print(f"Las fechas en las columnas {columna_inicio} y {columna_fin} no están agendadas correctamente, revisar y corregir.")
#                 mensajes += f"Las fechas en las columnas {columna_inicio} y {columna_fin} no están agendadas correctamente, revisar y corregir."
                
                
#     return mensajes

   






    
            
                 

