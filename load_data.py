from keras.models import Sequential
from keras.layers import Dense 
from keras.callbacks import EarlyStopping
from keras.models import load_model
import pandas as pd
import numpy as np

model = Sequential()
pred_data = np.array([[   32,     0, -9999, -9999,     0,     0,     1,     2,     0,     1,     0,     0,
     0,     0, -9999,     3,     0,     0,     1,     1,     1,     1,     0,     0,
  2014,     8,    27]])


my_model = load_model("model_file.h5")
predictions = my_model.predict(pred_data)  

# Calculate predicted probability of survival: predicted_prob_true
predicted_prob_true = predictions  

# print predicted_prob_true
print(predicted_prob_true) 
