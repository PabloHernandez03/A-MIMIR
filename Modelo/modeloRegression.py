import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold
import numpy as np
dataFrame = pd.read_csv('./DatasetRegression.csv')


kf = KFold(n_splits=6)
kf.get_n_splits(dataFrame)
mseRegArray=[]
mseRandArray=[]
for i, (train_index, test_index) in enumerate(kf.split(dataFrame)):
    X_train=dataFrame.iloc[train_index].drop(columns=['Sleep_Quality'])
    y_train=dataFrame.iloc[train_index]['Sleep_Quality']
    X_test=dataFrame.iloc[test_index].drop(columns=['Sleep_Quality'])
    y_test=dataFrame.iloc[test_index]['Sleep_Quality']

    reg = LinearRegression().fit(X_train,y_train)
    random= RandomForestRegressor().fit(X_train,y_train)
    resultReg=reg.predict(X_test)  
    resultRand=random.predict(X_test)
    mseReg=(mean_squared_error(y_test,resultReg))
    mseRand=(mean_squared_error(y_test,resultRand))
    mseRegArray.append(mseReg)
    mseRandArray.append(mseRand)
    

print("Modelo de regresion con random forest")
print(mseRandArray)
print(np.mean(mseRandArray))
print("Modelo de regresion con regresion lineal")
print(mseRegArray)
print(np.mean(mseRegArray))