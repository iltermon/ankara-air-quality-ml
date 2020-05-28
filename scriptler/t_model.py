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
from tensorflow.keras.layers import Dense,LSTM,Activation,BatchNormalization,Dropout,Flatten
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.metrics import roc_curve
from matplotlib import pyplot as plt
import tensorflow

# %%
le = LabelEncoder()
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
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
x_train, x_valid, y_train, y_valid = train_test_split(x_train, y_train, test_size=0.25, random_state=1) # 0.25 x 0.8 = 0.2
y_train = to_categorical(y_train)
y_valid = to_categorical(y_valid)
y_test = to_categorical(y_test)
x_train  = np.array(x_train).reshape(x_train.shape[0], x_train.shape[1],1)
x_valid  = np.array(x_valid).reshape(x_valid.shape[0], x_valid.shape[1],1)
x_test  = np.array(x_test).reshape(x_test.shape[0], x_test.shape[1],1)
# %%
model = Sequential()
model.add(LSTM(512,input_shape = (nb_features,1)))
model.add(Activation("relu"))
model.add(BatchNormalization())
model.add(Flatten())
model.add(Dropout(0.15))
model.add(Dense(2048, activation = "relu"))
model.add(Dense(1024, activation = "relu"))
model.add(Dense(nb_classes, activation="softmax"))
model.summary()
#%%
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
score = model.fit(x_train, y_train, epochs = 1, validation_data=(x_valid,y_valid),batch_size=32)
#%%
results = model.evaluate(x_test, y_test, batch_size=128)
# %%
plt.plot(model.history.history["acc"])
plt.plot(model.history.history["val_acc"])
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
model.save('path/to/location')

#%%
path1=Path("model") 
tensorflow.saved_model.load(str(repo_path)+"\\"+str(path1))