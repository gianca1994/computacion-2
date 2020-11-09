#!/usr/bin/python

import getopt, multiprocessing, sys

def option_reading():

    # Inicializamos las 3 variables como none...
    cantidad_procesos = num_min = num_max = None
    # Usamos getopt para tomar los 3 argumentos que necesitamos
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:m:n:')

    # Si, el numero de opciones ingresados, es diferente de 3, entonces...
    if len(opt) != 3:
        print("Error: Expected at least 3 options [-p] [-m] [-n]", len(opt), "received")
        sys.exit(0)

    # Si no, un for para almacenar en las variables "cantidad_procesos", "num_min", "num_max"
    for (opt, arg) in opt:
        if opt == '-p':
            cantidad_procesos = int(arg)
        elif opt == '-m':
            num_min = int(arg)
        elif opt == '-n':
            num_max = int(arg)

    # En caso de no ser none las 3 variables
    assert (cantidad_procesos, num_min, num_max) is not None

    # Error en caso de que hayan pas procesos que numeros o que el numero minimo sea mayor al maximo...
    if (cantidad_procesos > num_max - num_min) or (num_min > num_max):
        raise getopt.GetoptError('The num_min must be less than num_max, or it may have more processes than numbers.')
    
    # Sino, retornamos los valores.
    return cantidad_procesos, num_min, num_max

def number_squared(number):
    # Declaramos el nombre del proceso
    MultiProcssName = multiprocessing.current_process().name
    # y printeamos el process name y el cuadrado del numero...
    print(f'{MultiProcssName} --> {number}^2')


def main():

    # Cargamos a las 3 variables, los numeros leidos en el option reading
    cantidad_procesos, num_min, num_max = option_reading()

    # Ahora usaremos 2 funciones: pool.map y pool.apply

    # pool.map : Distribuye todas las tareas al pool (aplica la misma tarea a muchos argumentos) 
    # y te devuelve la lista mapeada y en orden.

    # pool.apply : Llama a func con argumentos args y argumentos de palabras clave kwds. 
    # Se bloquea hasta que el resultado esté listo.

    multipross = multiprocessing.Pool(cantidad_procesos)

    with multipross as pool:
        print("hit enter to get the map result and then hit enter again to get the apply result")

        num_est = range(num_min, num_max)

        # Utilizamos el pool.map y le pasamos como parametros la funcion number_squared y el rango de numeros
        pool.map(number_squared, num_est)
        # Al pool.apply le pasamos como argumentos el range del num_min, num_max y la funcion number_squared
        [pool.apply(number_squared, (num,)) for num in num_est]
    
main()