import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix

import numpy as np
dataFrame = pd.read_csv('./DatasetClasification.csv')


kf = KFold(n_splits=6)
kf.get_n_splits(dataFrame)
matrizLRArray=[]
matrizGNBArray=[]
for i, (train_index, test_index) in enumerate(kf.split(dataFrame)):
    X_train=dataFrame.iloc[train_index].drop(columns=['Sleep_Quality'])
    y_train=dataFrame.iloc[train_index]['Sleep_Quality']
    X_test=dataFrame.iloc[test_index].drop(columns=['Sleep_Quality'])
    y_test=dataFrame.iloc[test_index]['Sleep_Quality']
    logReg = LogisticRegression(max_iter = 1000).fit(X_train, y_train)
    gnb = GaussianNB().fit(X_train, y_train)
    resultGNB= gnb.predict(X_test)
    resultLog=logReg.predict(X_test)
    matrizLogReg=confusion_matrix(y_test, resultLog, labels=["Bajo", "Regular", "Bueno"])
    matrizGNB=confusion_matrix(y_test, resultGNB, labels=["Bajo", "Regular", "Bueno"])
    matrizLRArray.append(matrizLogReg)
    matrizGNBArray.append(matrizGNB)
    
print("Matriz de confusion promedio de logistic Regression")
promedio = np.mean(matrizLRArray,axis=0)
print(promedio)
print("Matriz de confusion promedio de naive bayes")
promedio = np.mean(matrizGNBArray,axis=0)
print(promedio)