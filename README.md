# Libreria de espacios vectoriales   
##espacios vectoriales
un espacio vectorial (o también llamado espacio lineal) es una 
estructura algebraica creada a partir de un conjunto no vacío, 
una operación interna, y una operación externa. 


A los elementos de un espacio 
vectorial se les llama vectores y a los elementos del cuerpo, escalares.


## Descripción y contexto
Es una libreria de espacios vectoriales que tiene las funciones basicas 
de los espacios vectoriales que son :

*Adición de vectores complejos.

*Inverso (aditivo) de un vector complejo.

*Multiplicación de un escalar por un vector complejo.

*Adición de matrices complejas.

*Inversa (aditiva) de una matriz compleja.

*Multiplicación de un escalar por una matriz compleja.

*Transpuesta de una matriz/vector

*Conjugada de una matriz/vector

*Adjunta (daga) de una matriz/vector

*Producto de dos matrices (de tamaños compatibles)

*Función para calcular la "acción" de una matriz sobre un vector.

*Producto interno de dos vectores

*Norma de un vector

*Distancia entre dos vectores

*Revisar si una matriz es unitaria

*Revisar si una matriz es Hermitiana

*Producto tensor de dos matrices/vectores

## Aclaraciones
***

1. la libreria de espacios vectoriales en la unitaria y hermitiana aveces falla
   porque en las pruebas el np.matrix no lo conisdera bien.
2. en las diferentes funciones de la libreria, en algunos toca poner diferentes entradas 
ya sea solo la tuplas arreglo, matrizes, numeros complejos, etc
   
3. se utilizo en gran parte para crear esta libreria la libreria de numpy
4. y las pruebas solo comparan los elementos entonces
solo saldra un error cuando esto las respuesta obtenida y la respuesta dada fueran diferentes
   
## Autor/es
***
* autor: SANTIAGO OSPINA MEJIA 

* apoyo/ aportes: LUIS DANIEL BENAVIDES NAVARRO
          
