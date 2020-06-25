#veri seti özelliklerini çıkaran script
import pandas as pd
import numpy as np
df = pd.read_csv("veri_seti\\veri_seti(temizlenmis).csv",sep=";")
print("max")
print(df.max(axis=0))
print("min")
print(df.min(axis=0))
print("ort")
print(df.mean(axis=0))
print("std")
print(df.std(axis=0))