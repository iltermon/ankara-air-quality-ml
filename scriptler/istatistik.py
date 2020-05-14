
#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import os
import pandas as pd
## Kritik Seviyeler #
## PM10: 50 µg/m3 ##  
## PM25: 25 µg/m3 ##  
## SO2: 125 µg/m3 ##  
## CO: 10 mg/m3   ##  
## NO2: 200 µg/m3 ##  
## NOX: 30 µg/m3  ##  
####################
dirpath = os.getcwd()
repopath = Path(dirpath).parent
path=Path("veri_seti\\veri_seti(temizlenmis).csv") 
df=pd.read_csv(str(repopath)+"\\"+str(path), sep=';', encoding = 'utf8')

# %%
#kritik seviyenin üzerinde pm10 olan günler
pm10_gunduz_kentsel=df[(df['PM10']>50) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==0)]["PM10"].count()
pm10_gunduz_trafik=df[(df['PM10']>50) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==1)]["PM10"].count()
pm10_gunduz_sanayi=df[(df['PM10']>50) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==2)]["PM10"].count()

pm10_gece_kentsel=df[(df['PM10']>50) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==0)]["PM10"].count()
pm10_gece_trafik=df[(df['PM10']>50) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==1)]["PM10"].count()
pm10_gece_sanayi=df[(df['PM10']>50) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==2)]["PM10"].count()

pm10_bahar_kentsel=df[(df['PM10']>50) & (df["Mevsim"]==0)&(df["IstasyonTipi"]==0)]["PM10"].count()
pm10_bahar_trafik=df[(df['PM10']>50) & (df["Mevsim"]==0)&(df["IstasyonTipi"]==1)]["PM10"].count()
pm10_bahar_sanayi=df[(df['PM10']>50) & (df["Mevsim"]==0)&(df["IstasyonTipi"]==2)]["PM10"].count()

pm10_kis_kentsel=df[(df['PM10']>50) & (df["Mevsim"]==1)&(df["IstasyonTipi"]==0)]["PM10"].count()
pm10_kis_trafik=df[(df['PM10']>50) & (df["Mevsim"]==1)&(df["IstasyonTipi"]==1)]["PM10"].count()
pm10_kis_sanayi=df[(df['PM10']>50) & (df["Mevsim"]==1)&(df["IstasyonTipi"]==2)]["PM10"].count()

pm10_sonbahar_kentsel=df[(df['PM10']>50) & (df["Mevsim"]==2)&(df["IstasyonTipi"]==0)]["PM10"].count()
pm10_sonbahar_trafik=df[(df['PM10']>50) & (df["Mevsim"]==2)&(df["IstasyonTipi"]==1)]["PM10"].count()
pm10_sonbahar_sanayi=df[(df['PM10']>50) & (df["Mevsim"]==2)&(df["IstasyonTipi"]==2)]["PM10"].count()

pm10_yaz_kentsel=df[(df['PM10']>50) & (df["Mevsim"]==3)&(df["IstasyonTipi"]==0)]["PM10"].count()
pm10_yaz_trafik=df[(df['PM10']>50) & (df["Mevsim"]==3)&(df["IstasyonTipi"]==1)]["PM10"].count()
pm10_yaz_sanayi=df[(df['PM10']>50) & (df["Mevsim"]==3)&(df["IstasyonTipi"]==2)]["PM10"].count()
# %%
pm25_gunduz_kentsel=df[(df['PM25']>25) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==0)]["PM25"].count()
pm25_gunduz_trafik=df[(df['PM25']>25) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==1)]["PM25"].count()
pm25_gunduz_sanayi=df[(df['PM25']>25) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==2)]["PM25"].count()
pm25_gece_kentsel=df[(df['PM25']>25) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==0)]["PM25"].count()
pm25_gece_trafik=df[(df['PM25']>25) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==1)]["PM25"].count()
pm25_gece_sanayi=df[(df['PM25']>25) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==2)]["PM25"].count()

pm25_bahar_kentsel=df[(df['PM25']>25) & (df["Mevsim"]==0)&(df["IstasyonTipi"]==0)]["PM25"].count()
pm25_bahar_trafik=df[(df['PM25']>25) & (df["Mevsim"]==0)&(df["IstasyonTipi"]==1)]["PM25"].count()
pm25_bahar_sanayi=df[(df['PM25']>25) & (df["Mevsim"]==0)&(df["IstasyonTipi"]==2)]["PM25"].count()

