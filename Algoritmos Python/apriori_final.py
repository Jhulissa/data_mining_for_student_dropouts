# -*- coding: utf-8 -*-
"""Apriori_Final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18rWros1E28JPow1sCpRoblrDnntQ6i20
"""

!pip install apyori

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

store_data = pd.read_csv('/content/compu_04.csv')

store_data.head()

#store_data = store_data.drop(columns=['Unnamed: 0'])

#store_data = store_data.drop(columns=['Unnamed: 0','genero','estado_civil', 'TEORIA DE LA PROGRAMACION', 'CONTABILIDAD GENERAL', 'ESTADISTICA INFERENCIAL', 'GESTION DE REDES', 'AUDITORIA INFORMATICA', 'ANALISIS NUMERICO',
       'ADMINISTRACION DE CENTROS DE COMPUTO', 'ESTRUCTURA DE DATOS II', 'PROGRAMACION II', 'BASE DE DATOS I','ADMINISTRACION DE CENTROS DE COMPUTO', 'INGENIERIA DE SOFTWARE II',
       'MODELAMIENTO MATEMATICO','INGENIERIA DEL SOFTWARE I', 'METODOLOGIA DE LA INVESTIGACION',
       'DISENO Y GESTION DE BASE DE DATOS', 'METODOLOGIA DE LA PROGRAMACION',
       'CONTABILIDAD GENERAL', 'ESTADISTICA INFERENCIAL','PROGRAMACION AVANZADA', 'DERECHO INFORMATICO', 'DISENO DE SISTEMAS'])

store_data.columns

store_data = store_data.drop(columns=['PROCESOS DE SOFTWARE'])

store_data.columns

store_data = store_data.replace({'genero':{1:'Femenino',0:'Masculino'}})

#store_data = store_data.replace({'genero':{1:'Femenino',0:'Masculino'},'ciclo':{1:'Primero',2:'Segundo',3:'Tercero',4:'Cuarto',5:'Quinto',6:'Sexto',7:'Septimo',8:'Octavo',9:'Noveno',10:'Decimo'}})

store_data = store_data.replace({'estado_civil':{1:'Soltero',0:'Casado'}})

store_data = store_data.replace({'sector_procedencia':{1:'Rural',0:'Urbano'}})

store_data = store_data.replace({'trabaja':{1:'Trabaja',0:'NTrabaja'}})

store_data = store_data.replace({'tipo_colegio':{1:'Público',2:'privado',3:'fisco'}})

store_data = store_data.replace({'numero_hijos':{1:'siH',0:'NoH'}})

store_data = store_data.replace({'ingreso_estudiante':{1:'siIngre',0:'NIngre'}})

store_data = store_data.replace({'INGENIERIA DE LA CONTAMINACION':{1:'IC_A',0:'IC_R'},'ECUACIONES DIFERENCIALES':{1:'ED_A',0:'ED_R'},'ESTRUCTURAS DE DATOS AVANZADAS':{1:'EDA_A',0:'EDA_R'},'PROCESAMIENTO DE TRANSACCIONES':{1:'PC_A',0:'PC_R'}})

#store_data = store_data.replace({'ARM':{1:'M=1',0:'M=0',2:'M=2',3:'M=3',4:'M=4',5:'M=5'}})

#store_data = store_data.replace({'ANRM':{1:'NM=1',0:'NM=0',2:'NM=2',3:'NM=3'}})

#store_data = store_data.replace({'ALGEBRA LINEAL':{1:'APRUEBA ALGEBRA',0:'REPRUEBA ALGEBRA',2:'NOCURSA ALGEBRA'},'CALCULO DIFERENCIAL':{1:'APRUEBA CALCULO',0:'REPRUEBA CALCULO',2:'NOCURSA CALCULO'}})

#store_data = store_data.replace({'TEORIA DE LA PROGRAMACION':{1:'APRUEBA TEORIA',0:'REPRUEBA TEORIA',2:'NOCURSA TEORIA'},'FUNDAMENTOS INFORMATICOS':{1:'APRUEBA FUNDAMENTOS',0:'REPRUEBA FUNDAMENTOS',2:'NOCURSA FUNDAMENTOS'}})

store_data = store_data.drop(columns=['ciclo','PERDIDAS','ingreso_estudiante','numero_hijos','etnia'])

print(store_data.columns)

rows, columns = store_data.shape

records = []
for i in range(0, rows):
    records.append([str(store_data.values[i,j]) for j in range(0, columns)])

print(records)

#store_data.to_csv('sistemas_pp.csv')

association_rules = apriori(records, min_support=0.7, min_confidence=0.7, min_lift=1.01, min_length=10)

association_results = list(association_rules)

print(association_results)

for item in association_results:
  print(item)
  print("=====================================")

