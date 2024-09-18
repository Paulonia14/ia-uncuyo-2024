import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Generar los gráficos
def plot_results(csv_file='results.csv'):
    data = pd.read_csv(csv_file)

    # Tiempo de ejecución
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Size', y='Avg Time (s)', hue='Algorithm', data=data)
    plt.title('Distribución de Tiempos de Ejecución por Tamaño del Tablero')
    plt.xlabel('Tamaño del Tablero')
    plt.ylabel('Tiempo de Ejecución Promedio (s)')
    plt.legend(title='Algoritmo')
    plt.show()

    # Pasos hasta la solución
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Size', y='Avg Steps', hue='Algorithm', data=data)
    plt.title('Distribución de Cantidad de Pasos por Tamaño del Tablero')
    plt.xlabel('Tamaño del Tablero')
    plt.ylabel('Pasos Promedio hasta la Solución')
    plt.legend(title='Algoritmo')
    plt.show()

    # Tasa de éxito
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Size', y='Success Rate (%)', hue='Algorithm', data=data)
    plt.title('Tasa de Éxito por Tamaño del Tablero y Algoritmo')
    plt.xlabel('Tamaño del Tablero')
    plt.ylabel('Tasa de Éxito (%)')
    plt.legend(title='Algoritmo')
    plt.show()
