import string
import os
from keras.models import Sequential
from keras.layers import Dense 
from keras.callbacks import EarlyStopping
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

print(predictors[2])

pred_data = np.array([[   32,     0, -9999, -9999,     0,     0,     1,     2,     0,     1,     0,     0,
     0,     0, -9999,     3,     0,     0,     1,     1,     1,     1,     0,     0,
  2014,     8,    27]])
n_cols = predictors.shape[1]
model = Sequential()

model.add(Dense(50, activation='relu', input_shape = (n_cols,)))
model.add(Dense(32, activation='relu'))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(predictors, target, epochs=100, callbacks = [early_stopping_monitor])
# Calculate predictions: predictions
predictions = model.predict(pred_data) 

# Calculate predicted probability of survival: predicted_prob_true
predicted_prob_true = predictions 

# print predicted_prob_true
print(predicted_prob_true) 
