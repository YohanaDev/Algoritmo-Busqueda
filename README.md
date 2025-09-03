# Solución al Problema de Algoritmia

Este repositorio contiene la solución a un problema de algoritmia que busca los números adyacentes a una lista de consultas dentro de una base de datos de números enteros.

## Descripción del Problema

El algoritmo busca, para cada número consultado, el número más alto que sea inferior a él y el número más pequeño que sea superior a él. Si no se encuentra un número, se debe reemplazar por una 'X'.

## Requisitos

* **Lenguaje de Programación:** Python 3.x

## Estructura del Proyecto

* `solucion.py`: Archivo principal que contiene la lógica del algoritmo.
* `README.md`: Este archivo, con las instrucciones y la descripción del proyecto.

## Instrucciones de Ejecución

1.  Asegúrate de tener Python 3 instalado en tu sistema.
2.  Abre una terminal o línea de comandos.
3.  Navega hasta el directorio donde se encuentra el archivo `solucion.py`.
    ```bash
    cd /ruta/a/tu/carpeta/del/proyecto
    ```
4.  Ejecuta el script con el siguiente comando:
    ```bash
    python solucion.py
    ```
5.  El programa te pedirá que ingreses los datos línea por línea, siguiendo este orden:
    * Tamaño de la lista base (un número entero).
    * Lista de números de la base de datos, separados por espacios.
    * Número de consultas a realizar (un número entero).
    * Lista de números a consultar, separados por espacios.

## Ejemplo de Uso

**Entrada (Input):**
5
2 4 5 7 9
4
2 5 6 10


**Salida (Output):**
X 4
4 7
5 7
9 X

