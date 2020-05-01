import pandas as pd
import numpy as np
df = pd.read_csv("veri_seti\\veri_seti(temizlenmis).csv",sep=";")
for i in df.index:
    if df.loc[i]["IstasyonTipi"]=="Kentsel":
        df.at[i,"IstasyonTipi"]=0
    elif df.loc[i]["IstasyonTipi"]=="Sanayi":
        df.at[i,"IstasyonTipi"]=1
    elif df.loc[i]["IstasyonTipi"]=="Trafik":
        df.at[i,"IstasyonTipi"]=2

    if df.loc[i]["GeceGunduz"]=="Gece":
        df.at[i,"GeceGunduz"]=0
    elif df.loc[i]["GeceGunduz"]=="Gunduz":
        df.at[i,"GeceGunduz"]=1

    if df.loc[i]["HaftasonuHaftaici"]=="Haftasonu":
        df.at[i,"HaftasonuHaftaici"]=0
    elif df.loc[i]["HaftasonuHaftaici"]=="Haftaici":
        df.at[i,"HaftasonuHaftaici"]=1

    if df.loc[i]["Mevsim"]=="Ilkbahar":
        df.at[i,"Mevsim"]=0
    elif df.loc[i]["Mevsim"]=="Kis":
        df.at[i,"Mevsim"]=1
    elif df.loc[i]["Mevsim"]=="Sonbahar":
        df.at[i,"Mevsim"]=2
    elif df.loc[i]["Mevsim"]=="Yaz":
        df.at[i,"Mevsim"]=3
    df.at[i,"Ay"]=df.at[i,"Ay"]-1
df.to_csv("veri_seti\\veri_seti(temizlenmis).csv",sep=";")