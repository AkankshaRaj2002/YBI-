# -*- coding: utf-8 -*-
"""YBI Internship.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IvK-PuVmDFbHi_qtoKm7cJDKUgtfxPBR
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('http://raw.githubusercontent.com/YBI-Foundation/Teaching-Data/main/Women%20Clothing%20E-Commerce%20Review.csv')

df.head()

df.info()

df.shape

df.isna().sum()

df[df['Review']==""] = np.nan

df['Review'].fillna("No Review",inplace=True)

df.isna().sum()

df['Review']

df.columns

x=df['Review']

y=df['Rating']

df['Rating'].value_counts()

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.7, stratify=y, random_state=2529)

x_train.shape, x_test.shape, y_train.shape, y_test.shape

from sklearn.feature_extraction.text import CountVectorizer

cv= CountVectorizer(lowercase=True, analyzer='word', ngram_range=(2,3),stop_words='english',max_features=5000)

x_train=cv.fit_transform(x_train)

cv.get_feature_names_out()

x_train.toarray()

x_test=cv.fit_transform(x_test)

cv.get_feature_names_out()

x_test.toarray()

from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

y_pred.shape

y_pred

model.predict_proba(x_test)

from sklearn.metrics import confusion_matrix, classification_report

print(confusion_matrix(y_test, y_pred))

print(classification_report(y_test, y_pred))

df['Rating'].value_counts()

df.replace({'Rating':{1:0,2:0,3:0,4:1,5:1}},inplace=True)

y=df['Rating']

x=df['Review']

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.7, stratify=y, random_state=2529)

x_train.shape, x_test.shape, y_train.shape, y_test.shape

from sklearn.feature_extraction.text import CountVectorizer

cv= CountVectorizer(lowercase=True, analyzer='word', ngram_range=(2,3),stop_words='english',max_features=5000)

x_train=cv.fit_transform(x_train)

x_test=cv.fit_transform(x_test)

from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

y_pred.shape

y_pred

from sklearn.metrics import confusion_matrix, classification_report

print(confusion_matrix(y_test, y_pred))

print(classification_report(y_test, y_pred))
