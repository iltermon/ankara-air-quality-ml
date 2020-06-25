#veri setiyle ilgili bazı grafikler oluşturan script
#%%
from pathlib import Path
import os
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.preprocessing  import LabelEncoder
from sklearn.preprocessing  import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import plot_model
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.metrics import roc_curve
from matplotlib import pyplot as plt
#%%
repo_path = os.getcwd()
repo_path = Path(repo_path).parent
path=Path("veri_seti\\veri_seti.csv") 
path_1=Path("veri_seti\\veri_seti(temizlenmis).csv")
df=pd.read_csv(str(repo_path)+"\\"+str(path), encoding = 'utf8')
df_1=pd.read_csv(str(repo_path)+"\\"+str(path_1), sep=";", encoding = 'utf8')

df_kentsel=df.loc[df['IstasyonTipi'] == "Kentsel"]
#%%
#Kentsel İstasyonlardan Gelen değerlerin Grafikleştirilmesi
plt.bar(df_kentsel['Yil'], df_kentsel['PM10'])
plt.title("Kentsel PM10")
plt.show()
plt.bar(df_kentsel['Yil'], df_kentsel['SO2'])
plt.title("Kentsel SO2")
plt.show()
plt.bar(df_kentsel['Yil'], df_kentsel['CO'])
plt.title("Kentsel CO")
plt.show()
plt.bar(df_kentsel['Yil'], df_kentsel['NO2'])
plt.title("Kentsel NO2")
plt.show()
plt.bar(df_kentsel['Yil'], df_kentsel['NOX'])
plt.title("Kentsel NOX")
plt.show()
plt.bar(df_kentsel['Yil'], df_kentsel['NO'])
plt.title("Kentsel NO")
plt.show()
plt.bar(df_kentsel['Yil'], df_kentsel['PM25'])
plt.title("Kentsel PM25")
plt.show()
#%%
kentsel=df[(df["IstasyonTipi"]=="Kentsel")]["PM10"].count()
trafik=df[(df["IstasyonTipi"]=="Trafik")]["PM10"].count()
sanayi=df[(df["IstasyonTipi"]=="Sanayi")]["PM10"].count()
kentsel_1=df_1[(df_1["IstasyonTipi"]==0)]["PM10"].count()
trafik_1=df_1[(df_1["IstasyonTipi"]==1)]["PM10"].count()
sanayi_1=df_1[(df_1["IstasyonTipi"]==2)]["PM10"].count()

# %%
istasyonlar = ['Kentsel', 'Trafik','Sanayi']
degerler1 =  [kentsel, trafik, sanayi]
degerler2 =  [kentsel_1 , trafik_1 , sanayi_1]
f=plt.figure(figsize=(12,6))
plt.subplot(121)
plt.bar(istasyonlar, degerler1)
plt.subplot(122)
plt.bar(istasyonlar, degerler2)
plt.suptitle('Temizlenmiş ve K-NN ile Tamamlanmış Verilerin Sayısal Karşılaştırması')
plt.savefig("karsilastirma.png")
plt.show()



# %%
