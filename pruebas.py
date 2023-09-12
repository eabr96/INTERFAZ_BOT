# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 14:06:37 2023

@author: ebolanos
"""

import pandas as pd

# DataFrame base (DataFrame 1)
dataBASE = {
    'PLAN_TRABAJO': ['DIAGNOSTICO', 'PQR_CONTRATISTA_CON_UCs', 'PQR_CONTRATISTA_SIN_UCs', 'ELECTRICA_CONTRATISTA_CON_UCs', 'ELECTRICA_CONTRATISTA_SIN_UCs', 'FORESTAL_CONTRATISTA', 'LV_ELECTRICA_CON_UCs', 'LV_ELECTRICA_SIN_UCs', 'LV_FORESTAL', 'SUBTERRANEO_CON_UCs', 'SUBTERRANEO_SIN_UCs'],
    # Otras columnas del DataFrame 1
}

df_correspondencia = pd.DataFrame(dataBASE)

# DataFrame de validación (DataFrame 2)
data_validar = {
    'ID': [1, 2, 3, 4, 5, 6],
    'PLAN_TRABAJO': ['PQR_CONTRATISTA_SIN_UCs', 'DIAGNOSTICO', 'DIAGNOSTICO', 'DIAGNOSTICO', 'DIAGNOSTICO', 'DIAGNOSTICO'],
    # Otras columnas del DataFrame 2
}

df_validar = pd.DataFrame(data_validar)

# Lista para almacenar los resultados
resultados = []

# Iterar a través del DataFrame de validación
for index, row in df_validar.iterrows():
    plan_trabajo = row['PLAN_TRABAJO']
    
    # Comprobar si el valor de 'PLAN_TRABAJO' está presente en el DataFrame base
    if plan_trabajo in df_correspondencia['PLAN_TRABAJO'].values:
        resultados.append(f'Cumple: ID {row["ID"]} - {plan_trabajo}')
        
        
        
        
        
    else:
        resultados.append(f'No Cumple: ID {row["ID"]} - {plan_trabajo}')

# Imprimir los resultados
#for resultado in resultados:
   # print(resultado)


#%% 2

import pandas as pd

# DataFrame base (DataFrame 1)
dataBASE = {
    'PLAN_TRABAJO': ['DIAGNOSTICO', 'PQR_CONTRATISTA_CON_UCs', 'PQR_CONTRATISTA_SIN_UCs', 'ELECTRICA_CONTRATISTA_CON_UCs', 'ELECTRICA_CONTRATISTA_SIN_UCs', 'FORESTAL_CONTRATISTA', 'LV_ELECTRICA_CON_UCs', 'LV_ELECTRICA_SIN_UCs', 'LV_FORESTAL', 'SUBTERRANEO_CON_UCs', 'SUBTERRANEO_SIN_UCs'],
    'DEPENDENCIA1': [None, True, False, True, False, None, True, False, None, True, False],
    # Otras columnas del DataFrame 1
}

df_correspondencia = pd.DataFrame(dataBASE)

# DataFrame de validación (DataFrame 2)
data_validar = {
    'ID': [1, 2, 3, 4, 5, 6],
    'PLAN_TRABAJO': ['PQR_CONTRATISTA_SIN_UCs', 'PQR_CONTRATISTA_CON_UCs', 'DIAGNOSTICO', 'DIAGNOSTICO', 'ELECTRICA_CONTRATISTA_CON_UCs', 'LV_ELECTRICA_CON_UCs'],
    # Otras columnas del DataFrame 2
}

df_validar = pd.DataFrame(data_validar)

# Lista para almacenar los resultados
resultados = []

# Iterar a través del DataFrame de validación
for index, row in df_validar.iterrows():
    plan_trabajo = row['PLAN_TRABAJO']
    
    # Comprobar si el valor de 'PLAN_TRABAJO' está presente en el DataFrame base
    if plan_trabajo in df_correspondencia['PLAN_TRABAJO'].values:
        # Obtener el valor de 'DEPENDENCIA1' correspondiente al 'PLAN_TRABAJO' en el DataFrame base
        dependencia1 = df_correspondencia.loc[df_correspondencia['PLAN_TRABAJO'] == plan_trabajo, 'DEPENDENCIA1'].values[0]

        if dependencia1 is None:
            resultados.append(f'Cumple: ID {row["ID"]} - {plan_trabajo} (Dependencia1: None)')
            
            
        elif dependencia1:
            resultados.append(f'Cumple: ID {row["ID"]} - {plan_trabajo} (Dependencia1: True)')
            
        else:
            resultados.append(f'Cumple: ID {row["ID"]} - {plan_trabajo} (Dependencia1: False)')
            
            
    else:
        resultados.append(f'No Cumple: ID {row["ID"]} - {plan_trabajo}')

# Imprimir los resultados
#for resultado in resultados:
#    print(resultado)

#%% 3 no

import pandas as pd

# DataFrame base (DataFrame 1)
dataBASE = {
    'PLAN_TRABAJO': ['DIAGNOSTICO', 'PQR_CONTRATISTA_CON_UCs', 'PQR_CONTRATISTA_SIN_UCs', 'ELECTRICA_CONTRATISTA_CON_UCs', 'ELECTRICA_CONTRATISTA_SIN_UCs', 'FORESTAL_CONTRATISTA', 'LV_ELECTRICA_CON_UCs', 'LV_ELECTRICA_SIN_UCs', 'LV_FORESTAL', 'SUBTERRANEO_CON_UCs', 'SUBTERRANEO_SIN_UCs'],
    'DEPENDENCIA1': [None, True, False, True, False, None, True, False, None, True, False],
    # Otras columnas del DataFrame 1
}

df_correspondencia = pd.DataFrame(dataBASE)

# DataFrame de validación (DataFrame 2)
data_validar = {
    'ID': [1, 2, 3, 4, 5, 6],
    'PLAN_TRABAJO': ['PQR_CONTRATISTA_SIN_UCs', 'PQR_CONTRATISTA_CON_UCs', 'DIAGNOSTICO', 'DIAGNOSTICO', 'ELECTRICA_CONTRATISTA_CON_UCs', 'LV_ELECTRICA_CON_UCs'],
    'DEPENDENCIA1': [True, False, None, True, False, None],  # Simula los valores de DEPENDENCIA1 en el DataFrame 2
    'TIPO_TRABAJO': ['PROY', '', '', '', '', ''],
    'UNIDAD_NEGOCIO': ['33REPOSIMTTO', '', '', '', '', ''],
    # Otras columnas del DataFrame 2
}

df_validar = pd.DataFrame(data_validar)

# Lista para almacenar los resultados
resultados = []

# Iterar a través del DataFrame de validación
for index, row in df_validar.iterrows():
    plan_trabajo = row['PLAN_TRABAJO']
    dependencia1 = row['DEPENDENCIA1']

    # Comprobar si el valor de 'PLAN_TRABAJO' está presente en el DataFrame base
    if plan_trabajo in df_correspondencia['PLAN_TRABAJO'].values:
        # Obtener el valor de 'DEPENDENCIA1' correspondiente al 'PLAN_TRABAJO' en el DataFrame 2
        # y verificar las condiciones adicionales
        correspondencia_dependencia1 = df_correspondencia.loc[df_correspondencia['PLAN_TRABAJO'] == plan_trabajo, 'DEPENDENCIA1'].values[0]
        tipo_trabajo = row['TIPO_TRABAJO']
        unidad_negocio = row['UNIDAD_NEGOCIO']

        if dependencia1 is None:
            resultados.append(f'Aquí pertenece: ID {row["ID"]} - {plan_trabajo} (Dependencia1: None)')
        elif correspondencia_dependencia1 is None:
            resultados.append(f'Cumple con informacion: ID {row["ID"]} - {plan_trabajo} (Dependencia1: None)')
        elif dependencia1 and tipo_trabajo == 'PROY' and unidad_negocio == '33REPOSIMTTO':
            resultados.append(f'Cumple: ID {row["ID"]} - {plan_trabajo} (Dependencia1: True, Tipo Trabajo: PROY, Unidad Negocio: 33REPOSIMTTO)')
        elif not dependencia1 and (tipo_trabajo == 'ATER' or tipo_trabajo == 'MBC') and unidad_negocio == '06337600':
            resultados.append(f'Cumple: ID {row["ID"]} - {plan_trabajo} (Dependencia1: False, Tipo Trabajo: {tipo_trabajo}, Unidad Negocio: {unidad_negocio})')
        else:
            resultados.append(f'No Cumple: ID {row["ID"]} - {plan_trabajo}')
    else:
        resultados.append(f'No Cumple: ID {row["ID"]} - {plan_trabajo}')

# # Imprimir los resultados
# for resultado in resultados:
#     print(resultado)
    
#%% 4 

import pandas as pd

# DataFrame base (DataFrame 1)
dataBASE = {
    'PLAN_TRABAJO': ['DIAGNOSTICO', 'PQR_CONTRATISTA_CON_UCs', 'PQR_CONTRATISTA_SIN_UCs', 'ELECTRICA_CONTRATISTA_CON_UCs', 'ELECTRICA_CONTRATISTA_SIN_UCs', 'FORESTAL_CONTRATISTA', 'LV_ELECTRICA_CON_UCs', 'LV_ELECTRICA_SIN_UCs', 'LV_FORESTAL', 'SUBTERRANEO_CON_UCs', 'SUBTERRANEO_SIN_UCs'],
    'DEPENDENCIA1': [None, True, False, True, False, None, True, False, None, True, False],
    'DEPENDENCIA2': [None, 'PQR', 'PQR', 'ELECTRICA', 'ELECTRICA', 'FORESTAL', None, 'LV', 'LV', 'SUBTERRANEO', 'SUBTERRANEO'],
    'FSE': ['', 'SEARCH', '', 'SEARCH', '', '', '', 'TRABAJOLINPRIMLV', '', 'SEARCH', ''],
    'TIPO_ACCION_FSE': [ 'MBC', 'PODARED02PLANES', 'PODARED02PLANES', 'PODARED02PLANES', 'PODARED02PLANES', 'PODARED02PLANES','TRABAJOLINPRIMLV', 'TRABAJOLINPRIMLV', 'TRABAJOLINPRIMLV', 'TRBREDSUBT', 'TRBREDSUBT'],
    'PRIORIDAD': ['DEE07', 'DEE14', 'DEE14', 'DEE27', 'DEE27', 'DEE27', 'DEE03', 'DEE03', 'DEE15', 'DEE09', 'DEE09' ],
    'GROT': ['DEE07', 'DEE14', 'DEE14', 'DEE27', 'DEE27', 'DEE27', 'DEE03', 'DEE03', 'DEE15', 'DEE09', 'DEE09' ],
    'RESIDUOS': ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0' ],
    'HEREDA': ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0' ],
    'DURACION': ['3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3' ],
    'UNIDAD_NEGOCIO':[ '33REPOSIMTTO', '06337600', '33REPOSIMTTO', '06337600', '06337600', '33REPOSIMTTO', '06337600', '06337600', '33REPOSIMTTO', '06337600'],
    'CONTRATO': ['CW215795', 'CW215795', 'CW215795', 'CW215795', 'CW215795', 'CW215795', 'CW215795', 'CW215795', 'CW215795', 'CW215795', 'CW215795'],

}
    
    # Otras columnas del DataFrame 1


df_base = pd.read_excel('Validacion_plan_trabajo.xlsx')

# DataFrame de validación (DataFrame 2)
data_validar = {
    'ID': [1, 2, 3, 4, 5, 6],
    'PLAN_TRABAJO': ['PQR_CONTRATISTA_SIN_UCs', 'PQR_CONTRATISTA_CON_UCs', 'DIAGNOSTICO', 'DIAGNOSTICO', 'ELECTRICA_CONTRATISTA_CON_UCs', 'LV_ELECTRICA_CON_UCs'],
    'TIPO_TRABAJO': ['PROY', 'ATER', '', '', 'MBC', 'PROY'],
    'UNIDAD_NEGOCIO': ['33REPOSIMTTO', '06337600', '', '', '06337600', ''],
    
    # Otras columnas del DataFrame 2
}

df_bot = pd.read_excel('Datos_entrada.xlsx')

# Lista para almacenar los resultados
resultados = []
resultados1 =[]
SIN_UC=False
CON_UC=True
NADA=None

# Iterar a través del DataFrame de validación
for index, row in df_bot.iterrows():
    plan_trabajo = row['PLAN_TRABAJO']
    
    
    # Comprobar si el valor de 'PLAN_TRABAJO' está presente en el DataFrame base
    if plan_trabajo in df_base['PLAN_TRABAJO'].values:
        
        # Obtener el valor de 'DEPENDENCIA1' correspondiente al 'PLAN_TRABAJO' en el DataFrame base
        dependencia0 = df_base.loc[df_base['PLAN_TRABAJO'] == plan_trabajo, 'DEPENDENCIA_PLAN'].values[0]



        if dependencia0 is True:
            resultados.append(f'OT: ID {row["ID"]} - {plan_trabajo} (Dependencia1: True)')
            dependencia0 = df_base.loc[df_base['PLAN_TRABAJO'] == plan_trabajo, 'DEPENDENCIA_UC'].values[0]
            
        
            
        elif dependencia0 is False:
            resultados.append(f'OT: ID {row["ID"]} - {plan_trabajo} (Dependencia1: False)')
            

            
        elif dependencia0 is None:
            resultados.append(f'OT: ID {row["ID"]} - {plan_trabajo} (Dependencia1: None)')
            
            
            
            
        else:
            resultados.append(f'OT: ID {row["ID"]} - {plan_trabajo} (Dependencia1: desconocida)')
    
            
    
            
    else:
        resultados.append(f'No Cumple: ID {row["ID"]} - {plan_trabajo}')

# Imprimir los resultados
for resultado in resultados:
    print(resultado)