pm25_kis_kentsel=df[(df['PM25']>25) & (df["Mevsim"]==1)&(df["IstasyonTipi"]==0)]["PM25"].count()
pm25_kis_trafik=df[(df['PM25']>25) & (df["Mevsim"]==1)&(df["IstasyonTipi"]==1)]["PM25"].count()
pm25_kis_sanayi=df[(df['PM10']>25) & (df["Mevsim"]==1)&(df["IstasyonTipi"]==2)]["PM25"].count()

pm25_sonbahar_kentsel=df[(df['PM25']>25) & (df["Mevsim"]==2)&(df["IstasyonTipi"]==0)]["PM25"].count()
pm25_sonbahar_trafik=df[(df['PM25']>25) & (df["Mevsim"]==2)&(df["IstasyonTipi"]==1)]["PM25"].count()
pm25_sonbahar_sanayi=df[(df['PM25']>25) & (df["Mevsim"]==2)&(df["IstasyonTipi"]==2)]["PM25"].count()

pm25_yaz_kentsel=df[(df['PM25']>25) & (df["Mevsim"]==3)&(df["IstasyonTipi"]==0)]["PM25"].count()
pm25_yaz_trafik=df[(df['PM25']>25) & (df["Mevsim"]==3)&(df["IstasyonTipi"]==1)]["PM25"].count()
pm25_yaz_sanayi=df[(df['PM25']>25) & (df["Mevsim"]==3)&(df["IstasyonTipi"]==2)]["PM25"].count()
# %%
so2_gunduz_kentsel=df[(df['SO2']>125) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==0)]["SO2"].count()
so2_gunduz_trafik=df[(df['SO2']>125) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==1)]["SO2"].count()
so2_gunduz_sanayi=df[(df['SO2']>125) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==2)]["SO2"].count()
so2_gece_kentsel=df[(df['SO2']>125) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==0)]["SO2"].count()
so2_gece_trafik=df[(df['SO2']>125) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==1)]["SO2"].count()
so2_gece_sanayi=df[(df['SO2']>125) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==2)]["SO2"].count()

so2_bahar_kentsel=df[(df['SO2']>125) & (df["Mevsim"]==0)&(df["IstasyonTipi"]==0)]["SO2"].count()
so2_bahar_trafik=df[(df['SO2']>125) & (df["Mevsim"]==0)&(df["IstasyonTipi"]==1)]["SO2"].count()
so2_bahar_sanayi=df[(df['SO2']>125) & (df["Mevsim"]==0)&(df["IstasyonTipi"]==2)]["SO2"].count()

so2_kis_kentsel=df[(df['SO2']>125) & (df["Mevsim"]==1)&(df["IstasyonTipi"]==0)]["SO2"].count()
so2_kis_trafik=df[(df['SO2']>125) & (df["Mevsim"]==1)&(df["IstasyonTipi"]==1)]["SO2"].count()
so2_kis_sanayi=df[(df['SO2']>125) & (df["Mevsim"]==1)&(df["IstasyonTipi"]==2)]["SO2"].count()

so2_sonbahar_kentsel=df[(df['SO2']>125) & (df["Mevsim"]==2)&(df["IstasyonTipi"]==0)]["SO2"].count()
so2_sonbahar_trafik=df[(df['SO2']>125) & (df["Mevsim"]==2)&(df["IstasyonTipi"]==1)]["SO2"].count()
so2_sonbahar_sanayi=df[(df['SO2']>125) & (df["Mevsim"]==2)&(df["IstasyonTipi"]==2)]["SO2"].count()

so2_yaz_kentsel=df[(df['SO2']>125) & (df["Mevsim"]==3)&(df["IstasyonTipi"]==0)]["SO2"].count()
so2_yaz_trafik=df[(df['SO2']>125) & (df["Mevsim"]==3)&(df["IstasyonTipi"]==1)]["SO2"].count()
so2_yaz_sanayi=df[(df['SO2']>125) & (df["Mevsim"]==3)&(df["IstasyonTipi"]==2)]["SO2"].count()

