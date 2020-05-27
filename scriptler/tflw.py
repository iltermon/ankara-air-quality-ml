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
le = LabelEncoder()
# %%
repo_path = os.getcwd()
repo_path = Path(repo_path).parent
path=Path("veri_seti\\veri_seti.csv") 
df=pd.read_csv(str(repo_path)+"\\"+str(path), encoding = 'utf8')

#%%


df["Gece/Gunduz"]=le.fit_transform(df["Gece/Gunduz"])
df["Haftasonu/Haftaici"]=le.fit_transform(df["Haftasonu/Haftaici"])
df["Mevsim"]=le.fit_transform(df["Mevsim"])
labels=LabelEncoder().fit_transform(df["IstasyonTipi"])
y = labels
x = df.drop(["IstasyonTipi"], axis=1)
classes=list(le.fit(df["IstasyonTipi"]).classes_)
nb_classes= len(classes)
nb_features = x.shape[1]
# %%
x = StandardScaler().fit_transform(x)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# %%
model = Sequential()
model.add(Dense(512,input_dim=nb_features,activation="relu"))
model.add(Dense(1024, activation="relu"))
model.add(Dense(2048,activation="relu"))
model.add(Dense(512,activation="relu"))
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
#%%