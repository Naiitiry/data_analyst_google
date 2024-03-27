'''
En primera instancia, se analizará el archivo para verificar nulos/vacíos
incongruencias, columnas que no sean necesarias, verificaremos los tipos
de datos (si son los correctos, en caso contraria se modificará los mismos).
'''
# Busqueda, carga del archivo car_prices.csv e importaciones de librerías
import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/Tangalanga/Desktop/Analista de Datos de Google/ventas_de_autos/car_prices.csv',sep=',')
# print(df.head()) # visualizamos, precariamente, las primeras 5 filas

# print(df.info()) 
'''
Con df.info() esto averiguamos casi todo de la tabla, cantidad de columnas, así como los Dtypes,
valores no nulos.
'''

# print(df.isna().sum())
# Con df.isna().cum() vemos cuantos nulos tienen cada columna
# en este caso year, state y seller son 0, el resto poseen nulos

# print(df.nunique())
# Con df.nunique() vemos cuantosúnicos poseen cada columna,
# dependiendo que columna tendrá mas o menos únicos.

#print(df['vin'])
# la columna vin trata el número de identificación del vahículo,
# para el analisis que realizaremos no es importante, se eeliminará la columna
# del archivo copia, el original quedará sin tocar

df.drop(columns=["vin"],inplace=True)
# se elimina la columna 'vin'

'''
Ahora debemos sacar del analisis los nulos, se procede
a realizarlo con la siguiente línea
'''
df.dropna(inplace=True)
# se eliminan los NA y se especifíca que no queremos un df nuevo, 
# sino en el que estamos trabajando

# Eliminar las filas que contienen nulos en columnas específicas
# df.dropna(inplace=True, subset=['columna1', 'columna2'])

print(df.info())

'''
Para realizar un trabajo más limpio y menos engorroso,
procedemos a crear un archivo copia con la limpieza realizada
'''
df.to_csv('C:/Users/Tangalanga/Desktop/Analista de Datos de Google/ventas_de_autos/car_prices_new.csv',index=False)