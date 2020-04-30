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

import os, getopt, sys, signal, time

def func():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:', ['process='])

    print('(Opcion ; Argumentos)', opt)

    # Creo un for para tomar la cantidad de procesos hijos a crear designados por el argumento ingresado
    for (op, ar) in opt:
        if (op in ['-p', '--process']):
            # Alojo el argumento en la variable "proc"
            proc = int(ar)
            print("Cantidad de procesos hijos a generar:", proc)
            print("PID del proceso PADRE:", os.getpid())
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            return proc


# Defino "signals" para el envio de señales.
def signals(child):
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    for pid in child:
        os.kill(pid, signal.SIGUSR2)
    os.wait()


# Definimos handler para el manejo de señales
def handler(signal, frame):
    print("Soy el PID", os.getpid(), "(PID DEL HIJO), recibí la señal", signal
          , "(NUM DE SEÑAL), de mi padre PID", os.getppid(), "(PID INICIAL DEL PROCESO PADRE).")


# Defino "function" para realizar todas las operaciones...
def function():
    # Primero en la variable "childnum" voy a alojar el valor que ingresamos como argumento, alojado en la variable proc.
    childnum = func()

    # Aca traemos el pid que le corresponde al padre y lo alojamos en la variable.
    idfath = os.getpid()
    pidchild = []

    # Por ultimo realizamos un for, con un range(Valor ingresado como argumento)
    for i in range(childnum):

        # Hacemos la bifurcacion de los procesos hijos
        son = os.fork()
        if son == 0:
            # Utilizamos signal.signal para el registro de señales
            signal.signal(signal.SIGUSR2, handler)
            signal.pause()
            break

        print("Creando proceso:", son)
        pidchild.append(son)

    if os.getpid() == idfath:
        time.sleep(1)
        signals(pidchild)

# Iniciamos el programa...
function()

# CORRECCION "agregado "import time" y un time.sleep de 1 segundo para correjir el problema de que se me mostraban,
# los proces los procesos hijos creados pero me mostraba 1 print menos del handler..."