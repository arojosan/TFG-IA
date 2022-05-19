# TFG-IA
Aprendizaje automático para categorizar los veredictos time-limit en jueces en línea  
Machine learning for clustering time-limit verdicts in online judges

El usuario no sabe si ese TLE se debe a que su solución es ineficiente desde un punto de vista de la complejidad, de la "constante multiplicativa" o simplemente tiene algún error de programación que le hace entrar en algún bucle infinito. El proyecto consiste en discernir en cuál de los tres casos anteriores se está.

Eso implica analizar los tiempos de ejecución de cada envío particular y deducir si los tiempos siguen una función lineal, cuadrática ...

En esta parte del repositorio veremos que implicación que resulta de adaptar la biblioteca python big_o + un plot, para que funcion de tiempo tienen los algoritmos.

Tambien se implementa un generador de casos con un cronometro y la escritura de tiempos de 3 y 4 ejecuciones.
