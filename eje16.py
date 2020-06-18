#!/usr/bin/python
import os, time, multiprocessing

# Definimos proc, para crear cada proceso hijo...
def proc(a, queue):
    # Inicia cada proceso indicando el numero de proceso ascendente de 1 a 10 y por igual los PID de
    # cada uno de los 10 hijos que se generara..
    print('Proceso %d, PID: %d' % (a, os.getpid()))
    time.sleep(a)
    queue.put(str(os.getpid()) + "  ")
    # Time.sleep tan bajo para que se muestren de forma ordenada...
    time.sleep(0.001)

# Definimos la funcion main para realizar
def main():
    queue = multiprocessing.Queue()
    listprocess = []
    # Definimos el for con un rango de 1 a 11, para crear los 10 procesos hijos..
    for i in range(1, 11):
        # En process targeteamos la funcion proc encargada de crear cada uno de los proesos hijo
        # y le pasamos la tupla con los argumentos.
        process = multiprocessing.Process(target=proc, args=(i, queue))
        # Iniciamos el multiproceso del objeto
        process.start()
        listprocess.append(process)
        # Time.sleep tan bajo para que se muestren de forma ordenada...
        time.sleep(0.001)

    # Hacemos for para ir recorriendo el array, hasta que el numero de procesos se iguale con el de listprocess
    for process in listprocess:
        # El proceso principal espera a que termine el proceso hijo para continuar con el siguiente...
        process.join()
    # Una vez que no se esta mas en cola..
    while not queue.empty():
        # Se muestra por consola los PIDS de cada hijo.
        print(queue.get(), end=' ')
main()
