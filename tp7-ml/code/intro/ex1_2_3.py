import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
import os
plt.rcParams['font.family'] = 'DejaVu Sans'

images_folder = '../../images'
os.makedirs(images_folder, exist_ok=True)

# ---------- Ejercicio 1 ----------
# ---- Dividir CSV ---- 
file_path = '../../data/arbolado-mza-dataset.csv'
data = pd.read_csv(file_path)
# Dividir el 80% para entrenamiento y 20% para validación
train_data, validation_data = train_test_split(data, test_size=0.2, random_state=42)

train_file_path = '../../data/arbolado-mendoza-dataset-train.csv'
validation_file_path = '../../data/arbolado-mendoza-dataset-validation.csv'

train_data.to_csv(train_file_path, index=False)
validation_data.to_csv(validation_file_path, index=False)
(train_file_path, validation_file_path)

# ---------- Ejercicio 2 ----------
# ---- gráfico inclinacion_peligrosa -----

df_train = pd.read_csv('../../data/arbolado-mendoza-dataset-train.csv')
inclinacion_counts = df_train['inclinacion_peligrosa'].value_counts()
sns.set(style="whitegrid") # Estilo
plt.figure(figsize=(8, 6))
sns.barplot(x=inclinacion_counts.index, y=inclinacion_counts.values, legend=False)
plt.title('Distribucion de la Clase inclinacion_peligrosa', fontsize=16)
plt.xlabel('inclinacion_peligrosa (0 = No peligrosa, 1 = Peligrosa)', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.xticks(rotation=0)
plt.savefig('../../images/inclinacion_peligrosa.png')
plt.show()
plt.clf()

# ---- Secciones por peligrosidad -----

# Agrupar por sección
seccion_inclinacion = df_train.groupby('nombre_seccion')['inclinacion_peligrosa'].mean().sort_values()

plt.figure(figsize=(10, 8))
sns.barplot(x=seccion_inclinacion.values, y=seccion_inclinacion.index, legend=False)
plt.title('Proporcion de Arboles con inclinacion_peligrosa por Seccion', fontsize=16)
plt.xlabel('Proporcion de Arboles Peligrosos', fontsize=12)
plt.ylabel('Nombre de la Seccion', fontsize=12)
plt.savefig('../../images/inclinacion_peligrosa_seccion.png')
plt.show()
plt.clf()

# ---- Especies por peligrosidad -----

# Agrupar por especie
especie_inclinacion = df_train.groupby('especie')['inclinacion_peligrosa'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 8))
sns.barplot(x=especie_inclinacion.values, y=especie_inclinacion.index, legend=False)
plt.title('Proporcion de Arboles con inclinacion_peligrosa por Especie (Top 10)', fontsize=16)
plt.xlabel('Proporcion de Arboles Peligrosos', fontsize=12)
plt.ylabel('Especie', fontsize=12)
plt.savefig('../../images/inclinacion_peligrosa_especie.png')
plt.show()
plt.clf()

# ---------- Ejercicio 3 ----------
# ---- b) y c) Histogramas de circ_tronco_cm -----

def plot_histogram(df, variable, bins_list):
    plt.figure(figsize=(14, 10))

    # Histograma por cantidad de bins
    for i, bins in enumerate(bins_list, start=1):
        plt.subplot(2, 2, i)
        plt.hist(df[variable], bins=bins, color='blue', alpha=0.7)
        plt.title(f'Histograma de {variable} - {bins} bins', fontsize=14)
        plt.xlabel(variable)
        plt.ylabel('Frecuencia')
        plt.tight_layout()
        plt.savefig('../../images/histograma_circ_tronco_cm_bins.png')
    plt.show()
    plt.clf()

def plot_histogram_by_class(df, variable, class_variable, bins_list):
    plt.figure(figsize=(14, 10))
    # Filtrar por cada clase
    for i, bins in enumerate(bins_list, start=1):
        plt.subplot(2, 2, i)
        clase_0 = df[df[class_variable] == 0][variable]
        clase_1 = df[df[class_variable] == 1][variable]
        plt.hist(clase_0, bins=bins, alpha=0.7, label='No peligrosa (0)', color='blue')
        plt.hist(clase_1, bins=bins, alpha=0.7, label='Peligrosa (1)', color='red')
        plt.title(f'Histograma de {variable} por {class_variable} - {bins} bins', fontsize=14)
        plt.xlabel(variable)
        plt.ylabel('Frecuencia')
        plt.legend()
        # Guardar cada gráfico por cantidad de bins
        plt.tight_layout()
        plt.savefig('../../images/histograma_circ_tronco_cm_class_bins.png')
    plt.show()
    plt.clf()

bins_list = [10, 35, 60, 90]
plot_histogram(df_train, 'circ_tronco_cm', bins_list)
plot_histogram_by_class(df_train, 'circ_tronco_cm', 'inclinacion_peligrosa', bins_list)

# ----- d) circ_tronco_cm_cat a partir de circ_tronco_cm -----

# Se usan cuartiles de referencia
quartiles = df_train['circ_tronco_cm'].quantile([0.25, 0.5, 0.75])
df_train['circ_tronco_cm_cat'] = pd.cut(df_train['circ_tronco_cm'],
                                        bins=[-float('inf'), quartiles[0.25], quartiles[0.5], quartiles[0.75], float('inf')],
                                        labels=['bajo', 'medio', 'alto', 'muy alto'])

df_train.to_csv('../../data/arbolado-mendoza-dataset-circ_tronco_cm-train.csv', index=False)
