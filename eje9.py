# Escribir un programa que genere un proceso hijo (fork), y a su vez, éste genere un nuevo proceso hijo (fork)
# (ver esquema abajo). Todos los procesos estarán comunicados mediante un pipe.
#
#      A → B →C
#
# El proceso B escribirá en el pipe el mensaje "Mensaje 1 (PID=BBBB)\n" en el momento en que el proceso A le
# envíe la señal USR1.
#
# Cuando esto ocurra, el proceso B le enviará la señal USR1 al proceso C, y C escribirá en el pipe el mensaje
# "Mensaje 2 (PID=CCCC)\n".
#
# Cuando el proceso C escriba este mensaje, le enviará al proceso A la señal USR2, y el proceso A leerá el
# contenido del pipe y lo mostrará por pantalla, en el formato:
#
# A (PID=AAAA) leyendo:
# Mensaje 1 (PID=BBBB)
# Mensaje 2 (PID=CCCC)
#
# Notas:
#
# AAAA, BBBB, y CCCC son los respectivos PIDs de los procesos A, B y C.
# Inicialmente el proceso B envía un mensaje al pipe cuando A le hace llegar la señal USR1, por lo que B
# deberá quedar esperando al principio una señal.
# El proceso C también deberá quedar esperando inicialmente una señal que recibirá desde el proceso B para
# poder realizar su tarea.
# El proceso A inicialmente envía la señal USR1 al proceso B, y automáticamente debe quedar esperando una
# señal desde el proceso C para proceder a leer desde el pipe.
# Los saltos de línea en los mensajes (“\n”) son necesarios para que el pipe acumule varias líneas, y no
# concatene los mensajes en la misma línea.
# El pipe es uno solo en el que los procesos B y C deberán escribir, y el proceso A deberá leer.
# Pista: la utilización de señales es para sincronizar los procesos, no necesariamente los handlers deben
# gestionar el pipe.

#------------------------------------------------------------------------------------------------------#
#---------------------------------------COMIENZA EL EJERCICIO------------------------------------------#
#------------------------------------------------------------------------------------------------------#

# !/usr/bin/python3

import time
import signal
import os


def handler(signum, frame):
    return


def main():
    # Proceso A
    procesoA = os.getpid()
    a, b = os.pipe()
    signal.signal(signal.SIGUSR1, handler)
    print("A (PID = %s) leyendo:" % os.getpid())
    procesoB = os.fork()

    if not procesoB:
        procesoC = os.fork()

    if os.getpid() == procesoA:
        time.sleep(0.1)
        os.close(b)
        pipea = os.fdopen(a)
        os.kill(procesoB, signal.SIGUSR1)
        signal.pause()
        print(pipea.read())

    # Proceso B
    elif not procesoB and procesoC:
        signal.pause()
        os.close(a)
        pipe_b = os.fdopen(b, 'w')
        pipe_b.write("Mensaje 1 (PID = %d)" % os.getpid())
        os.kill(procesoC, signal.SIGUSR1)

    # Proceso C
    else:
        signal.pause()
        os.close(a)
        pipe_a = os.fdopen(b, 'w')
        pipe_a.write("\nMensaje 2 (PID = %d)" % os.getpid())
        os.kill(procesoA, signal.SIGUSR1)

main()
