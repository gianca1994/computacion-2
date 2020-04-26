# Escribir un programa que genere N procesos hijos. N será un argumento pasado por línea de comandos mediante
# el modificador “-p” o “--process” (ambas deben estar contempladas).
#
# El proceso padre deberá mostrar un mensaje del estilo “Creando proceso: xxxx” al momento de crear cada uno de
# sus procesos hijos.
#
# El proceso padre, luego de crear los N hijos, enviará una señal a cada uno de ellos (SIGUSR2).
#
# Cada hijo mostrará por pantalla, al recibir la señal, el mensaje: “Soy el PID xxxx, recibí la señal yyyy
# de mi padre PID zzzz”, donde xxxx es el pid del hijo en cuestión, yyyy el número de señal, y zzzz el pid
# del proceso padre inicial.
#
# Debe verificar que los PIDs mostrados por el padre coincidan con los pids mostrados por cada hijo, y por supuesto,
# todos los hijos deberán ser del mismo padre.


# ------------------------------------------------------------------------------------------------------#
# ---------------------------------------COMIENZA EL EJERCICIO------------------------------------------#
# ------------------------------------------------------------------------------------------------------#

# !/usr/bin/python3

import getopt
#import os.path
import sys

(opt, arg) = getopt.getopt(sys.argv[1:], 'p:', ['process='])

print('(Opciones ; Argumentos)', opt)

for (op, ar) in opt:
    if (op in ['-p', '--process']):
        proc = str(ar)
        print("Cantidad de procesos a generar = ", ar)

    else:
        print("Opcion invalida")
