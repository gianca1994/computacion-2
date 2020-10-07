#!/usr/bin/python

import getopt, sys, time, string, os, threading
from datetime import dtime


def CreateLog(NumThread):
    # En la variable Datime alojamos, la fecha y la hora
    Datime = dtime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Abrimos el archivo "eje23ex19_LOG.txt" en el directorio "etc_23" en modo escritura
    with open('etc_23/eje23ex19_LOG.txt', 'w') as file_LOG:
        # Escribimos en el archivo los logs, tanto de la fecha y hora que se ejecuto, la cantida de hilos y la capturas de ps
        file_LOG.write(f'Se ejecuto el : {Datime} y genero {NumThread} hilos\n')

# Definimos option_oeading para que el cliente ingrese la la cantidad de procesos, iteraciones y el nombre del archivo.
def option_reading():

    # Aplicamos el getopt para tomar los 3 argumentos que necesitamos: n(cant_process),r(cant_iterations), f(name_file)
    (opt, arg) = getopt.getopt(sys.argv[1:], 'n:r:f:')

    # Valores por defecto...
    cant_process = None
    cant_iterations = None
    name_file = None

    # Si, el numero de opciones ingresados, es menor que 3, entonces...
    if len(opt) < 3:
        print("Error: Expected at least 3 options [-n] [-r] [-f]", len(opt), "received")
        sys.exit(0)

    # Si no, un for para almacenar en las variables "cant_process", "cant_iterations"  y el "name_file"
    for (opt, arg) in opt:
        if opt == '-n':
            cant_process = arg
        elif opt == '-r':
            cant_iterations = int(arg)
        elif opt == '-f':
            name_file = int(arg)

    # Si, se comprueba que el name_file, el cant_iterations y cant_process no son "None", entonces, nos retorna los mismos
    assert name_file and cant_iterations and cant_process is not None
    return name_file, cant_iterations, cant_process


def writing_letters(cant_iterations, letters, name_file, blocking):
    blocking.acquire()
    # Abrimos el archivo.
    with open(name_file, 'a') as file:
        # Con este for recorremos la cantidad de iteraciones que argumento el usuario
        for i in range(cant_iterations):
            # Escribimos en el archivo, las letters..
            file.write(letters)

            # Delay de 1 segundo
            time.sleep(1)
    blocking.release()


def main():
    # Seteamos las 3 variables con las 3 opciones ingresadas por el usuario/cliente.
    cant_process, cant_iterations, name_file = read_options()
    # A la variable alphabet le asignamos: (string.ascii_uppercase) que contiene todos los caracteres ASCII en mayúsculas
    alphabet = string.ascii_uppercase

    blocking = threading.Lock()
    # Eliminamos el archivo si esta en la ruta: os.path.isfile sino, lo lo creamos
    os.system('rm ' + name_file) if os.path.isfile(name_file) else os.system('touch ' + name_file)

    # Un for para recorrer el array generado por: (if opt == '-n': then --> cant_process = arg) la cantidad de argumentos
    for i in range(cant_process):
        # Creamos un nuevo proceso, targeteando a la funcion writing_letters y traemos como argumentos: "cant_iterations, abecedary, name_file, blocking"
        proc = threading.Thread(target=writing_letters, args=(cant_iterations, alphabet[i], name_file, blocking))
        # Inicializamos el proceso.
        proc.start()

    # Ejecutamos la funcion para crear el log
    CreateLog(len(threading.enumerate()))
    for j in threading.enumerate():
        if not j != threading.main_thread():
            continue
        j.join()

main()
