# FILE SPLITTER

***

Utilidad para dividir archivos de grandes dimensiones en partes de tamaño configurable.

Necesita de dos parámetros, el primero es obligatorio siendo el nombre del archivo a dividir o el path completo hasta este, el segundo es opcional, siendo la cantidad de líneas que poseerá cada uno de los archivos divididos, por default es 500.000.

Cada parte tendrá un total de (cantidad de líneas + 1) líneas, ya que todos compartirán el mismo header.

```shell
~$ python main.py "archivo.csv" 100000
```

El comando anterior generará archivos en el mismo directorio en el que se encuentre el archivo original de 100K líneas en el siguiente formato:
* archivo_0.csv
* archivo_1.csv
* ...