# %%
co_gunduz_kentsel=df[(df['CO']>10) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==0)]["CO"].count()
co_gunduz_trafik=df[(df['CO']>10) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==1)]["CO"].count()
co_gunduz_sanayi=df[(df['CO']>10) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==2)]["CO"].count()
co_gece_kentsel=df[(df['CO']>10) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==0)]["CO"].count()
co_gece_trafik=df[(df['CO']>10) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==1)]["CO"].count()
co_gece_sanayi=df[(df['CO']>10) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==2)]["CO"].count()

co_bahar_kentsel=df[(df['CO']>10) & (df["Mevsim"]==0)&(df["IstasyonTipi"]==0)]["CO"].count()
co_bahar_trafik=df[(df['CO']>10) & (df["Mevsim"]==0)&(df["IstasyonTipi"]==1)]["CO"].count()
co_bahar_sanayi=df[(df['CO']>10) & (df["Mevsim"]==0)&(df["IstasyonTipi"]==2)]["CO"].count()

co_kis_kentsel=df[(df['CO']>10) & (df["Mevsim"]==1)&(df["IstasyonTipi"]==0)]["CO"].count()
co_kis_trafik=df[(df['CO']>10) & (df["Mevsim"]==1)&(df["IstasyonTipi"]==1)]["CO"].count()
co_kis_sanayi=df[(df['CO']>10) & (df["Mevsim"]==1)&(df["IstasyonTipi"]==2)]["CO"].count()

co_sonbahar_kentsel=df[(df['CO']>10) & (df["Mevsim"]==2)&(df["IstasyonTipi"]==0)]["CO"].count()
co_sonbahar_trafik=df[(df['CO']>10) & (df["Mevsim"]==2)&(df["IstasyonTipi"]==1)]["CO"].count()
co_sonbahar_sanayi=df[(df['CO']>10) & (df["Mevsim"]==2)&(df["IstasyonTipi"]==2)]["CO"].count()

co_yaz_kentsel=df[(df['CO']>10) & (df["Mevsim"]==3)&(df["IstasyonTipi"]==0)]["CO"].count()
co_yaz_trafik=df[(df['CO']>10) & (df["Mevsim"]==3)&(df["IstasyonTipi"]==1)]["CO"].count()
co_yaz_sanayi=df[(df['CO']>10) & (df["Mevsim"]==3)&(df["IstasyonTipi"]==2)]["CO"].count()
# %%
no2_gunduz_kentsel=df[(df['NO2']>200) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==0)]["NO2"].count()
no2_gunduz_trafik=df[(df['NO2']>200) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==1)]["NO2"].count()
no2_gunduz_sanayi=df[(df['NO2']>200) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==2)]["NO2"].count()
no2_gece_kentsel=df[(df['NO2']>200) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==0)]["NO2"].count()
no2_gece_trafik=df[(df['NO2']>200) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==1)]["NO2"].count()
no2_gece_sanayi=df[(df['NO2']>200) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==2)]["NO2"].count()

no2_bahar_kentsel=df[(df['NO2']>200) & (df["Mevsim"]==0)&(df["IstasyonTipi"]==0)]["NO2"].count()
no2_bahar_trafik=df[(df['NO2']>200) & (df["Mevsim"]==0)&(df["IstasyonTipi"]==1)]["NO2"].count()
no2_bahar_sanayi=df[(df['NO2']>200) & (df["Mevsim"]==0)&(df["IstasyonTipi"]==2)]["NO2"].count()

no2_kis_kentsel=df[(df['NO2']>200) & (df["Mevsim"]==1)&(df["IstasyonTipi"]==0)]["NO2"].count()
no2_kis_trafik=df[(df['NO2']>200) & (df["Mevsim"]==1)&(df["IstasyonTipi"]==1)]["NO2"].count()
no2_kis_sanayi=df[(df['NO2']>200) & (df["Mevsim"]==1)&(df["IstasyonTipi"]==2)]["NO2"].count()

