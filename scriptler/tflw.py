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
# %%
repo_path = os.getcwd()
repo_path = Path(repo_path).parent
path=Path("veri_seti\\veri_seti(temizlenmis).csv") 
df=pd.read_csv(str(repo_path)+"\\"+str(path), sep=';', encoding = 'utf8')
label_encoder=LabelEncoder().fit(df["IstasyonTipi"])
labels=LabelEncoder().fit_transform(df["IstasyonTipi"])
x = df.drop(["Tarih","IstasyonTipi"], axis=1)
y = labels
# %%
x = StandardScaler().fit_transform(x)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# %%
model = Sequential()
model.add(Dense(16,input_dim=14,activation="relu"))
model.add(Dense(32, activation="relu"))
model.add(Dense(64,activation="relu"))
model.add(Dense(128,activation="relu"))
model.add(Dense(256,activation="relu"))
model.add(Dense(512,activation="softmax"))
model.add(Dense(3))
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(x_train,y_train, validation_data=(x_test,y_test), epochs=100)
# %%
plt.plot(model.history.history["accuracy"])
plt.plot(model.history.history["val_accuracy"])
plt.title("Model Başarımları")
plt.ylabel("Başarım")
plt.xlabel("Epok Sayısı")
plt.legend(["Eğitim","Test"], loc="upper left")
plt.show()


# %%
plt.plot(model.history.history["loss"])
plt.plot(model.history.history["val_loss"])
plt.title("Model Kayıpları")
plt.ylabel("Kayıp")
plt.xlabel("Epok Sayısı")
plt.legend(["Eğitim","Test"], loc="upper left")
plt.show()

# %%
plt.plot(model.history.history["accuracy"])
plt.plot(model.history.history["val_accuracy"])
plt.title("Model Başarımları")
plt.ylabel("Başarım")
plt.xlabel("Epok Sayısı")
plt.legend(["Eğitim","Test"], loc="upper left")
plt.show()


# %%
