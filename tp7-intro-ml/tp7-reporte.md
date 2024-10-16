# Trabajo Práctico 7 - Introducción

## Lectura del segundo capítulo del libro Introduction to Statistical Learning y proveer las respuestas a los puntos 1,2,5,6,7 de la sección 2.4 (página 52 del ISLRv2).

---

## Pregunta 1
1. Para cada una de las partes (a) a (d), indique si en general cabe esperar que el rendimiento de un método de aprendizaje estadístico flexible sea mejor o peor que el de un método inflexible. Justifique su respuesta.
   - (a) El tamaño de la muestra n es extremadamente grande y el número de predictores p es pequeño.
   - (b) El número de predictores p es extremadamente grande, y el número de observaciones n es pequeño.
   - (c) La relación entre los predictores y la respuesta es muy poco lineal.
   - (d) La varianza de los términos de error, es decir, σ2 = Var(ϵ), es extremadamente alta.

### Respuesta:
a) En este caso si la muestra es muy grande es conveniente usar un modelo flexible, ya que se puede aprovechar la gran cantidad de datos para modelar relaciones más complejas y no corre el riesgo de sobreajustar por el tamaño de la muestra.

b) Si el número de predictores es muy grande y el número de observaciones pequeño, entonces es conveniente usar un modelo más restrictivo para evitar "overfitting".   

c) Un método flexible puede dar mejores resultados porque puede modelar relaciones complejas y no lineales entre los predictores y la respuesta.   

d) En este caso un modelo flexible es peor ya que una alta varianza (mayor dispersión) en los errores puede llevar a un "overfitting", por lo que conviene utilizar un modelo más restrictivo.

---
## Pregunta 2
2. Explique si cada escenario es un problema de clasificación o de regresión, e indique si nos interesa más la inferencia o la predicción. Por último, indique n y p.
    - (a) Recopilamos un conjunto de datos sobre las 500 empresas más importantes de Estados Unidos. Para cada empresa registramos los beneficios, el número de empleados, el sector y el salario del director general. Nos interesa saber qué factores influyen en el salario del CEO.
    - (b) Estamos pensando en lanzar un nuevo producto y queremos saber si será un éxito o un fracaso. Recopilamos datos sobre 20 productos similares lanzados anteriormente. Para cada producto hemos registrado si fue un éxito o un fracaso, el precio cobrado por el producto, el presupuesto de marketing, el precio de la competencia y otras diez variables.
    - (c) Nos interesa predecir el % de variación del tipo de cambio USD/Euro en relación con las variaciones semanales de los mercados bursátiles mundiales. Por lo tanto, recogemos datos semanales para todo el año 2012. Para cada semana registramos el % de cambio en el USD/Euro, el % de cambio en el mercado estadounidense, el % de cambio en el británico y el % de cambio en el mercado alemán.

### Respuesta:
a) Esto es un problema de **regresión** y nos interesa la **inferencia** ya que queremos saber qué factores afectan  al salario del CEO. **n = 500, p = 4**  
b) Es un problema de **clasificación** ya que queremos saber si es exitoso o no, y nos interesa la **predicción**. **n = 20, p = 14**  
c) Es un problema de **regresión** y nos interesa la **predicción**. **n = 52, p = 4**

---
## Pregunta 5

5. ¿Cuáles son las ventajas y los inconvenientes de un enfoque muy flexible (frente a uno menos flexible) para la  regresión o la clasificación? ¿En qué circunstancias es preferible un enfoque más flexible a uno menos flexible?  ¿Cuándo es preferible un enfoque menos flexible?

### Respuesta:

- Ventajas: 
  - Puede capturar relaciones más complejas. 
  - Potencialmente una mayor precisión en la predicción.
- Desventajas: 
  - Tienden a sobreajustar los datos (overfitting), es decir, pueden captar el ruido de los datos.
  - Menos interpretables, lo que dificulta la inferencia.  