no2_sonbahar_kentsel=df[(df['NO2']>200) & (df["Mevsim"]==2)&(df["IstasyonTipi"]==0)]["NO2"].count()
no2_sonbahar_trafik=df[(df['NO2']>200) & (df["Mevsim"]==2)&(df["IstasyonTipi"]==1)]["NO2"].count()
no2_sonbahar_sanayi=df[(df['NO2']>200) & (df["Mevsim"]==2)&(df["IstasyonTipi"]==2)]["NO2"].count()

no2_yaz_kentsel=df[(df['NO2']>200) & (df["Mevsim"]==3)&(df["IstasyonTipi"]==0)]["NO2"].count()
no2_yaz_trafik=df[(df['NO2']>200) & (df["Mevsim"]==3)&(df["IstasyonTipi"]==1)]["NO2"].count()
no2_yaz_sanayi=df[(df['NO2']>200) & (df["Mevsim"]==3)&(df["IstasyonTipi"]==2)]["NO2"].count()
# %%
nox_gunduz_kentsel=df[(df['NOX']>30) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==0)]["NOX"].count()
nox_gunduz_trafik=df[(df['NOX']>30) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==1)]["NOX"].count()
nox_gunduz_sanayi=df[(df['NOX']>30) & (df["GeceGunduz"]==1)&(df["IstasyonTipi"]==2)]["NOX"].count()
nox_gece_kentsel=df[(df['NOX']>30) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==0)]["NOX"].count()
nox_gece_trafik=df[(df['NOX']>30) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==1)]["NOX"].count()
nox_gece_sanayi=df[(df['NOX']>30) & (df["GeceGunduz"]==0)&(df["IstasyonTipi"]==2)]["NOX"].count()

nox_bahar_kentsel=df[(df['NOX']>30) & (df["Mevsim"]==0)&(df["IstasyonTipi"]==0)]["NOX"].count()
nox_bahar_trafik=df[(df['NOX']>30) & (df["Mevsim"]==0)&(df["IstasyonTipi"]==1)]["NOX"].count()
nox_bahar_sanayi=df[(df['NOX']>30) & (df["Mevsim"]==0)&(df["IstasyonTipi"]==2)]["NOX"].count()

nox_kis_kentsel=df[(df['NOX']>30) & (df["Mevsim"]==1)&(df["IstasyonTipi"]==0)]["NOX"].count()
nox_kis_trafik=df[(df['NOX']>30) & (df["Mevsim"]==1)&(df["IstasyonTipi"]==1)]["NOX"].count()
nox_kis_sanayi=df[(df['NOX']>30) & (df["Mevsim"]==1)&(df["IstasyonTipi"]==2)]["NOX"].count()

nox_sonbahar_kentsel=df[(df['NOX']>30) & (df["Mevsim"]==2)&(df["IstasyonTipi"]==0)]["NOX"].count()
nox_sonbahar_trafik=df[(df['NOX']>30) & (df["Mevsim"]==2)&(df["IstasyonTipi"]==1)]["NOX"].count()
nox_sonbahar_sanayi=df[(df['NOX']>30) & (df["Mevsim"]==2)&(df["IstasyonTipi"]==2)]["NOX"].count()

nox_yaz_kentsel=df[(df['NOX']>30) & (df["Mevsim"]==3)&(df["IstasyonTipi"]==0)]["NOX"].count()
nox_yaz_trafik=df[(df['NOX']>30) & (df["Mevsim"]==3)&(df["IstasyonTipi"]==1)]["NOX"].count()
nox_yaz_sanayi=df[(df['NOX']>30) & (df["Mevsim"]==3)&(df["IstasyonTipi"]==2)]["NOX"].count()
# %%
saatler = ['Gece', 'Gunduz']
degerler1 = [pm10_gece_kentsel, pm10_gunduz_kentsel]
degerler2 = [pm10_gece_trafik, pm10_gunduz_trafik]
degerler3 = [pm10_gece_sanayi, pm10_gunduz_sanayi]
f=plt.figure(figsize=(12,6))

plt.subplot(131)
plt.bar(saatler, degerler1)
plt.subplot(132)
plt.bar(saatler, degerler2)
plt.subplot(133)
plt.bar(saatler, degerler3)
plt.suptitle('PM10 ( µg/m³ )')
plt.savefig("pm10_gun.png")
plt.show()

