
#%%
from pathlib import Path
import os
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
#%%
repo_path = os.getcwd()
repo_path = Path(repo_path).parent
path=Path("veri_seti\\veri_seti.csv") 
df=pd.read_csv(str(repo_path)+"\\"+str(path), sep=',', encoding = 'utf8')
#%%
imputer = KNNImputer(n_neighbors=1)
df.iloc[:, 1:12]=imputer.fit_transform(df.iloc[:, 1:12])

#%%
df.to_csv(str(repo_path)+"\\"+str(path),sep=",",index=False)

# %%
