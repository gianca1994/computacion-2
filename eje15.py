#!/usr/bin/python

import os, sys, signal, multiprocessing

# Definimos la funcion para el primer proceso
def stdinread(pipe, xD):
    sys.stdin = os.fdopen(xD)
    # Mostramos por consola el mensaje de que el proceso 1 esta leyendo.
    print("process 1 reading...")
    # Utilizamos el array para leer lo ingresado por teclado
    for line in sys.stdin:
        # y enviamos ese mensaje "line" por la tuberia (pipe)
        pipe.send(line)

# Definimos la funcion para el segundo proceso
def piperead(pipe):
    # While true, porque es un bucle infinito, a menos que el usuario detenga el proceso con Ctrl+Z por ejemplo
    while True:
        # Creamos la variable msg en la cual alojamos el mensaje ingresado por teclado
        msg = pipe.recv()
        # Imprimimos en consola el mensaje con el pid del hijo y el mensaje que esta en el pipe.
        print("Leyendo (PID: %d):%s" % (os.getpid(), msg))

# Definimos la funcion, en esta va lo que va a hacer el proceso hijo
def main():
    x, y = multiprocessing.Pipe()
    stdin_fd = sys.stdin.fileno()

    # Creamos los 2 procesos hijos, obejtos p1 y p2
    # En process1 targeteamos la funcion stdinread y le pasamos la tupla con los argumentos.
    process1 = multiprocessing.Process(target=stdinread, args=(x, stdin_fd))
    # en el process2 targeteamos la funcion piperead + argumentos
    process2 = multiprocessing.Process(target=piperead, args=(y,))
    # Iniciamos el multiproceso del primer objeto
    process1.start()
    # Eh iniciamos el segundo...
    process2.start()

    # El proceso principal espera a que termine el proceso hijo para continuar...
    process1.join()
    # Finalizamos el proceso 1 y matamos el proceso 2
    os.kill(process2.pid, signal.SIGTERM)
main()
