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
