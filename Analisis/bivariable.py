import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
# from pandas.plotting import scatter_matrix

df = pd.read_csv("student_sleep_patterns.csv")

#Columnas numéricas
df = df[['Age ', 'Sleep_Duration ', 'Study_Hours ', 'Screen_Time ', 'Caffeine_Intake ', 'Physical_Activity ', 'Sleep_Quality ', 'Weekday_Sleep_Start ','Weekend_Sleep_Start ', 'Weekday_Sleep_End ', 'Weekend_Sleep_End']]

correlacion_pearson = df.corr(method='pearson')

plt.figure(figsize=(10,6))
plt.imshow(correlacion_pearson, cmap="YlGnBu")
plt.colorbar(label='Coeficiente de correlación')

longitud_matriz = len(correlacion_pearson.columns)

for i in range(longitud_matriz):
    for j in range(longitud_matriz):
        plt.text(j, i, f"{correlacion_pearson.iat[i, j]:.2f}",ha='center', va='center', color='black')

plt.xticks(range(longitud_matriz), correlacion_pearson.columns, rotation=45, ha='right')
plt.yticks(range(longitud_matriz), correlacion_pearson.columns)
plt.title("Matriz de Correlación de Pearson")
plt.tight_layout()
plt.savefig("Analisis/Graficas/correlacion_pearson.png", format="png", dpi=300)
plt.show()
plt.close()

# print(df.columns)
# print(df.columns[0])

for i in range(longitud_matriz):
    atr_principal = df.columns[i]
    num_graficas = longitud_matriz - 1

    cols = 3
    rows = (num_graficas // cols) + (num_graficas % cols > 0)
    fig = plt.figure(figsize=(15, 5 * rows))
    gs = gridspec.GridSpec(rows, cols, figure=fig)
    idx = 0
    for j in range(longitud_matriz):
        if i != j:
            atr_secundario = df.columns[j]
            ax = fig.add_subplot(gs[idx])
            ax.scatter(df[atr_principal], df[atr_secundario], alpha=0.6)
            ax.set_title(f'{atr_principal} vs {atr_secundario}')
            ax.set_xlabel(atr_principal)
            ax.set_ylabel(atr_secundario)
            ax.grid(True)
            idx += 1

    plt.tight_layout()

    # plt.show()
    plt.savefig(f"Analisis/Graficas/{atr_principal}_vs_otros.png", format="png", dpi=300)
    plt.close()
