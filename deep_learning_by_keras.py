import pandas as pd
import numpy as np

df = pd.read_csv("face20_500.csv")
df = df.iloc[:,1:]
dfy = df["label"]
dfX = df.iloc[:,:-1]
dfX2 = np.array(dfX).reshape(len(dfy), 96, 96)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(dfX2, dfy, test_size=0.2, random_state=42)

X_train = X_train.astype('float32')/255.0
X_test = X_test.astype('float32')/255.0
outNum = len(np.unique(dfy))

print(outNum)
print(X_train.shape, X_train.dtype)

from keras.utils import np_utils

Y_train = np_utils.to_categorical(y_train, outNum)
Y_test = np_utils.to_categorical(y_test, outNum)
Y_train[:4]

X_train.shape

X_train = X_train.reshape(-1, 96, 96 ,1)
X_test = X_test.reshape(-1, 96, 96, 1)

from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.regularizers import l2

np.random.seed(0)

model = Sequential()

model.add(Conv2D(128, (5, 5), activation='relu', input_shape=(96, 96, 1), padding='same', kernel_regularizer=l2(0.001)))
model.add(Conv2D(128, (5, 5), activation='relu', padding='same'))
model.add(MaxPooling2D())
model.add(Dropout(0.1))

model.add(Conv2D(128, (5, 5), activation='relu', padding='same', kernel_regularizer=l2(0.001)))
model.add(Conv2D(128, (5, 5), activation='relu', padding='same', kernel_regularizer=l2(0.001)))
model.add(MaxPooling2D())
model.add(Dropout(0.2))

model.add(Conv2D(128, (5, 5), activation='relu', padding='same', kernel_regularizer=l2(0.001)))
model.add(Conv2D(128, (5, 5), activation='relu', padding='same', kernel_regularizer=l2(0.001)))
model.add(MaxPooling2D())
model.add(Dropout(0.2))

model.add(Conv2D(128, (5, 5), activation='relu', padding='same', kernel_regularizer=l2(0.001)))
model.add(Conv2D(128, (5, 5), activation='relu', padding='same', kernel_regularizer=l2(0.001)))
model.add(MaxPooling2D())
model.add(Dropout(0.2))

model.add(Conv2D(128, (5, 5), activation='relu', padding='same', kernel_regularizer=l2(0.001)))
model.add(Conv2D(128, (5, 5), activation='relu', padding='same', kernel_regularizer=l2(0.001)))
model.add(MaxPooling2D())
model.add(Dropout(0.3))

model.add(Conv2D(128, (5, 5), activation='relu', padding='same', kernel_regularizer=l2(0.001)))
model.add(Conv2D(128, (5, 5), activation='relu', padding='same', kernel_regularizer=l2(0.001)))
model.add(MaxPooling2D())
model.add(Dropout(0.4))

model.add(Flatten())
model.add(Dense(256, activation='relu', kernel_regularizer=l2(0.001)))
model.add(Dense(128, activation='relu', kernel_regularizer=l2(0.001)))
model.add(Dropout(0.5))
model.add(Dense(outNum, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adadelta', metrics=['accuracy'])

%%time
hist = model.fit(X_train, Y_train, epochs=100, batch_size=100, validation_data=(X_test, Y_test), verbose=2)


import matplotlib.pyplot as plt

plt.figure(figsize=(5,7), dpi=200)
plt.plot(hist.history["acc"], label="train")
plt.plot(hist.history["val_acc"], label="test")
plt.legend()
plt.show()