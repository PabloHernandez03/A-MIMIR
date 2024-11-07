import pandas as pd
import matplotlib.pyplot as plt
dataFrame = pd.read_csv('./student_sleep_patterns.csv')
print(dataFrame)

print("Analisis estadistico")
dominiosObject={
    'Gender':['Other','Male','Female'],
    'University_Year':['1st Year','2nd Year','3rd Year','4th Year']
}
for column in dataFrame.iloc[:, 1:]:
    print(f'Nombre de atributo: {column}')
    print(f'Tipo de atributo: {dataFrame[column].dtype}')
    print(dataFrame[column].describe())
    print()
   
    fig = plt.figure()
    if dataFrame[column].dtype == object:
        outliers_column = dataFrame[~dataFrame[column].isin(dominiosObject[column])]
        if len(outliers_column) != 0:
            print(f'Valores atípicos en {column}')
            print(outliers_column)
        else:
            print('Sin valores atipicos')
        fig.canvas.manager.set_window_title("Histograma de columna: "+str(column))
        frecuencias = dataFrame[column].value_counts()
        frecuencias.plot(kind='barh',figsize=(10,10))
        plt.title('Columna: '+column)
        plt.show()
    else:
        sesgo = dataFrame[column].skew()
        print(f'Sesgo de la columna {column}: {sesgo}')
        Q1 = dataFrame[column].quantile(0.25)
        Q3 = dataFrame[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers_column = dataFrame[(dataFrame[column] < lower_bound) | (dataFrame[column] > upper_bound)]
        if len(outliers_column) != 0:
            print(f'Valores atípicos en {column}')
            print(outliers_column)
        else:
            print('Sin valores atipicos')
        fig.canvas.manager.set_window_title("Grafica de caja de columna: "+str(column))
        dataFrame[column].plot(kind='box',figsize=(10,10))
        plt.title('Columna: '+column)
        plt.show()