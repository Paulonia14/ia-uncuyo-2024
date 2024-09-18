import matplotlib.pyplot as plot
import os
import numpy 
#Realiza el gráfico de cajas y extensiones. Recibe los datos a graficar, el título del gráfico, el título del eje X, el título del eje Y y el nombre del archivo donde se guardará el gráfico.
def whiskers(data, title, x_label, y_label, filename, algList, executeRemoveEmpty = False):
    #Se eliminan los datos vacíos
    if executeRemoveEmpty == True:
        data = removeEmpty(data)
    #Se forma la ruta de la carpeta de imágenes
    baseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    imagesDir = os.path.join(baseDir, 'images')
    os.makedirs(imagesDir, exist_ok=True)

    #Se crea el gráfico de cajas
    plot.figure(figsize=(10,7))
    plot.boxplot(data, patch_artist=True, showmeans=True)

    #Se agrega la desviación estándar y la media a los gráficos
    for i, dataset in enumerate(data, start=1):
        if dataset == []:
            continue
        std = numpy.std(dataset)
        mean = numpy.mean(dataset)
        
        plot.errorbar(x=i, y=mean, yerr=std, fmt='o', color='red', capsize=5)

    #Se añade el título
    plot.title(title)
    #Se añade el título del eje X
    plot.xlabel(x_label)
    #Se añade el título del eje Y
    plot.ylabel(y_label)
    #Se hace visible la cuadrícula en el gráfico
    plot.grid(True)
    #Se añaden las etiquetas a los valores del eje X
    plot.xticks([i for i in range(1, len(algList) + 1)], algList)    #Se guarda el gráfico
    plot.savefig(os.path.join(imagesDir, filename + ".png"))
    
    return 0

#Grafica los resultados de los algoritmos. Recibe los resultados y el nombre del archivo donde se guardará el gráfico.
def plotData(results, filename, iter, title, xlabel, ylabel, sizeX, sizeY):
    #Se forma la ruta de la carpeta de imágenes
    baseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    imagesDir = os.path.join(baseDir, 'images')
    os.makedirs(imagesDir, exist_ok=True)

    #Se crea el gráfico de celdas limpiadas
    plot.figure(figsize=(sizeX,sizeY))

    for i in range(0, len(results)):
        #Se colocan los puntos
        plot.scatter([i + 1], results[i], color="red")
        
        #Se colocan los valores en los puntos
        plot.text(i + 1, results[i], str(results[i]), ha='right', color='red')

    #Se añaden las etiquetas a los valores del eje X
    plot.xticks(range(1, len(iter) + 1), iter)
    #Se añade el título
    plot.title(title)
    #Se añade el título del eje X
    plot.xlabel(xlabel)
    #Se añade el título del eje Y
    plot.ylabel(ylabel)
    #Se hace visible la cuadrícula en el gráfico
    plot.grid(True)
    #Se guarda el gráfico
    plot.savefig(os.path.join(imagesDir, filename + ".png"))
    return 0

def removeEmpty(data):
    aux = []
    for i in range(0, len(data)):
        if data[i] != []:
            aux.append(data[i])
    return aux