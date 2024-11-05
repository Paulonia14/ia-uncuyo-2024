## Resultados sobre la evaluación sobre tennis.csv

| Atributo | Ganancia de Información |
|----------|-------------------------|
| Outlook  | 0.246                   |
| Humidity | 0.151                   |
| Wind     | 0.048                   |
| Temp     | 0.029                   |

El atributo Outlook tiene la ganancia de información más alta, por lo que se selecciona como el nodo raíz del árbol.

El árbol comienza dividiendo los datos con base en el atributo outlook:
- Si el valor es "sunny", el árbol evalúa el atributo humidity.
    - Si la humedad es alta, la decisión es no jugar.
    - Si la humedad es normal, la decisión es jugar.
- Si el valor es "overcast", la decisión es directamente jugar, sin necesidad de evaluar más atributos.
- Si el valor es "rainy", el árbol evalúa el atributo windy.
    - Si no hay viento, la decisión es jugar.
    - Si hay viento, la decisión es no jugar.

#### Algunos ejemplos de las predicciones
Para el día outlook = sunny, humidity = high, windy = false, el árbol predice no jugar.
Para el día outlook = rainy, windy = true, humidity = normal, el árbol predice no jugar.
Para el día outlook = overcast, sin importar los demás atributos, el árbol predice jugar.
Para el día outlook = sunny, humidity = normal, el árbol predice jugar.

## Información sobre las estrategias para datos de tipo real

En el código del árbol de decisión implementado, solo se trabajó con atributos discretos, ya que el algoritmo ID3 es para clasificar utilizando variables categóricas. Los datos continuos, como la temperatura o la humedad en su forma real, no fueron utilizados. 
Si tuviéramos que trabajar con variables continuas, una estrategia común en ID3 sería convertir los datos continuos en intervalos discretos. 
En este caso, el dataset usado (tennis.csv) ya contiene valores discretos, por lo que no se necesitó aplicar ninguna transformación.