import sys
import os
import csv

# Tamaño por default de los archivos a crear
default_size = 500000
filesize = 0
# Header del archivo original que voy a colocar en todas las partes
header = ""
# Nombre del archivo original sin la extensión
new_filename = ""
# Extensión del archivo original
extension = ""
# Delimitadores de columnas en el archivo
default_delimiter = ","
delimiter = ""


# Escribo cada parte del archivo
def write_chunk(part, lines):
    with open(new_filename + '_' + str(part) + extension, 'w') as file:
        file_writer = csv.writer(file, delimiter=delimiter)

        file_writer.writerow(header)
        file_writer.writerows(lines)


# Verifico los parámetros pasados y comienzo a procesar el archivo original
def main(args):
    global filesize
    global header
    global new_filename
    global extension
    global delimiter

    # Verifico que me hayan pasado el parámetro del nombre de archivo
    try:
        filename = args[1]
    except:
        print('Tenés que incluir el nombre del archivo CSV a dividir.')
        return

    # Verifico que el archivo en cuestión exista
    try:
        file = open(filename)
    except:
        print('No pudimos encontrar el archivo especificado.')
        return

    # Obtengo el nombre de archivo y su extensión para posteriormente crear las partes
    new_filename, extension = os.path.splitext(filename)

    # Verifico si pasaron el parámetro de tamaño de archivo deseado, si no lo pasaron, será 500K lineas
    try:
        filesize = int(args[2])
        if filesize < 1:
            print("¿En serio?")
            return
    except:
        filesize = default_size

    # Verifico si me pasaron un delimitador custom
    try:
        temp_delimiter = args[3]
        if len(temp_delimiter) > 0:
            delimiter = temp_delimiter
            print("Se utilizará el delimitador: " + delimiter + ", si el mismo no es el correcto las partes generadas "
                                                                "tendrán un formato incorrecto")
        else:
            delimiter = default_delimiter
    except:
        delimiter = default_delimiter

    print("Iniciando división...\n")

    # Esto sirve para interpretar el archivo original como un csv, de esta manera me
    # ahorro el problema de saltos de línea en lugares inesperados
    file_reader = csv.reader(file, delimiter=delimiter)

    count = 0
    part = 0
    # Obtengo la primera línea(header) para colocarlo en todas las partes
    header = next(file_reader)
    lines = []
    for line in file_reader:
        count += 1
        lines.append(line)
        # Se completó el buffer con la cantidad de líneas especificadas en filesize, lo
        # vuelco en un archivo
        if count % filesize == 0:
            print("Creando parte " + str(part + 1) + "...")
            write_chunk(part, lines)
            lines = []
            part += 1
    # Vuelco las líneas restantes en un archivo, en este caso no llegamos a completar el
    # buffer con la cantidad especificada en filesize
    if len(lines) > 0:
        print("Creando parte " + str(part + 1) + "...\n")
        write_chunk(part, lines)
    print("El archivo fue dividido en " + str(part + 1) + " partes en el directorio " + os.path.dirname(filename))
    file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv)
