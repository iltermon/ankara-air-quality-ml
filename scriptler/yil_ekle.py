#%%
from pathlib import Path
import os
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler
#%%
repo_path = os.getcwd()
repo_path = Path(repo_path).parent
csv=Path("veri_seti\\veri_seti.csv") 
df=pd.read_csv(str(repo_path)+"\\"+str(csv), sep=',', encoding = 'utf8')
df = StandardScaler().fit_transform(df)
# %%
for i in range(len(df["Tarih"])):
   df["Tarih"][i]=df["Tarih"][i][:4]
# %%
df.to_csv(str(repo_path)+"\\"+str(csv),sep=",",index=False)

# %%
df