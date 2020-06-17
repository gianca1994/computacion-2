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
import os
import sys

# Defino la variable "fifo" la cual va a contener el mensaje del consumidor alojado en "fifo1"
fifo = '/tmp/fifo1'

# Definimos la funcion...
def main():
    # Cargamos en la variable "msg" la lista de argumentos, solo leera 1 argumento
    msg=sys.argv[1]
    # Si no existe el "fifo1", con el "os.path.exists" verificamos que exista el archivo.
    if not os.path.exists(fifo):
        # Creamos la tuberia...
        os.mkfifo(fifo)
        # Abrimos el archivo "fifo" en modo escritura y lo cargo en la variable "fifo1"
        fifo_write = open(fifo, 'w')
        # El fifo escribe el mensaje
        fifo_write.write(msg)
        # Limpiamos el buffer.
        fifo_write.flush()

# Iniciamos la funcion.
main()
