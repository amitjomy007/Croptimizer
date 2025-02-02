# -*- coding: utf-8 -*-
"""ForestFirePredictor

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Bp6mMuAYdvzIgZroyN1IJV2lqwdkZXai
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle

df = pd.read_csv('Forest_fire.csv')
df = np.array(df)

X = df[1:, 1:-1]
y = df[1:, -1]
y = y.astype('int')
X = X.astype('int')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

model = LogisticRegression()
model.fit(X_train, y_train)

preds = model.predict(X_test)
accuracy = accuracy_score(y_test, preds)
print(accuracy)

pickle.dump(model, open('model.pkl', 'wb'))