Un enfoque **flexible** es preferible cuando el objetivo es la **predicción** y la relación entre los predictores y la respuesta es muy poco lineal.  

Un enfoque **inflexible** o menos flexible es preferible cuando el objetivo es la **inferencia**, aún más si necesitamos un  modelo sencillo que nos permita comprender la relación entre las variables.

---
## Pregunta 6
6. Describa las diferencias entre un enfoque de aprendizaje estadístico paramétrico y uno no paramétrico. ¿Cuáles son las ventajas de un enfoque paramétrico de regresión o clasificación (frente a un enfoque no paramétrico)? ¿Cuáles son sus desventajas?

### Respuesta:
- Enfoque paramétrico: **Asume una forma específica para el modelo**.   
La principal ventaja es que simplifica el problema al reducirlo a la estimación de unos pocos parámetros, lo que requiere menos datos. La desventaja es que el modelo sólo es tan bueno como la suposición, es decir, si la forma elegida es incorrecta, el rendimiento será muy malo.
- Enfoque no paramétrico: **No asume ninguna forma específica para la función**.   
La ventaja es su flexibilidad ya que puede modelizar una mayor variedad de relaciones. Su desventaja es que requiere un tamaño de muestra mucho mayor para estimar la función con precisión, y el riesgo de "overfitting" es mayor.

---
## Pregunta 7 

7. La siguiente tabla proporciona un conjunto de datos de entrenamiento que contiene seis observaciones, tres predictores  y una variable de respuesta cualitativa.

| Obs   | X1 | X2 | X3 | Y     |
|-------|----|----|----|-------|
| **1** | 0  | 3  | 0  | Red   |
| **2** | 2  | 0  | 0  | Red   |
| **3** | 0  | 1  | 3  | Red   |
| **4** | 0  | 1  | 2  | Green |
| **5** | -1 | 0  | 1  | Green |
| **6** | 1  | 1  | 1  | Red   |

Supongamos que deseamos utilizar este conjunto de datos para hacer una predicción para Y cuando X1 = X2 = X3 = 0 utilizando K-vecinos más cercanos.  
- (a) Calcule la distancia euclídea entre cada observación y el punto de prueba, X1 = X2 = X3 = 0.
- (b) ¿Cuál es nuestra predicción con K = 1? ¿Por qué?
- (c) ¿Cuál es nuestra predicción con K = 3? ¿Por qué?
- (d) Si la frontera de decisión de Bayes en este problema es altamente no lineal, entonces ¿Esperaríamos que el mejor valor para K fuera grande o pequeño? ¿Por qué?

### Respuesta:

a) La distancia euclidiana entre dos puntos \( (X_1, X_2, X_3) \) y \( (Y_1, Y_2, Y_3) \) puede calcularse como:

\[
\text{Distancia} = \sqrt{(X_1 - Y_1)^2 + (X_2 - Y_2)^2 + (X_3 - Y_3)^2}
\]

- 1: Distancia = 3  
- 2: Distancia = 2
- 3: Distancia = sqrt{10}
- 4: Distancia = sqrt{5}
- 5: Distancia = sqrt{2}
- 6: Distancia = sqrt{3}

b) Para K = 1, usamos el vecino más cercano para hacer la predicción, el cual es la Observación 5 con una distancia de sqrt{2} = 1.41, y su respuesta Y es **Green**.
Así que la predicción para K=1 es **Green**.

c) Para K = 3, vemos los 3 vecinos más cercanos:
- Observación 5 (Green, distancia 1.41)
- Observación 6 (Red, distancia 1.73)
- Observación 2 (Red, distancia 2)
Por lo tanto, la predicción para K = 3 es **Red**, ya que es la mayoría.

d) Si la frontera de decisión de Bayes es altamente no lineal, esperaríamos que el mejor valor para K sea pequeño. Un menor K permite que el algoritmo sea más flexible y sensible a las variaciones locales de los datos. Un K grande daría lugar a un límite de decisión que estaría más cerca de una forma lineal.
