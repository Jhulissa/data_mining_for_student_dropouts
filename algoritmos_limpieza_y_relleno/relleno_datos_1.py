# -*- coding: utf-8 -*-
"""Relleno_datos_1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18E4A9C5i16C-JcsYa6Nsm-t7lnUQMgeg
"""

import pandas
import math
from scipy.spatial import distance
import random
from numpy.random import permutation
import numpy as np
from sklearn.neighbors import KNeighborsRegressor

with open("dataset_origen.csv", 'r') as csvfile:
    ciclo = pandas.read_csv(csvfile)

distance_columns = ciclo.columns

def euclidean_distance(row):
    """
    A simple euclidean distance function
    """
    inner_value = 0
    for k in distance_columns:
        inner_value += (row[k] - selected_player[k]) ** 2
    return math.sqrt(inner_value)

ciclo_numeric = ciclo[distance_columns]

ciclo_normalized = (ciclo_numeric - ciclo_numeric.mean()) / ciclo_numeric.std()

ciclo = ciclo.drop(columns=['periodo_lectivo'])

count_tipo_colegio = len(ciclo.loc[ciclo['tipo_colegio'].isnull()])
print(count_tipo_colegio)

ciclo_predecir = ciclo.drop(ciclo.index[ciclo['tipo_colegio'].isnull()])

print(ciclo_predecir)

random_indices = permutation(ciclo_predecir.index)

test_cutoff = math.floor(count_tipo_colegio+1)

test = ciclo_predecir.loc[random_indices[1:test_cutoff]]

train = ciclo_predecir.loc[random_indices[test_cutoff:]]

#ciclo_predecir = ciclo_predecir.replace(['col_fiscal'],'PUBLICO')

#ciclo_predecir = ciclo_predecir.replace(['col_particular'],'PRIVADO')

#ciclo_predecir = ciclo_predecir.replace(['particular'],'PRIVADO')

#ciclo_predecir = ciclo_predecir.replace(['Medio'],'FISCOMISIONAL')

#ciclo_predecir = ciclo_predecir.replace(['medio'],'FISCOMISIONAL')

#ciclo_predecir = ciclo_predecir.replace(['Med'],'FISCOMISIONAL')

#ciclo_predecir = ciclo_predecir.replace(['Medio \n'],'FISCOMISIONAL')

#ciclo_predecir.loc[ciclo_predecir.tipo_colegio.str.upper() == 'FISCAL','tipo_colegio'] = 1

#ciclo_predecir.loc[ciclo_predecir.tipo_colegio.str.upper() == 'PARTICULAR','tipo_colegio'] = 2

#ciclo_predecir.loc[ciclo_predecir.tipo_colegio.str.upper() == 'FISCOMISIONAL','tipo_colegio'] = 3

for numero in ciclo_predecir.tipo_colegio:
  if type(numero) == object:
    print(type(numero))
    print(numero)

print(ciclo_predecir.tipo_colegio)

x_columns = ['provincia_nacimiento']

y_column = ['provincia_nacimiento','tipo_colegio']


knn = KNeighborsRegressor(n_neighbors=5)

knn.fit(train[x_columns], train[y_column])

predictions = np.round(knn.predict(test[x_columns]),0)

print(len(predictions))

for prediction in predictions:
  ciclo.loc[ciclo['tipo_colegio'].isnull() & ciclo['provincia_nacimiento']==prediction[0],'tipo_colegio']=prediction[1]

for prediction in predictions:
  ciclo.loc[ciclo['tipo_colegio'].isnull(),'tipo_colegio']=prediction[1]

print(len(ciclo.loc[ciclo['tipo_colegio'].isnull()].values))

#ciclo_aux = pandas.DataFrame(new_data, columns = ciclo.columns)

#ciclo_final = ciclo.append(ciclo_aux, ignore_index=True)



ciclo.to_csv('data_inicial_completa.csv')