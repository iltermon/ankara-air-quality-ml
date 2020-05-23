#%%
from pathlib import Path
import os
import pandas as pd
import numpy as np
#%%
repo_path = os.getcwd()
repo_path = Path(repo_path).parent
path=Path("veri_seti\\veri_seti.xlsx") 
csv=Path("veri_seti\\veri_seti.csv") 
df=pd.read_excel(str(repo_path)+"\\"+str(path))
#%%
for i in df.index:
    if df.loc[i]["Ay"]==12 or df.loc[i]["Ay"]==1 or df.loc[i]["Ay"]==2:
        df.at[i,"Mevsim"]="Kis"
    elif df.loc[i]["Ay"]==3 or df.loc[i]["Ay"]==4 or df.loc[i]["Ay"]==5:
        df.at[i,"Mevsim"]="Ilkbahar"
    elif df.loc[i]["Ay"]==6 or df.loc[i]["Ay"]==7 or df.loc[i]["Ay"]==8:
        df.at[i,"Mevsim"]="Yaz"
    elif df.loc[i]["Ay"]==9 or df.loc[i]["Ay"]==10 or df.loc[i]["Ay"]==11:
        df.at[i,"Mevsim"]="Sonbahar"

# %%
df.to_csv(str(repo_path)+"\\"+str(csv))


# %%