# %%
saatler = ['Gece', 'Gunduz']
degerler1 = [pm25_gece_kentsel, pm25_gunduz_kentsel]
degerler2 = [pm25_gece_trafik, pm25_gunduz_trafik]
degerler3 = [pm25_gece_sanayi, pm25_gunduz_sanayi]
f=plt.figure(figsize=(12,6))

plt.subplot(131)
plt.bar(saatler, degerler1)
plt.subplot(132)
plt.bar(saatler, degerler2)
plt.subplot(133)
plt.bar(saatler, degerler3)
plt.suptitle('PM25 ( µg/m³ )')
plt.savefig("pm25_gun.png")
plt.show()
# %% 
saatler = ['Gece', 'Gunduz']
degerler1 = [so2_gece_kentsel, so2_gunduz_kentsel]
degerler2 = [so2_gece_trafik, so2_gunduz_trafik]
degerler3 = [so2_gece_sanayi, so2_gunduz_sanayi]
f=plt.figure(figsize=(12,6))

plt.subplot(131)
plt.bar(saatler, degerler1)
plt.subplot(132)
plt.bar(saatler, degerler2)
plt.subplot(133)
plt.bar(saatler, degerler3)
plt.suptitle('SO2 ( µg/m³ )')
plt.savefig("so2_gun.png")
plt.show()
# %% 
saatler = ['Gece', 'Gunduz']
degerler1 = [co_gece_kentsel, co_gunduz_kentsel]
degerler2 = [co_gece_trafik, co_gunduz_trafik]
degerler3 = [co_gece_sanayi, co_gunduz_sanayi]
f=plt.figure(figsize=(12,6))

plt.subplot(131)
plt.bar(saatler, degerler1)
plt.subplot(132)
plt.bar(saatler, degerler2)
plt.subplot(133)
plt.bar(saatler, degerler3)
plt.suptitle('CO ( mg/m³ )')
plt.savefig("co_gun.png")
plt.show()
# %% 
saatler = ['Gece', 'Gunduz']
degerler1 = [no2_gece_kentsel, no2_gunduz_kentsel]
degerler2 = [no2_gece_trafik, no2_gunduz_trafik]
degerler3 = [no2_gece_sanayi, no2_gunduz_sanayi]
f=plt.figure(figsize=(12,6))

plt.subplot(131)
plt.bar(saatler, degerler1)
plt.subplot(132)
plt.bar(saatler, degerler2)
plt.subplot(133)
plt.bar(saatler, degerler3)
plt.suptitle('NO2 ( µg/m³ )')
plt.savefig("no2_gun.png")
plt.show()
# %% 
saatler = ['Gece', 'Gunduz']
degerler1 = [nox_gece_kentsel, nox_gunduz_kentsel]
degerler2 = [nox_gece_trafik, nox_gunduz_trafik]
degerler3 = [nox_gece_sanayi, nox_gunduz_sanayi]
f=plt.figure(figsize=(12,6))

plt.subplot(131)
plt.bar(saatler, degerler1)
plt.subplot(132)
plt.bar(saatler, degerler2)
plt.subplot(133)
plt.bar(saatler, degerler3)
plt.suptitle('NOX ( µg/m³ )')
plt.savefig("nox_gun.png")
plt.show()

# %%
mevsim = ['İlkbahar', 'Yaz','Sonbahar', 'Kış']
degerler1 = [pm10_bahar_kentsel, pm10_yaz_kentsel, pm10_sonbahar_kentsel, pm10_kis_kentsel]
degerler2 = [pm10_bahar_trafik , pm10_yaz_trafik , pm10_sonbahar_trafik , pm10_kis_trafik]
degerler3 = [pm10_bahar_sanayi , pm10_yaz_sanayi , pm10_sonbahar_sanayi , pm10_kis_sanayi]
f=plt.figure(figsize=(12,6))

plt.subplot(131)
plt.bar(mevsim, degerler1)
plt.subplot(132)
plt.bar(mevsim, degerler2)
plt.subplot(133)
plt.bar(mevsim, degerler3)
plt.suptitle('PM10 ( µg/m³ )')
plt.savefig("pm10_mev.png")
plt.show()
# %%
mevsim = ['İlkbahar', 'Yaz','Sonbahar', 'Kış']
degerler1 = [pm25_bahar_kentsel, pm25_yaz_kentsel, pm25_sonbahar_kentsel, pm25_kis_kentsel]
degerler2 = [pm25_bahar_trafik , pm25_yaz_trafik , pm25_sonbahar_trafik , pm25_kis_trafik]
degerler3 = [pm25_bahar_sanayi , pm25_yaz_sanayi , pm25_sonbahar_sanayi , pm25_kis_sanayi]
f=plt.figure(figsize=(12,6))

