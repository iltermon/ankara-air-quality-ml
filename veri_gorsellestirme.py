import pandas as pd
import matplotlib as mat

dataframe=pd.read_csv("veri_seti/veri_seti.csv", sep=';', encoding = 'utf8')
print(dataframe.columns)