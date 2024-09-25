import matplotlib.pyplot as plot
import os
import numpy


# Realiza el gráfico de cajas y extensiones.
def whiskers(data, title, x_label, y_label, filename, algList, executeRemoveEmpty=False):
    print("Iniciando la función whiskers...")  # Depuración
    if executeRemoveEmpty:
        data = removeEmpty(data)

    # Ruta fija de la carpeta 'images' en relación a la ubicación actual
    imagesDir = os.path.join(os.path.dirname(__file__), '../images')
    os.makedirs(imagesDir, exist_ok=True)  # Crea la carpeta 'images' si no existe

    plot.figure(figsize=(10, 7))
    plot.boxplot(data, patch_artist=True, showmeans=True)

    for i, dataset in enumerate(data, start=1):
        if dataset == []:
            continue
        std = numpy.std(dataset)
        mean = numpy.mean(dataset)
        plot.errorbar(x=i, y=mean, yerr=std, fmt='o', color='red', capsize=5)

    plot.title(title)
    plot.xlabel(x_label)
    plot.ylabel(y_label)
    plot.grid(True)
    plot.xticks([i for i in range(1, len(algList) + 1)], algList)

    # Guardar gráfico en carpeta 'images'
    save_path = os.path.join(imagesDir, filename + ".png")
    print(f"Guardando gráfico en: {save_path}")  # Depuración
    plot.savefig(save_path)

    # Mostrar el gráfico para verificar que se genera correctamente
    plot.show()  # Añadido para mostrar temporalmente el gráfico


def plotData(results, filename, iter, title, xlabel, ylabel, sizeX, sizeY):
    print("Iniciando la función plotData...")  # Depuración
    # Ruta fija de la carpeta 'images' en relación a la ubicación actual
    imagesDir = os.path.join(os.path.dirname(__file__), '../images')
    os.makedirs(imagesDir, exist_ok=True)  # Crea la carpeta 'images' si no existe

    plot.figure(figsize=(sizeX, sizeY))

    for i in range(0, len(results)):
        plot.scatter([i + 1], results[i], color="red")
        plot.text(i + 1, results[i], str(results[i]), ha='right', color='red')

    plot.xticks(range(1, len(iter) + 1), iter)
    plot.title(title)
    plot.xlabel(xlabel)
    plot.ylabel(ylabel)
    plot.grid(True)

    # Guardar gráfico en carpeta 'images'
    save_path = os.path.join(imagesDir, filename + ".png")
    print(f"Guardando gráfico en: {save_path}")  # Depuración
    plot.savefig(save_path)

    # Mostrar el gráfico para verificar que se genera correctamente
    plot.show()  # Añadido para mostrar temporalmente el gráfico

def plotData2(results, filename, iter, title, xlabel, ylabel, sizeX, sizeY):
    print("Iniciando la función plotData...")  # Depuración
    # Ruta fija de la carpeta 'images' en relación a la ubicación actual
    imagesDir = os.path.join(os.path.dirname(__file__), '../images')
    os.makedirs(imagesDir, exist_ok=True)  # Crea la carpeta 'images' si no existe

    plot.figure(figsize=(sizeX, sizeY))
    plot.plot(iter, results, '-o', color="blue")  # Gráfico de línea con puntos en cada dato

    plot.title(title)
    plot.xlabel(xlabel)
    plot.ylabel(ylabel)
    plot.grid(True)

    # Guardar gráfico en carpeta 'images'
    save_path = os.path.join(imagesDir, filename + ".png")
    print(f"Guardando gráfico en: {save_path}")  # Depuración
    plot.savefig(save_path)

    # Mostrar el gráfico para verificar que se genera correctamente
    plot.show()  # Añadido para mostrar temporalmente el gráfico


def removeEmpty(data):
    aux = []
    for i in range(0, len(data)):
        if data[i] != []:
            aux.append(data[i])
    return aux
