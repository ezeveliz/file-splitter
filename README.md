# FILE SPLITTER

***

Utilidad para dividir archivos de grandes dimensiones en partes de tamaño configurable

Necesita de dos parámetros, el primero es obligatorio siendo el nombre del archivo a dividir, el segundo es opcional, siendo el tamaño del archivo dividido que se requiere, por default es 500000.


```shell
~$ python main.py "archivo.csv" 100000
```

El comando anterior generará archivos en el mismo directorio en el que se encuentre el archivo original de 100K líneas en el siguiente formato:
* archivo_0.csv
* archivo_1.csv
* ...