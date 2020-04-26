# Realice un programa que genere dos procesos.
# El proceso hijo1 enviará la señal SIGUSR1 al proceso padre y mostrará la cadena "Soy el hijo1
# con PID=XXXX: ping" cada 5 segundos.
#
# El proceso padre, al recibir la señal SIGUSR1 enviará esta misma señal al proceso hijo2.
# El proceso hijo2, al recibir dicha señal mostrará la cadena "Soy el hijo2 con PID=YYYY: pong" por pantalla.
#
# Este comportamiento se deberá detener a las 10 señales enviadas por el proceso hijo1.
#
# Soy proceso hijo1 con PID=1545: "ping"
# Soy proceso hijo2 con PID=1547: "pong"
#
# [... 5 segundos mas tarde ...]
# Soy proceso hijo1 con PID=1545: "ping"
# Soy proceso hijo2 con PID=1547: "pong"
# [... y así sucesivamente ...]

# ------------------------------------------------------------------------------------------------------#
# ---------------------------------------COMIENZA EL EJERCICIO------------------------------------------#
# ------------------------------------------------------------------------------------------------------#

# !/usr/bin/python3

import os
import time
import signal
from multiprocessing import Process


# Definimos handler para el manejo de señales
def handler(signum, frame):
    return

# Utilizamos signal.signal para el registro de señales
signal.signal(signal.SIGUSR1, handler)

# Definimos "child1" para definir el proceso hijo 1
def child1(pid_p):
    for x in range(10):
        print('Soy el hijo1 con PID=%s: ping' % (os.getpid()))
        # El proceso hijo1 enviará la señal SIGUSR1 al proceso padre.
        os.kill(pid_p, signal.SIGUSR1)
        # y mostrará la cadena "Soy el hijo1 con PID=XXXX: ping" cada 5 segundos.
        time.sleep(5)
    # Mensaje que indica el fin del programa...
    print("--------------------- TERMINO EL EJERCICIO -----------------------")


# Definimos "child2" para definir el proceso hijo 2
def child2():
    while True:
        # El proceso hijo2, al recibir dicha señal mostrará la cadena "Soy el hijo2 con PID=YYYY: pong" por pantalla.
        print('Soy el hijo2 con PID=%s: pong' % (os.getpid()))
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
        signal.pause()


# Ahora trabajaremos con el proceso PADRE...
# El proceso padre, al recibir la señal SIGUSR1 enviará esta misma señal al proceso hijo2.
if __name__ == '__main__':
    pid_p = os.getpid()
    # Asignamos a la variable "p1" el process, targeteando al "hijo1" con el argumento "pid_p".
    p1 = Process(target=child1, args=(pid_p,))
    # Asignamos a la variable "p2" el process, targeteando al "hijo2".
    p2 = Process(target=child2)
    # Iniciamos las 2 variables...
    p1.start()
    p2.start()

    # Utilizamos while para el bucle de las señales
    while True:
        os.kill(p2.pid, signal.SIGUSR1)
        signal.pause()
