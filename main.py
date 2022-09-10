import sys
import os

# Tamaño por default de los archivos a crear
default_size = 500000
filesize = 0
# Header del archivo original que voy a colocar en todas las partes
header = ""
# Nombre del archivo original sin la extensión
new_filename = ""
# Extensión del archivo original
extension = ""


# Escribo cada parte del archivo
def write_chunk(part, lines):
    with open(new_filename + '_' + str(part) + extension, 'w') as f_out:
        f_out.write(header)
        f_out.writelines(lines)


# Verifico los parámetros pasados y comienzo a procesar el archivo original
def main(args):
    global filesize
    global header
    global new_filename
    global extension

    # Verifico que me hayan pasado el parámetro del nombre de archivo
    try:
        filename = args[1]
    except:
        print('Tenés que incluir el nombre del archivo CSV a dividir')
        return

    # Verifico que el archivo en cuestión exista
    try:
        file = open(filename)
    except:
        print('No pudimos encontrar el archivo especificado')
        return

    # Obtengo el nombre de archivo y su extensión para posteriormente crear las partes
    new_filename, extension = os.path.splitext(filename)

    # Verifico si pasaron el parámetro de tamaño de archivo deseado, si no lo pasaron, será 500K lineas
    try:
        filesize = int(args[2])
    except:
        filesize = default_size

    print("Iniciando división...\n")

    count = 0
    part = 0
    header = file.readline()
    lines = []
    for line in file:
        count += 1
        lines.append(line)
        if count % filesize == 0:
            print("Creando parte " + str(part + 1) + "...")
            write_chunk(part, lines)
            lines = []
            part += 1
    # write remainder
    if len(lines) > 0:
        print("Creando parte " + str(part + 1) + "...\n")
        write_chunk(part, lines)
    print("El archivo fue dividido en " + str(part + 1) + " partes en el directorio " + os.path.dirname(filename))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv)
