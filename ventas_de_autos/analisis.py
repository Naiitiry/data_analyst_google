import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/Tangalanga/Desktop/Analista de Datos de Google/ventas_de_autos/car_prices_new.csv',sep=',')

#print(df.info())
#print(df.isna().sum())
# realizamos 2 prints para verificar estado de nulos 
# y las columnas eliminadas

df.columns.to_list()
# convertimos las columnas en listas