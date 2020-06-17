# Crear un sistema Productor-Consumidor (Escritor-Lector) donde un proceso productor almacene un mensaje de
# saludo en una tubería FIFO. Ese mensaje será enviado mediante línea de comandos como argumento del programa.
#
# Ejemplo:
#
# ./saludofifo "HOLA MUNDO"
#
# Otro programa (consumidor) deberá leer el mensaje desde la tubería FIFO, generar un proceso hijo (fork)
# y enviarle por PIPE el mensaje al hijo.
#
# El proceso hijo mostrará por pantalla el mensaje recibido.
#
# Proc1_fifo_escritor → FIFO → Proc2_fifo_lector → pipe → Proc2hijo

#------------------------------------------------------------------------------------------------------#
#---------------------------------------COMIENZA EL EJERCICIO------------------------------------------#
#------------------------------------------------------------------------------------------------------#

# !/usr/bin/python3

import signal
import os

# Definimos el Handler para el manejo de los sockets
def handler(s,f):
    pass

# Definimos la funcion...
def main():
    # Declaramos el "Manejador de señales"
    signal.signal(signal.SIGUSR1, handler)
    # Abrimos una tuberia (un pipe)
    read, write = os.pipe()
    # Creamos el proceso hijo
    child = os.fork()

    # Si el PID del hijo es diferente de 0, entonces ejecutamos el padre.
    if child != 0:
        # Entonces abrimos "fifo1" y lo alojamos en la variable
        fifo_read = open("/tmp/fifo1")
        # Leemos el mensaje que tiene "fifo1" alojado en la variable "fifo_r"
        msg = fifo_read.readline()

        # Aca definimos la variable pipe de ESCRITURA
        pipe_write = os.fdopen(write, 'w')
        # Escribimos en el pipe_write el mensaje alojado por el "fifo_read"
        pipe_write.write(msg)
        pipe_write.close()
        # Matamos la señal
        os.kill(child, signal.SIGUSR1)
        # Y le decimos que espere
        os.wait()

    # si no, ejecutamos al proceso hijo
    else:
        # Pauseamos la señal.
        signal.pause()
        # Cerramos el extremo de escritura
        os.close(write)
        # Aca definimos la variable pipe de LECTURA
        pipe_read = os.fdopen(read)
        # Mostramos el mensaje leido
        print(pipe_read.read())
main()