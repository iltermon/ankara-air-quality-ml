
#%%
from pathlib import Path
import os
import pandas as pd
import numpy as np
from sklearn.utils import shuffle
#%%
repo_path = os.getcwd()
repo_path = Path(repo_path).parent
path=Path("veri_seti\\veri_seti.csv") 
df=shuffle(pd.read_csv(str(repo_path)+"\\"+str(path), sep=',', encoding = 'utf8'))

#%%
df.to_csv(str(repo_path)+"\\"+str(path),sep=",",index=False)