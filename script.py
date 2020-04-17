import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("veri_seti/ay_ortalama.csv", sep=';', encoding = 'utf8')
plt.bar(df["Tarih"],df["PM10"])
plt.show()


