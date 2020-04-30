
#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
## Kritik Seviyeler #
## PM10: 50 µg/m3 ##  
## PM25: 25 µg/m3 ##  
## SO2: 125 µg/m3 ##  
## CO: 10 mg/m3   ##  
## NO2: 200 µg/m3 ##  
## NOX: 30 µg/m3  ##  
####################
df=pd.read_csv("veri_seti/veri_seti(temizlenmis).csv", sep=';', encoding = 'utf8')

# %%
#kritik seviyenin üzerinde pm10 olan günler
pm10_gunduz_kentsel=df[(df['PM10']>50) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==0)]["PM10"].count()
pm10_gunduz_trafik=df[(df['PM10']>50) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==1)]["PM10"].count()
pm10_gunduz_sanayi=df[(df['PM10']>50) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==2)]["PM10"].count()
pm10_gece_kentsel=df[(df['PM10']>50) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==0)]["PM10"].count()
pm10_gece_trafik=df[(df['PM10']>50) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==1)]["PM10"].count()
pm10_gece_sanayi=df[(df['PM10']>50) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==2)]["PM10"].count()


# %%
pm25_gunduz_kentsel=df[(df['PM25']>25) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==0)]["PM25"].count()
pm25_gunduz_trafik=df[(df['PM25']>25) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==1)]["PM25"].count()
pm25_gunduz_sanayi=df[(df['PM25']>25) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==2)]["PM25"].count()
pm25_gece_kentsel=df[(df['PM25']>25) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==0)]["PM25"].count()
pm25_gece_trafik=df[(df['PM25']>25) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==1)]["PM25"].count()
pm25_gece_sanayi=df[(df['PM25']>25) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==2)]["PM25"].count()

# %%
so2_gunduz_kentsel=df[(df['SO2']>125) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==0)]["SO2"].count()
so2_gunduz_trafik=df[(df['SO2']>125) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==1)]["SO2"].count()
so2_gunduz_sanayi=df[(df['SO2']>125) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==2)]["SO2"].count()
so2_gece_kentsel=df[(df['SO2']>125) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==0)]["SO2"].count()
so2_gece_trafik=df[(df['SO2']>125) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==1)]["SO2"].count()
so2_gece_sanayi=df[(df['SO2']>125) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==2)]["SO2"].count()


# %%
co_gunduz_kentsel=df[(df['CO']>10) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==0)]["CO"].count()
co_gunduz_trafik=df[(df['CO']>10) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==1)]["CO"].count()
co_gunduz_sanayi=df[(df['CO']>10) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==2)]["CO"].count()
co_gece_kentsel=df[(df['CO']>10) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==0)]["CO"].count()
co_gece_trafik=df[(df['CO']>10) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==1)]["CO"].count()
co_gece_sanayi=df[(df['CO']>10) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==2)]["CO"].count()

# %%
no2_gunduz_kentsel=df[(df['NO2']>200) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==0)]["NO2"].count()
no2_gunduz_trafik=df[(df['NO2']>200) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==1)]["NO2"].count()
no2_gunduz_sanayi=df[(df['NO2']>200) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==2)]["NO2"].count()
no2_gece_kentsel=df[(df['NO2']>200) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==0)]["NO2"].count()
no2_gece_trafik=df[(df['NO2']>200) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==1)]["NO2"].count()
no2_gece_sanayi=df[(df['NO2']>200) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==2)]["NO2"].count()

# %%
nox_gunduz_kentsel=df[(df['NOX']>30) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==0)]["NOX"].count()
nox_gunduz_trafik=df[(df['NOX']>30) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==1)]["NOX"].count()
nox_gunduz_sanayi=df[(df['NOX']>30) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==2)]["NOX"].count()
nox_gece_kentsel=df[(df['NOX']>30) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==0)]["NOX"].count()
nox_gece_trafik=df[(df['NOX']>30) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==1)]["NOX"].count()
nox_gece_sanayi=df[(df['NOX']>30) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==2)]["NOX"].count()