plt.subplot(131)
plt.bar(mevsim, degerler1)
plt.subplot(132)
plt.bar(mevsim, degerler2)
plt.subplot(133)
plt.bar(mevsim, degerler3)
plt.suptitle('PM25 ( µg/m³ )')
plt.savefig("pm25_mev.png")
plt.show()
# %%
mevsim = ['İlkbahar', 'Yaz','Sonbahar', 'Kış']
degerler1 = [so2_bahar_kentsel, pm10_yaz_kentsel, so2_sonbahar_kentsel, so2_kis_kentsel]
degerler2 = [so2_bahar_trafik , so2_yaz_trafik , so2_sonbahar_trafik , so2_kis_trafik]
degerler3 = [so2_bahar_sanayi , so2_yaz_sanayi , so2_sonbahar_sanayi , so2_kis_sanayi]
f=plt.figure(figsize=(12,6))

plt.subplot(131)
plt.bar(mevsim, degerler1)
plt.subplot(132)
plt.bar(mevsim, degerler2)
plt.subplot(133)
plt.bar(mevsim, degerler3)
plt.suptitle('SO2 ( µg/m³ )')
plt.savefig("so2_mev.png")
plt.show()
# %%
mevsim = ['İlkbahar', 'Yaz','Sonbahar', 'Kış']
degerler1 = [co_bahar_kentsel, co_yaz_kentsel, co_sonbahar_kentsel, co_kis_kentsel]
degerler2 = [co_bahar_trafik , co_yaz_trafik , co_sonbahar_trafik , co_kis_trafik]
degerler3 = [co_bahar_sanayi , co_yaz_sanayi , co_sonbahar_sanayi , co_kis_sanayi]
f=plt.figure(figsize=(12,6))

plt.subplot(131)
plt.bar(mevsim, degerler1)
plt.subplot(132)
plt.bar(mevsim, degerler2)
plt.subplot(133)
plt.bar(mevsim, degerler3)
plt.suptitle('CO ( mg/m³ )')
plt.savefig("co_mev.png")
plt.show()
# %%
mevsim = ['İlkbahar', 'Yaz','Sonbahar', 'Kış']
degerler1 =  [no2_bahar_kentsel, no2_yaz_kentsel, no2_sonbahar_kentsel, no2_kis_kentsel]
degerler2 =  [no2_bahar_trafik , no2_yaz_trafik , no2_sonbahar_trafik , no2_kis_trafik]
degerler3 =  [no2_bahar_sanayi , no2_yaz_sanayi , no2_sonbahar_sanayi , no2_kis_sanayi]
f=plt.figure(figsize=(12,6))

plt.subplot(131)
plt.bar(mevsim, degerler1)
plt.subplot(132)
plt.bar(mevsim, degerler2)
plt.subplot(133)
plt.bar(mevsim, degerler3)
plt.suptitle('NOX ( µg/m³ )')
plt.savefig("nox_mev.png")
plt.show()
# %%
mevsim = ['İlkbahar', 'Yaz','Sonbahar', 'Kış']
degerler1 =  [nox_bahar_kentsel, nox_yaz_kentsel, nox_sonbahar_kentsel, nox_kis_kentsel]
degerler2 =  [nox_bahar_trafik , nox_yaz_trafik , nox_sonbahar_trafik , nox_kis_trafik]
degerler3 =  [nox_bahar_sanayi , nox_yaz_sanayi , nox_sonbahar_sanayi , nox_kis_sanayi]
f=plt.figure(figsize=(12,6))

plt.subplot(131)
plt.bar(mevsim, degerler1)
plt.subplot(132)
plt.bar(mevsim, degerler2)
plt.subplot(133)
plt.bar(mevsim, degerler3)
plt.suptitle('NO2 ( µg/m³ )')
plt.savefig("no2_mev.png")
plt.show()
