import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('no-informada-results.csv')

df_solutions = df[df['solution_found'] == True]

sns.set(style="whitegrid")

fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(8, 10))

sns.boxplot(x='algorithm_name', y='states_n', data=df_solutions, ax=axes[0])
axes[0].set_title('Cantidad de estados explorados')

sns.boxplot(x='algorithm_name', y='cost_e1', data=df_solutions, ax=axes[1])
axes[1].set_title('Costo total de las acciones (Escenario 1)')

sns.boxplot(x='algorithm_name', y='time', data=df_solutions, ax=axes[2])
axes[2].set_title('Tiempo empleado (segundos)')

plt.tight_layout()

# Mostrar los gráficos
plt.show()
