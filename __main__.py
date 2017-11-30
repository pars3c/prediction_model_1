import string
import os
from keras.models import Sequential
from keras.layers import Dense 
from keras.callbacks import EarlyStopping
from keras.models import load_model
import pandas as pd
import numpy as np
from data_format import data_form, data_form2

early_stopping_monitor = EarlyStopping(patience=5)

df = data_form()
df2 = data_form2()


df = df.drop(['Timestamp'], axis=1)
df = df.drop(['Country'], axis=1)
predictors = df.as_matrix()
target = df2.as_matrix()




n_cols = predictors.shape[1]
model = Sequential()

model.add(Dense(200, input_shape = (n_cols,)))
model.add(Dense(32))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(predictors, target, epochs=500, callbacks = [early_stopping_monitor])
# Calculate predictions: predictions
model.save("model_file.h5")