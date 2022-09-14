# FILE SPLITTER

***

Utilidad para dividir archivos de grandes dimensiones en partes de tamaño configurable.

### Parámetros

Ingresar los siguientes parámetros en el orden especificado

1. Archivo: **obligatorio**, ruta del archivo a dividir, las partes se colocarán en el mismo directorio en el que se encuentre.
2. Cantidad de líneas: **opcional**, cantidad de líneas de cada una de las partes, por default es 500.000. Todas las partes excepto la última tendrán la cantidad especificada de líneas más una para el header del archivo.
3. Delimitador: **opcional**, delimitador de columnas, por default es: ",". Cuidado: si el delimitador es incorrecto, las partes generadas estarán mal formadas.

#### Ejemplo

```shell
python main.py "archivo.csv" 100000 "|"
```

El comando anterior generará las partes en el mismo directorio en el que se encuentre el archivo original de 100K líneas cada una utilizando el delimitador "|" en el siguiente formato:
* archivo_0.csv
* archivo_1.csv
* ...