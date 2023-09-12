# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:09:57 2023

@author: ebolanos
"""
#prueba 2, aun no funcina comparacion y se debe eliminar algunas funciones

import tkinter as tk
from tkinter import filedialog, messagebox
import openpyxl
import pandas as pd
from tkinter import Frame 
from tkinter import ttk
from validacion_ import ProcesadorDatos
from datetime import datetime 
import json
import tkinter as tk

from tkinter import ttk
from tkinter import messagebox
import subprocess
import sys
import os #reset
import pandas as pd
import numpy as np






class BotApp:
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.data = {}
        self.boton_crear_ot = None
        self.etiqueta_verificacion = None
        #self.mensaje_fecha = None  # Etiqueta para mostrar el mensaje de validación de fechas
        
        # Crear una instancia de ProcesadorDatos
        self.procesador = ProcesadorDatos()
        self.df_excel = None
        self.archivo_seleccionado = None
        
        
#%% interfaz
        ventana.title("Ingreso de credenciales")
        ventana.geometry("1200x1000")
        ventana.pack_propagate(False)  # Desactiva el ajuste automático
            
        etiqueta_entrada = tk.Label(ventana, text="BOT PARA CREACION DE ORDENES DE TRABAJO EN MX", font=(16), fg="black")
        etiqueta_entrada.pack(pady=5)
        
        # Crear un Frame
        frame1 = tk.Frame(ventana, bg="#84d5db")
        frame1.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Crear otro Frame
        self.frame2 = tk.Frame(ventana, bg="#68aeb3")
        self.frame2.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        
        #Cuadro de información para Resumen
        columna_mensajes_generales = tk.LabelFrame(self.frame2, text="Resumen información", fg="black", bg="#68aeb3", font=(12))
        columna_mensajes_generales.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
 
        # Cuadro de información para Validación
        columna_mensajes_validacion = tk.LabelFrame(self.frame2, text="Validación datos", fg="black", bg="#68aeb3", font=(12))
        columna_mensajes_validacion.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")
        
        
        # Crear otro Frame
        frame3 = tk.Frame(ventana, bg="#729195")
        frame3.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Crear un segundo marco (frame) dentro de frame3 para contener los botones en una fila horizontal
        frame_botones = tk.Frame(frame3, bg="#729195")
        frame_botones.pack()
        
        
        # Agregar widgets al segundo Frame
        etiqueta3 = tk.Label(frame3, text="Opciones", fg="black", bg="#729195")
        etiqueta3.pack(padx=10, pady=10)
        
        boton_entrada = tk.Button(frame1, text="Clic aqui para subir archivo",  fg="black",  bg="#eeae56" , command=self.elegir_resumir)
        boton_entrada.pack(pady= 5)
        
       
        # Etiqueta para mostrar el mensaje de selección de archiv
        self.texto_resumen = tk.Text(frame1, height=5, width=100)
        self.texto_resumen.pack(pady=5)
        
    
        # Mensajes informacion
        self.mensaje_resultado_ots = tk.Label(columna_mensajes_generales, text="", fg="white", bg="#68aeb3", font=(10))
        self.mensaje_resultado_ots.pack(padx=10, pady=5)
        
        self.mensaje_resumen = tk.Label(columna_mensajes_generales, text="", fg="white", bg="#68aeb3", font=(10))
        self.mensaje_resumen.pack(padx=10, pady=5)
        
        self.mensaje_validacion_ubicacion = tk.Label(columna_mensajes_generales, text="", fg="white" , bg="#68aeb3",  font=(10))
        self.mensaje_validacion_ubicacion.pack( padx=10, pady=5)
        
        self.mensaje_validacion_plan_trabajo = tk.Label(columna_mensajes_generales, text="", fg="white" , bg="#68aeb3",  font=(10))
        self.mensaje_validacion_plan_trabajo.pack( padx=10, pady=5)
                 
        
        # Mensajes de validación
        self.mensaje_validacionJSON = tk.Label(columna_mensajes_validacion, text="", fg="white", bg="#68aeb3", font=(10))
        self.mensaje_validacionJSON.pack(padx=10, pady=5)
        
        self.mensaje_validacion_hojas = tk.Label(columna_mensajes_validacion, text="", fg="white", bg="#68aeb3", font=(10))
        self.mensaje_validacion_hojas.pack(padx=10, pady=5)
        
        self.mensaje_verificacion_numeros = tk.Label(columna_mensajes_validacion, text="", fg="white", bg="#68aeb3", font=(10))
        self.mensaje_verificacion_numeros.pack(padx=10, pady=5)
        
        
        self.mensaje_campos_obligatorios = tk.Label(columna_mensajes_validacion, text="", fg="white", bg="#68aeb3", font=(10))
        self.mensaje_campos_obligatorios.pack(padx=10, pady=5)
        
        
        self.mensaje_validar_correspondencia = tk.Label(columna_mensajes_validacion, text="", fg="white", bg="#68aeb3", font=(10))
        self.mensaje_validar_correspondencia.pack(padx=10, pady=5)
        
        #FALTA FECHA VALIADA, FECHA CORRECTA Y COMPARACION
        self.mensaje_validacion_formato_fecha = tk.Label(columna_mensajes_validacion, text="", fg="white" , bg="#68aeb3",  font=(10))
        self.mensaje_validacion_formato_fecha.pack( padx=10, pady=5)
        
        
        
        
        
        

        #FRAME 3
        # Crear botón "RESET"
        
        # boton_validacion_datos = tk.Button(frame3, text="Validar Datos", fg="black", bg="#eeae56", command=self.validacion_de_datos)
        # boton_validacion_datos.pack(side=tk.RIGHT, padx=5)  # Ubica el botón a la derecha
        
        # self.boton_ejecutar_main = tk.Button(frame3, text="Ejecutar Main", fg="black", bg="#eeae56", command=self.ejecutar_main)
        # self.boton_ejecutar_main.pack(side=tk.RIGHT, padx=5)  # Ubica el botón a la derecha
        
        
        # boton_resetear = tk.Button(frame3, text="Eliminar archivo seleccionado", fg="black", bg="#eeae56", command=self.resetear)
        # boton_resetear.pack(side=tk.RIGHT, padx=5)  # Ubica el botón a la derecha
        
        # self.boton_detener = tk.Button(frame3, text="Detener", fg="black", bg="#eeae56", command=self.detener)
        # self.boton_detener.pack(side=tk.RIGHT, padx=5)  # Ubica el botón a la 
        


     #Cuadro de opciones desplegable
        # Cuadro de opciones desplegable
        opciones_combo = ttk.Combobox(frame3, values=["RESET", "Validar Datos", "" ])
        opciones_combo.pack(padx=10, pady=10)
        opciones_combo.set("")  # Texto inicial en el cuadro de opciones

        # Botón Aceptar
        boton_aceptar = tk.Button(frame3, text="Aceptar", command=self.ejecutar_opcion_seleccionada, state=tk.DISABLED)
        boton_aceptar.pack(padx=10, pady=10)

        # Variable para almacenar la opción seleccionada
        self.opcion_seleccionada = tk.StringVar()
        self.opcion_seleccionada.set("")  # Inicialmente, no se ha seleccionado ninguna opción

        # Asociar comandos a las opciones
        opciones_combo.bind("<<ComboboxSelected>>", self.actualizar_opcion_seleccionada)
        self.boton_aceptar = boton_aceptar

    def actualizar_opcion_seleccionada(self, event):
        self.opcion_seleccionada.set(event.widget.get())
        if self.opcion_seleccionada.get():
            self.boton_aceptar.config(state=tk.NORMAL)
        else:
            self.boton_aceptar.config(state=tk.DISABLED)

    def ejecutar_opcion_seleccionada(self):
        opcion = self.opcion_seleccionada.get()
        if opcion == "RESET":
            self.resetear()
        elif opcion == "Validar Datos":
            self.validacion_de_datos()
        elif opcion == "Detener":
            self.detener()

        
    def detener(self):
        sys.exit()  # Detiene el programa completamente



    def ajustar_ancho_columnas(self, contenido_tabla):
        ancho_maximo = [max(len(str(cell)) for cell in column) for column in zip(*contenido_tabla)]
        contenido_formateado = ""
        
        for row in contenido_tabla:
            fila_formateada = "\t".join(f"{cell:{ancho}}" for cell, ancho in zip(row, ancho_maximo))
            contenido_formateado += f"{fila_formateada}\n"
        
        return contenido_formateado
        
    
    
    def elegir_resumir(self):
        try:
            self.archivo_seleccionado = self.procesador.seleccionar_archivo()
            #seleccion_resultado= self.archivo_seleccionado = self.procesador.seleccionar_archivo()
    
            # Actualizar la etiqueta con el resultado de la selección
            #self.mensaje_seleccion.config(text=seleccion_resultado)
    
            # # Generar el resumen y mostrarlo en el widget de texto
            # resumen_resultado, _ = self.procesador.resumen()
            # self.texto_resumen.delete("1.0", tk.END)
            # self.texto_resumen.insert(tk.END, resumen_resultado)
    
            if self.procesador.df_excel is not None:
                # Obtener las primeras 5 filas y 5 columnas
                primeras_filas_columnas = self.procesador.df_excel.iloc[:5, :5]
    
                # Convertir las primeras filas y columnas en una lista de listas para formatear
                contenido_formateado = [primeras_filas_columnas.columns.tolist()]  # Agregar nombres de columnas como primera fila
                for _, row in primeras_filas_columnas.iterrows():
                    contenido_formateado.append([str(cell) for cell in row])
    
                # Ajustar el ancho de las columnas y unir en un solo string
                contenido_formateado = self.ajustar_ancho_columnas(contenido_formateado)
    
                # Mostrar la información en el cuadro de texto
                self.texto_resumen.delete("1.0", tk.END)
                self.texto_resumen.insert(tk.END, contenido_formateado)
                
      
    
        except Exception as e:
            messagebox.showerror("Error", f"Error al procesar los datos: {str(e)}")
     
            
            
    def resetear(self):# Reiniciar la interfaz eliminando las etiquetas, widgets y botones adicionales
        
        self.procesador.eliminar_archivo()
        # Restablece los atributos o datos que necesitas
        self.data.clear()
        # Restablece los mensajes a cadena vacía
        self.mensaje_resultado_ots.config(text="")
        self.mensaje_resumen.config(text="")
        self.mensaje_validacionJSON.config(text="")
        self.mensaje_verificacion_ID.config(text="")
        self.mensaje_verificacion_TAREAS.config(text="")
        self.mensaje_campos_obligatorios.config(text="")
        
        self.mensaje_validar_correspondencia.config(text="")
        self.mensaje_validacion_ubicacion.config(text="")
        self.mensaje_validacion_hojas.config(text="")
        
        self.texto_resumen.delete("1.0", tk.END)  # Limpia el contenido del Text widget
       
        self.mensaje_validacion_formato_fecha.config(text="")

        
    
    def ejecutar_main(self):
        try:
            # Ejecutar el archivo main.py utilizando subprocess.run()
            subprocess.run(["python", "Main_Cargar_Servicios.py"], check=True)  # Agrega "python" antes del nombre del archivo
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Error al ejecutar Main_Cargar_Servicios.py: {str(e)}")



#%%validacion de archivo

    def validacion_de_datos(self):
        
       
        if self.procesador.excel_file is None:
            messagebox.showinfo("Información", "Selecciona un archivo Excel primero.")
            return

    
        else:
            try:
                columna_a_contar = 'ID'  # Intenta contar una columna diferente a 'ID'
        
                resultado_ots = self.procesador.cantidad_elementos_OTs(columna_a_contar)
                self.mensaje_resultado_ots.config(text=resultado_ots)
                print("Resultado contar OTs:", resultado_ots)
                        
            except Exception as e:
                self.mensaje_resultado_ots.config(text=f"Error contar órdenes de trabajo en el programa o archivo seleccionado: {str(e)}.\n Contacta a .")
                print(f"Error en validación para contar ordenes de trabajo: {str(e)}")

            
            # try:
            #     # Validacion de datos con JSON
            #     validacion_datos = self.procesador.validacion_datos()
            #     self.mensaje_validacionJSON.config(text=validacion_datos)
            #     print("Resultado de validación:", validacion_datos)
             
            # except Exception as e:
            #     self.mensaje_validacionJSON.config(text=f"Error en validación de información: {str(e)}")
    
    
            try:
                # Información resumen del documento seleccionado
                informacion_archivo = self.procesador.informacion_archivo()
                self.mensaje_resumen.config(text=informacion_archivo)
                print("Resultado de resumen:", informacion_archivo)
             
            except Exception as e:
                self.mensaje_resumen.config(text=f"Error en información resumen: {str(e)}")
    

            try:
                verificacion_ID = self.procesador.validacion_NUMEROS("OTs", "ID", ["MO", "SERVICIOS", "MATERIALES"], ["Planes_Trabajo", "Tablas_Apoyo"])
                verificacion_TAREAS = self.procesador.validacion_NUMEROS("TAREAS", "TAREA", ["MO", "SERVICIOS", "MATERIALES"], ["Planes_Trabajo", "Tablas_Apoyo"])
                self.mensaje_verificacion_numeros.config(text=(verificacion_ID + verificacion_TAREAS))
                print("Resultado de validación para números:", verificacion_ID + verificacion_TAREAS)
                       
            except Exception as e:
                self.mensaje_verificacion_ID.config(text=f"Error en validación de IDs: {str(e)}")
                print(f"Se produjo un error al validar numero IDs: {str(e)}")
    
            
                
            
            try:
                columnas_requeridas = ['DESCRIPCION', 'CLASIFICACION', 'UBICACION', 'TIPO_TRABAJO', 'PRIORIDAD', 'GROT', 'DURACION']
                columna_ot = 'OT'
            
                resultado_campos_obligatorios = self.procesador.campos_obligatorios(columnas_requeridas, columna_ot)
                self.mensaje_campos_obligatorios.config(text=resultado_campos_obligatorios)
                print("Campos obligatorios:", resultado_campos_obligatorios)
    
            except Exception as e:
                self.mensaje_validacion_formato_fecha.config(text=f"Error en validación de información: {str(e)}")
                print(f"Se produjo un error en campos obligaorios: {str(e)}")
                
            
            try:
                fechas1 = self.procesador.validar_formato_fechas("INICIO_PREVISTO", "FIN_PREVISTO", "ID")
                fechas2 = self.procesador.validar_formato_fechas("INICIO_PROGRAMADO", "FIN_PROGRAMADO", "ID")
            
                self.mensaje_validacion_formato_fecha.config(text=(fechas1 + fechas2 ))

                                                                 
            except Exception as e:
                self.mensaje_validacion_formato_fecha.config(text=f"Error en validación de información: {str(e)} al llamar la funcion validar formato fecha")
                print(f"Error en validación de formato fecha: {str(e)}")
              
            
            
            try:
                correspondencia1 = self.procesador.validar_correspondencia("NOMBRE_CLASIFICACION", "CLASIFICACION", 'datos_clasificaciones', "ID")
                correspondencia2 = self.procesador.validar_correspondencia("NOMBRE_PLANIFICADOR", "PLANIFICADOR", 'datos_planificadores', "ID")
                
                self.mensaje_validar_correspondencia.config(text=(correspondencia1 + correspondencia2))
                
            except Exception as e:
                self.mensaje_validar_correspondencia.config(text=f"Error en validación de corre: {str(e)}")
                print(f"Error en validación acorr: {str(e)}")


            try:
                hojas_correctas = ["OTs", "TAREAS", "MO", "SERVICIOS", "MATERIALES", "Planes_Trabajo", "Tablas_Apoyo"]
                numero_hojas = 7
                validacion_hojas = self.procesador.validar_archivo_excel(hojas_correctas, numero_hojas)
                self.mensaje_validacion_hojas.config(text=(validacion_hojas))
                
            except Exception as e:
                self.mensaje_validacion_hojas.config(text=f"Error en validación de corre: {str(e)}")
                print(f"Error en validación acorr: {str(e)}")
                
                
            try:
                validacion_ubicacion = self.procesador.ubicacion()
                self.mensaje_validacion_ubicacion.config(text=(validacion_ubicacion ))
                
            except Exception as e:
                self.mensaje_validacion_ubicacion.config(text=f"Error en validación de corre: {str(e)}")
                print(f"Error en validación acorr: {str(e)}")
                
            # try:
            #     validacion_plan_trabajo = self.procesador.validacion_plan_trabajo()
            #     self.mensaje_validacion_plan_trabajo.config(text=(validacion_plan_trabajo))
                
            # except Exception as e:
            #     self.mensaje_validacion_plan_trabajo.config(text=f"Error en validación de plaannn: {str(e)}")
            #     print(f"Error en validación plannn: {str(e)}")


                

ventana = tk.Tk()
bot_app = BotApp(ventana)
ventana.mainloop()
