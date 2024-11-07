import pandas as pd
import matplotlib.pyplot as plt
dataFrame = pd.read_csv('./student_sleep_patterns.csv')
print(dataFrame)

print("Analisis estadistico")
for column in dataFrame:
    print("Nombre de atributo: ",column)
    print("Tipo de atributo: ",dataFrame[column].dtype)
    print(dataFrame[column].describe())
    print()
    fig = plt.figure()
    if dataFrame[column].dtype == object:
        fig.canvas.manager.set_window_title("Histograma de columna: "+str(column))
        frecuencias = dataFrame[column].value_counts()
        frecuencias.plot(kind='barh',figsize=(10,10))
        plt.title('Columna: '+column)
        plt.show()
    else:
        fig.canvas.manager.set_window_title("Grafica de caja de columna: "+str(column))
        dataFrame[column].plot(kind='box',figsize=(10,10))
        plt.title('Columna: '+column)
        plt.show()