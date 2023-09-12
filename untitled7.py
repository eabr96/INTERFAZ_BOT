# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 11:23:56 2023

@author: ebolanos
"""

import pandas as pd


# DataFrame con las correspondencias
dataBASE = {
    'PLAN_TRABAJO': ['DIAGNOSTICO', 'PQR_CONTRATISTA_CON_UCs', 'PQR_CONTRATISTA_SIN_UCs', 'ELECTRICA_CONTRATISTA_CON_UCs', 'ELECTRICA_CONTRATISTA_SIN_UCs', 'FORESTAL_CONTRATISTA', 'LV_ELECTRICA_CON_UCs', 'LV_ELECTRICA_SIN_UCs', 'LV_FORESTAL', 'SUBTERRANEO_CON_UCs', 'SUBTERRANEO_SIN_UCs'],
    'DEPENDENCIA_UC': [None, 1, 0, 1, 0, None, 1, 0, None, 1, 0],
    'DEPENDENCIA_PLAN': [None, 'PQR', 'ATTER', 'PROYE', 'MBC', 'MBC', 'PROYE', 'MBC', 'MBC', 'PROYE', 'MBC'],
    'TIPO_TRABAJO': ['', '', '', '', '', '', '', '', '', '', ''],
    'TIPO_PROYECTO': ['MBC', 'PROYE', 'ATTER', 'PROYE', 'MBC', 'MBC', 'PROYE', 'MBC', 'MBC', 'PROYE', 'MBC'],
    'FSE': ['', 'PODARED02PLANES', 'PODARED02PLANES', 'PODARED02PLANES', 'PODARED02PLANES', 'PODARED02PLANES', 'TRABAJOLINPRIMLV', 'TRABAJOLINPRIMLV', 'TRABAJOLINPRIMLV', 'TRBREDSUBT', 'TRBREDSUBT'],
    'TIPO_ACCION_FSE': ['3', 'MODIFICAR', 'MODIFICAR', '3', 'MODIFICAR', 'MODIFICAR', '3', 'MODIFICAR', 'MODIFICAR', '3', 'MODIFICAR'],
    'PRIORIDAD': ['DEE07', 'DEE14', 'DEE14', 'DEE27', 'DEE27', 'DEE27', 'DEE03', 'DEE03', 'DEE15', 'DEE09', 'DEE09'],
    'GROT': ['DEE07', 'DEE14', 'DEE14', 'DEE27', 'DEE27', 'DEE27', 'DEE03', 'DEE03', 'DEE15', 'DEE09', 'DEE09'],
    'RESIDUOS': ['3', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8'],
    'HEREDA': ['', '', '', '', '', '', '', '', '', '', ''],
    'DURACION': ['1087996698', '9862651', '9862651', '9862651', '9862651', '9862651', '4423598', '4423598', '4423598', '89002163', '89002163'],
    'INTERVENTOR': ['06337600', '1088257828', '1088257828', '1088257828', '1088257828', '1088257828', '1088257828', '1088257828', '1088257828', '1088257828', '1088257828'],
    'RESPONSABLE': ['742', '33REPOSIMTTO', '06337600', '33REPOSIMTTO', '06337600', '06337600', '33REPOSIMTTO', '06337600', '06337600', '33REPOSIMTTO', '06337600'],
    'UNIDAD_NEGOCIO': ['CW215795', 'CW215795', 'CW215795', 'CW215795', 'CW215795', 'CW215795', 'CW215795', 'CW215795', 'CW215795', 'CW215795', 'CW215795'],
    'ACTIVIDAD_COSTEO': ['', '742', '742', '742', '742', '742', '742', '742', '742', '742', '742'],
    'CONTRATO': ['', 'CW215795', 'CW215795', 'CW215795', 'CW215795', 'CW215795', 'CW215795', 'CW215795', 'CW215795', 'CW215795', 'CW215795'],
}






df_correspondencia = pd.DataFrame(dataBASE)

# # DataFrame de datos a validar
# data_validar = {
#     'ID': [1, 2, 3, 4, 5, 6],
#     'OT': [120166, 122394, 125470, 126374, 126395, 126417],
#     'PLAN_TRABAJO': ['PQR_CONTRATISTA_SIN_UCs', 'DIAGNOSTICO', 'DIAGNOSTICO', 'DIAGNOSTICO', 'DIAGNOSTICO', 'DIAGNOSTICO'],
#     'NOMBRE_PLANIFICADOR': ['JORGE HERNAN', 'JORGE HERNAN', 'JORGE HERNAN', 'JORGE HERNAN', 'JORGE HERNAN', 'JORGE HERNAN'],
#     'NOMBRE_INTERVENTOR': ['ALEJANDRO LOPEZ', 'ALEJANDRO LOPEZ', 'ALEJANDRO LOPEZ', 'ALEJANDRO LOPEZ', 'ALEJANDRO LOPEZ', 'ALEJANDRO LOPEZ'],
#     'DESCRIPCION': ['', '', '', '', '', ''],
#     'INICIO_PREVISTO': ['07/08/2023 17:00', '07/08/2023 17:01', '07/08/2023 17:02', '07/08/2023 17:03', '07/08/2023 17:04', '07/08/2023 17:05'],
#     'FIN_PREVISTO': ['', '11/08/2023 17:01', '11/08/2023 17:02', '11/08/2023 17:03', '11/08/2023 17:04', '11/08/2023 17:05'],
#     'INICIO_PROGRAMADO': ['07/08/2023 17:00', '07/08/2023 17:01', '07/08/2023 17:02', '07/08/2023 17:03', '07/08/2023 17:04', '07/08/2023 17:05'],
#     'FIN_PROGRAMADO': ['', '11/08/2023 17:01', '11/08/2023 17:02', '11/08/2023 17:03', '11/08/2023 17:04', '11/08/2023 17:05'],
#     'UBICACION': ['ARMONIA ELECTROVEGETAL', '', '', '', '', ''],
#     'NOMBRE_CLASIFICACION': ['ASIGNADA', 'ASIGNADA', 'ASIGNADA', 'ASIGNADA', 'ASIGNADA', 'ASIGNADA'],
#     'ESTADO_DESEADO': ['PODARED02PLANES', '', '', '', '', ''],
#     'FSE': ['MODIFICAR', 'MBC', 'MBC', 'MBC', 'MBC', 'MBC'],
#     'TIPO_ACCION_FSE': ['ATTER', '', '', '', '', ''],
#     'NO_ANTERIOR': ['3', '3', '3', '3', '3', '3'],
#     'MAS_TARDAR': ['0', '0', '0', '0', '0', '0'],
#     'CLASIFICACION': ['DEE14', 'DEE07', 'DEE07', 'DEE07', 'DEE07', 'DEE07'],
#     'GROT': [ 'DEE14', 'DEE07', 'DEE07', 'DEE07', 'DEE07', 'DEE07'],
#     'TIPO_TRABAJO': ['8', '3', '3', '3', '3', '3'],
#     'TIPO_PROYECTO': ['71311745', '71311745', '71311745', '71311745', '71311745', '71311745'],
#     'PRIORIDAD': ['1088345128', '1087996698', '1087996698', '1087996698', '1087996698', '1087996698'],
#     'RESIDUOS': ['1088257828', '06337600', '06337600', '06337600', '06337600', '06337600'],
#     'HEREDA': ['742', '742', '742', '742', '742', '742'],
#     'DURACION': ['PVMTTO \ AEV', 'MBC', 'MBC', 'MBC', 'MBC', 'MBC'],
#     'PLANIFICADOR': ['ATTER', 'DEE07', 'DEE07', 'DEE07', 'DEE07', 'DEE07'],
#     'INTERVENTOR': ['3', '3', '3', '3', '3', '3'],
#     'RESPONSABLE': ['71311745', '71311745', '71311745', '71311745', '71311745', '71311745'],
#     'UNIDAD_NEGOCIO': ['1088345128', '1087996698', '1087996698', '1087996698', '1087996698', '1087996698'],
#     'ACTIVIDAD_COSTEO': ['1088257828', '06337600', '06337600', '06337600', '06337600', '06337600'],
#     'CONTRATO': ['742', 'CW215795', 'CW215795', 'CW215795', 'CW215795', 'CW215795'],
# }


df_validar = pd.read_excel('Datos_entrada.xlsx')

 #Crear una función para validar una fila de df_validar
def validar_fila(row):
    plan_trabajo = row['PLAN_TRABAJO']
    fse = row['FSE']
    tipo_accion_fse = row['TIPO_ACCION_FSE']
 
    tipo_trabajo = row['TIPO_TRABAJO']
    tipo_proyecto = row['TIPO_PROYECTO']
    grot = row['GROT']
    unidad_negocio = row['UNIDAD_NEGOCIO']
    actividad_costeo = row['ACTIVIDAD_COSTEO']
    contrato = row['CONTRATO']

    # Validación de PLAN_TRABAJO
    if plan_trabajo not in df_correspondencia['PLAN_TRABAJO'].values:
        return 'INCORRECTO', f"PLAN_TRABAJO '{plan_trabajo}' no válido"

    # Validación de FSE
    if fse not in df_correspondencia['FSE'].values:
        return 'INCORRECTO', f"FSE '{fse}' no válido"

    # Validación de TIPO_ACCION_FSE
    if tipo_accion_fse not in df_correspondencia['TIPO_ACCION_FSE'].values:
        return 'INCORRECTO', f"TIPO_ACCION_FSE '{tipo_accion_fse}' no válido"

  
    # Validación de TIPO_TRABAJO
    if tipo_trabajo not in df_correspondencia['TIPO_TRABAJO'].values:
        return 'INCORRECTO', f"TIPO_TRABAJO '{tipo_trabajo}' no válido"

    # Validación de TIPO_PROYECTO
    if tipo_proyecto not in df_correspondencia['TIPO_PROYECTO'].values:
        return 'INCORRECTO', f"TIPO_PROYECTO '{tipo_proyecto}' no válido"

    # Validación de GROT
    if grot not in df_correspondencia['GROT'].values:
        return 'INCORRECTO', f"GROT '{grot}' no válido"

    # Validación de UNIDAD_NEGOCIO
    if unidad_negocio not in df_correspondencia['UNIDAD_NEGOCIO'].values:
        return 'INCORRECTO', f"UNIDAD_NEGOCIO '{unidad_negocio}' no válido"

    # Validación de ACTIVIDAD_COSTEO
    if actividad_costeo not in df_correspondencia['ACTIVIDAD_COSTEO'].values:
        return 'INCORRECTO', f"ACTIVIDAD_COSTEO '{actividad_costeo}' no válido"

    # Validación de CONTRATO
    if contrato not in df_correspondencia['CONTRATO'].values:
        return 'INCORRECTO', f"CONTRATO '{contrato}' no válido"

    return 'CORRECTO', ''

# Aplicar la función de validación a cada fila de df_validar
df_validar[['Validacion', 'Mensaje']] = df_validar.apply(validar_fila, axis=1, result_type='expand')

# Mostrar el resultado
print(df_validar[['ID', 'Validacion', 'Mensaje']])