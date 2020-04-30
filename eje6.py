# Desde un proceso padre crear un hijo y enviarle una señal SIGUSR1 cada 5 segundos.
# El proceso hijo estará a la espera y escribirá un aviso en pantalla cada vez que llega la señal de su padre.
# Este comportamiento se detendrá luego de haber enviado 10 señales, o cuando el proceso padre reciba la señal
# de interrupción SIGINT, momento en el que deberá mostrar un mensaje de despedida en pantalla, y terminar la ejecución

# ------------------------------------------------------------------------------------------------------#
# ---------------------------------------COMIENZA EL EJERCICIO------------------------------------------#
# ------------------------------------------------------------------------------------------------------#

# !/usr/bin/python3

import os, time, signal


# Primero definimos el proceso Hijo
def child():
    print('Proceso "Hijo": CREADO!!!')
    time.sleep(1)
    while True:
        time.sleep(1)
        print('Hijo: Señal recibida!!!')
        signal.pause()


# Definimos "handler" para el manejo o manipulacion de señales.
def handler(signum, frame):
    print('Padre: Mandando señal..........')
    return


# Utilizamos la funcion signal.signal para definir el manejo de señales utilizando el "handler" definido anteriormente.
signal.signal(signal.SIGUSR1, handler)

# Ahora definimos el "fork".
pid = os.fork()

# Difinimos el "pid == 0", si es "0" es el proceso hijo y sino vamos al proceso padre
if pid == 0:
    child()

# En caso de no ser 0 el pid...
else:
    print('Proceso "Padre": Iniciando.')
    time.sleep(1)
    # Utilizamos for para hacer el ciclo.
    for x in range(10):
        os.kill(pid, signal.SIGUSR1)
        time.sleep(5)
    print("------------------------Procesos terminados... ADIOS!!------------------------")