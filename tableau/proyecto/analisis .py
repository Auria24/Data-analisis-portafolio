import pandas as pd

datos= pd.read_csv('trending_by_time.csv')
print(datos)

datos_por_cateforia= datos['category_title'].value_counts()
print(datos_por_cateforia)
datos_cat=datos['category_title'].unique()
print(datos_cat)

