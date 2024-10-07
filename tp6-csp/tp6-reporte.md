# Trabajo Práctico 6: Satisfacción de restricciones

---

## Ejercicio 1
Una formulación CSP para un Sudoku puede ser de la forma:
- Variables: Cada casillero en el que puede colocarse un número (81 casilleros)
- Dominio: {1, 2, 3, 4, 5, 6, 7, 8, 9}
- Restricciones: Un mismo número no puede estar en la misma fila, misma columna, o misma "caja" de 3x3.

---
## Ejercicio 2
a. Remove SA − WA, delete G from SA.   
b. Remove SA − V , delete R from SA, leaving only B.   
c. Remove NT − WA, delete G from N T .   
d. Remove NT − SA, delete B from N T , leaving only R.   
e. Remove NSW − SA, delete B from N SW .   
f. Remove NSW − V , delete R from N SW , leaving only G.   
g. Remove Q − NT , delete R from Q.   
h. Remove Q − SA, delete B from Q.   
i. Remove Q − NSW , delete G from Q, leaving no domain for Q.

---
## Ejercicio 3
La complejidad en el peor caso cuando se ejecuta AC-3 en un árbol estructurado CSP es de O(E*D), donde E es la cantidad
de edges/aristas y D es el tamaño del dominio más grande.

---
## Ejercicio 4
Para cada valor de Xi, mantenemos un registro de las variables Xk para las que un arco de Xk a Xi se satisface con ese
valor concreto de Xi. Esto puede calcularse en un tiempo proporcional al tamaño de la representación del problema. 
Entonces, cuando se elimina un valor de Xi, reducimos en 1 el conteo de valores permitidos para cada arco (Xk, Xi)
registrado bajo ese valor.

---
## Ejercicio 5
- a)  
Un CSP tiene n-consistencia cuando, para cada subconjunto de variables de tamaño menor o igual a n, cualquier 
asignación a esas variables puede extenderse a una asignación consistente para una variable adicional.
La 2-consistencia implica que cada variable es consistente con las variables conectadas a ella (vecinos). Además, la
estructura de árbol permite que cualquier subconjunto de k variables (con k < n) que sea consistente puede extenderse
a la siguiente variable en el orden del árbol.  
Dado que los árboles no contienen ciclos, no hay conflictos que puedan requerir la reconsideración de las asignaciones
previas. Por lo tanto, la 2-consistencia es suficiente para garantizar la n-consistencia.
- b)  
Ya que cada subconjunto de variables puede extenderse a una asignación consistente para la siguiente variable
en el árbol (por su estructura), y dado que el árbol se puede recorrer sin necesidad de retroceder, la 2-consistencia 
es suficiente para asegurar que se pueden satisfacer todas las restricciones sin necesidad de verificar subconjuntos 
más grandes. 

---
## Ejercicio 7




